local pdfs = {
  {
    key = "part1",
    pdf = "build/part1.pdf",
    original = "EM_Module 3_Part1 (1).pdf",
    label = "Part 1",
    title = "Synchronous Generator Basics, EMF Equation and Construction",
    summary = "Principle of operation, AC generation, EMF equation, rotor and stator construction, and alternator classification.",
  },
  {
    key = "part2",
    pdf = "build/part2.pdf",
    original = "EM_Module 3_Part2.pdf",
    label = "Part 2",
    title = "Load Operation, Regulation and Synchronisation",
    summary = "Armature reaction, synchronous impedance, phasor diagrams, voltage regulation, and methods of synchronisation.",
  },
  {
    key = "part3",
    pdf = "build/part3.pdf",
    original = "EM_Module 3_Part3.pdf",
    label = "Part 3",
    title = "Synchronous Motor Construction and Starting",
    summary = "Construction of the synchronous motor, principle of operation, failure to self-start, starting methods, and equivalent circuit.",
  },
}

local accents = { "anthOrange", "anthBlue", "anthGreen" }

local function shell_quote(value)
  return "'" .. value:gsub("'", "'\\''") .. "'"
end

local function run(command)
  local handle = assert(io.popen(command, "r"))
  local data = handle:read("*a")
  local ok, why, code = handle:close()
  if ok == nil then
    error(string.format("command failed (%s): %s", tostring(code or why), command))
  end
  return data
end

local font_catalog = run("fc-list")

local function has_font(name)
  return font_catalog:lower():find(name:lower(), 1, true) ~= nil
end

local function trim(value)
  return (value:gsub("^%s+", ""):gsub("%s+$", ""))
end

local function starts_with_bullet(line)
  return line:match("^[•*%-]%s+") or line:match("^%d+[.)]%s+") or line:match("^[ivxIVX]+%)%s+")
end

local function strip_leading_marker(line)
  line = line:gsub("^[•]%s*", "")
  line = line:gsub("^[-*]%s*", "")
  return trim(line)
end

local glyph_map = {
  [""] = "=",
  [""] = "(",
  [""] = ")",
  [""] = "θ",
  [""] = "ω",
  [""] = "Φ",
  [""] = "φ",
  [""] = "•",
  [""] = "→",
  [""] = "⇒",
}

local function normalise_glyphs(text)
  text = text:gsub("\r", "")
  for source, target in pairs(glyph_map) do
    text = text:gsub(source, target)
  end
  text = text:gsub("→", "->")
  text = text:gsub("⇒", "=>")
  text = text:gsub("mmfmethod", "mmf method")
  text = text:gsub("Lamp MethoSynchronization of 1%-Phase Alternatorsd", "Lamp Method Synchronisation of Single-Phase Alternators")
  text = text:gsub("frequency of flick", "frequency of flicker")
  return text
end

local function clean_page(page_text)
  page_text = normalise_glyphs(page_text)

  local raw_lines = {}
  for raw_line in page_text:gmatch("([^\n]*)\n?") do
    if raw_line == "" and #raw_lines > 0 and raw_lines[#raw_lines] == "\0END\0" then
      break
    end
    raw_lines[#raw_lines + 1] = raw_line
  end

  local cleaned = {}
  local previous_index = nil

  for _, raw_line in ipairs(raw_lines) do
    local stripped = trim(raw_line)
    local indent = raw_line:match("^(%s*)") or ""

    if stripped == "" then
      if #cleaned > 0 and cleaned[#cleaned] ~= "" then
        cleaned[#cleaned + 1] = ""
      end
    elseif stripped:match("^%d+$") and #stripped <= 3 then
      -- skip standalone slide/page numbers
    elseif previous_index
      and cleaned[previous_index]
      and cleaned[previous_index] ~= ""
      and #indent >= 2
      and not starts_with_bullet(stripped)
      and not stripped:match("^[A-Z][A-Z%s%-]+$")
    then
      cleaned[previous_index] = cleaned[previous_index] .. " " .. stripped
    else
      cleaned[#cleaned + 1] = stripped
      if stripped ~= "" then
        previous_index = #cleaned
      end
    end
  end

  while cleaned[1] == "" do
    table.remove(cleaned, 1)
  end
  while cleaned[#cleaned] == "" do
    table.remove(cleaned, #cleaned)
  end

  return cleaned
end

local function page_count(pdf)
  local info = run("pdfinfo " .. shell_quote(pdf))
  local count = info:match("Pages:%s+(%d+)")
  return tonumber(count)
end

local function extract_pages(pdf)
  local text = run("pdftotext -layout " .. shell_quote(pdf) .. " -")
  local pages = {}
  text = text:gsub("\r", "")
  if not text:find("\f", 1, true) then
    pages[1] = text
    return pages
  end

  for page in (text .. "\f"):gmatch("(.-)\f") do
    pages[#pages + 1] = page
  end
  if #pages > 0 and trim(pages[#pages]) == "" then
    table.remove(pages, #pages)
  end
  return pages
end

local function tex_escape(text)
  local replacements = {
    ["\\"] = "\\textbackslash{}",
    ["{"] = "\\{",
    ["}"] = "\\}",
    ["$"] = "\\$",
    ["&"] = "\\&",
    ["#"] = "\\#",
    ["%"] = "\\%",
    ["_"] = "\\_",
    ["^"] = "\\textasciicircum{}",
    ["~"] = "\\textasciitilde{}",
  }

  return (text:gsub("[\\{}$&#%%_^~]", replacements))
end

local function choose_title(lines, page_number)
  if #lines == 0 then
    return "Slide " .. page_number, {}
  end

  if lines[1]:match("^PCEOT%d+$") or lines[1]:match("^MODULE%s+[IVX]+$") then
    local title_parts = {}
    local body_start = 1
    for index, line in ipairs(lines) do
      if line == "" then
        body_start = index + 1
        break
      end
      if #title_parts < 4 then
        title_parts[#title_parts + 1] = line
        body_start = index + 1
      end
    end
    local body = {}
    for index = body_start, #lines do
      body[#body + 1] = lines[index]
    end
    return table.concat(title_parts, " · "), body
  end

  if starts_with_bullet(lines[1]) then
    local title = strip_leading_marker(lines[1])
    local body = {}
    for index = 2, #lines do
      body[#body + 1] = lines[index]
    end
    return title ~= "" and title or ("Slide " .. page_number), body
  end

  local title = lines[1]
  local body = {}
  for index = 2, #lines do
    body[#body + 1] = lines[index]
  end

  return title, body
end

local function normalise_title_text(text)
  local replacements = {
    ["Φ"] = "Phi",
    ["φ"] = "phi",
    ["θ"] = "theta",
    ["ω"] = "omega",
    ["δ"] = "delta",
    ["Δ"] = "Delta",
    ["->"] = "to",
    ["=>"] = "implies",
  }

  for source, target in pairs(replacements) do
    text = text:gsub(source, target)
  end
  return text
end

local function body_to_tex(lines, accent)
  if #lines == 0 then
    return "\\textit{This slide is primarily a title page or visual reference. The original slide is preserved in the appendix.}\n"
  end

  local chunks = {}
  for _, line in ipairs(lines) do
    if line == "" then
      chunks[#chunks + 1] = "\\smallskip\n"
    else
      local bullet = line:match("^([•*%-])%s+(.+)$")
      local numbered_a, numbered_b = line:match("^(%d+[.)])%s+(.+)$")

      if bullet then
        local content = strip_leading_marker(line)
        chunks[#chunks + 1] = string.format("\\textcolor{%s}{\\textbullet}\\hspace{0.65em}%s\\\\\n", accent, tex_escape(content))
      elseif numbered_a and numbered_b then
        chunks[#chunks + 1] = string.format("\\textcolor{%s}{\\textbf{%s}}\\hspace{0.5em}%s\\\\\n", accent, tex_escape(numbered_a), tex_escape(numbered_b))
      else
        chunks[#chunks + 1] = tex_escape(line) .. "\\\\\n"
      end
    end
  end

  return table.concat(chunks)
end

local function write_line(handle, text)
  handle:write(text)
  handle:write("\n")
end

local output = assert(io.open("EM_Module3_Anthropic_Study_Guide.tex", "w"))
local body_font = has_font("Lora") and "Lora" or (has_font("Georgia") and "Georgia" or "Liberation Serif")
local heading_font = has_font("Poppins") and "Poppins" or (has_font("Arial") and "Arial" or "Liberation Sans")

write_line(output, "\\documentclass[11pt,a4paper]{article}")
write_line(output, "\\usepackage[a4paper,margin=18mm]{geometry}")
write_line(output, "\\usepackage{fontspec}")
write_line(output, "\\usepackage{xcolor}")
write_line(output, "\\usepackage{graphicx}")
write_line(output, "\\usepackage{tikz}")
write_line(output, "\\usepackage{titlesec}")
write_line(output, "\\usepackage{hyperref}")
write_line(output, "\\usepackage{mdframed}")
write_line(output, "\\usepackage{pdflscape}")
write_line(output, "\\usepackage{fancyhdr}")
write_line(output, "\\usepackage{setspace}")
write_line(output, "\\usepackage{enumitem}")
write_line(output, "\\usepackage{parskip}")
write_line(output, "\\usepackage{needspace}")
write_line(output, "")
write_line(output, "\\definecolor{anthDark}{HTML}{141413}")
write_line(output, "\\definecolor{anthLight}{HTML}{FAF9F5}")
write_line(output, "\\definecolor{anthMid}{HTML}{B0AEA5}")
write_line(output, "\\definecolor{anthSoft}{HTML}{E8E6DC}")
write_line(output, "\\definecolor{anthOrange}{HTML}{D97757}")
write_line(output, "\\definecolor{anthBlue}{HTML}{6A9BCC}")
write_line(output, "\\definecolor{anthGreen}{HTML}{788C5D}")
write_line(output, "")
write_line(output, "\\pagecolor{anthLight}")
write_line(output, "\\color{anthDark}")
write_line(output, "")
write_line(output, string.format("\\setmainfont{%s}[Ligatures=TeX]", body_font))
write_line(output, string.format("\\newfontfamily\\HeadingFont{%s}[Ligatures=TeX]", heading_font))
write_line(output, "")
write_line(output, "\\setstretch{1.08}")
write_line(output, "\\setlength{\\parindent}{0pt}")
write_line(output, "\\setlength{\\parskip}{0.45em}")
write_line(output, "\\setlength{\\headheight}{22pt}")
write_line(output, "")
write_line(output, "\\hypersetup{colorlinks=true,linkcolor=anthOrange,urlcolor=anthBlue,pdfauthor={OpenAI Codex},pdftitle={EM Module 3 Anthropic Study Guide}}")
write_line(output, "")
write_line(output, "\\titleformat{\\section}{\\HeadingFont\\fontsize{24}{28}\\selectfont\\color{anthDark}}{}{0pt}{}")
write_line(output, "\\titleformat{\\subsection}{\\HeadingFont\\fontsize{16}{20}\\selectfont\\color{anthDark}}{}{0pt}{}")
write_line(output, "\\pagestyle{fancy}")
write_line(output, "\\fancyhf{}")
write_line(output, "\\fancyhead[L]{\\HeadingFont\\small EM Module 3 Study Guide}")
write_line(output, "\\fancyhead[R]{\\color{anthMid}\\small Synchronous Machines}")
write_line(output, "\\fancyfoot[C]{\\color{anthMid}\\thepage}")
write_line(output, "\\renewcommand{\\headrulewidth}{0.2pt}")
write_line(output, "\\renewcommand{\\headrule}{\\hbox to\\headwidth{\\color{anthSoft}\\leaders\\hrule height \\headrulewidth\\hfill}}")
write_line(output, "")
write_line(output, "\\newcommand{\\partsummary}[3]{%")
write_line(output, "  \\begin{mdframed}[roundcorner=8pt,backgroundcolor=anthSoft,linecolor=#1,linewidth=1.2pt,innerleftmargin=12pt,innerrightmargin=12pt,innertopmargin=10pt,innerbottommargin=10pt,skipabove=8pt,skipbelow=10pt]")
write_line(output, "  {\\HeadingFont\\fontsize{15}{18}\\selectfont #2}\\par")
write_line(output, "  \\vspace{0.35em}")
write_line(output, "  {\\color{anthDark}#3}")
write_line(output, "  \\end{mdframed}")
write_line(output, "}")
write_line(output, "")
write_line(output, "\\begin{document}")
write_line(output, "\\begin{titlepage}")
write_line(output, "\\thispagestyle{empty}")
write_line(output, "\\begin{tikzpicture}[remember picture,overlay]")
write_line(output, "  \\fill[anthLight] (current page.south west) rectangle (current page.north east);")
write_line(output, "  \\fill[anthOrange!18] ([xshift=-12mm,yshift=-18mm]current page.north east) circle [radius=25mm];")
write_line(output, "  \\fill[anthBlue!20] ([xshift=18mm,yshift=20mm]current page.south west) circle [radius=28mm];")
write_line(output, "  \\fill[anthGreen!18] ([xshift=-5mm,yshift=55mm]current page.south east) rectangle ++(-38mm,18mm);")
write_line(output, "  \\fill[anthSoft] ([xshift=0mm,yshift=-40mm]current page.north west) rectangle ++(\\paperwidth,-20mm);")
write_line(output, "\\end{tikzpicture}")
write_line(output, "\\vspace*{24mm}")
write_line(output, "{\\HeadingFont\\fontsize{30}{34}\\selectfont\\color{anthDark}Electrical Machines\\\\[0.2em]Module 3 Study Guide\\par}")
write_line(output, "\\vspace{5mm}")
write_line(output, "{\\HeadingFont\\fontsize{15}{18}\\selectfont\\color{anthOrange}Synchronous Machines\\par}")
write_line(output, "\\vspace{10mm}")
write_line(output, "{\\large This guide combines all three source slide decks into one branded study PDF. It includes cleaned reading notes first and every original slide in the appendix so no material is lost.\\par}")
write_line(output, "\\vfill")
write_line(output, "\\begin{mdframed}[roundcorner=8pt,backgroundcolor=anthDark,linecolor=anthDark,linewidth=0pt,innerleftmargin=14pt,innerrightmargin=14pt,innertopmargin=10pt,innerbottommargin=10pt]")
write_line(output, "{\\color{anthLight}\\HeadingFont\\fontsize{13}{16}\\selectfont Anthropic Brand Styling}\\par")
write_line(output, "{\\color{anthLight}\\small Palette: \\texttt{\\#141413}, \\texttt{\\#FAF9F5}, \\texttt{\\#B0AEA5}, \\texttt{\\#E8E6DC}, \\texttt{\\#D97757}, \\texttt{\\#6A9BCC}, \\texttt{\\#788C5D}. Headings use Poppins when available. Body text uses Lora when available, with serif fallback when not present on the system.}")
write_line(output, "\\end{mdframed}")
write_line(output, "\\vspace{8mm}")
write_line(output, "{\\color{anthMid}\\small Generated from: EM\\_Module 3\\_Part1 (1).pdf, EM\\_Module 3\\_Part2.pdf, EM\\_Module 3\\_Part3.pdf\\par}")
write_line(output, "\\end{titlepage}")
write_line(output, "")
write_line(output, "\\tableofcontents")
write_line(output, "\\clearpage")
write_line(output, "")
write_line(output, "\\section{Module Roadmap}")
write_line(output, "This document is structured in two layers: a readable study section for revision, followed by a full appendix containing every original slide exactly as supplied.")
write_line(output, "")
write_line(output, "\\partsummary{anthOrange}{Part 1: Generator Fundamentals}{Principle of operation of the 3-phase synchronous generator, AC generation, EMF equation, and the main constructional classifications of alternators.}")
write_line(output, "\\partsummary{anthBlue}{Part 2: Load Behaviour and Synchronisation}{Armature reaction, synchronous impedance, phasor diagrams, voltage regulation by EMF and MMF methods, and synchronising conditions and lamp methods.}")
write_line(output, "\\partsummary{anthGreen}{Part 3: Synchronous Motor}{Construction, working principle, why the motor is not self-starting, starting methods, and the basic equivalent-circuit idea.}")
write_line(output, "")
write_line(output, "\\section{Study Notes}")
write_line(output, "The note cards below are cleaned from the slide text for easier reading. Use the appendix whenever a page is mainly diagrammatic or whenever you want the exact original slide layout.")
write_line(output, "")

local total_slides = 0

for part_index, pdf in ipairs(pdfs) do
  local pages = extract_pages(pdf.pdf)
  local expected_pages = page_count(pdf.pdf)
  if expected_pages ~= #pages then
    io.stderr:write(string.format("warning: %s expected %d pages, extracted %d segments\n", pdf.original, expected_pages, #pages))
  end

  write_line(output, string.format("\\subsection{%s}", tex_escape(pdf.label .. ": " .. pdf.title)))
  write_line(output, tex_escape(pdf.summary))
  write_line(output, "")

  for page_number, page_text in ipairs(pages) do
    total_slides = total_slides + 1
    local lines = clean_page(page_text)
    local title, body = choose_title(lines, page_number)
    title = normalise_title_text(title)
    local accent = accents[((total_slides - 1) % #accents) + 1]

    write_line(output, "\\Needspace{12\\baselineskip}")
    write_line(output, string.format("\\begin{mdframed}[roundcorner=9pt,backgroundcolor=white,linecolor=%s,linewidth=1pt,innerleftmargin=12pt,innerrightmargin=12pt,innertopmargin=10pt,innerbottommargin=10pt,skipabove=8pt,skipbelow=10pt]", accent))
    write_line(output, string.format("{\\HeadingFont\\fontsize{15}{18}\\selectfont\\color{anthDark}%s\\par}", tex_escape(title)))
    write_line(output, string.format("{\\color{anthMid}\\small %s \\textbullet{} Slide %d \\textbullet{} Source: %s\\par}", tex_escape(pdf.label), page_number, tex_escape(pdf.original)))
    write_line(output, "\\vspace{0.5em}")
    write_line(output, "{\\small")
    write_line(output, body_to_tex(body, accent))
    write_line(output, "}")
    write_line(output, "\\end{mdframed}")
    write_line(output, "")
  end
end

write_line(output, "\\clearpage")
write_line(output, "\\section{Original Slide Appendix}")
write_line(output, "Every source slide is embedded below for exact reference. This appendix preserves diagrams, formula layouts, and any visual content that may not extract cleanly as text.")
write_line(output, "")

for _, pdf in ipairs(pdfs) do
  local count = page_count(pdf.pdf)
  write_line(output, string.format("\\subsection{%s}", tex_escape(pdf.label .. ": Original Slides")))
  write_line(output, "")
  for page = 1, count do
    write_line(output, "\\clearpage")
    write_line(output, "\\begin{landscape}")
    write_line(output, "\\thispagestyle{fancy}")
    write_line(output, string.format("{\\HeadingFont\\fontsize{15}{18}\\selectfont %s \\textbullet{} Slide %d\\par}", tex_escape(pdf.label), page))
    write_line(output, string.format("{\\color{anthMid}\\small Source: %s\\par}", tex_escape(pdf.original)))
    write_line(output, "\\vspace{0.6em}")
    write_line(output, "\\begin{center}")
    write_line(output, string.format("\\includegraphics[page=%d,width=0.92\\linewidth,height=0.82\\textheight,keepaspectratio]{%s}", page, tex_escape(pdf.pdf)))
    write_line(output, "\\end{center}")
    write_line(output, "\\end{landscape}")
  end
end

write_line(output, "\\end{document}")
output:close()
