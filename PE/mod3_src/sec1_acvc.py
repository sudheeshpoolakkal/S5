# -*- coding: utf-8 -*-
"""Section 1: AC Voltage Controllers (ACVC)"""

def get_section():
    return r'''
\section{AC Voltage Controllers (ACVC) / AC Regulators}

\subsection{Foundational Principles and Classification}

An \textbf{AC Voltage Controller} (also termed an \textbf{AC Voltage Regulator}) is a line-frequency phase-controlled or integral-cycle switched converter that converts a fixed-voltage, fixed-frequency alternating current supply into a \textbf{variable-voltage, fixed-frequency AC output} without an intermediate DC stage:
\begin{equation}
\text{Fixed AC Input } (V_s, f) \xrightarrow{\text{AC Voltage Controller}} \text{Variable AC Output } (V_{or}, f)
\end{equation}
Because conversion is accomplished entirely in a single stage using line-commutated thyristors or TRIACs, AC voltage controllers feature extremely high operational efficiency ($\eta > 98\%$), rugged mechanical simplicity, low initial cost, and the complete absence of bulky reactive filter banks.

\subsubsection{Classification of AC Voltage Control Methods}
AC voltage controllers are categorized into three distinct operational methodologies according to the switching mechanism employed (frequently evaluated in university examinations):

\begin{enumerate}[leftmargin=*]
  \item \textbf{Phase Angle Control (PAC):}
  \begin{itemize}[leftmargin=*]
    \item \textbf{Mechanism:} The power semiconductor switches (a pair of anti-parallel SCRs or a TRIAC) connect the load to the AC source for a controllable fraction of each supply half-cycle. Conduction is initiated at a controllable delay angle $\alpha$ (measured relative to the zero-crossing of the input supply voltage) and ceases naturally at current zero ($\beta$) via natural (line) commutation.
    \item \textbf{Advantages:} Provides continuous, smooth, instantaneous, and infinitely variable control of RMS load voltage from $0$ to $V_s$.
    \item \textbf{Disadvantages:} The abrupt chopping of sinusoidal voltage waveforms introduces substantial low-order current harmonics (3rd, 5th, 7th) and causes the supply displacement factor to lag significantly as $\alpha$ increases.
    \item \textbf{Primary Applications:} Universal motor speed control, light dimmers, induction motor soft-starters, industrial furnace heating.
  \end{itemize}

  \item \textbf{Integral Cycle Control (On-Off / Burst Firing Control):}
  \begin{itemize}[leftmargin=*]
    \item \textbf{Mechanism:} The thyristor switches connect the load to the AC mains for an integral number of complete supply cycles ($n$ cycles), and then remain un-triggered for another integral number of cycles ($m$ cycles). Switching is always synchronized to occur at the zero-crossing of the supply voltage ($v_s(t) = 0$).
    \item \textbf{Mathematical Duty Ratio and RMS Voltage:}
    \begin{equation}
    k = \frac{n}{n + m} = \frac{T_{on}}{T_o} \implies V_{or} = V_s \sqrt{k} = V_s \sqrt{\frac{n}{n + m}}
    \end{equation}
    where $T_o = (n + m)T$ is the overall repeating period.
    \item \textbf{Advantages:} Because switching transitions occur exclusively at natural voltage zero-crossings ($dv/dt \to 0$ and $di/dt \to 0$), radio frequency interference (RFI), electromagnetic interference (EMI), and switching losses are virtually zero.
    \item \textbf{Disadvantages:} Sub-harmonic frequency components (frequencies below the mains supply frequency $f$) and line flicker are introduced, making this method completely unsuitable for motor speed control or lighting systems.
    \item \textbf{Primary Applications:} Loads with very large mechanical or thermal time constants, such as industrial electric ovens, boiler heaters, and plastic extrusion mold heaters.
  \end{itemize}

  \item \textbf{Sequence Control of AC Voltage Controllers:}
  \begin{itemize}[leftmargin=*]
    \item \textbf{Mechanism:} Two or more parallel transformer-tapped stages of AC voltage controllers are fired in sequence. By controlling only one stage at a time while leaving others fully ON or fully OFF, the output voltage is varied with substantially reduced harmonic distortion and a significantly improved supply power factor across the entire operating range.
  \end{itemize}
\end{enumerate}

\begin{figure}[htbp]
\centering
\includegraphics[width=0.65\textwidth]{hart_fig_5_1_acvc_r.png}
\caption{Single-phase full-wave AC voltage controller with resistive load: (a) Power circuit diagram using two anti-parallel thyristors $T_1$ and $T_2$; (b) Supply voltage $v_s$, gating signals $i_{g1}$ and $i_{g2}$, load voltage $v_o$, and thyristor voltage $v_{T1}$ waveforms for firing delay angle $\alpha$. (Source: Daniel W. Hart, Fig.\ 5-1)}
\label{fig:acvc_r_circuit}
\end{figure}

\subsection{Single-Phase Full-Wave AC Voltage Controller with Pure Resistive ($R$) Load}

Consider the circuit of Figure~\ref{fig:acvc_r_circuit}a supplied by a single-phase sinusoidal AC source $v_s(t) = V_m \sin(\omega t) = \sqrt{2}V_s \sin(\omega t)$. Two SCRs ($T_1$ and $T_2$) are connected in anti-parallel (back-to-back) between the AC mains and a resistive load $R$.

\subsubsection{Circuit Operation Across One Full Fundamental Cycle}
\begin{itemize}[leftmargin=*]
  \item \textbf{Positive Half-Cycle ($0 \le \omega t \le \pi$):} Supply voltage $v_s > 0$. Thyristor $T_1$ is forward-biased, while $T_2$ is reverse-biased ($v_{AK2} < 0$).
  \begin{itemize}
    \item From $\omega t = 0$ to $\omega t = \alpha$, $T_1$ remains OFF. No current flows ($i_o = 0$), load voltage $v_o = 0$, and the full line voltage appears across $T_1$ ($v_{T1} = v_s$).
    \item At $\omega t = \alpha$, a firing pulse is applied to the gate of $T_1$. $T_1$ turns ON instantaneously.
    \item From $\omega t = \alpha$ to $\pi$, $T_1$ conducts load current:
    \begin{equation}
    v_o(t) = v_s(t) = V_m \sin(\omega t), \quad i_o(t) = \frac{v_s(t)}{R} = \frac{V_m}{R}\sin(\omega t)
    \end{equation}
    \item At $\omega t = \pi$, the supply voltage reverses polarity. The current through $T_1$ drops naturally to zero ($i_o(\pi) = 0$), turning $T_1$ OFF via natural (line) commutation.
  \end{itemize}

  \item \textbf{Negative Half-Cycle ($\pi \le \omega t \le 2\pi$):} Supply voltage $v_s < 0$. Thyristor $T_2$ is forward-biased, while $T_1$ is reverse-biased.
  \begin{itemize}
    \item At $\omega t = \pi + \alpha$, a firing pulse is applied to the gate of $T_2$. $T_2$ turns ON.
    \item From $\omega t = \pi + \alpha$ to $2\pi$, $T_2$ conducts negative load current:
    \begin{equation}
    v_o(t) = v_s(t) = V_m \sin(\omega t), \quad i_o(t) = \frac{V_m}{R}\sin(\omega t) \quad (< 0)
    \end{equation}
    \item At $\omega t = 2\pi$, $i_o(2\pi) = 0$, and $T_2$ turns OFF naturally.
  \end{itemize}
\end{itemize}

\subsubsection{Rigorous Mathematical Derivation of RMS Output Voltage}
Because the output voltage waveform exhibits half-wave symmetry ($v_o(\omega t + \pi) = -v_o(\omega t)$), the root-mean-square (RMS) value can be computed over a half-cycle ($0$ to $\pi$):
\begin{align}
V_{or} &= \sqrt{\frac{1}{\pi} \int_{\alpha}^{\pi} \left[V_m \sin(\omega t)\right]^2 d(\omega t)} = \sqrt{\frac{V_m^2}{\pi} \int_{\alpha}^{\pi} \frac{1 - \cos(2\omega t)}{2} d(\omega t)} \notag\\
&= \sqrt{\frac{V_m^2}{2\pi} \left[ \omega t - \frac{\sin(2\omega t)}{2} \right]_{\alpha}^{\pi}} = \sqrt{\frac{V_m^2}{2\pi} \left[ (\pi - \alpha) - \left(\frac{\sin(2\pi) - \sin(2\alpha)}{2}\right) \right]} \notag\\
&= \sqrt{\frac{V_m^2}{2\pi} \left[ (\pi - \alpha) + \frac{\sin(2\alpha)}{2} \right]} = \frac{V_m}{\sqrt{2}} \sqrt{\frac{1}{\pi} \left[ (\pi - \alpha) + \frac{\sin(2\alpha)}{2} \right]}
\end{align}
Recognizing that $V_s = V_m / \sqrt{2}$ is the RMS value of the input source:
\begin{formulabox}[Master Equation: RMS Output Voltage ($R$ Load)]
\begin{equation}
V_{or} = V_s \sqrt{1 - \frac{\alpha}{\pi} + \frac{\sin(2\alpha)}{2\pi}}
\label{eq:acvc_rms_r}
\end{equation}
\end{formulabox}

\subsubsection{Performance Characteristics with $R$ Load}
\begin{itemize}[leftmargin=*]
  \item \textbf{RMS Load Current:} $I_{or} = \frac{V_{or}}{R} = \frac{V_s}{R} \sqrt{1 - \frac{\alpha}{\pi} + \frac{\sin(2\alpha)}{2\pi}}$.
  \item \textbf{Average and RMS Thyristor Currents:} Each thyristor conducts for only one half of the symmetrical period:
  \begin{equation}
  I_{T(avg)} = \frac{1}{2\pi} \int_{\alpha}^{\pi} \frac{V_m}{R}\sin(\omega t) d(\omega t) = \frac{V_m}{2\pi R} (1 + \cos\alpha) = \frac{\sqrt{2}V_s}{2\pi R}(1 + \cos\alpha)
  \end{equation}
  \begin{equation}
  I_{T(rms)} = \frac{I_{or}}{\sqrt{2}} = \frac{V_s}{\sqrt{2}R} \sqrt{1 - \frac{\alpha}{\pi} + \frac{\sin(2\alpha)}{2\pi}}
  \end{equation}
  \item \textbf{Input Power Factor (PF):} Since input current $i_s(t) = i_o(t)$, the apparent power supplied by the mains is $S = V_s I_{or}$. The active power dissipated in the load is $P_o = I_{or}^2 R = \frac{V_{or}^2}{R}$.
  \begin{equation}
  \text{PF} = \frac{P_o}{S} = \frac{V_{or}^2 / R}{V_s I_{or}} = \frac{V_{or} I_{or}}{V_s I_{or}} = \frac{V_{or}}{V_s} = \sqrt{1 - \frac{\alpha}{\pi} + \frac{\sin(2\alpha)}{2\pi}}
  \end{equation}
  \item \textbf{Control Range:} As $\alpha$ varies from $0$ to $\pi$ ($180^\circ$):
  \begin{itemize}
    \item At $\alpha = 0$: $V_{or} = V_s$, $\text{PF} = 1.0$ (Full sinusoidal conduction).
    \item At $\alpha = \pi/2$ ($90^\circ$): $V_{or} = V_s / \sqrt{2} \approx 0.707 V_s$, $\text{PF} \approx 0.707$.
    \item At $\alpha = \pi$ ($180^\circ$): $V_{or} = 0$, $\text{PF} = 0$ (Output completely blocked).
  \end{itemize}
\end{itemize}

\subsection{Single-Phase Full-Wave AC Voltage Controller with $RL$ Load}

When the load consists of an inductive impedance $Z = \sqrt{R^2 + (\omega L)^2}$ with characteristic load impedance angle $\phi = \arctan\left(\frac{\omega L}{R}\right)$, the inductance opposes sudden changes in load current. Consequently, \textbf{the current continues to flow after the source voltage reverses polarity at $\omega t = \pi$}.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.68\textwidth]{hart_fig_5_4_acvc_rl.png}
\caption{Single-phase AC voltage controller with $RL$ load: Waveforms of input voltage $v_s$, thyristor gating pulses, output voltage $v_o$, and inductive load current $i_o(\omega t)$ showing the extinction angle $\beta$ and conduction angle $\gamma = \beta - \alpha$. (Source: Daniel W. Hart, Fig.\ 5-4)}
\label{fig:acvc_rl_waveforms}
\end{figure}

\subsubsection{Derivation of the Load Current Differential Equation}
During the conduction of thyristor $T_1$ ($\alpha \le \omega t \le \beta$), the governing Kirchhoff's Voltage Law (KVL) differential equation is:
\begin{equation}
L \frac{di_o(t)}{dt} + R i_o(t) = v_s(t) = V_m \sin(\omega t)
\end{equation}
The total solution consists of a steady-state particular solution $i_{ss}(t)$ and a transient complementary solution $i_{tr}(t)$:
\begin{equation}
i_o(\omega t) = \frac{V_m}{Z}\sin(\omega t - \phi) + A e^{-\frac{R}{\omega L}\omega t}
\end{equation}
where $Z = \sqrt{R^2 + (\omega L)^2}$ and $\phi = \arctan(\omega L / R)$.

Applying the initial boundary condition at the firing instant: at $\omega t = \alpha$, $i_o(\alpha) = 0$:
\begin{equation}
0 = \frac{V_m}{Z}\sin(\alpha - \phi) + A e^{-\frac{R}{\omega L}\alpha} \implies A = -\frac{V_m}{Z}\sin(\alpha - \phi) e^{\frac{R}{\omega L}\alpha}
\end{equation}
Substituting $A$ back into the current expression yields the closed-form equation for the instantaneous load current:
\begin{formulabox}[Instantaneous Load Current in ACVC with $RL$ Load]
\begin{equation}
i_o(\omega t) = \frac{V_m}{Z} \left[ \sin(\omega t - \phi) - \sin(\alpha - \phi) e^{-\frac{R}{\omega L}(\omega t - \alpha)} \right], \quad \text{for } \alpha \le \omega t \le \beta
\label{eq:acvc_io_rl}
\end{equation}
\end{formulabox}

\subsubsection{Extinction Angle ($\beta$) and Conduction Angle ($\gamma$)}
At $\omega t = \beta$, the magnetic energy stored in inductor $L$ is completely dissipated into $R$, and the current extinguishes to zero ($i_o(\beta) = 0$). Setting equation~\eqref{eq:acvc_io_rl} to zero at $\omega t = \beta$ gives the transcendental equation:
\begin{equation}
\sin(\beta - \phi) = \sin(\alpha - \phi) e^{-\frac{R}{\omega L}(\beta - \alpha)}
\label{eq:acvc_beta_transcendental}
\end{equation}
The conduction angle of each thyristor is defined as $\gamma = \beta - \alpha$. Equation~\eqref{eq:acvc_beta_transcendental} can be expressed in terms of $\gamma$ as:
\begin{equation}
\sin(\alpha + \gamma - \phi) = \sin(\alpha - \phi) e^{-\frac{R}{\omega L}\gamma}
\end{equation}

\subsubsection{Three Critical Conduction Regimes Based on Firing Angle $\alpha$ vs $\phi$}
The behavior of the $RL$ AC voltage controller depends decisively on the relative relationship between the firing delay angle $\alpha$ and the load impedance phase angle $\phi$:

\begin{enumerate}[leftmargin=*]
  \item \textbf{Case 1: $\alpha > \phi$ (Discontinuous Conduction Mode --- Standard Operation):}
  \begin{itemize}
    \item The current extinguishes before the next half-cycle thyristor is triggered: $\beta < \pi + \alpha$, which means the conduction angle $\gamma = (\beta - \alpha) < \pi$.
    \item There is a finite zero-current interval between the extinction of $T_1$ and the firing of $T_2$.
    \item The output voltage is fully controllable by varying $\alpha$ between $\phi$ and $\pi$.
  \end{itemize}

  \item \textbf{Case 2: $\alpha = \phi$ (Boundary / Critical Conduction Mode):}
  \begin{itemize}
    \item Substituting $\alpha = \phi$ into equation~\eqref{eq:acvc_beta_transcendental}:
    \begin{equation}
    \sin(\beta - \phi) = \sin(0) \cdot e^{-\frac{R}{\omega L}(\beta - \phi)} = 0 \implies \beta - \phi = \pi \implies \beta = \pi + \phi = \pi + \alpha
    \end{equation}
    \item The conduction angle is exactly $\gamma = \beta - \alpha = \pi$ ($180^\circ$).
    \item Thyristor $T_1$ conducts for exactly $180^\circ$. The moment $T_1$ extinguishes at $\omega t = \pi + \alpha$, thyristor $T_2$ is triggered!
    \item The load current becomes a continuous, perfectly sinusoidal waveform: $i_o(t) = \frac{V_m}{Z}\sin(\omega t - \phi)$. The converter behaves as if the load is directly connected across the AC supply!
  \end{itemize}

  \item \textbf{Case 3: $\alpha < \phi$ (Dangerous / Loss of Control Mode):}
  \begin{itemize}
    \item If a narrow gate pulse is applied at $\alpha < \phi$, thyristor $T_1$ cannot turn ON if the previous thyristor $T_2$ is still conducting negative current!
    \item If continuous or long gate pulses are used, $T_1$ will not turn ON until $T_2$ current reaches zero at $\beta$. This effectively clamps the minimum firing angle to $\alpha_{\text{min}} = \phi$.
    \item \textbf{Critical Exam Rule:} Firing angle $\alpha$ must always satisfy $\alpha \ge \phi$. A firing angle smaller than $\phi$ does not increase the load voltage and causes a loss of independent phase control or asymmetrical DC saturation of feeding transformers!
  \end{itemize}
\end{enumerate}

\subsubsection{Derivation of RMS Output Voltage with $RL$ Load}
During the conduction interval $\alpha \le \omega t \le \beta$, the load voltage equals the supply voltage: $v_o(t) = V_m \sin(\omega t)$. Outside this interval, $v_o(t) = 0$.
\begin{align}
V_{or} &= \sqrt{\frac{1}{\pi} \int_{\alpha}^{\beta} \left[V_m \sin(\omega t)\right]^2 d(\omega t)} = \sqrt{\frac{V_m^2}{2\pi} \int_{\alpha}^{\beta} \left[1 - \cos(2\omega t)\right] d(\omega t)} \notag\\
&= \sqrt{\frac{V_m^2}{2\pi} \left[ (\beta - \alpha) - \frac{\sin(2\beta) - \sin(2\alpha)}{2} \right]}
\end{align}
In terms of $V_s = V_m / \sqrt{2}$ and conduction angle $\gamma = \beta - \alpha$:
\begin{formulabox}[Master Equation: RMS Output Voltage ($RL$ Load)]
\begin{equation}
V_{or} = V_s \sqrt{\frac{1}{\pi} \left[ (\beta - \alpha) - \frac{\sin(2\beta) - \sin(2\alpha)}{2} \right]} = V_s \sqrt{\frac{1}{\pi} \left[ \gamma - \frac{\sin(2\beta) - \sin(2\alpha)}{2} \right]}
\label{eq:acvc_rms_rl}
\end{equation}
\end{formulabox}

\subsection{Single-Phase AC Voltage Controller with Pure Inductive ($L$) Load}

For a purely inductive load ($R = 0 \implies \phi = 90^\circ = \pi/2$):
\begin{equation}
L \frac{di_o}{dt} = V_m \sin(\omega t) \implies i_o(\omega t) = \frac{V_m}{\omega L} \int_{\alpha}^{\omega t} \sin(\omega t) d(\omega t) = \frac{V_m}{\omega L} (\cos\alpha - \cos\omega t)
\end{equation}
The current extinguishes when $i_o(\beta) = 0$:
\begin{equation}
\cos\alpha - \cos\beta = 0 \implies \beta = 2\pi - \alpha
\end{equation}
The conduction angle is:
\begin{equation}
\gamma = \beta - \alpha = 2\pi - 2\alpha = 2(\pi - \alpha)
\end{equation}
\begin{itemize}[leftmargin=*]
  \item Since $\phi = \pi/2$ ($90^\circ$), the control range for $\alpha$ is restricted to $\pi/2 \le \alpha \le \pi$.
  \item At $\alpha = \pi/2$: $\beta = 2\pi - \pi/2 = 3\pi/2$, $\gamma = \pi$ ($180^\circ$). Current is continuous.
  \item At $\alpha = \pi$: $\beta = \pi$, $\gamma = 0$. No current flows.
  \item This configuration is the fundamental building block of \textbf{Thyristor-Controlled Reactors (TCR)} utilized extensively in static VAR compensators (SVC) on power transmission grids!
\end{itemize}

\subsection{Gate Firing Pulse Requirements for Inductive Loads}
With an inductive load, a standard short gate trigger pulse ($10 - 20\,\mu\text{s}$) cannot ensure reliable thyristor turn-on:
\begin{conceptbox}[Gate Firing Requirements with Inductive Loads]
Because $di/dt = v_s/L$ is restricted by the load inductance, the anode current rises slowly after triggering. If a short gate pulse ends before the anode current crosses the \textbf{latching current} ($I_L$), the thyristor will immediately turn back OFF when the gate pulse is removed!

Furthermore, due to current overlap between consecutive half-cycles, the incoming thyristor may be triggered while the outgoing thyristor is still conducting.

\textbf{Mandatory Solutions:}
\begin{enumerate}
  \item \textbf{Continuous Gate Gating:} Maintain gate current throughout the desired conduction period ($\alpha$ to $\pi$). (Drawback: High average gate power dissipation).
  \item \textbf{High-Frequency Pulse Train Gating (Carrier Frequency Modulation):} Modulate the firing signal with a $10 - 30\text{ kHz}$ pulse train generated by a 555 timer or microcontroller. This reduces gate power dissipation by $>80\%$ while allowing small, compact pulse isolation transformers!
\end{enumerate}
\end{conceptbox}

\subsection{Engineering Applications of AC Voltage Controllers}
\begin{enumerate}[leftmargin=*]
  \item \textbf{Industrial and Domestic Heating:} Closed-loop temperature regulation in resistance furnaces, kilns, soldering stations, and water heaters.
  \item \textbf{Lighting Control (Dimmers):} Theater stage lighting, architectural illumination, and incandescent lamp dimming.
  \item \textbf{AC Motor Soft Starters:} During the starting of high-power three-phase squirrel-cage induction motors, direct-on-line (DOL) starting draws $6 - 8 \times I_{\text{rated}}$, creating severe line voltage dips. By ramping $\alpha$ from $150^\circ$ down to $\phi$, starting current is limited to $2 - 3 \times I_{\text{rated}}$.
  \item \textbf{Speed Control of AC Fan and Pump Motors:} Controlling stator voltage on high-slip single-phase and three-phase induction motors provides stable variable-speed torque for centrifugal fans and water pumps.
  \item \textbf{On-Load Transformer Tap Changers:} Thyristorized tap changers switch transformer winding taps under full load without mechanical arcing, contact wear, or line interruption.
  \item \textbf{Static VAR Compensators (SVC):} Thyristor-Controlled Reactors (TCR) dynamically absorb variable inductive reactive power ($Q$) to stabilize grid voltages.
\end{enumerate}
'''
