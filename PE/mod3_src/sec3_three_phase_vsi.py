# -*- coding: utf-8 -*-
"""Section 3: Three-Phase Pulse Width Modulated Voltage Source Inverters"""

def get_section():
    return r'''
\section{Three-Phase Pulse Width Modulated Voltage Source Inverters}

\subsection{Three-Phase Bridge Inverter Topology and Conduction Mechanics}

The three-phase voltage source inverter (Figure~\ref{fig:3ph_inverter_ckt}) is the universal industry-standard power conversion topology for variable-frequency AC motor drives (VFDs), grid-tied solar photovoltaic central inverters, wind turbine grid converters, and electric vehicle traction drives ($50\text{ kW} - 300\text{ kW}$).

The topology comprises six controlled switches ($S_1$ through $S_6$) arranged in three inverter legs ($A, B, C$) across a common DC link voltage $V_{dc}$, with six anti-parallel freewheeling diodes ($D_1$ through $D_6$).

\begin{figure}[htbp]
\centering
\includegraphics[width=0.75\textwidth]{mohan_fig_8_21_3ph_inverter_ckt.png}
\caption{Three-phase switch-mode voltage source inverter power circuit: Three phase legs ($A, B, C$) feeding a three-phase star ($Y$) or delta ($\Delta$) connected AC load from a stiff DC link capacitor bank. (Source: Ned Mohan, Fig.\ 8-21)}
\label{fig:3ph_inverter_ckt}
\end{figure}

\subsubsection{Switch Numbering and Firing Sequence}
The switches are traditionally numbered according to their natural firing sequence in a balanced three-phase cycle:
\begin{itemize}[leftmargin=*]
  \item Upper switches: $S_1$ (Phase A), $S_3$ (Phase B), $S_5$ (Phase C).
  \item Lower switches: $S_4$ (Phase A), $S_6$ (Phase B), $S_2$ (Phase C).
  \item Firing sequence: $S_1 \to S_2 \to S_3 \to S_4 \to S_5 \to S_6$, spaced by intervals of $60^\circ$ ($\pi/3$).
\end{itemize}

\subsection{Sinusoidal PWM in Three-Phase VSIs}

In three-phase SPWM, three balanced sinusoidal reference voltages displaced by $120^\circ$ are compared against a common high-frequency triangular carrier wave $v_{\text{tri}}$:
\begin{align}
v_{\text{control},A} &= \hat{V}_{\text{control}} \sin(\omega t) \notag\\
v_{\text{control},B} &= \hat{V}_{\text{control}} \sin(\omega t - 120^\circ) \notag\\
v_{\text{control},C} &= \hat{V}_{\text{control}} \sin(\omega t - 240^\circ) = \hat{V}_{\text{control}} \sin(\omega t + 120^\circ)
\end{align}

\begin{figure}[htbp]
\centering
\includegraphics[width=0.72\textwidth]{mohan_fig_8_22_3ph_pwm_waveforms.png}
\caption{Three-phase PWM waveforms and harmonic spectrum: (a) Modulation references and carrier; (b) Pole voltages $v_{Ao}$ and $v_{Bo}$; (c) Line-to-line output voltage $v_{AB}(t) = v_{Ao} - v_{Bo}$; (d) Harmonic spectrum of line-to-line voltage showing total cancellation of all triplen harmonics ($3rd, 9th, 15th, \dots$). (Source: Ned Mohan, Fig.\ 8-22)}
\label{fig:3ph_pwm_waveforms}
\end{figure}

\subsubsection{Pole Voltages and Line-to-Line Voltages}
Each leg operates identically to a single-phase half-bridge pole relative to the fictitious DC-bus midpoint $o$:
\begin{equation}
v_{Ao}(t) = \begin{cases} +V_{dc}/2, & \text{if } v_{\text{control},A} > v_{\text{tri}} \\ -V_{dc}/2, & \text{if } v_{\text{control},A} < v_{\text{tri}} \end{cases}
\end{equation}
The line-to-line output voltages are obtained by taking the difference between individual leg pole voltages:
\begin{align}
v_{AB}(t) &= v_{Ao}(t) - v_{Bo}(t) \notag\\
v_{BC}(t) &= v_{Bo}(t) - v_{Co}(t) \notag\\
v_{CA}(t) &= v_{Co}(t) - v_{Ao}(t)
\end{align}

\subsubsection{Cancellation of Triplen Harmonics in Three-Phase PWM}
A fundamental property of three-phase balanced systems is that \textbf{all triplen harmonics ($n = 3, 9, 15, 21, \dots$) are identical in magnitude and in-phase across all three phase legs}:
\begin{equation}
v_{Ao,3}(t) = v_{Bo,3}(t) = v_{Co,3}(t)
\end{equation}
Taking the line-to-line difference completely cancels all triplen harmonics:
\begin{equation}
v_{AB,3}(t) = v_{Ao,3}(t) - v_{Bo,3}(t) \equiv 0!
\end{equation}
\begin{conceptbox}[Fundamental Voltage Relationships in 3-Phase SPWM]
In the linear modulation range ($0 \le m_a \le 1.0$):
\begin{enumerate}
  \item \textbf{Peak Fundamental Pole-to-Midpoint Voltage:}
  \begin{equation}
  \hat{V}_{Ao1} = m_a \frac{V_{dc}}{2}
  \end{equation}
  \item \textbf{Peak Fundamental Line-to-Line Voltage:}
  \begin{equation}
  \hat{V}_{LL1} = \sqrt{3} \hat{V}_{Ao1} = \sqrt{3} m_a \frac{V_{dc}}{2} = \frac{\sqrt{3}}{2} m_a V_{dc} \approx 0.866 m_a V_{dc}
  \label{eq:vll1_peak}
  \end{equation}
  \item \textbf{RMS Fundamental Line-to-Line Voltage:}
  \begin{equation}
  V_{LL1(rms)} = \frac{\hat{V}_{LL1}}{\sqrt{2}} = \frac{\sqrt{3}}{2\sqrt{2}} m_a V_{dc} = \frac{\sqrt{6}}{4} m_a V_{dc} \approx 0.6124 m_a V_{dc}
  \label{eq:vll1_rms}
  \end{equation}
  \item \textbf{Maximum Linear Line-to-Line RMS Voltage ($m_a = 1.0$):}
  \begin{equation}
  V_{LL1(rms),\text{max}} = 0.6124 V_{dc}
  \end{equation}
\end{enumerate}
\end{conceptbox}

\subsubsection{Three-Phase Frequency Modulation Ratio ($m_f$) Selection Criteria}
To ensure optimum harmonic elimination in three-phase inverters, $m_f$ must adhere to two strict design criteria:
\begin{enumerate}
  \item $m_f$ must be an \textbf{odd integer}: Ensures half-wave symmetry, completely eliminating all even harmonics.
  \item $m_f$ must be an \textbf{odd multiple of 3} ($m_f = 9, 15, 21, 27, 33, \dots$):
  \begin{itemize}
    \item Forces the dominant carrier-frequency harmonic cluster to appear at $m_f$ and its multiples.
    \item Because $m_f$ is a multiple of 3, this dominant harmonic cluster becomes a \textbf{triplen harmonic}, which is \textbf{completely cancelled out from the line-to-line voltage}!
    \item The lowest harmonic sidebands remaining in the line-to-line output voltage are pushed up to $(m_f \pm 2)$ and $(m_f \pm 4)$.
  \end{itemize}
\end{enumerate}

\subsection{Overmodulation and Square-Wave Operation in Three-Phase Inverters}

\subsubsection{Overmodulation Region ($1.0 < m_a \le 3.24$)}
When $m_a$ exceeds $1.0$, the peak reference wave exceeds the carrier amplitude. The fundamental line-to-line output voltage increases beyond $0.6124 V_{dc}$, but non-linear saturation occurs and low-order non-triplen harmonics (5th, 7th, 11th, 13th) appear in the output.

\subsubsection{Square-Wave Operation ($m_a > 3.24$ / Six-Step Inverter)}
In the extreme limit, the inverter operates as a classical **six-step (square-wave) inverter**, where each switch conducts for $180^\circ$ per cycle.
\begin{itemize}[leftmargin=*]
  \item The line-to-line voltage is a six-step waveform alternating between $+V_{dc}, 0,$ and $-V_{dc}$.
  \item The Fourier series of the line-to-line voltage is:
  \begin{equation}
  v_{AB}(t) = \sum_{n=1,5,7,11,13,\dots}^{\infty} \frac{4V_{dc}}{n\pi} \cos\left(\frac{n\pi}{6}\right) \sin(n\omega t)
  \end{equation}
  Notice that for all triplen harmonics ($n = 3, 9, 15, \dots$), $\cos(n\pi/6) = 0$, confirming complete triplen elimination!
  \item \textbf{Peak Fundamental Line-to-Line Voltage:}
  \begin{equation}
  \hat{V}_{LL1,\text{square}} = \frac{4V_{dc}}{\pi} \cos\left(\frac{\pi}{6}\right) = \frac{4V_{dc}}{\pi} \frac{\sqrt{3}}{2} = \frac{2\sqrt{3}}{\pi}V_{dc} \approx 1.1026 V_{dc}
  \end{equation}
  \item \textbf{RMS Fundamental Line-to-Line Voltage in Square-Wave Mode:}
  \begin{equation}
  V_{LL1(rms),\text{square}} = \frac{\hat{V}_{LL1,\text{square}}}{\sqrt{2}} = \frac{\sqrt{6}}{\pi}V_{dc} \approx 0.7797 V_{dc}
  \end{equation}
  \item \textbf{Total RMS Value of Line-to-Line Voltage:}
  \begin{equation}
  V_{LL(rms)} = \sqrt{\frac{1}{\pi} \int_0^{2\pi/3} V_{dc}^2 d(\omega t)} = V_{dc}\sqrt{\frac{2}{3}} \approx 0.8165 V_{dc}
  \end{equation}
\end{itemize}

\subsection{Third Harmonic Injection PWM (THIPWM)}

In standard sinusoidal PWM, the maximum linear fundamental line-to-line voltage is limited to $\hat{V}_{LL1} = \frac{\sqrt{3}}{2}V_{dc} \approx 0.866 V_{dc}$ because the peak of each phase reference sine wave cannot exceed the DC rails ($\pm V_{dc}/2$) without causing overmodulation distortion.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.68\textwidth]{mod_p52_img1.jpeg}
\caption{Third Harmonic Injection PWM (THIPWM): Addition of a 3rd harmonic zero-sequence component ($\frac{1}{6}\hat{V}_m \sin 3\omega t$) flattens the reference waveform peak, preventing carrier clipping while boosting DC bus utilization by $15.5\%$. (Source: CET Lecture Slides)}
\label{fig:thipwm}
\end{figure}

\subsubsection{Mathematical Formulation of THIPWM}
By adding a triplen zero-sequence third-harmonic component to the fundamental sinusoidal reference:
\begin{equation}
v_{\text{control},A}(t) = \hat{V}_1 \left[ \sin(\omega t) + \frac{1}{6} \sin(3\omega t) \right]
\label{eq:thipwm_formula}
\end{equation}
The optimal amplitude of the injected third harmonic is exactly $\frac{1}{6} \approx 16.7\%$ of the fundamental amplitude.

\subsubsection{Why Third Harmonic Injection Works}
\begin{conceptbox}[Physics of Third Harmonic Injection]
\begin{enumerate}
  \item \textbf{Peak Flattening:} At $\omega t = \pi/2$ ($90^\circ$), where $\sin(\omega t) = 1$, the third harmonic evaluates to $\sin(3 \cdot \pi/2) = \sin(270^\circ) = -1$. The reference voltage becomes:
  \begin{equation}
  v_{\text{control}}(\pi/2) = \hat{V}_1 \left[ 1 - \frac{1}{6} \right] = \frac{5}{6} \hat{V}_1
  \end{equation}
  The peak of the reference waveform is \textbf{flattened by a factor of $\frac{\sqrt{3}}{2} \approx 0.866$}!
  \item \textbf{15.5\% Voltage Boost in Linear Range:} Because the peak is flattened, the fundamental reference amplitude $\hat{V}_1$ can be boosted by $\frac{2}{\sqrt{3}} \approx 1.1547$ ($+15.47\%$) before the waveform touches the carrier peak!
  \begin{equation}
  \hat{V}_{LL1,\text{max (THIPWM)}} = 1.1547 \times 0.866 V_{dc} = 1.000 V_{dc}
  \end{equation}
  \begin{equation}
  V_{LL1(rms),\text{max (THIPWM)}} = \frac{V_{dc}}{\sqrt{2}} \approx 0.707 V_{dc}
  \end{equation}
  This represents an immense **$15.5\%$ increase in output voltage** compared to standard SPWM ($0.707 V_{dc}$ vs $0.612 V_{dc}$) without leaving the linear modulation region!
  \item \textbf{Zero Distortion Across Load:} Because the three phases are identical and balanced, the injected third harmonic components across phase legs $A, B,$ and $C$ are in-phase and cancel completely in the line-to-line voltage:
  \begin{equation}
  v_{AB}(t) = v_{Ao}(t) - v_{Bo}(t) = \text{Pure fundamental without any 3rd harmonic!}
  \end{equation}
  \item \textbf{Equivalence to Space Vector PWM (SVPWM):} Third harmonic injection PWM produces line-to-line voltage waveforms and DC bus utilization virtually identical to Space Vector Modulation (SVM), but with the computational simplicity of carrier-based analog/digital comparators!
\end{enumerate}
\end{conceptbox}
'''
