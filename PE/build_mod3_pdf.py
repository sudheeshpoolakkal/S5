# -*- coding: utf-8 -*-
"""
Build Script for Module 3 Comprehensive Study Guide (KTU S5 EEE)
Compiles LaTeX source using XeLaTeX with RakutenSerifApp font.
"""

import os
import subprocess
import sys

from mod3_src import sec1_acvc
from mod3_src import sec2_single_phase_vsi
from mod3_src import sec3_three_phase_vsi
from mod3_src import sec4_csi_vs_vsi
from mod3_src import sec5_utility_interface
from mod3_src import sec6_solved_problems
from mod3_src import sec7_master_summary

PREAMBLE = r'''\documentclass[11pt,a4paper]{article}
\usepackage[margin=1.8cm,top=2.5cm,bottom=2.2cm,headheight=24pt]{geometry}
\usepackage{fontspec}
\setmainfont{RakutenSerifApp}[
  Path = /home/sudheesh/.fonts/Notesnook/,
  Extension = .ttf,
  UprightFont = *-Regular,
  BoldFont = *-Bold,
  ItalicFont = *-Italic,
  BoldItalicFont = *-BoldItalic
]
\usepackage{amsmath,amssymb,mathtools}
\usepackage{booktabs,array,tabularx,multirow}
\usepackage{graphicx}
\graphicspath{{figures_mod3/}}
\usepackage{xcolor}
\usepackage{titlesec}
\usepackage{fancyhdr}
\usepackage{enumitem}
\usepackage{caption}
\usepackage{tcolorbox}
\tcbuselibrary{skins,breakable}
\usepackage{tikz}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
\usetikzlibrary{arrows.meta,calc,positioning,patterns,decorations.pathmorphing}
\usepackage[hidelinks,pdfusetitle]{hyperref}

% Define custom column for tabularx
\newcolumntype{Y}{>{\centering\arraybackslash}X}

% Define color palette
\definecolor{navyprimary}{RGB}{15, 35, 65}
\definecolor{accentblue}{RGB}{2, 132, 199}
\definecolor{tealaccent}{RGB}{13, 148, 136}
\definecolor{cardbg}{RGB}{248, 250, 252}
\definecolor{cardborder}{RGB}{203, 213, 225}
\definecolor{calloutbg}{RGB}{241, 245, 249}
\definecolor{calloutframe}{RGB}{100, 116, 139}
\definecolor{formulabg}{RGB}{238, 242, 255}
\definecolor{formulaframe}{RGB}{99, 102, 241}
\definecolor{examplebg}{RGB}{250, 250, 250}
\definecolor{exampleframe}{RGB}{56, 189, 248}
\definecolor{highlightgold}{RGB}{180, 83, 9}
\definecolor{alertbg}{RGB}{254, 242, 242}
\definecolor{alertframe}{RGB}{239, 68, 68}

% Caption styling
\captionsetup{font=small,labelfont={bf,color=navyprimary},skip=5pt}

% Typography & Header/Footer
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0.6pt}
\renewcommand{\headrule}{\hbox to\headwidth{\color{navyprimary}\leaders\hrule height \headrulewidth\hfill}}
\fancyhead[L]{\small\bfseries\color{navyprimary}Power Electronics (Module 3) --- Master Study Guide}
\fancyhead[R]{\small\color{accentblue}CET S5 EEE}
\fancyfoot[L]{\small\color{gray}College of Engineering Trivandrum}
\fancyfoot[R]{\small\bfseries\color{navyprimary}Page \thepage}

% Section Titles Styling
\titleformat{\section}{\Large\bfseries\color{navyprimary}}{}{0em}{}[\vspace{1mm}{\color{accentblue}\hrule height 1.2pt}]
\titleformat{\subsection}{\large\bfseries\color{accentblue}}{}{0em}{}
\titleformat{\subsubsection}{\normalsize\bfseries\color{tealaccent}}{}{0em}{}

% Tcolorbox custom environments (Border-free modern cards with solid background colors)
\newtcolorbox{conceptbox}[1][]{
  enhanced,
  colback=calloutbg,
  colframe=calloutbg,
  colbacktitle=calloutbg,
  coltitle=navyprimary,
  fonttitle=\bfseries,
  title={#1},
  titlerule=0pt,
  boxrule=0pt,
  frame hidden,
  arc=2.5mm,
  left=4mm, right=4mm, top=3mm, bottom=3mm,
  breakable
}

\newtcolorbox{formulabox}[1][]{
  enhanced,
  colback=formulabg,
  colframe=formulabg,
  colbacktitle=formulabg,
  coltitle=navyprimary,
  fonttitle=\bfseries,
  title={#1},
  titlerule=0pt,
  boxrule=0pt,
  frame hidden,
  arc=2.5mm,
  left=4mm, right=4mm, top=3mm, bottom=3mm,
  breakable
}

\newtcolorbox{examplebox}[1][]{
  enhanced,
  colback=examplebg,
  colframe=examplebg,
  colbacktitle=examplebg,
  coltitle=navyprimary,
  fonttitle=\bfseries,
  title={#1},
  titlerule=0pt,
  boxrule=0pt,
  frame hidden,
  arc=2.5mm,
  left=4mm, right=4mm, top=3mm, bottom=3mm,
  middle=2.5mm,
  segmentation style={solid, draw=cardborder, line width=0.6pt},
  breakable
}

\newtcolorbox{alertbox}[1][]{
  enhanced,
  colback=alertbg,
  colframe=alertbg,
  colbacktitle=alertbg,
  coltitle=alertframe,
  fonttitle=\bfseries,
  title={#1},
  titlerule=0pt,
  boxrule=0pt,
  frame hidden,
  arc=2.5mm,
  left=4mm, right=4mm, top=3mm, bottom=3mm,
  breakable
}

% Remove boxed black borders
\renewcommand{\boxed}[1]{#1}

\begin{document}

% Title Block
\begin{center}
  {\LARGE\bfseries\color{navyprimary}POWER ELECTRONICS}\\[2mm]
  {\Large\bfseries\color{accentblue}Module 3: AC Voltage Controllers, DC-AC Inverters \& Utility Interface}\\[3mm]
  {\normalsize\bfseries B.Tech S5 Electrical \& Electronics Engineering (EEE) $\cdot$ APJ Abdul Kalam Technological University}\\[1mm]
  {\small\color{gray}Comprehensive Master Study Guide \& University Examination Preparation Manual}\\[2mm]
  \noindent\makebox[\linewidth]{\color{navyprimary}\rule{\linewidth}{1.5pt}}
\end{center}

\vspace{-2mm}
\tableofcontents
\vspace{4mm}
\noindent\makebox[\linewidth]{\color{cardborder}\rule{\linewidth}{0.6pt}}
\vspace{2mm}
'''

POSTAMBLE = r'''
\end{document}
'''

def main():
    tex_filename = "Module_3_Comprehensive_Study_Guide.tex"
    print(f"Generating {tex_filename}...")
    
    sections = [
        sec1_acvc.get_section(),
        sec2_single_phase_vsi.get_section(),
        sec3_three_phase_vsi.get_section(),
        sec4_csi_vs_vsi.get_section(),
        sec5_utility_interface.get_section(),
        sec6_solved_problems.get_section(),
        sec7_master_summary.get_section(),
    ]
    
    full_content = PREAMBLE + "\n".join(sections) + POSTAMBLE
    
    with open(tex_filename, "w", encoding="utf-8") as f:
        f.write(full_content)
        
    print(f"Successfully generated {tex_filename} ({len(full_content)} characters).")
    
    # Compile with XeLaTeX (Pass 1)
    print("Compiling with XeLaTeX (Pass 1)...")
    res1 = subprocess.run(["xelatex", "-interaction=nonstopmode", tex_filename], capture_output=True, text=True)
    if res1.returncode != 0:
        print("ERROR: XeLaTeX Pass 1 failed!")
        # Print relevant error lines
        for line in res1.stdout.split('\n')[-35:]:
            print(line)
        sys.exit(1)
    print("XeLaTeX Pass 1 succeeded.")
    
    # Compile with XeLaTeX (Pass 2 for TOC & references)
    print("Compiling with XeLaTeX (Pass 2 for TOC & references)...")
    res2 = subprocess.run(["xelatex", "-interaction=nonstopmode", tex_filename], capture_output=True, text=True)
    if res2.returncode != 0:
        print("ERROR: XeLaTeX Pass 2 failed!")
        sys.exit(1)
    print("XeLaTeX Pass 2 succeeded.")
    
    pdf_filename = tex_filename.replace(".tex", ".pdf")
    if os.path.exists(pdf_filename):
        size_mb = os.path.getsize(pdf_filename) / (1024 * 1024)
        print(f"SUCCESS: Generated {pdf_filename} ({size_mb:.2f} MB)")
    else:
        print("ERROR: PDF was not generated.")
        sys.exit(1)

if __name__ == "__main__":
    main()
