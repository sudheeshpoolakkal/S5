import subprocess
import os

tex_content = r'''\documentclass[10pt,a4paper]{article}

% --- Packages ---
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{geometry}
\geometry{
    a4paper,
    top=1.8cm,
    bottom=1.8cm,
    left=1.6cm,
    right=1.6cm,
    headheight=22pt,
    headsep=10pt,
    footskip=16pt
}
\usepackage{xcolor}
\usepackage{amsmath,amssymb}
\usepackage{tikz}
\usetikzlibrary{shapes.geometric, arrows.meta, positioning, calc, backgrounds, fit}
\usepackage{tcolorbox}
\tcbuselibrary{breakable}
\usepackage{listings}
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{enumitem}
\usepackage{hyperref}

% --- High-Contrast Dark Theme Color Palette ---
\definecolor{bgDark}{HTML}{000000}       % Pure pitch black background
\definecolor{cardDark}{HTML}{11141D}     % Dark obsidian card background
\definecolor{cardBorder}{HTML}{262D3D}   % Clean subtle border
\definecolor{textWhite}{HTML}{F3F4F6}    % Crisp white text
\definecolor{textMuted}{HTML}{9CA3AF}    % Muted secondary text
\definecolor{accentBlue}{HTML}{38BDF8}   % Electric sky blue (Headers)
\definecolor{accentCyan}{HTML}{34D399}   % Mint cyan (Subsections)
\definecolor{accentGreen}{HTML}{4ADE80}  % Vibrant green (Cards / Success)
\definecolor{accentOrange}{HTML}{FBBF24} % Warm golden amber (Alerts / Warnings)
\definecolor{accentPurple}{HTML}{C084FC} % Neon purple (Keywords / Components)
\definecolor{accentRed}{HTML}{F87171}    % Coral red (Violations / Errors)
\definecolor{codeBg}{HTML}{090D15}       % Deep code block background

% --- Page Setup ---
\pagecolor{bgDark}
\color{textWhite}

\hypersetup{
    colorlinks=true,
    linkcolor=accentBlue,
    urlcolor=accentCyan,
    citecolor=accentPurple
}

% --- Header & Footer ---
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0.5pt}
\renewcommand{\headrule}{\hbox to\headwidth{\color{cardBorder}\leaders\hrule height \headrulewidth\hfill}}
\fancyhead[L]{\textcolor{accentBlue}{\footnotesize\textbf{OPERATING SYSTEMS (MOS)}}}
\fancyhead[R]{\textcolor{textMuted}{\footnotesize KTU S5 $\bullet$ Core Engineering Study Reference}}
\fancyfoot[C]{\textcolor{textMuted}{\footnotesize \textbf{Page \thepage}}}

% --- Section Styling ---
\titleformat{\section}
  {\normalfont\large\bfseries\color{accentBlue}}
  {\llap{\color{accentOrange}\thesection\hspace{0.5em}}}{0em}{}
  [\color{cardBorder}\titlerule]

\titleformat{\subsection}
  {\normalfont\normalsize\bfseries\color{accentCyan}}
  {\thesubsection}{0.5em}{}

\titleformat{\subsubsection}
  {\normalfont\small\bfseries\color{accentPurple}}
  {\thesubsubsection}{0.5em}{}

\titlespacing*{\section}{0pt}{10pt}{6pt}
\titlespacing*{\subsection}{0pt}{8pt}{4pt}
\titlespacing*{\subsubsection}{0pt}{6pt}{3pt}

% --- Custom TColorBoxes ---
\newtcolorbox{darkcard}[2][]{
    breakable,
    colback=cardDark,
    colframe=accentBlue!70!cardBorder,
    coltitle=accentBlue,
    fonttitle=\bfseries\small,
    title={#2},
    coltext=textWhite,
    arc=2mm,
    boxrule=0.8pt,
    top=2.5mm,
    bottom=2.5mm,
    left=3mm,
    right=3mm,
    #1
}

\newtcolorbox{conceptcard}[2][]{
    breakable,
    colback=cardDark,
    colframe=accentGreen!70!cardBorder,
    coltitle=accentGreen,
    fonttitle=\bfseries\small,
    title={#2},
    coltext=textWhite,
    arc=2mm,
    boxrule=0.8pt,
    top=2.5mm,
    bottom=2.5mm,
    left=3mm,
    right=3mm,
    #1
}

\newtcolorbox{alertbox}[2][]{
    breakable,
    colback=cardDark,
    colframe=accentOrange,
    coltitle=accentOrange,
    fonttitle=\bfseries\small,
    title={#2},
    coltext=textWhite,
    arc=2mm,
    boxrule=0.8pt,
    top=2.5mm,
    bottom=2.5mm,
    left=3mm,
    right=3mm,
    #1
}

\newtcolorbox{defbox}[1][]{
    breakable,
    colback=cardDark,
    colframe=accentBlue,
    arc=2mm,
    boxrule=0.8pt,
    coltext=textWhite,
    left=3mm,
    right=3mm,
    top=2.5mm,
    bottom=2.5mm,
    #1
}

% --- Code Listing Style ---
\lstdefinestyle{darkc}{
    backgroundcolor=\color{codeBg},
    basicstyle=\ttfamily\scriptsize\color{textWhite},
    keywordstyle=\bfseries\color{accentPurple},
    commentstyle=\itshape\color{textMuted},
    stringstyle=\color{accentGreen},
    numberstyle=\tiny\color{textMuted},
    numbers=left,
    numbersep=5pt,
    frame=single,
    rulecolor=\color{cardBorder},
    breaklines=true,
    showstringspaces=false,
    tabsize=4,
    xleftmargin=8pt,
    framexleftmargin=8pt
}
\lstset{style=darkc}

% --- List Spacing ---
\setlist{itemsep=1.5pt, topsep=1.5pt, parsep=0.5pt, leftmargin=15pt}

% --- TikZ Style Settings ---
\tikzset{
    darknode/.style={
        rectangle, 
        rounded corners=1.5mm, 
        draw=accentBlue, 
        fill=cardDark, 
        text=textWhite, 
        align=center, 
        inner sep=4pt, 
        font=\scriptsize\bfseries
    },
    darkgreen/.style={
        rectangle, 
        rounded corners=1.5mm, 
        draw=accentGreen, 
        fill=cardDark, 
        text=textWhite, 
        align=center, 
        inner sep=4pt, 
        font=\scriptsize\bfseries
    },
    darkorange/.style={
        rectangle, 
        rounded corners=1.5mm, 
        draw=accentOrange, 
        fill=cardDark, 
        text=textWhite, 
        align=center, 
        inner sep=4pt, 
        font=\scriptsize\bfseries
    },
    darkpurple/.style={
        rectangle, 
        rounded corners=1.5mm, 
        draw=accentPurple, 
        fill=cardDark, 
        text=textWhite, 
        align=center, 
        inner sep=4pt, 
        font=\scriptsize\bfseries
    },
    darkarrow/.style={
        -{Stealth[scale=0.9]}, 
        thick, 
        draw=accentBlue
    },
    greenarrow/.style={
        -{Stealth[scale=0.9]}, 
        thick, 
        draw=accentGreen
    },
    orangearrow/.style={
        -{Stealth[scale=0.9]}, 
        thick, 
        draw=accentOrange
    }
}

\begin{document}

% --- Title Block ---
\begin{center}
    {\fontsize{20}{24}\selectfont \textbf{\textcolor{accentBlue}{OPERATING SYSTEMS (MOS)}}}\\[4pt]
    {\normalsize \textcolor{accentCyan}{\textbf{Complete Handwritten Lecture Notes Transcribed to Digital Format}}}\\[2pt]
    {\footnotesize \textcolor{textMuted}{High-Contrast Dark Edition $\bullet$ KTU B.Tech S5 Computer Science \& Engineering}}
    \vspace{4pt}
    \hrule height 0.8pt \relax
    \vspace{6pt}
\end{center}

% ==============================================================================
\section{Introduction to Operating Systems}
% ==============================================================================

\begin{defbox}
    \textbf{\textcolor{accentBlue}{Operating System Definition:}} An \textbf{Operating System (OS)} is a software that manages and handles hardware and software resources of a computing device. It acts as an interface between the user and hardware.
\end{defbox}

\subsection*{Key Roles \& Functions}
\begin{itemize}
    \item \textbf{Resource Manager:} Manages computer resources such as CPU, memory (RAM), and files/storage.
    \item \textbf{User-Hardware Interface:} Acts as an interface between user applications and the raw hardware.
    \item \textbf{Performs Core Functions:} Executes core functions like process, memory, and file management.
    \item \textbf{Organizes Resources:} Organizes system resources similar to different departments in a government.
    \item \textbf{Real-World Examples:} Linux, Unix, Windows 11, MS-DOS, Android, macOS, iOS.
\end{itemize}

\subsubsection*{Abstract View of System Components}
\begin{center}
\begin{tikzpicture}[node distance=0.85cm and 0.5cm, auto, scale=0.92, every node/.style={transform shape}]
    % Users
    \node[darkorange, minimum width=1.5cm] (u1) {User 1};
    \node[darkorange, minimum width=1.5cm, right=0.3cm of u1] (u2) {User 2};
    \node[darkorange, minimum width=1.5cm, right=0.3cm of u2] (u3) {User 3};
    \node[darkorange, minimum width=1.5cm, right=0.3cm of u3] (u4) {User $n$};

    % Application Programs Box
    \node[draw=accentPurple, dashed, inner sep=5pt, rounded corners=2mm, fill=cardDark!70, fit=(u1) (u4), below=0.55cm of u2.south, xshift=0.9cm, minimum width=10.0cm, minimum height=1.0cm] (appbox) {};
    \node at (appbox.north) [yshift=2mm, fill=cardDark, text=accentPurple, font=\tiny\bfseries] {Application Programs};
    \node[darkpurple, font=\tiny] at ([xshift=-3.1cm]appbox.center) {Text Editor};
    \node[darkpurple, font=\tiny] at ([xshift=0cm]appbox.center) {Compiler};
    \node[darkpurple, font=\tiny] at ([xshift=3.1cm]appbox.center) {Database System};

    % Operating System
    \node[darknode, minimum width=10.0cm, minimum height=0.7cm, below=0.55cm of appbox] (os) {OPERATING SYSTEM};

    % Hardware
    \node[darkgreen, minimum width=10.0cm, minimum height=0.7cm, below=0.55cm of os] (hw) {HARDWARE};

    % Arrows
    \draw[orangearrow] (u1.south) -- ++(0,-0.25);
    \draw[orangearrow] (u2.south) -- ++(0,-0.25);
    \draw[orangearrow] (u3.south) -- ++(0,-0.25);
    \draw[orangearrow] (u4.south) -- ++(0,-0.25);

    \draw[darkarrow, <->] (appbox.south) -- (os.north);
    \draw[greenarrow, <->] (os.south) -- (hw.north);
\end{tikzpicture}
\end{center}

\subsection{Components of an OS}
There are two basic components of an OS:
\begin{enumerate}
    \item \textbf{Shell:} It is the outermost layer of the operating system and handles user interaction. It interprets input for the OS and handles the output from the OS.
    \item \textbf{Kernel:} It is the core component of the OS. The kernel is the primary interface between the operating system and hardware.
\end{enumerate}

% ==============================================================================
\section{Functions of an Operating System}
% ==============================================================================

The OS controls all computer resources, coordinates program execution, hides system complexity, ensures security, and improves resource utilization.

\begin{center}
\begin{tikzpicture}[node distance=0.7cm and 0.4cm, scale=0.88, every node/.style={transform shape}]
    \node[darknode, minimum width=3.2cm, minimum height=0.8cm, fill=accentBlue!25!cardDark] (os) {\textbf{OPERATING SYSTEM}};

    \node[darkgreen, above left=0.5cm and 0.1cm of os] (p1) {Process Management};
    \node[darkpurple, above right=0.5cm and 0.1cm of os] (p2) {Memory Management};
    \node[darkorange, below left=0.5cm and 0.1cm of os] (p3) {File Management};
    \node[darkgreen, below=0.85cm of os] (p4) {Device Management};
    \node[darkpurple, below right=0.5cm and 0.1cm of os] (p5) {Protection \& Security};

    \draw[darkarrow] (os) -- (p1);
    \draw[darkarrow] (os) -- (p2);
    \draw[darkarrow] (os) -- (p3);
    \draw[darkarrow] (os) -- (p4);
    \draw[darkarrow] (os) -- (p5);
\end{tikzpicture}
\end{center}

\subsection{Process Management}
Process management in an operating system is about managing processes. A \textbf{process} is a running program.
\begin{itemize}
    \item \textbf{a) Scheduling:} Decides which process uses the CPU next.
    \item \textbf{b) Synchronization:} Ensures orderly execution using locks, semaphores, or monitors to prevent race conditions.
    \item \textbf{c) Deadlock Handling:} Detects \& prevents situations where processes wait forever for resources.
    \item \textbf{d) Inter-Process Communication (IPC):} Allows processes to exchange data via shared memory or message passing.
\end{itemize}

\subsection{Memory Management}
Memory management in an operating system controls how data is stored and organized in main memory and secondary storage, ensuring programs get the memory they need and freeing it when no longer used.

\begin{center}
\begin{tikzpicture}[scale=0.78, every node/.style={transform shape}]
    % Main Memory
    \draw[draw=accentBlue, thick, fill=cardDark, rounded corners=1.5mm] (0,0) rectangle (3.2, 3.0);
    \node[text=accentBlue, font=\scriptsize\bfseries] at (1.6, 2.7) {Main Memory};
    \draw[draw=cardBorder, fill=accentBlue!15!cardDark] (0.2, 1.6) rectangle (3.0, 2.3) node[pos=.5, font=\tiny, text=textWhite] {Operating System};
    \draw[draw=cardBorder, fill=cardDark] (0.2, 0.3) rectangle (3.0, 1.4) node[pos=.5, font=\tiny, text=textWhite] {User Space};

    % Secondary Memory
    \draw[draw=accentGreen, thick, fill=cardDark, rounded corners=1.5mm] (6.0,0) rectangle (9.2, 3.0);
    \node[text=accentGreen, font=\scriptsize\bfseries] at (7.6, 2.7) {Secondary Memory};
    \draw[draw=cardBorder, fill=accentGreen!15!cardDark] (6.2, 1.3) rectangle (9.0, 2.0) node[pos=.5, font=\tiny, text=textWhite] {Process 1};
    \draw[draw=cardBorder, fill=accentGreen!15!cardDark] (6.2, 0.3) rectangle (9.0, 1.0) node[pos=.5, font=\tiny, text=textWhite] {Process 2};

    % Arrows
    \draw[orangearrow, <->] (3.0, 1.0) -- (6.2, 1.6);
    \draw[orangearrow, <->] (3.0, 0.6) -- (6.2, 0.7);
\end{tikzpicture}
\end{center}

\begin{conceptcard}{Key Activities in Memory Management}
\begin{itemize}
    \item \textbf{Allocation \& Deallocation:} Assign and free memory as needed.
    \item \textbf{Protection:} Prevents processes from interfering with each other's memory.
    \item \textbf{Virtual Memory:} Uses disk space as extra memory to run large programs.
    \item \textbf{Fragmentation Handling:} Reduces wasted space through compaction.
    \item \textbf{Disk Management:} Handles file storage, free space, disk scheduling, and backups.
\end{itemize}
\end{conceptcard}

\subsection{File System Management}
File management in an OS organizes and controls how data is stored, named, and accessed on storage devices, making it easy for users to find and use their files.
\begin{itemize}
    \item \textbf{File Attributes:} Names, type, size, and permissions.
    \item \textbf{File Types:} Text, binary, and executable files.
    \item \textbf{Operations:} Create, read, write, and delete files.
    \item \textbf{Access Methods:} Sequential, direct, and indexed access for faster retrieval.
\end{itemize}

\subsection{Device Management (I/O System)}
Device management in an OS controls how the computer communicates with hardware devices like printers or disks, using drivers and techniques to ensure smooth and efficient operation.

\begin{center}
\begin{tikzpicture}[node distance=0.45cm and 0.8cm, auto, scale=0.82, every node/.style={transform shape}]
    \node[darknode, minimum width=6.8cm] (up) {User Process};
    \node[darkpurple, minimum width=6.8cm, below=0.4cm of up] (k) {Kernel};
    \node[darkgreen, minimum width=6.8cm, below=0.4cm of k] (dd) {Driver};
    \node[darkorange, minimum width=6.8cm, below=0.4cm of dd] (dev) {Device};

    \node[darknode, below left=0.45cm and -0.7cm of dev, minimum width=3.0cm] (net) {Ethernet / Wi-Fi Card};
    \node[darknode, below right=0.45cm and -0.7cm of dev, minimum width=3.0cm] (disk) {Disk Storage};

    \draw[darkarrow, <->] (up) -- node[left, font=\tiny] {Send Data / Read File} (k);
    \draw[darkarrow, <->] (k) -- node[left, font=\tiny] {Form Packet / Determine Disk Block} (dd);
    \draw[darkarrow, <->] (dd) -- node[left, font=\tiny] {Write Tx / Issue Disk Head Move} (dev);

    \draw[greenarrow, ->] (dev.south -| net.north) -- node[left, font=\tiny] {Perform Transmission} (net.north);
    \draw[greenarrow, ->] (dev.south -| disk.north) -- node[right, font=\tiny] {Read Block from Disk} (disk.north);
\end{tikzpicture}
\end{center}

\begin{conceptcard}{Major Components in Device Management}
\begin{itemize}
    \item \textbf{Device Drivers:} Interface between hardware and OS.
    \item \textbf{Buffering \& Caching:} Temporarily store data to match device speeds and improve performance.
    \item \textbf{Spooling:} Spooling manages data waiting to be processed, particularly in devices like printers. The OS places print jobs in a \textbf{spool} (a temporary storage area), allowing the CPU to continue other tasks while the printer works through the queue.
\end{itemize}
\end{conceptcard}

\subsection{Protection and Security}
Protection and security mechanisms in an OS are designed to safeguard system resources from unauthorized access or misuse.
\begin{itemize}
    \item These mechanisms control which processes or users can access specific resources (such as memory, files, and CPU time).
    \item Ensures that only authorized users can perform specific actions.
    \item \textbf{Access Control:} Limits user and process permissions.
    \item \textbf{Authentication:} Verifies users through credentials (UID / SID).
    \item \textbf{Resource Protection:} Prevents misuse of files, memory, or devices.
    \item \textbf{Security:} Guards against malware, denial-of-service (DoS) attacks, and data theft.
\end{itemize}

\clearpage
% ==============================================================================
\section{Processes and Process Lifecycle}
% ==============================================================================

\subsection{Process Concept}
\begin{itemize}
    \item A \textbf{process} is a program in execution.
    \item A process is more than the program code, sometimes known as the \textbf{text section}.
    \item It includes the current activity as represented by the value of the \textbf{Program Counter (PC)} and processor registers.
    \item A process includes the \textbf{process stack} (temporary data: parameters, return addresses, local variables) and a \textbf{data section} (global variables).
\end{itemize}

\subsubsection*{Process Address Space Layout}
Each process runs in its own virtual memory address space:
\begin{center}
\begin{tikzpicture}[scale=0.88]
    \draw[draw=accentBlue, thick, fill=cardDark, rounded corners=2mm] (0,0) rectangle (9.2, 4.3);
    \draw[draw=cardBorder, fill=accentOrange!20!cardDark] (0.2, 3.35) rectangle (9.0, 4.1) node[pos=.5, text=textWhite, font=\footnotesize\bfseries] {Stack Space (Functions \& System Calls) $\quad \downarrow$};
    \draw[draw=cardBorder, fill=cardDark!80] (0.2, 2.25) rectangle (9.0, 3.15) node[pos=.5, text=textMuted, font=\scriptsize] {Variables (Static \& Dynamic) / Heap Growth Space $\quad \uparrow$};
    \draw[draw=cardBorder, fill=accentGreen!20!cardDark] (0.2, 1.25) rectangle (9.0, 2.05) node[pos=.5, text=textWhite, font=\footnotesize\bfseries] {Data Space (Global Variables)};
    \draw[draw=cardBorder, fill=accentBlue!20!cardDark] (0.2, 0.2) rectangle (9.0, 1.05) node[pos=.5, text=textWhite, font=\footnotesize\bfseries] {Text Space (Program Code)};
\end{tikzpicture}
\end{center}

\subsection{Process States}
The state of a process is defined by its current activity. Each process may be in one of the following states:
\begin{itemize}
    \item \textbf{New:} The process is being created.
    \item \textbf{Running:} Instructions are being executed.
    \item \textbf{Waiting:} The process is waiting for some event to occur (e.g., I/O completion or signal).
    \item \textbf{Ready:} The process is waiting to be assigned to a processor.
    \item \textbf{Terminated:} The process has finished execution.
\end{itemize}

\subsubsection*{5-State Process Transition Diagram}
\begin{center}
\begin{tikzpicture}[node distance=1.4cm and 1.6cm, auto, scale=0.88, every node/.style={transform shape}]
    \node[darknode] (new) {NEW};
    \node[darkgreen, right=1.3cm of new] (ready) {READY};
    \node[darkorange, right=2.0cm of ready] (running) {RUNNING};
    \node[darkpurple, below=1.3cm of $(ready)!0.5!(running)$] (waiting) {WAITING};
    \node[darknode, right=1.3cm of running] (term) {TERMINATED};

    \draw[darkarrow] (new) -- node[above, font=\tiny] {admitted} (ready);
    \draw[greenarrow] (ready) -- node[above, font=\tiny] {scheduler dispatch} (running);
    \draw[orangearrow] (running) to[bend left=28] node[below, font=\tiny] {interrupt} (ready);
    \draw[orangearrow] (running) to[bend left=24] node[right, font=\tiny] {I/O or event wait} (waiting);
    \draw[darkpurple, thick, -{Stealth[scale=0.9]}] (waiting) to[bend left=24] node[left, font=\tiny] {I/O or event completion} (ready);
    \draw[darkarrow] (running) -- node[above, font=\tiny] {exit} (term);
\end{tikzpicture}
\end{center}

\subsection{Process Control Block (PCB)}
Each process is represented in the operating system by a \textbf{Process Control Block (PCB)}:

\begin{darkcard}{Process Control Block (PCB) Fields}
\begin{itemize}
    \item \textbf{Pointer:} Pointer to next PCB in scheduling queues.
    \item \textbf{Process State:} New, ready, running, waiting, terminated.
    \item \textbf{Process Number (PID):} Unique integer identifier.
    \item \textbf{Program Counter:} Indicates the address of the next instruction to be executed.
    \item \textbf{Registers:} Accumulator, index registers, stack pointers, general purpose registers, condition code info.
    \item \textbf{Memory Limits:} Values of base and limit registers, page tables, or segment tables.
    \item \textbf{List of Open Files:} Table of file handles open by this process.
    \item \textbf{CPU Scheduling Information:} Process priority, pointers to scheduling queues, and scheduling parameters.
    \item \textbf{Accounting Information:} CPU time used, time limits, execution/account numbers, clock time / timestamps.
    \item \textbf{I/O Status Information:} Tracks all input and output operations and devices linked to the process.
\end{itemize}
\end{darkcard}

\clearpage
% ==============================================================================
\section{Process Operations \& CPU Schedulers}
% ==============================================================================

\subsection{Process Creation}
During the process lifecycle, a process may create several new processes. The creating process is called a \textbf{parent process}, and the new processes are called \textbf{children} of that process. Each of these new processes may in turn create other processes, forming a \textbf{tree of processes}.

\subsubsection*{Process Tree Hierarchy (\texttt{pstree})}
Operating systems identify processes with a unique \textbf{Process Identifier (PID)}, which is typically an integer number.

\begin{center}
\begin{tikzpicture}[
    level 1/.style={sibling distance=3.2cm, level distance=1.0cm},
    level 2/.style={sibling distance=2.0cm, level distance=0.9cm},
    every node/.style={darknode, font=\tiny}
]
\node[draw=accentBlue] {init (pid = 1)}
    child { node[draw=accentGreen] {login (pid = 8415)}
        child { node {bash (pid = 8416)}
            child { node {pid = 9204} }
            child { node {pid = 9205} }
        }
    }
    child { node[draw=accentPurple] {kthreadd (pid = 2)}
        child { node {pid = 6} }
        child { node {pid = 200} }
    }
    child { node[draw=accentOrange] {sshd (pid = 3028)}
        child { node {sshd (pid = 3610)} }
    };
\end{tikzpicture}
\end{center}

\begin{conceptcard}{Execution \& Address Space Alternatives}
\textbf{Execution Possibilities:} (1) Parent continues to execute concurrently with its children, OR (2) Parent waits until some or all of its children have terminated.\\
\textbf{Address Space Possibilities:} (1) Child process is a duplicate of the parent process, OR (2) Child process has a new program loaded into it.\\
\textbf{Resource Allocation:} Child may obtain resources directly from the OS, or be constrained to a subset of the parent process's resources.
\end{conceptcard}

\subsubsection*{Process Creation using System Calls: \texttt{fork()}, \texttt{exec()}, \texttt{wait()}, \texttt{exit()}}
\begin{center}
\begin{tikzpicture}[node distance=0.9cm and 1.2cm, auto, scale=0.85, every node/.style={transform shape}]
    \node[darknode] (p_start) {Parent};
    \node[darkorange, right=1.2cm of p_start] (fork) {\texttt{pid = fork()}};
    
    \node[darkgreen, above right=0.45cm and 1.3cm of fork] (p_wait) {\texttt{wait()} (Parent: \texttt{pid > 0})};
    \node[darkpurple, below right=0.45cm and 1.3cm of fork] (c_exec) {\texttt{exec("ls")} (Child: \texttt{pid == 0})};

    \node[darkpurple, right=1.3cm of c_exec] (c_exit) {\texttt{exit()} (Terminates)};
    \node[darkgreen, right=1.3cm of p_wait] (p_resume) {Parent Resumes};

    \draw[darkarrow] (p_start) -- (fork);
    \draw[orangearrow] (fork) to[bend left=18] (p_wait);
    \draw[orangearrow] (fork) to[bend right=18] (c_exec);
    \draw[darkarrow] (c_exec) -- (c_exit);
    \draw[greenarrow] (c_exit) -- (p_wait);
    \draw[greenarrow] (p_wait) -- (p_resume);
\end{tikzpicture}
\end{center}

\subsection{Process Termination}
A process terminates when it finishes executing and asks the operating system to delete it by using the \texttt{exit()} system call.
\begin{itemize}
    \item Returns a status value to parent process (via \texttt{wait()} system call).
    \item All resources (memory, open files, I/O buffers) are deallocated by the OS.
\end{itemize}

\begin{alertbox}{Cascading Termination}
A parent may terminate children if resource limits are exceeded or the assigned task is no longer required. If a parent terminates, all its children must also be terminated (\textbf{cascading termination}).
\end{alertbox}

\subsection{Schedulers}
A \textbf{scheduler} manages multitasking by deciding which processes gain access to the CPU:
\begin{enumerate}
    \item \textbf{Long-Term (Job) Scheduler:} Selects programs from secondary memory (disk) and loads them into RAM. Controls \textbf{degree of multiprogramming} and balances CPU-bound vs. I/O-bound processes.
    \item \textbf{Short-Term (CPU) Scheduler:} Extremely fast and frequent; selects the next ready process in RAM to execute on the CPU.
    \item \textbf{Medium-Term Scheduler:} Manages memory by temporarily \textbf{swapping} blocked or idle processes out to the disk (to free up RAM) and swapping them back in when they resume.
\end{enumerate}

\clearpage
% ==============================================================================
\section{Threads and Multithreading}
% ==============================================================================

\subsection{Thread Concept}
A \textbf{thread} is a lightweight process (LWP) because it is smaller and faster.
\begin{itemize}
    \item Allows multiple tasks to run simultaneously, improving program efficiency.
    \item \textbf{Single-core:} Illusion of parallelism (concurrency). \textbf{Multicore:} True parallel execution across cores.
    \item \textbf{Thread Private State:} Program Counter (PC), register set, and stack space.
    \item \textbf{Shared State:} Code, data, and OS resources (files) within the same process.
\end{itemize}

\subsubsection*{Single-Threaded vs. Multi-Threaded Process Architecture}
\begin{center}
\begin{tikzpicture}[scale=0.76, every node/.style={transform shape}]
    % Single Threaded Box
    \draw[draw=accentBlue, thick, fill=cardDark, rounded corners=2mm] (0,0) rectangle (4.6, 4.6);
    \node[text=accentBlue, font=\scriptsize\bfseries] at (2.3, 4.2) {Single-Threaded Process};
    \draw[draw=cardBorder, fill=accentPurple!20!cardDark] (0.2, 3.3) rectangle (1.4, 3.8) node[pos=.5, text=textWhite, font=\tiny\bfseries] {Code};
    \draw[draw=cardBorder, fill=accentGreen!20!cardDark] (1.6, 3.3) rectangle (2.8, 3.8) node[pos=.5, text=textWhite, font=\tiny\bfseries] {Data};
    \draw[draw=cardBorder, fill=accentOrange!20!cardDark] (3.0, 3.3) rectangle (4.4, 3.8) node[pos=.5, text=textWhite, font=\tiny\bfseries] {Files};
    \draw[draw=cardBorder, fill=cardDark!90] (0.3, 2.2) rectangle (4.3, 3.0);
    \node[text=textWhite, font=\tiny] at (1.3, 2.6) {Registers};
    \node[text=textWhite, font=\tiny] at (3.3, 2.6) {Stack};
    \draw[draw=accentBlue, fill=accentBlue!20!cardDark, rounded corners=1mm] (0.8, 0.5) rectangle (3.8, 1.3) node[pos=.5, text=textWhite, font=\scriptsize\bfseries] {Thread $\sim$};

    % Multi Threaded Box
    \draw[draw=accentGreen, thick, fill=cardDark, rounded corners=2mm] (5.8,0) rectangle (13.6, 4.6);
    \node[text=accentGreen, font=\scriptsize\bfseries] at (9.7, 4.2) {Multi-Threaded Process};
    \draw[draw=cardBorder, fill=accentPurple!20!cardDark] (6.0, 3.3) rectangle (8.1, 3.8) node[pos=.5, text=textWhite, font=\tiny\bfseries] {Code};
    \draw[draw=cardBorder, fill=accentGreen!20!cardDark] (8.4, 3.3) rectangle (10.8, 3.8) node[pos=.5, text=textWhite, font=\tiny\bfseries] {Data};
    \draw[draw=cardBorder, fill=accentOrange!20!cardDark] (11.1, 3.3) rectangle (13.4, 3.8) node[pos=.5, text=textWhite, font=\tiny\bfseries] {Files};

    % Thread 1
    \draw[draw=cardBorder, fill=cardDark!90] (6.0, 1.6) rectangle (8.1, 3.0);
    \node[text=textWhite, font=\tiny] at (7.05, 2.65) {Registers};
    \node[text=textWhite, font=\tiny] at (7.05, 2.3) {Stack};
    \node[text=textWhite, font=\tiny] at (7.05, 1.95) {PC};
    \draw[draw=accentGreen, fill=accentGreen!20!cardDark, rounded corners=1mm] (6.0, 0.5) rectangle (8.1, 1.2) node[pos=.5, text=textWhite, font=\scriptsize\bfseries] {Thread 1 $\sim$};

    % Thread 2
    \draw[draw=cardBorder, fill=cardDark!90] (8.5, 1.6) rectangle (10.7, 3.0);
    \node[text=textWhite, font=\tiny] at (9.6, 2.65) {Registers};
    \node[text=textWhite, font=\tiny] at (9.6, 2.3) {Stack};
    \node[text=textWhite, font=\tiny] at (9.6, 1.95) {PC};
    \draw[draw=accentGreen, fill=accentGreen!20!cardDark, rounded corners=1mm] (8.5, 0.5) rectangle (10.7, 1.2) node[pos=.5, text=textWhite, font=\scriptsize\bfseries] {Thread 2 $\sim$};

    % Thread 3
    \draw[draw=cardBorder, fill=cardDark!90] (11.1, 1.6) rectangle (13.3, 3.0);
    \node[text=textWhite, font=\tiny] at (12.2, 2.65) {Registers};
    \node[text=textWhite, font=\tiny] at (12.2, 2.3) {Stack};
    \node[text=textWhite, font=\tiny] at (12.2, 1.95) {PC};
    \draw[draw=accentGreen, fill=accentGreen!20!cardDark, rounded corners=1mm] (11.1, 0.5) rectangle (13.3, 1.2) node[pos=.5, text=textWhite, font=\scriptsize\bfseries] {Thread 3 $\sim$};
\end{tikzpicture}
\end{center}

\subsection{Need of Threads}
\begin{enumerate}
    \item \textbf{Improves Performance:} Multiple tasks run simultaneously (parallel/interleaved), making programs faster.
    \item \textbf{Increase Responsiveness:} If one thread is busy, another handles user input, keeping UI responsive.
    \item \textbf{Enable Concurrency:} Multiple operations (saving, processing, input) occur simultaneously.
    \item \textbf{Better CPU Utilization:} On multicore systems, threads run on different cores to maximize CPU power.
    \item \textbf{Efficient Resource Sharing:} Threads share process memory, reducing communication overhead.
\end{enumerate}

\subsection{Components of Threads}
\begin{itemize}
    \item \textbf{Stack Space:} Stores local variables, function calls, and return addresses specific to the thread.
    \item \textbf{Register Set:} Holds temporary data and intermediate results during thread execution.
    \item \textbf{Program Counter (PC):} Tracks the current instruction being executed by the thread.
\end{itemize}

\subsection{Types of Threads}
\begin{enumerate}
    \item \textbf{User-Level Thread (ULT):} Managed entirely by application libraries; kernel is unaware of them. Fast creation and management in user space. \textit{Limitation:} If one thread makes a blocking system call, the entire process blocks.
    \item \textbf{Kernel-Level Thread (KLT):} Supported directly by the OS kernel. Slower to create and manage, but allows kernel to schedule threads on different processors; if one thread blocks, others continue.
\end{enumerate}

\clearpage
% ==============================================================================
\section{Inter-Process Communication (IPC)}
% ==============================================================================

\begin{defbox}
    \textbf{\textcolor{accentBlue}{IPC Definition:}} \textbf{Inter-Process Communication (IPC)} is a mechanism that allows processes to communicate and share data with each other while they are running.
\end{defbox}

\begin{itemize}
    \item Since each process has its own memory space, IPC provides controlled methods for exchanging information.
    \item Helps processes work together efficiently, safely, and avoid conflicts while accessing shared resources.
\end{itemize}

\subsection{Two Models of IPC}
\begin{enumerate}
    \item \textbf{Shared Memory Model:} A region of shared memory is created within the address space of a process. Other processes attach to this shared memory segment. Fastest method (memory speed); synchronization is managed by the application.
    \item \textbf{Message Passing Model:} Processes exchange messages via the OS kernel without sharing address space. Ideal for distributed and networked environments.
\end{enumerate}

\begin{center}
\begin{tikzpicture}[scale=0.76, every node/.style={transform shape}]
    % Model 1: Shared Memory
    \draw[draw=accentBlue, thick, fill=cardDark, rounded corners=2mm] (0,0) rectangle (6.2, 3.8);
    \node[text=accentBlue, font=\scriptsize\bfseries] at (3.1, 3.4) {Shared Memory};
    \draw[draw=cardBorder, fill=accentBlue!20!cardDark] (0.4, 2.2) rectangle (2.8, 2.9) node[pos=.5, text=textWhite, font=\tiny\bfseries] {Process A};
    \draw[draw=cardBorder, fill=accentGreen!20!cardDark] (3.4, 2.2) rectangle (5.8, 2.9) node[pos=.5, text=textWhite, font=\tiny\bfseries] {Process B};
    \draw[draw=accentOrange, fill=accentOrange!20!cardDark, rounded corners=1mm] (1.3, 1.1) rectangle (4.9, 1.7) node[pos=.5, text=textWhite, font=\tiny\bfseries] {Shared Memory};
    \draw[darkarrow, <->] (1.6, 2.2) -- (2.3, 1.7);
    \draw[darkarrow, <->] (4.6, 2.2) -- (3.9, 1.7);
    \draw[draw=cardBorder, fill=cardDark!90] (0.4, 0.3) rectangle (5.8, 0.75) node[pos=.5, text=textMuted, font=\tiny] {Kernel (setup only)};

    % Model 2: Message Passing
    \draw[draw=accentGreen, thick, fill=cardDark, rounded corners=2mm] (7.2,0) rectangle (13.6, 3.8);
    \node[text=accentGreen, font=\scriptsize\bfseries] at (10.4, 3.4) {Message Passing};
    \draw[draw=cardBorder, fill=accentBlue!20!cardDark] (7.6, 2.2) rectangle (10.0, 2.9) node[pos=.5, text=textWhite, font=\tiny\bfseries] {Process A};
    \draw[draw=cardBorder, fill=accentGreen!20!cardDark] (10.8, 2.2) rectangle (13.2, 2.9) node[pos=.5, text=textWhite, font=\tiny\bfseries] {Process B};
    \draw[draw=accentPurple, fill=accentPurple!20!cardDark, rounded corners=1mm] (7.6, 0.4) rectangle (13.2, 1.3);
    \node[text=accentPurple, font=\tiny\bfseries] at (10.4, 1.0) {Kernel Message Queue};
    \draw[orangearrow, ->] (8.8, 2.2) -- node[left, font=\tiny] {\texttt{send()}} (8.8, 1.3);
    \draw[greenarrow, ->] (12.0, 1.3) -- node[right, font=\tiny] {\texttt{receive()}} (12.0, 2.2);
\end{tikzpicture}
\end{center}

\subsection{Message Passing Operations \& Links}
Primitives: \texttt{send(message)} and \texttt{receive(message)}. Messages may be of fixed or variable size.

\subsubsection{Direct vs. Indirect Communication}
\begin{itemize}
    \item \textbf{Direct Communication:} Senders and receivers explicitly name each other:
    \begin{itemize}
        \item \texttt{send(P, message)}: Send a message to Process $P$.
        \item \texttt{receive(Q, message)}: Receive a message from Process $Q$.
    \end{itemize}
    \item \textbf{Indirect Communication:} Messages are sent/received through shared \textbf{mailboxes} or \textbf{ports}:
    \begin{itemize}
        \item Each mailbox has a unique ID (e.g., POSIX message queues).
        \item \texttt{send(A, message)}: Send message to Mailbox $A$.
        \item \texttt{receive(A, message)}: Receive message from Mailbox $A$.
    \end{itemize}
\end{itemize}

\subsubsection{Synchronization Schemes}
\begin{itemize}
    \item \textbf{Blocking Send:} Sender is blocked until the message is received by receiver or mailbox.
    \item \textbf{Non-Blocking Send:} Sender sends the message and immediately resumes operation.
    \item \textbf{Blocking Receive:} Receiver blocks until a message is available.
    \item \textbf{Non-Blocking Receive:} Receiver retrieves either a valid message or null.
\end{itemize}

\subsubsection{Buffering Capacity}
\begin{itemize}
    \item \textbf{Zero Capacity:} Queue length is 0. Sender must block until receiver receives (rendezvous).
    \item \textbf{Bounded Capacity:} Queue has finite length $n$. Sender blocks only if queue is completely full.
    \item \textbf{Unbounded Capacity:} Queue length is infinite. Sender never blocks.
\end{itemize}

\clearpage
% ==============================================================================
\section{Process Synchronization \& Critical Section Problem}
% ==============================================================================

\begin{itemize}
    \item \textbf{Independent Process:} Execution of one process does not affect the execution of others.
    \item \textbf{Cooperative Process:} Execution of one process \textbf{affects} the execution of other processes.
\end{itemize}

\begin{defbox}
    \textbf{\textcolor{accentBlue}{Critical Section Problem:}} A \textbf{Critical Section (CS)} is a code segment in a program that accesses shared variables or resources. Only one process can access the critical section at a time; other processes must be in a \textbf{wait state}.
\end{defbox}

\subsection{Standard Structure of a Process}
\begin{lstlisting}[language=C]
do {
    /* 1. ENTRY SECTION  (Controls entry into CS, acquires lock on resources) */
    
        /* 2. CRITICAL SECTION (Accesses shared variables) */
        
    /* 3. EXIT SECTION   (Releases lock on resources & notifies others) */
    
    /* 4. REMAINDER SECTION (Non-critical computation) */
} while (true);
\end{lstlisting}

\subsection{Three Mandatory Criteria for Solution to C.S. Problem}
\begin{conceptcard}{1. Mutual Exclusion}
If a process is executing in its critical section, no other process is allowed to execute in its critical section.
\end{conceptcard}

\begin{conceptcard}{2. Progress}
If no process is executing in its critical section and some processes wish to enter, only those processes that are \textbf{not executing in their remainder section} can participate in the decision on which will enter next, and this selection \textbf{cannot be postponed indefinitely}.
\end{conceptcard}

\begin{conceptcard}{3. Bounded Waiting}
There exists a bound on the number of times other processes are allowed to enter their critical section after a process has made a request to enter, before that request is granted (prevents starvation).
\end{conceptcard}

\subsection{Two-Process Software Solutions}

\subsubsection{Algorithm 1: Strict Alternation (Turn Variable)}
Runs in user mode. Uses shared integer \texttt{int turn;} initialized to 0 or 1.

\begin{lstlisting}[language=C]
// Code for Process Pi
do {
    while (turn != i);  // Spinlock / Busy waiting (Entry Section)
    
    /* CRITICAL SECTION */
    
    turn = j;           // Exit Section
    
    /* REMAINDER SECTION */
} while (true);
\end{lstlisting}

\begin{alertbox}{Analysis of Algorithm 1}
\begin{itemize}
    \item \textbf{Mutual Exclusion:} Ensured (since \texttt{turn} can only be $i$ or $j$).
    \item \textbf{Progress:} \textbf{NOT satisfied.} Requires strict alternation. If $P_0$ exits and does not want to enter again, $P_1$ cannot enter either because $P_0$ never sets \texttt{turn = 1}.
\end{itemize}
\end{alertbox}

\clearpage
% ------------------------------------------------------------------------------
\subsubsection{Algorithm 2: Flag Array (Desire to Enter)}
% ------------------------------------------------------------------------------
Uses a boolean array \texttt{boolean flag[2];} initialized to \texttt{false}. \texttt{flag[i] = true} indicates $P_i$ is ready to enter CS.

\begin{lstlisting}[language=C]
// Code for Process Pi
do {
    flag[i] = true;     // Signal intent to enter CS
    while (flag[j]);    // Wait if Pj is also ready
    
    /* CRITICAL SECTION */
    
    flag[i] = false;    // Signal exit from CS
    
    /* REMAINDER SECTION */
} while (true);
\end{lstlisting}

\begin{alertbox}{Analysis of Algorithm 2}
\begin{itemize}
    \item \textbf{Mutual Exclusion:} Satisfied.
    \item \textbf{Progress \& Bounded Waiting:} \textbf{NOT satisfied (Deadlock).} If both $P_i$ and $P_j$ set their flag to \texttt{true} simultaneously, both wait forever in the \texttt{while} loop.
\end{itemize}
\end{alertbox}

% ------------------------------------------------------------------------------
\subsubsection{Algorithm 3: Peterson's Solution}
% ------------------------------------------------------------------------------
Peterson's solution is a complete two-process software solution. Processes share two variables:
\begin{lstlisting}[language=C]
int turn;
boolean flag[2];
\end{lstlisting}
\begin{itemize}
    \item \texttt{turn}: Indicates whose turn it is to enter C.S. (\texttt{turn = i} implies turn of Process $P_i$).
    \item \texttt{flag}: Used to indicate if a process is ready to enter C.S. (\texttt{flag[i] = true} implies Process $P_i$ is ready).
\end{itemize}

\noindent
\begin{minipage}[t]{0.48\textwidth}
\begin{conceptcard}{Process $P_i$}
\begin{lstlisting}[language=C]
while (true) {
    flag[i] = true;
    turn = j;
    while (flag[j] && turn == j);
    
    /* CRITICAL SECTION */
    
    flag[i] = false;
    
    /* REMAINDER SECTION */
}
\end{lstlisting}
\end{conceptcard}
\end{minipage}
\hfill
\begin{minipage}[t]{0.48\textwidth}
\begin{conceptcard}{Process $P_j$}
\begin{lstlisting}[language=C]
while (true) {
    flag[j] = true;
    turn = i;
    while (flag[i] && turn == i);
    
    /* CRITICAL SECTION */
    
    flag[j] = false;
    
    /* REMAINDER SECTION */
}
\end{lstlisting}
\end{conceptcard}
\end{minipage}

\vspace{0.4em}
\begin{conceptcard}{Key Properties of Peterson's Solution}
\begin{itemize}
    \item Provides a complete algorithmic solution to C.S. problems for two processes.
    \item Addresses the requirements of \textbf{Mutual Exclusion}, \textbf{Progress}, and \textbf{Bounded Waiting}.
\end{itemize}
\end{conceptcard}

\begin{alertbox}{Limitation on Modern Architectures}
\begin{itemize}
    \item \textbf{Not guaranteed to work on modern architectures.}
    \item To improve performance, modern processors and/or compilers may reorder operations that have no dependencies.
    \item Modern OS systems rely on hardware-supported atomic operations (e.g., \texttt{TestAndSet}, \texttt{CompareAndSwap}) and memory barriers.
\end{itemize}
\end{alertbox}

\end{document}
'''

tex_path = '/home/sudheesh/Documents/CET/S5/MOS/MOS_notes.tex'
with open(tex_path, 'w') as f:
    f.write(tex_content)

# Compile 2 passes
subprocess.run(['pdflatex', '-interaction=nonstopmode', '-jobname=MOS_Neat_DarkMode', 'MOS_notes.tex'], cwd='/home/sudheesh/Documents/CET/S5/MOS', check=True)
subprocess.run(['pdflatex', '-interaction=nonstopmode', '-jobname=MOS_Neat_DarkMode', 'MOS_notes.tex'], cwd='/home/sudheesh/Documents/CET/S5/MOS', check=True)
print('Compilation completed successfully!')
