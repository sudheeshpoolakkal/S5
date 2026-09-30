# -*- coding: utf-8 -*-
"""Section 7: Master Formula Sheet & Exam Quick Revision Summary"""

def get_section():
    return r'''
\section{Master Formula Sheet \& Quick Revision Tables}

\subsection{Master Analytical Formula Matrix}

\begin{table}[htbp]
\centering
\small
\caption{Module 3 Master Analytical Formula Cheat-Sheet for Fast Exam Revision}
\label{tab:module3_master_formulas}
\begin{tabularx}{\textwidth}{l p{5.5cm} X}
\toprule
\textbf{Topic / Circuit} & \textbf{Key Formulas / Governing Equations} & \textbf{Exam Tips \& Critical Insights} \\
\midrule
\textbf{ACVC ($R$ Load)} &
$V_{or} = V_s \sqrt{1 - \frac{\alpha}{\pi} + \frac{\sin 2\alpha}{2\pi}}$ \newline
$\text{PF} = \frac{V_{or}}{V_s} = \sqrt{1 - \frac{\alpha}{\pi} + \frac{\sin 2\alpha}{2\pi}}$ &
At $\alpha=0 \implies V_{or}=V_s, \text{PF}=1.0$. \newline
At $\alpha=90^\circ \implies V_{or}=0.707 V_s, \text{PF}=0.707$. \newline
At $\alpha=180^\circ \implies V_{or}=0, \text{PF}=0$. \\
\midrule
\textbf{ACVC ($RL$ Load)} &
$i_o(\omega t) = \frac{V_m}{Z}[\sin(\omega t-\phi) - \sin(\alpha-\phi)e^{-\frac{R}{\omega L}(\omega t-\alpha)}]$ \newline
$\sin(\beta-\phi) = \sin(\alpha-\phi)e^{-\frac{R}{\omega L}(\beta-\alpha)}$ \newline
$V_{or} = V_s \sqrt{\frac{1}{\pi}[(\beta-\alpha) - \frac{\sin 2\beta - \sin 2\alpha}{2}]}$ &
\textbf{Rule:} $\alpha \ge \phi = \arctan(\omega L / R)$. \newline
If $\alpha = \phi \implies \beta = \pi + \alpha \implies \gamma = 180^\circ$ (continuous sinusoidal current). \newline
Requires high-frequency pulse train gating! \\
\midrule
\textbf{ACVC (Integral Cycle)} &
$k = \frac{n}{n+m}$, \quad $V_{or} = V_s \sqrt{k}$ \newline
$\text{PF} = \sqrt{k}$ &
Zero switching EMI ($dv/dt=0, di/dt=0$). \newline
Causes line flicker/sub-harmonics. Used for thermal loads. \\
\midrule
\textbf{Half-Bridge VSI (Square Wave)} &
$v_o = \pm V_{dc}/2$, \quad $V_{or} = V_{dc}/2$ \newline
$\hat{V}_{o1} = \frac{2}{\pi}V_{dc}$, \quad $V_{o1(rms)} = \frac{\sqrt{2}}{\pi}V_{dc} \approx 0.45 V_{dc}$ &
Requires 3-wire DC split supply. \newline
Switch voltage rating $= V_{dc}$ ($2 \times$ peak output). \\
\midrule
\textbf{Full-Bridge VSI (Square Wave)} &
$v_o = \pm V_{dc}$, \quad $V_{or} = V_{dc}$ \newline
$\hat{V}_{o1} = \frac{4}{\pi}V_{dc}$, \quad $V_{o1(rms)} = \frac{2\sqrt{2}}{\pi}V_{dc} \approx 0.90 V_{dc}$ \newline
$\text{THD}_v = \sqrt{\frac{\pi^2}{8}-1} = 48.34\%$ &
Odd harmonics only ($n=1, 3, 5, 7, \dots$). \newline
Harmonic amplitude $\hat{V}_{on} = \hat{V}_{o1}/n$. \newline
Twice the voltage, $4\times$ power of half-bridge! \\
\midrule
\textbf{Single-Phase Bipolar SPWM} &
$m_a = \frac{\hat{V}_{\text{control}}}{\hat{V}_{\text{tri}}}$, \quad $m_f = \frac{f_s}{f_o}$ \newline
$\hat{V}_{o1} = m_a V_{dc}$, \quad $V_{o1(rms)} = \frac{m_a V_{dc}}{\sqrt{2}}$ &
$m_f$ must be an odd integer (eliminates even harmonics). \newline
Lowest harmonics clustered at $m_f \pm 2$. \\
\midrule
\textbf{Single-Phase Unipolar SPWM} &
$\hat{V}_{o1} = m_a V_{dc}$, \quad $V_{o1(rms)} = \frac{m_a V_{dc}}{\sqrt{2}}$ \newline
Effective switching frequency $= 2f_s$ &
3-level output ($+V_{dc}, 0, -V_{dc}$). \newline
Harmonics around $m_f$ cancel! First cluster at $2m_f$. \newline
$LC$ filter product reduced by $4\times$! \\
\midrule
\textbf{Three-Phase SPWM (Linear)} &
$\hat{V}_{Ao1} = m_a \frac{V_{dc}}{2}$ \newline
$\hat{V}_{LL1} = \frac{\sqrt{3}}{2} m_a V_{dc} \approx 0.866 m_a V_{dc}$ \newline
$V_{LL1(rms)} = \frac{\sqrt{6}}{4} m_a V_{dc} \approx 0.6124 m_a V_{dc}$ &
Triplen harmonics ($3rd, 9th, 15th, \dots$) cancel in line-line! \newline
Choose $m_f$ as an odd multiple of 3 ($9, 15, 21, \dots$). \newline
Max linear RMS line voltage $= 0.6124 V_{dc}$. \\
\midrule
\textbf{Three-Phase Six-Step (Square)} &
$V_{LL(rms)} = \sqrt{\frac{2}{3}}V_{dc} \approx 0.8165 V_{dc}$ \newline
$V_{LL1(rms)} = \frac{\sqrt{6}}{\pi}V_{dc} \approx 0.7797 V_{dc}$ &
$180^\circ$ conduction. Output contains $n=6k \pm 1$ ($5th, 7th, 11th$). \newline
Fundamental is $27.3\%$ higher than max linear SPWM. \\
\midrule
\textbf{Third Harmonic Injection (THIPWM)} &
$v_{\text{control}} = \hat{V}_1 [\sin(\omega t) + \frac{1}{6}\sin(3\omega t)]$ \newline
$V_{LL1(rms),\text{max}} = \frac{V_{dc}}{\sqrt{2}} \approx 0.707 V_{dc}$ &
Flattens sine peak by $0.866$. \newline
\textbf{Boosts linear output voltage by 15.5\%!} \newline
Third harmonic cancels out in line-to-line output! \\
\midrule
\textbf{Blanking Time (Dead-Time)} &
$\Delta V_o = 4 f_s t_d V_{dc}$ &
Prevents DC link shoot-through. \newline
Reduces fundamental voltage, distorts zero-crossings. \\
\midrule
\textbf{Harmonics \& Power Factor} &
$\text{PF} = \left(\frac{I_{s1}}{I_s}\right) \cos\phi_1 = \frac{\cos\phi_1}{\sqrt{1 + \text{THD}_i^2}}$ \newline
$\text{THD}_i = \frac{\sqrt{I_s^2 - I_{s1}^2}}{I_{s1}}$ &
True PF $=$ Distortion Factor $\times$ Displacement Factor. \newline
Harmonics alone reduce power factor even if $\cos\phi_1 = 1.0$! \\
\midrule
\textbf{Active PFC Boost Inductor} &
$\Delta I_{L,\text{max}} = \frac{V_d}{4 f_s L} \implies L = \frac{V_d}{4 f_s \Delta I_{L,\text{max}}}$ &
Max ripple occurs at $d=0.5$ ($|v_s| = V_d/2$). \newline
Universal AC input, regulates $V_d \approx 400\text{ V}$ DC, $\text{THD}_i < 5\%$. \\
\bottomrule
\end{tabularx}
\end{table}

\subsection{Essential Examination Quick-Tips for KTU S5 EEE Students}
\begin{enumerate}[leftmargin=*]
  \item \textbf{When asked for ACVC RMS Voltage Derivation:} Always state the half-wave symmetry condition ($v_o(\omega t + \pi) = -v_o(\omega t)$), integrate $[V_m \sin\omega t]^2$ from $\alpha$ to $\pi$ (or $\alpha$ to $\beta$ for $RL$ load), convert $\sin^2\theta = \frac{1 - \cos 2\theta}{2}$, and show every intermediate integration step clearly to secure full marks.
  \item \textbf{Why $\alpha < \phi$ is prohibited in $RL$ ACVC:} Remember the physical mechanism: If $\alpha < \phi$, the current in the previous thyristor is still flowing when the next thyristor is triggered. Conduction becomes continuous, phase control is completely lost, and the converter acts as a short circuit directly connecting the load to the AC mains.
  \item \textbf{Fourier Series of Square Wave Inverter:} Write down the general half-wave symmetry property first. State why all even harmonics and DC term are zero ($a_0 = 0, a_n = 0, b_{\text{even}} = 0$). Write the general formula $\sum \frac{4V_{dc}}{n\pi}\sin(n\omega t)$ and calculate $\text{THD}_v = \sqrt{\frac{\pi^2}{8}-1} = 48.34\%$.
  \item \textbf{Bipolar vs. Unipolar PWM Comparison:} Draw the two-level vs. three-level output waveforms side-by-side. Highlight the three killer facts: (1) Effective switching frequency doubles to $2f_s$; (2) Harmonics around $m_f$ cancel out completely; (3) Output filter size drops by $4\times$.
  \item \textbf{Why Triplen Harmonics Disappear in 3-Phase Inverters:} State that triplen harmonics ($3rd, 9th, 15th, \dots$) form a zero-sequence set—they are exactly equal in magnitude and in phase in all three inverter legs ($v_{Ao,3} = v_{Bo,3} = v_{Co,3}$). When computing line-to-line voltage $v_{AB} = v_{Ao} - v_{Bo}$, they subtract to exactly zero!
  \item \textbf{Dead-Time Derivation:} Draw the leg diagram showing $S_1, S_4$ and diodes $D_1, D_4$. Explain that when both switches are off during $t_d$, the load current $i_o$ forces either $D_1$ or $D_4$ to conduct depending solely on the sign of $i_o$, subtracting or adding volt-seconds to the output pulse.
  \item \textbf{IEEE 519 PCC Rule:} Remember that IEEE 519 applies strictly at the \textbf{Point of Common Coupling (PCC)}, NOT inside the customer plant. Limits are specified in terms of \textbf{Total Demand Distortion (TDD)} and depend directly on the short-circuit ratio $I_{sc} / I_L$.
\end{enumerate}
'''
