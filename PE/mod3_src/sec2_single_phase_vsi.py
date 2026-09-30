# -*- coding: utf-8 -*-
"""Section 2: Single-Phase Switch-Mode DC-AC Voltage Source Inverters (VSI)"""

def get_section():
    return r'''
\section{Single-Phase Switch-Mode DC-AC Voltage Source Inverters (VSI)}

\subsection{Fundamental Operating Principles and Bridge Topologies}

An \textbf{Inverter} is a power electronic converter that transforms direct current (DC) electrical energy into alternating current (AC) electrical energy at a desired, precisely regulated voltage magnitude and frequency:
\begin{equation}
\text{DC Input } (V_{dc}) \xrightarrow{\text{Inverter}} \text{AC Output } (v_o(t), f_o)
\end{equation}
In a \textbf{Voltage Source Inverter (VSI)}, the DC input source is modeled as an ideal voltage source with negligible internal impedance (stiff DC bus supported by a large electrolytic DC-link capacitor bank). The output voltage waveform is strictly determined by the switching states of the converter power semiconductors, while the output current waveform is governed by the connected load impedance.

\subsubsection{Single-Phase Half-Bridge Inverter Configuration}
The single-phase half-bridge topology (Figure~\ref{fig:half_bridge}) utilizes two fully controlled semiconductor switches ($S_1, S_2$) and a three-wire split DC supply with center-tap $O$ (established by two identical series capacitors $C_1 = C_2$, each holding $V_{dc}/2$). Two anti-parallel freewheeling diodes ($D_1, D_2$) provide a continuous path for inductive load currents.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.68\textwidth]{hart_fig_8_1_half_bridge.png}
\caption{Single-phase half-bridge voltage source inverter: (a) Power circuit diagram with split DC source $V_{dc}/2$; (b) Square-wave output voltage $v_o(t)$ and inductive load current $i_o(t)$ waveforms showing conduction intervals of switches and freewheeling feedback diodes. (Source: Daniel W. Hart, Fig.\ 8-1)}
\label{fig:half_bridge}
\end{figure}

\begin{itemize}[leftmargin=*]
  \item \textbf{Interval 1 ($0 \le t < T/2$):} Switch $S_1$ is turned ON. Load terminal $A$ is connected to the positive DC rail ($+V_{dc}/2$ relative to center tap $O$):
  \begin{equation}
  v_o(t) = v_{AO}(t) = +\frac{V_{dc}}{2}
  \end{equation}
  \item \textbf{Interval 2 ($T/2 \le t < T$):} Switch $S_1$ is turned OFF, and $S_2$ is turned ON. Load terminal $A$ is connected to the negative DC rail ($-V_{dc}/2$):
  \begin{equation}
  v_o(t) = v_{AO}(t) = -\frac{V_{dc}}{2}
  \end{equation}
  \item \textbf{Freewheeling Diode Operation with Inductive Load:} If $S_1$ turns OFF while positive load current $i_o > 0$ is still flowing, inductor energy forces diode $D_2$ into conduction, clamping $v_o = -V_{dc}/2$ and feeding reactive energy back into the lower DC capacitor $C_2$ until $i_o$ decays to zero!
  \item \textbf{RMS Output Voltage:}
  \begin{equation}
  V_{or} = \sqrt{\frac{1}{T}\left[ \int_0^{T/2} \left(+\frac{V_{dc}}{2}\right)^2 dt + \int_{T/2}^T \left(-\frac{V_{dc}}{2}\right)^2 dt \right]} = \frac{V_{dc}}{2}
  \end{equation}
  \item \textbf{Major Limitations of the Half-Bridge Inverter:}
  \begin{enumerate}
    \item Requires a split three-wire DC supply or large center-tapped balancing capacitors.
    \item DC bus voltage utilization is low: the maximum peak-to-peak output voltage is only $V_{dc}$, yielding a fundamental peak of only $\hat{V}_{o1} = \frac{2}{\pi}V_{dc} \approx 0.637 V_{dc}$.
    \item Peak blocking voltage across the OFF-state switch equals the full DC supply $V_{dc} = 2 \times (V_{dc}/2)$, requiring devices rated for twice the output voltage!
  \end{enumerate}
\end{itemize}

\subsubsection{Single-Phase Full-Bridge (H-Bridge) Inverter Configuration}
The full-bridge inverter (Figure~\ref{fig:full_bridge}) eliminates the center-tap requirement by employing four controlled semiconductor switches ($S_1, S_2, S_3, S_4$) arranged in two phase legs ($A$ and $B$) across a single DC source $V_{dc}$.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.68\textwidth]{hart_fig_8_4_full_bridge.png}
\caption{Single-phase full-bridge (H-bridge) inverter: (a) Power circuit diagram; (b) Square-wave output voltage $v_o(t) = v_A - v_B$ alternating between $+V_{dc}$ and $-V_{dc}$, and inductive load current $i_o(t)$. (Source: Daniel W. Hart, Fig.\ 8-4)}
\label{fig:full_bridge}
\end{figure}

\begin{itemize}[leftmargin=*]
  \item \textbf{Diagonal Pair Conduction:}
  \begin{itemize}
    \item When switches $(S_1, S_2)$ are gated ON: $v_{Ao} = +V_{dc}/2$ and $v_{Bo} = -V_{dc}/2$, producing output voltage:
    \begin{equation}
    v_o(t) = v_{AB}(t) = v_{Ao} - v_{Bo} = +V_{dc}
    \end{equation}
    \item When switches $(S_3, S_4)$ are gated ON: $v_{Ao} = -V_{dc}/2$ and $v_{Bo} = +V_{dc}/2$, producing output voltage:
    \begin{equation}
    v_o(t) = v_{AB}(t) = -V_{dc}
    \end{equation}
  \end{itemize}
  \item \textbf{RMS Output Voltage:}
  \begin{equation}
  V_{or} = \sqrt{\frac{1}{T}\int_0^T (\pm V_{dc})^2 dt} = V_{dc}
  \end{equation}
  The full-bridge produces \textbf{twice} the output voltage of the half-bridge for the same DC link voltage, yielding four times the output power into a given load resistance!
\end{itemize}

\subsection{Fourier Analysis and Harmonic Spectrum of Square-Wave Inverters}

The square-wave output voltage $v_o(t)$ of a full-bridge inverter alternating between $+V_{dc}$ and $-V_{dc}$ possesses \textbf{odd half-wave symmetry}:
\begin{equation}
v_o(\omega t) = -v_o(\omega t + \pi) \quad \text{and} \quad v_o(-\omega t) = -v_o(\omega t)
\end{equation}
Consequently, all DC offset and all even harmonics are identically zero ($a_0 = 0$, $a_n = 0$, $b_n = 0$ for even $n$). The Fourier series contains only odd sine harmonics:
\begin{equation}
b_n = \frac{2}{\pi} \int_0^\pi V_{dc} \sin(n\omega t) d(\omega t) = \frac{2V_{dc}}{n\pi} \left[-\cos(n\omega t)\right]_0^\pi = \frac{2V_{dc}}{n\pi} \left[1 - (-1)^n\right]
\end{equation}
For odd $n$ ($n = 1, 3, 5, 7, \dots$), $1 - (-1)^n = 2$:
\begin{formulabox}[Fourier Series of Single-Phase Full-Bridge Square-Wave Inverter]
\begin{equation}
v_o(t) = \sum_{n=1,3,5,\dots}^{\infty} \frac{4V_{dc}}{n\pi} \sin(n\omega t) = \frac{4V_{dc}}{\pi} \sin(\omega t) + \frac{4V_{dc}}{3\pi} \sin(3\omega t) + \frac{4V_{dc}}{5\pi} \sin(5\omega t) + \dots
\label{eq:fourier_square_full}
\end{equation}
\end{formulabox}

\subsubsection{Key Harmonic Metrics}
\begin{itemize}[leftmargin=*]
  \item \textbf{Peak Amplitude of Fundamental:} $\hat{V}_{o1} = \frac{4V_{dc}}{\pi} \approx 1.273 V_{dc}$.
  \item \textbf{RMS Value of Fundamental:} $V_{o1(rms)} = \frac{\hat{V}_{o1}}{\sqrt{2}} = \frac{4V_{dc}}{\sqrt{2}\pi} = \frac{2\sqrt{2}}{\pi}V_{dc} \approx 0.9003 V_{dc}$.
  \item \textbf{Harmonic Amplitudes:} The amplitude of the $n$-th harmonic decreases inversely with harmonic order:
  \begin{equation}
  \hat{V}_{on} = \frac{\hat{V}_{o1}}{n} \implies \frac{V_{on}}{V_{o1}} = \frac{1}{n}
  \end{equation}
  Specifically: 3rd harmonic is $33.3\%$ of fundamental, 5th harmonic is $20\%$, 7th harmonic is $14.3\%$.
  \item \textbf{Total Harmonic Distortion (THD) of Voltage:}
  \begin{equation}
  \text{THD}_v = \frac{\sqrt{V_{or}^2 - V_{o1(rms)}^2}}{V_{o1(rms)}} = \frac{\sqrt{V_{dc}^2 - \left(\frac{2\sqrt{2}}{\pi}V_{dc}\right)^2}}{\frac{2\sqrt{2}}{\pi}V_{dc}} = \sqrt{\frac{\pi^2}{8} - 1} \approx \sqrt{1.2337 - 1} = 0.4834 \implies 48.34\%
  \end{equation}
  A total harmonic distortion of $48.34\%$ is severe and unacceptable for sensitive AC loads or utility grid interconnection, motivating the necessity of Pulse Width Modulation (PWM)!
\end{itemize}

\subsection{Sinusoidal Pulse Width Modulation (SPWM)}

In \textbf{Sinusoidal Pulse Width Modulation (SPWM)}, the inverter switches are turned ON and OFF multiple times per half-cycle at a high switching frequency. The widths of the gating pulses are modulated proportionally to the instantaneous amplitude of a sinusoidal reference wave.

\subsubsection{Fundamental Definitions and Modulation Parameters}
\begin{enumerate}[leftmargin=*]
  \item \textbf{Modulating / Reference Wave ($v_{\text{control}}$ or $v_{\text{sine}}$):} A low-frequency sinusoidal voltage whose frequency $f_o$ defines the fundamental output frequency of the inverter, and whose peak amplitude $\hat{V}_{\text{control}}$ dictates the output voltage magnitude.
  \item \textbf{Carrier Wave ($v_{\text{tri}}$):} A high-frequency symmetrical triangular waveform of frequency $f_s$ (or $f_c$) and peak amplitude $\hat{V}_{\text{tri}}$.
  \item \textbf{Amplitude Modulation Index ($m_a$):}
  \begin{formulabox}[Amplitude Modulation Index]
  \begin{equation}
  m_a = \frac{\hat{V}_{\text{control}}}{\hat{V}_{\text{tri}}}
  \label{eq:ma_def}
  \end{equation}
  \end{formulabox}
  $m_a$ governs the amplitude of the fundamental output voltage component.
  \item \textbf{Frequency Modulation Ratio ($m_f$):}
  \begin{formulabox}[Frequency Modulation Ratio]
  \begin{equation}
  m_f = \frac{f_s}{f_o} = \frac{f_{\text{carrier}}}{f_{\text{reference}}}
  \label{eq:mf_def}
  \end{equation}
  \end{formulabox}
  $m_f$ determines the frequency at which switching harmonics appear in the output spectrum.
\end{enumerate}

\subsection{PWM with Bipolar Voltage Switching}

In bipolar voltage switching, the diagonally opposite switch pairs $(S_1, S_2)$ and $(S_3, S_4)$ in the full bridge are switched simultaneously in complementary fashion:
\begin{itemize}[leftmargin=*]
  \item When $v_{\text{control}} > v_{\text{tri}}$: Switches $S_1$ and $S_2$ are ON $\implies v_o(t) = +V_{dc}$.
  \item When $v_{\text{control}} < v_{\text{tri}}$: Switches $S_3$ and $S_4$ are ON $\implies v_o(t) = -V_{dc}$.
\end{itemize}
Because the output voltage transitions directly between the two extreme polarities ($+V_{dc}$ and $-V_{dc}$), this scheme is termed \textbf{bipolar switching}.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.72\textwidth]{mohan_fig_8_5_bipolar_pwm.png}
\caption{Pulse-width modulation with bipolar voltage switching: (a) Comparison of sinusoidal reference $v_{\text{control}}$ and triangular carrier $v_{\text{tri}}$; (b) Switched pole voltages $v_{Ao}$ and $v_{Bo}$; (c) Bipolar output voltage $v_o(t)$ alternating between $+V_{dc}$ and $-V_{dc}$; (d) Harmonic spectrum showing fundamental at $f_1$ and harmonic sidebands centered around $m_f, 2m_f, 3m_f$. (Source: Ned Mohan, Fig.\ 8-5)}
\label{fig:bipolar_pwm}
\end{figure}

\subsubsection{Harmonic Characteristics of Bipolar PWM}
\begin{itemize}[leftmargin=*]
  \item \textbf{Fundamental Peak Voltage in Linear Range ($m_a \le 1.0$):}
  \begin{equation}
  \hat{V}_{o1} = m_a V_{dc} \implies V_{o1(rms)} = \frac{m_a V_{dc}}{\sqrt{2}} \approx 0.707 m_a V_{dc}
  \end{equation}
  The fundamental output voltage is strictly linearly proportional to the modulation index $m_a$.
  \item \textbf{Harmonic Sidebands:} Harmonics appear as sidebands clustered around the switching frequency and its integer multiples:
  \begin{equation}
  f_h = \left(j \cdot m_f \pm k\right) f_o
  \end{equation}
  where the harmonic order $h = j \cdot m_f \pm k$.
  \item \textbf{Selection Rules for $m_f$:}
  \begin{itemize}
    \item $m_f$ should be chosen as an \textbf{odd integer}. This establishes \textbf{odd half-wave symmetry} ($v_o(\omega t + \pi) = -v_o(\omega t)$), which completely eliminates all even harmonics from the output spectrum!
    \item If $m_f$ is an odd integer, the dominant harmonics occur at $m_f$ and $m_f \pm 2$.
    \item Synchronous PWM ($m_f = \text{integer}$) is essential for $m_f < 21$ to prevent sub-harmonic frequencies. For $m_f > 21$, asynchronous PWM can be utilized.
  \end{itemize}
\end{itemize}

\subsection{PWM with Unipolar Voltage Switching}

In unipolar voltage switching, the two inverter legs are controlled independently by comparing the carrier wave $v_{\text{tri}}$ with two reference sine waves that are $180^\circ$ out of phase:
\begin{itemize}[leftmargin=*]
  \item \textbf{Leg A Control:} $v_{\text{control}}$ is compared with $v_{\text{tri}}$:
  \begin{itemize}
    \item If $v_{\text{control}} > v_{\text{tri}}$: Switch $S_1$ is ON ($v_{Ao} = +V_{dc}/2$).
    \item If $v_{\text{control}} < v_{\text{tri}}$: Switch $S_4$ is ON ($v_{Ao} = -V_{dc}/2$).
  \end{itemize}
  \item \textbf{Leg B Control:} $-v_{\text{control}}$ is compared with $v_{\text{tri}}$:
  \begin{itemize}
    \item If $-v_{\text{control}} > v_{\text{tri}}$: Switch $S_3$ is ON ($v_{Bo} = +V_{dc}/2$).
    \item If $-v_{\text{control}} < v_{\text{tri}}$: Switch $S_2$ is ON ($v_{Bo} = -V_{dc}/2$).
  \end{itemize}
\end{itemize}

\begin{figure}[htbp]
\centering
\includegraphics[width=0.72\textwidth]{mohan_fig_8_11_unipolar_pwm.png}
\caption{Pulse-width modulation with unipolar voltage switching: (a) Reference waves $v_{\text{control}}$ and $-v_{\text{control}}$ compared with carrier $v_{\text{tri}}$; (b) Pole voltages $v_{Ao}$ and $v_{Bo}$; (c) Unipolar output voltage $v_o(t)$ switching between $0$ and $+V_{dc}$ or $0$ and $-V_{dc}$; (d) Harmonic spectrum showing the total absence of harmonics around $m_f$ and first harmonic cluster shifted to $2m_f$. (Source: Ned Mohan, Fig.\ 8-11)}
\label{fig:unipolar_pwm}
\end{figure}

\subsubsection{The Remarkable Advantages of Unipolar PWM}
During each switching event, the output voltage transitions between \textbf{three voltage levels}: $+V_{dc}$, $0$, and $-V_{dc}$:
\begin{itemize}
  \item During the positive half-cycle of $v_{\text{control}}$, $v_o(t)$ switches between $0$ and $+V_{dc}$.
  \item During the negative half-cycle of $v_{\text{control}}$, $v_o(t)$ switches between $0$ and $-V_{dc}$.
\end{itemize}
\begin{conceptbox}[Why Unipolar Switching Outperforms Bipolar Switching]
\begin{enumerate}
  \item \textbf{Doubling of Effective Switching Frequency:} The output voltage pulses appear at \textbf{twice the carrier frequency} ($2f_s$). The fundamental output voltage equation remains identical:
  \begin{equation}
  \hat{V}_{o1} = m_a V_{dc} \quad (0 \le m_a \le 1.0)
  \end{equation}
  \item \textbf{Cancellation of Harmonics at $m_f$:} Harmonics centered around $m_f, 3m_f, 5m_f, \dots$ are completely cancelled out! The lowest-order harmonic sidebands appear centered around $2m_f$:
  \begin{equation}
  h = 2m_f \pm 1, \quad 2m_f \pm 3
  \end{equation}
  \item \textbf{Dramatically Smaller Output Filter:} Because the lowest harmonic frequency is doubled ($2f_s$), the required inductance and capacitance of the output low-pass filter are cut in half, slashing converter weight, volume, and cost!
  \item \textbf{Reduced Current Ripple:} Load current ripple is substantially smaller compared to bipolar PWM for identical device switching frequencies.
\end{enumerate}
\end{conceptbox}

\begin{table}[htbp]
\centering
\small
\caption{Comprehensive Comparison: Bipolar vs. Unipolar PWM Schemes}
\label{tab:bipolar_vs_unipolar}
\begin{tabularx}{\textwidth}{l X X}
\toprule
\textbf{Feature} & \textbf{Bipolar PWM} & \textbf{Unipolar PWM} \\
\midrule
\textbf{Output Voltage Levels} & 2 levels: $+V_{dc}, -V_{dc}$ & 3 levels: $+V_{dc}, 0, -V_{dc}$ \\
\textbf{Leg Control} & Legs A and B switched simultaneously & Legs A and B switched independently \\
\textbf{Carrier References} & Single sine wave $v_{\text{control}}$ & Complementary pair: $+v_{\text{control}}, -v_{\text{control}}$ \\
\textbf{Selection of $m_f$} & $m_f$ must be an odd integer & $m_f$ is typically chosen as an even integer \\
\textbf{Effective Output Frequency} & $f_s$ (Carrier frequency) & $2f_s$ (Double carrier frequency) \\
\textbf{Dominant Harmonics} & Clustered around $m_f, 2m_f, 3m_f$ & Absent at $m_f$; first appear around $2m_f$ \\
\textbf{Output Filter Size} & Large & Significantly smaller ($\approx 50\%$ reduction) \\
\textbf{Switching Stress ($dv/dt$)} & Steps of $2V_{dc}$ across load terminals & Steps of $V_{dc}$ across load terminals \\
\textbf{Control Complexity} & Minimal & Moderately higher \\
\bottomrule
\end{tabularx}
\end{table}

\subsection{Operating Modes: Linear Modulation, Overmodulation, and Square-Wave}

The relationship between the fundamental output voltage $\hat{V}_{o1}$ and the modulation index $m_a$ spans three distinct operational regimes:

\begin{enumerate}[leftmargin=*]
  \item \textbf{Linear Modulation Region ($0 \le m_a \le 1.0$):}
  \begin{itemize}
    \item The peak of the modulating sine wave is less than or equal to the triangular carrier peak ($\hat{V}_{\text{control}} \le \hat{V}_{\text{tri}}$).
    \item The fundamental peak output voltage varies strictly linearly with $m_a$:
    \begin{equation}
    \hat{V}_{o1} = m_a V_{dc}
    \end{equation}
    \item The harmonic frequencies are independent of $m_a$, and harmonic amplitudes are directly proportional to $m_a$.
  \end{itemize}

  \item \textbf{Overmodulation Region ($1.0 < m_a \le 3.24$):}
  \begin{itemize}
    \item The reference sine wave amplitude exceeds the carrier peak ($\hat{V}_{\text{control}} > \hat{V}_{\text{tri}}$).
    \item For intervals near the sine wave peaks, the reference wave completely exceeds the triangular carrier, resulting in \textbf{pulse dropping}—the switch remains continuously ON for multiple carrier cycles without pulsing.
    \item The relationship between $\hat{V}_{o1}$ and $m_a$ becomes \textbf{non-linear} and begins to saturate.
    \item Low-order harmonics (3rd, 5th, 7th) re-appear directly in the output voltage spectrum, increasing harmonic distortion. However, overmodulation is widely utilized in industrial AC motor drives to extract maximum fundamental voltage during high-speed operation!
  \end{itemize}

  \item \textbf{Square-Wave Operation ($m_a > 3.24$):}
  \begin{itemize}
    \item As $m_a$ becomes large ($m_a > 3.24$), the PWM pulses merge completely into a single square wave per half-cycle.
    \item The inverter operates in pure square-wave mode, and the fundamental peak saturates at its absolute theoretical maximum:
    \begin{equation}
    \hat{V}_{o1,\text{max}} = \frac{4V_{dc}}{\pi} \approx 1.273 V_{dc}
    \end{equation}
    \item In this regime, the output voltage is completely independent of $m_a$ and can only be regulated by varying the input DC link voltage $V_{dc}$.
  \end{itemize}
\end{enumerate}

\subsection{The Critical Need for Blanking Time (Dead-Time)}

In practical bridge inverters, power semiconductor switches (IGBTs, MOSFETs) do not turn OFF instantaneously due to stored minority carrier recombination and gate charge discharging times ($t_{off} > t_{on}$).

\begin{figure}[htbp]
\centering
\includegraphics[width=0.72\textwidth]{mohan_fig_8_31_blanking_time.png}
\caption{Effect of blanking time (dead time) in a bridge inverter: (a) Inverter leg showing upper and lower switches and freewheeling diodes; (b) Gate signals with blanking time $t_\Delta$; (c) Resulting pole voltage waveforms showing voltage reduction for positive current and voltage increase for negative current. (Source: Ned Mohan, Fig.\ 8-31)}
\label{fig:blanking_time}
\end{figure}

\subsubsection{The Shoot-Through Catastrophe}
If the turn-ON gate command is applied to the upper switch ($S_1$) at the exact instant the turn-OFF command is sent to the lower switch ($S_4$) in the same leg, both switches will be simultaneously ON for the turn-off duration $t_{off}$. This creates a zero-impedance \textbf{shoot-through dead short circuit directly across the DC bus}:
\begin{equation}
I_{\text{fault}} = \frac{V_{dc}}{R_{\text{parasitic}}} \to \text{Thousands of Amperes} \implies \text{Explosive device destruction!}
\end{equation}

\subsubsection{Implementation of Blanking Time ($t_d$ or $t_\Delta$)}
To prevent shoot-through, a deliberate hardware/software delay called \textbf{blanking time} (or \textbf{dead-time}, $t_d$) is inserted between the turn-OFF command of one switch and the turn-ON command of the complementary switch in the same leg:
\begin{equation}
t_d > t_{off,\text{max}} + t_{\text{driver delay mismatch}}
\end{equation}
Typical values: $1.0 - 3.0\,\mu\text{s}$ for IGBTs; $100 - 500\text{ ns}$ for silicon MOSFETs; $< 50\text{ ns}$ for GaN HEMTs.

\subsubsection{Adverse Effects and Voltage Penalty Caused by Blanking Time}
During the blanking interval $t_d$, both controlled switches in the leg are commanded OFF. The actual pole voltage is determined entirely by the \textbf{direction of the load current} flowing through the freewheeling diodes:
\begin{itemize}[leftmargin=*]
  \item \textbf{When $i_o > 0$:} The current must flow through lower diode $D_4$. Even though $S_1$ was commanded ON, the pole voltage is clamped to $0\text{ V}$ instead of $+V_{dc}$. The pulse width is reduced by $t_d$, causing a loss of output voltage!
  \item \textbf{When $i_o < 0$:} The current flows through upper diode $D_1$, clamping the pole voltage to $+V_{dc}$ instead of $0\text{ V}$. The pulse width is increased by $t_d$.
  \item \textbf{Fundamental Voltage Drop:} Averaging this error over one fundamental cycle results in an average fundamental voltage reduction of:
  \begin{equation}
  \Delta V_o = \frac{4 t_d}{T_s} V_{dc} = 4 f_s t_d V_{dc}
  \label{eq:deadtime_voltage_drop}
  \end{equation}
  \item \textbf{Adverse Consequences:}
  \begin{enumerate}
    \item Causes a noticeable reduction in fundamental output voltage, especially prominent at low modulation indices.
    \item Generates severe \textbf{low-order harmonics} (5th, 7th, 11th) that are in-phase with current zero-crossings, producing torque pulsations in AC motors.
    \item Introduces waveform distortion and zero-crossing deadbands in precision motor drives.
  \end{enumerate}
\end{itemize}
'''
