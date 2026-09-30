# -*- coding: utf-8 -*-
"""Section 6: Ten Comprehensive Exam-Style Solved Problems"""

def get_section():
    return r'''
\section{Ten Comprehensive University Exam Solved Numerical Problems}

\subsection{Problem 1: Single-Phase Full-Wave AC Voltage Controller with Resistive Load}
\begin{examplebox}[Problem 1: ACVC with $R$ Load Design \& Analysis]
\textbf{Statement:} A single-phase full-wave AC voltage controller is supplied from a $230\text{ V}$, $50\text{ Hz}$ single-phase source and feeds a purely resistive load of $R = 10\,\Omega$. The firing delay angle is set to $\alpha = \pi/3$ ($60^\circ$). Determine:
\begin{enumerate}
  \item The RMS output voltage $V_{or}$.
  \item The RMS load current $I_{or}$ and real active power dissipated in the load $P_o$.
  \item The input power factor $\text{PF}$.
  \item The average and RMS current ratings required for each individual thyristor.
\end{enumerate}

\tcblower
\textbf{Solution:}
\begin{enumerate}
  \item \textbf{RMS Output Voltage ($V_{or}$):}
  Using the master analytical formula for resistive load (equation~\eqref{eq:acvc_rms_r}):
  \begin{equation*}
  V_{or} = V_s \sqrt{1 - \frac{\alpha}{\pi} + \frac{\sin(2\alpha)}{2\pi}}
  \end{equation*}
  Here, $\alpha = \frac{\pi}{3} = 60^\circ$ ($1.0472\text{ rad}$), and $2\alpha = \frac{2\pi}{3} = 120^\circ$.
  \begin{equation*}
  \sin(2\alpha) = \sin(120^\circ) = \frac{\sqrt{3}}{2} \approx 0.8660
  \end{equation*}
  Substituting the numerical values into the square root expression:
  \begin{align*}
  \text{Term} &= 1 - \frac{\pi/3}{\pi} + \frac{0.8660}{2\pi} = 1 - \frac{1}{3} + \frac{0.8660}{6.2832} = \frac{2}{3} + 0.1378 = 0.6667 + 0.1378 = 0.8045 \notag\\
  \sqrt{0.8045} &\approx 0.8969
  \end{align*}
  Therefore, the RMS load voltage is:
  \begin{equation*}
  \mathbf{V_{or}} = 230 \times 0.8969 = \mathbf{206.3\text{ V}}
  \end{equation*}

  \item \textbf{RMS Load Current and Active Load Power:}
  \begin{equation*}
  \mathbf{I_{or}} = \frac{V_{or}}{R} = \frac{206.3\text{ V}}{10\,\Omega} = \mathbf{20.63\text{ A}}
  \end{equation*}
  The real power absorbed by the load resistor is:
  \begin{equation*}
  \mathbf{P_o} = I_{or}^2 \cdot R = (20.63)^2 \times 10 = \mathbf{4256\text{ W} = 4.256\text{ kW}}
  \end{equation*}

  \item \textbf{Input Power Factor ($\text{PF}$):}
  \begin{equation*}
  \mathbf{\text{PF}} = \frac{P_o}{V_s I_{or}} = \frac{V_{or}}{V_s} = \frac{206.3}{230} = \mathbf{0.897\text{ (lagging)}}
  \end{equation*}

  \item \textbf{Thyristor Current Ratings:}
  Each thyristor carries current for one half-cycle. Peak supply voltage is $V_m = \sqrt{2} \times 230 = 325.27\text{ V}$.
  \begin{align*}
  \mathbf{I_{T(avg)}} &= \frac{V_m}{2\pi R}(1 + \cos\alpha) = \frac{325.27}{2\pi \times 10}\left(1 + \cos 60^\circ\right) = \frac{32.527}{6.2832} (1 + 0.5) = 5.177 \times 1.5 = \mathbf{7.77\text{ A}} \notag\\
  \mathbf{I_{T(rms)}} &= \frac{I_{or}}{\sqrt{2}} = \frac{20.63}{\sqrt{2}} = \mathbf{14.59\text{ A}}
  \end{align*}
\end{enumerate}
\end{examplebox}

\subsection{Problem 2: Single-Phase AC Voltage Controller with Inductive $RL$ Load}
\begin{examplebox}[Problem 2: ACVC with $RL$ Load and Extinction Angle]
\textbf{Statement:} A $230\text{ V}$, $50\text{ Hz}$ single-phase AC voltage controller feeds a series $RL$ load with $R = 4\,\Omega$ and $\omega L = 3\,\Omega$. 
\begin{enumerate}
  \item Determine the minimum permissible firing angle $\alpha_{\text{min}}$ for controllable operation.
  \item For a firing angle $\alpha = 60^\circ$, if the numerical extinction angle is found to be $\beta = 220^\circ$ ($3.8397\text{ rad}$), calculate the conduction angle $\gamma$ and the RMS output voltage $V_{or}$.
\end{enumerate}

\tcblower
\textbf{Solution:}
\begin{enumerate}
  \item \textbf{Minimum Firing Angle ($\alpha_{\text{min}}$):}
  The load impedance magnitude and phase angle are:
  \begin{align*}
  Z &= \sqrt{R^2 + (\omega L)^2} = \sqrt{4^2 + 3^2} = \sqrt{16 + 9} = 5.0\,\Omega \notag\\
  \phi &= \arctan\left(\frac{\omega L}{R}\right) = \arctan\left(\frac{3}{4}\right) = 36.87^\circ = 0.6435\text{ rad}
  \end{align*}
  As established in Section 1, to maintain independent phase control and avoid current continuity breakdown, the firing delay angle must satisfy $\alpha \ge \phi$:
  \begin{equation*}
  \mathbf{\alpha_{\text{min}} = \phi = 36.87^\circ}
  \end{equation*}

  \item \textbf{Conduction Angle ($\gamma$) and RMS Output Voltage ($V_{or}$):}
  Given $\alpha = 60^\circ = \frac{\pi}{3}\text{ rad}$ ($1.0472\text{ rad}$) and $\beta = 220^\circ = 3.8397\text{ rad}$:
  \begin{equation*}
  \mathbf{\gamma} = \beta - \alpha = 220^\circ - 60^\circ = \mathbf{160^\circ = 2.7925\text{ rad}}
  \end{equation*}
  Using equation~\eqref{eq:acvc_rms_rl}:
  \begin{equation*}
  V_{or} = V_s \sqrt{\frac{1}{\pi} \left[ (\beta - \alpha) - \frac{\sin(2\beta) - \sin(2\alpha)}{2} \right]}
  \end{equation*}
  Evaluate the sinusoidal arguments:
  \begin{align*}
  2\beta &= 2 \times 220^\circ = 440^\circ = 80^\circ \implies \sin(440^\circ) = \sin(80^\circ) = 0.9848 \notag\\
  2\alpha &= 2 \times 60^\circ = 120^\circ \implies \sin(120^\circ) = 0.8660 \notag\\
  \frac{\sin(2\beta) - \sin(2\alpha)}{2} &= \frac{0.9848 - 0.8660}{2} = \frac{0.1188}{2} = 0.0594
  \end{align*}
  Now evaluate the term inside the square root:
  \begin{align*}
  \text{Term} &= \frac{1}{\pi} [2.7925 - 0.0594] = \frac{2.7331}{3.1416} = 0.8700 \notag\\
  \sqrt{\text{Term}} &= \sqrt{0.8700} \approx 0.9327
  \end{align*}
  Therefore, the RMS output voltage is:
  \begin{equation*}
  \mathbf{V_{or}} = 230 \times 0.9327 = \mathbf{214.5\text{ V}}
  \end{equation*}
\end{enumerate}
\end{examplebox}

\subsection{Problem 3: Single-Phase Full-Bridge Square-Wave Inverter Analysis}
\begin{examplebox}[Problem 3: Square-Wave Full-Bridge Inverter Analysis]
\textbf{Statement:} A single-phase full-bridge inverter is fed from a $48\text{ V}$ battery bank and delivers power to a series $RL$ load with $R = 5\,\Omega$ and $L = 20\text{ mH}$ operating at fundamental frequency $f = 50\text{ Hz}$. Determine:
\begin{enumerate}
  \item The total RMS output voltage $V_{or}$ and the fundamental RMS output voltage $V_{o1(rms)}$.
  \item The Fourier expression for the fundamental load current $i_{o1}(t)$ and its RMS magnitude $I_{o1(rms)}$.
  \item The fundamental active power $P_1$ absorbed by the load.
  \item The total harmonic distortion of the output voltage $\text{THD}_v$.
\end{enumerate}

\tcblower
\textbf{Solution:}
\begin{enumerate}
  \item \textbf{Output Voltages:}
  For a full-bridge square wave inverter:
  \begin{align*}
  \mathbf{V_{or}} &= V_{dc} = \mathbf{48.0\text{ V}} \notag\\
  \mathbf{V_{o1(rms)}} &= \frac{2\sqrt{2}}{\pi} V_{dc} = \frac{2\sqrt{2}}{\pi} \times 48 = 0.9003 \times 48 = \mathbf{43.21\text{ V}}
  \end{align*}
  Peak fundamental voltage: $\hat{V}_{o1} = \frac{4V_{dc}}{\pi} = \frac{4 \times 48}{\pi} = 61.12\text{ V}$.

  \item \textbf{Fundamental Load Current:}
  At $f = 50\text{ Hz}$, angular frequency $\omega = 2\pi \times 50 = 314.16\text{ rad/s}$.
  \begin{align*}
  X_{L1} &= \omega L = 314.16 \times 20 \times 10^{-3} = 6.283\,\Omega \notag\\
  Z_1 &= \sqrt{R^2 + X_{L1}^2} = \sqrt{5^2 + (6.283)^2} = \sqrt{25 + 39.48} = \sqrt{64.48} = 8.03\,\Omega \notag\\
  \phi_1 &= \arctan\left(\frac{6.283}{5}\right) = \arctan(1.2566) = 51.49^\circ = 0.8987\text{ rad}
  \end{align*}
  Peak fundamental load current:
  \begin{equation*}
  \hat{I}_{o1} = \frac{\hat{V}_{o1}}{Z_1} = \frac{61.12\text{ V}}{8.03\,\Omega} = 7.61\text{ A} \implies \mathbf{I_{o1(rms)}} = \frac{7.61}{\sqrt{2}} = \mathbf{5.38\text{ A}}
  \end{equation*}
  The instantaneous fundamental current expression is:
  \begin{equation*}
  \mathbf{i_{o1}(t) = 7.61 \sin(314.16 t - 51.49^\circ)\text{ A}}
  \end{equation*}

  \item \textbf{Fundamental Active Power ($P_1$):}
  \begin{equation*}
  \mathbf{P_1} = I_{o1(rms)}^2 \cdot R = (5.38)^2 \times 5 = 28.94 \times 5 = \mathbf{144.7\text{ W}}
  \end{equation*}

  \item \textbf{Total Harmonic Distortion ($\text{THD}_v$):}
  \begin{equation*}
  \mathbf{\text{THD}_v} = \sqrt{\frac{V_{or}^2 - V_{o1(rms)}^2}{V_{o1(rms)}^2}} = \sqrt{\left(\frac{48}{43.21}\right)^2 - 1} = \sqrt{1.2337 - 1} = \mathbf{48.34\%}
  \end{equation*}
\end{enumerate}
\end{examplebox}

\subsection{Problem 4: SPWM Full-Bridge Inverter with Bipolar Voltage Switching}
\begin{examplebox}[Problem 4: Bipolar SPWM Inverter Parameter Sizing]
\textbf{Statement:} A single-phase full-bridge inverter utilizing sinusoidal PWM with bipolar switching is supplied from a $V_{dc} = 300\text{ V}$ DC rail. The carrier frequency is $f_s = 2.0\text{ kHz}$ and the desired fundamental output frequency is $f_o = 50\text{ Hz}$. The amplitude of the triangular carrier is $\hat{V}_{\text{tri}} = 5\text{ V}$, and the amplitude of the control reference is $\hat{V}_{\text{control}} = 4\text{ V}$.
\begin{enumerate}
  \item Determine the amplitude modulation index $m_a$ and frequency modulation ratio $m_f$.
  \item Calculate the peak and RMS fundamental output voltages.
  \item Identify the frequencies of the first four dominant harmonic components in the output voltage.
\end{enumerate}

\tcblower
\textbf{Solution:}
\begin{enumerate}
  \item \textbf{Modulation Indices:}
  \begin{align*}
  \mathbf{m_a} &= \frac{\hat{V}_{\text{control}}}{\hat{V}_{\text{tri}}} = \frac{4\text{ V}}{5\text{ V}} = \mathbf{0.80} \notag\\
  \mathbf{m_f} &= \frac{f_s}{f_o} = \frac{2000\text{ Hz}}{50\text{ Hz}} = \mathbf{40}
  \end{align*}
  \textit{Design Note:} In practical design, $m_f$ would be selected as an odd integer (e.g., 39 or 41) to ensure half-wave symmetry and eliminate even harmonics.

  \item \textbf{Fundamental Output Voltages:}
  Since $m_a = 0.80 \le 1.0$, the inverter operates in the linear modulation range:
  \begin{align*}
  \mathbf{\hat{V}_{o1}} &= m_a \cdot V_{dc} = 0.80 \times 300\text{ V} = \mathbf{240.0\text{ V}} \notag\\
  \mathbf{V_{o1(rms)}} &= \frac{\hat{V}_{o1}}{\sqrt{2}} = \frac{240}{\sqrt{2}} = \mathbf{169.7\text{ V}}
  \end{align*}

  \item \textbf{Dominant Harmonic Frequencies:}
  For bipolar switching, harmonics appear as sidebands centered around $m_f$ and its multiples:
  \begin{itemize}
    \item Center harmonic: $f_{m_f} = m_f \cdot f_o = 40 \times 50 = \mathbf{2000\text{ Hz}}$.
    \item Sidebands around $m_f$: $(m_f \pm 2) f_o = (40 \pm 2) \times 50 \implies \mathbf{1900\text{ Hz}}$ and $\mathbf{2100\text{ Hz}}$.
    \item Sidebands around $2m_f$: $2m_f \cdot f_o = 4000\text{ Hz}$; sidebands at $(2m_f \pm 1) f_o \implies \mathbf{3950\text{ Hz}}$ and $\mathbf{4050\text{ Hz}}$.
  \end{itemize}
\end{enumerate}
\end{examplebox}

\subsection{Problem 5: SPWM Full-Bridge Inverter with Unipolar Voltage Switching}
\begin{examplebox}[Problem 5: Unipolar Switching vs. Bipolar Output Filter Sizing]
\textbf{Statement:} The inverter of Problem 4 is reconfigured to operate with **unipolar voltage switching** with the same DC link voltage ($V_{dc} = 300\text{ V}$), $m_a = 0.80$, and carrier frequency $f_s = 2\text{ kHz}$.
\begin{enumerate}
  \item Determine the peak and RMS fundamental output voltages.
  \item What is the lowest harmonic frequency present in the unipolar output voltage?
  \item If an $LC$ low-pass filter with corner frequency $f_c = \frac{1}{2\pi\sqrt{LC}}$ is designed to be one decade below the lowest harmonic frequency, calculate the required $LC$ product for both bipolar and unipolar PWM.
\end{enumerate}

\tcblower
\textbf{Solution:}
\begin{enumerate}
  \item \textbf{Fundamental Voltages:}
  The fundamental output voltage in unipolar switching is identical to bipolar switching:
  \begin{align*}
  \mathbf{\hat{V}_{o1}} &= m_a \cdot V_{dc} = 0.80 \times 300 = \mathbf{240\text{ V}} \notag\\
  \mathbf{V_{o1(rms)}} &= \frac{240}{\sqrt{2}} = \mathbf{169.7\text{ V}}
  \end{align*}

  \item \textbf{Lowest Harmonic Frequency:}
  In unipolar switching, all harmonics centered around $m_f$ ($2000\text{ Hz}$) cancel out! The first cluster appears around $2m_f$:
  \begin{equation*}
  f_{\text{lowest}} = (2m_f - 1) f_o = (80 - 1) \times 50 = 79 \times 50 = \mathbf{3950\text{ Hz}} \approx \mathbf{4.0\text{ kHz}}
  \end{equation*}

  \item \textbf{$LC$ Filter Product Comparison:}
  \begin{itemize}
    \item \textbf{Bipolar PWM:} Lowest harmonic occurs around $f_s = 2000\text{ Hz}$. One decade below gives filter cutoff $f_{c,\text{bipolar}} = 200\text{ Hz}$:
    \begin{equation*}
    (LC)_{\text{bipolar}} = \frac{1}{(2\pi f_{c,\text{bipolar}})^2} = \frac{1}{(2\pi \times 200)^2} = \frac{1}{(1256.6)^2} = \mathbf{6.33 \times 10^{-7}\text{ s}^2}
    \end{equation*}
    \item \textbf{Unipolar PWM:} Lowest harmonic occurs around $2f_s = 4000\text{ Hz}$. One decade below gives filter cutoff $f_{c,\text{unipolar}} = 400\text{ Hz}$:
    \begin{equation*}
    (LC)_{\text{unipolar}} = \frac{1}{(2\pi \times 400)^2} = \frac{1}{(2513.3)^2} = \mathbf{1.58 \times 10^{-7}\text{ s}^2}
    \end{equation*}
  \end{itemize}
  \textbf{Conclusion:} Unipolar switching allows a **$4 \times$ reduction in the $LC$ product**, dramatically reducing filter inductor weight, copper losses, and capacitor cost!
\end{enumerate}
\end{examplebox}

\subsection{Problem 6: Three-Phase PWM Voltage Source Inverter}
\begin{examplebox}[Problem 6: Three-Phase SPWM Line-to-Line Voltage Calculation]
\textbf{Statement:} A three-phase bridge inverter is supplied from an electric vehicle battery pack of $V_{dc} = 400\text{ V}$. The inverter is controlled using three-phase sinusoidal PWM in the linear modulation range with $m_a = 0.85$ and $m_f = 21$.
\begin{enumerate}
  \item Calculate the peak and RMS values of the fundamental phase-to-neutral (pole) voltage.
  \item Calculate the peak and RMS values of the fundamental line-to-line output voltage.
  \item Calculate the maximum achievable RMS fundamental line-to-line voltage in the linear range ($m_a = 1.0$), and compare it to the six-step square-wave mode.
\end{enumerate}

\tcblower
\textbf{Solution:}
\begin{enumerate}
  \item \textbf{Fundamental Phase Voltage ($v_{Ao1}$):}
  \begin{align*}
  \mathbf{\hat{V}_{Ao1}} &= m_a \frac{V_{dc}}{2} = 0.85 \times \frac{400}{2} = \mathbf{170.0\text{ V}} \notag\\
  \mathbf{V_{Ao1(rms)}} &= \frac{\hat{V}_{Ao1}}{\sqrt{2}} = \frac{170}{\sqrt{2}} = \mathbf{120.2\text{ V}}
  \end{align*}

  \item \textbf{Fundamental Line-to-Line Voltage ($V_{LL1}$):}
  Using equations~\eqref{eq:vll1_peak} and~\eqref{eq:vll1_rms}:
  \begin{align*}
  \mathbf{\hat{V}_{LL1}} &= \sqrt{3} \hat{V}_{Ao1} = \sqrt{3} \times 170.0\text{ V} = \mathbf{294.4\text{ V}} \notag\\
  \mathbf{V_{LL1(rms)}} &= \frac{\sqrt{6}}{4} m_a V_{dc} = 0.6124 \times 0.85 \times 400 = \mathbf{208.2\text{ V}}
  \end{align*}

  \item \textbf{Maximum Voltage Comparison:}
  \begin{itemize}
    \item \textbf{Maximum Linear SPWM ($m_a = 1.0$):}
    \begin{equation*}
    V_{LL1(rms),\text{max}} = 0.6124 \times 400\text{ V} = \mathbf{245.0\text{ V}}
    \end{equation*}
    \item \textbf{Six-Step Square-Wave Mode:}
    \begin{equation*}
    V_{LL1(rms),\text{square}} = \frac{\sqrt{6}}{\pi} V_{dc} = \frac{\sqrt{6}}{\pi} \times 400 = 0.7797 \times 400 = \mathbf{311.9\text{ V}}
    \end{equation*}
  \end{itemize}
  Operating in six-step mode yields $\frac{311.9}{245.0} = 1.273$ ($+27.3\%$) higher fundamental voltage than linear SPWM.
\end{enumerate}
\end{examplebox}

\subsection{Problem 7: Third Harmonic Injection PWM (THIPWM) Voltage Boost}
\begin{examplebox}[Problem 7: THIPWM DC Bus Utilization Advantage]
\textbf{Statement:} A 3-phase inverter fed by a $V_{dc} = 600\text{ V}$ DC bus supplies a $415\text{ V}$ (RMS line-to-line), $50\text{ Hz}$ three-phase induction motor.
\begin{enumerate}
  \item Determine if standard sinusoidal PWM in the linear range can deliver the required $415\text{ V}$ RMS line-to-line motor voltage.
  \item Calculate the maximum line-to-line RMS voltage achievable using Third Harmonic Injection PWM (THIPWM) while remaining strictly within the linear modulation boundary.
  \item Can THIPWM supply the motor at rated voltage without overmodulation?
\end{enumerate}

\tcblower
\textbf{Solution:}
\begin{enumerate}
  \item \textbf{Maximum Linear Voltage with Standard SPWM:}
  For standard SPWM, the maximum modulation index is $m_a = 1.0$:
  \begin{equation*}
  V_{LL1(rms),\text{max (SPWM)}} = 0.6124 \times V_{dc} = 0.6124 \times 600\text{ V} = \mathbf{367.4\text{ V}}
  \end{equation*}
  Since $367.4\text{ V} < 415\text{ V}$, \textbf{standard SPWM cannot provide the rated voltage} without entering severe overmodulation distortion!

  \item \textbf{Maximum Linear Voltage with THIPWM:}
  With optimal third harmonic injection ($v_3 = \frac{1}{6}\hat{V}_1 \sin 3\omega t$), the maximum fundamental voltage in the linear range is boosted by $\frac{2}{\sqrt{3}} \approx 1.1547$:
  \begin{equation*}
  \mathbf{V_{LL1(rms),\text{max (THIPWM)}}} = \frac{V_{dc}}{\sqrt{2}} = \frac{600\text{ V}}{\sqrt{2}} = \mathbf{424.26\text{ V}}
  \end{equation*}

  \item \textbf{Feasibility Assessment:}
  Since $424.26\text{ V} > 415\text{ V}$, \textbf{THIPWM comfortably delivers the rated $415\text{ V}$ output} with $m_a = \frac{415}{424.26} = 0.978 \le 1.0$, completely avoiding low-order harmonic distortion!
\end{enumerate}
\end{examplebox}

\subsection{Problem 8: Analytical Evaluation of Dead-Time (Blanking Time) Voltage Drop}
\begin{examplebox}[Problem 8: Dead-Time Induced Fundamental Voltage Reduction]
\textbf{Statement:} A high-power IGBT three-phase inverter operates from a $V_{dc} = 750\text{ V}$ DC bus with switching frequency $f_s = 10\text{ kHz}$. To prevent shoot-through, a blanking time of $t_d = 2.5\,\mu\text{s}$ is programmed into the gate drive controller.
\begin{enumerate}
  \item Calculate the average voltage error $\Delta V_o$ per phase leg.
  \item Determine the percentage reduction in fundamental output voltage if the inverter is operating at modulation index $m_a = 0.20$ (low-speed motor operation).
  \item Propose how this distortion can be compensated in industrial DSP motor drives.
\end{enumerate}

\tcblower
\textbf{Solution:}
\begin{enumerate}
  \item \textbf{Average Leg Voltage Error ($\Delta V_o$):}
  Using equation~\eqref{eq:deadtime_voltage_drop}:
  \begin{equation*}
  \mathbf{\Delta V_o} = 4 f_s t_d V_{dc} = 4 \times (10 \times 10^3\text{ Hz}) \times (2.5 \times 10^{-6}\text{ s}) \times 750\text{ V}
  \end{equation*}
  \begin{equation*}
  \mathbf{\Delta V_o} = 4 \times 0.025 \times 750 = 0.10 \times 750 = \mathbf{75.0\text{ V}}
  \end{equation*}

  \item \textbf{Percentage Voltage Reduction at $m_a = 0.20$:}
  Nominal fundamental peak pole voltage without dead time:
  \begin{equation*}
  \hat{V}_{Ao1} = m_a \frac{V_{dc}}{2} = 0.20 \times \frac{750}{2} = 75.0\text{ V}
  \end{equation*}
  The fundamental component of the dead-time error square wave is $\frac{4}{\pi}\Delta V_o$:
  \begin{equation*}
  \hat{V}_{\text{error},1} = \frac{4}{\pi} (f_s t_d V_{dc}) = \frac{4}{\pi} \times 18.75 = 23.87\text{ V}
  \end{equation*}
  Percentage fundamental loss:
  \begin{equation*}
  \mathbf{\% \text{ Loss}} = \frac{23.87\text{ V}}{75.0\text{ V}} \times 100\% = \mathbf{31.8\%!}
  \end{equation*}
  At low speeds ($m_a = 0.20$), dead-time causes an enormous $31.8\%$ drop in motor flux and severe 5th/7th torque pulsations!

  \item \textbf{Compensation Strategy:}
  DSP controllers implement **Dead-Time Compensation**: the controller detects the sign of the phase current ($i_A > 0$ or $i_A < 0$) using current sensors and dynamically adds or subtracts a pulse width correction $\Delta t = t_d$ to the PWM timer registers, completely restoring fundamental voltage linearity!
\end{enumerate}
\end{examplebox}

\subsection{Problem 9: Power Factor and THD in Non-Sinusoidal Rectifiers}
\begin{examplebox}[Problem 9: True Power Factor and Distortion Factor Evaluation]
\textbf{Statement:} A single-phase diode bridge rectifier with a capacitive filter draws a non-sinusoidal input current from a $230\text{ V}$, $50\text{ Hz}$ supply. A power quality analyzer records the fundamental current component as $I_{s1} = 10\text{ A}$ (RMS) lagging the line voltage by $\phi_1 = 18^\circ$, and harmonic current components of: $I_{s3} = 7.5\text{ A}$, $I_{s5} = 4.5\text{ A}$, $I_{s7} = 2.0\text{ A}$, and $I_{s9} = 1.0\text{ A}$ (higher harmonics negligible).
\begin{enumerate}
  \item Calculate the total RMS input current $I_s$.
  \item Compute the current Total Harmonic Distortion ($\text{THD}_i$).
  \item Determine the Distortion Factor ($K_{\text{dist}}$) and Displacement Power Factor ($\text{DPF}$).
  \item Calculate the True Power Factor ($\text{PF}$) and real active power drawn from the mains.
\end{enumerate}

\tcblower
\textbf{Solution:}
\begin{enumerate}
  \item \textbf{Total RMS Current ($I_s$):}
  \begin{align*}
  I_{\text{dist}}^2 &= \sum_{h=3,5,7,9} I_{sh}^2 = (7.5)^2 + (4.5)^2 + (2.0)^2 + (1.0)^2 = 56.25 + 20.25 + 4.0 + 1.0 = 81.5\text{ A}^2 \notag\\
  I_s &= \sqrt{I_{s1}^2 + I_{\text{dist}}^2} = \sqrt{10^2 + 81.5} = \sqrt{181.5} = \mathbf{13.47\text{ A}}
  \end{align*}

  \item \textbf{Current Total Harmonic Distortion ($\text{THD}_i$):}
  \begin{equation*}
  \mathbf{\text{THD}_i} = \frac{\sqrt{I_{\text{dist}}^2}}{I_{s1}} = \frac{\sqrt{81.5}}{10} = \frac{9.028}{10} = 0.9028 \implies \mathbf{90.28\%}
  \end{equation*}

  \item \textbf{Distortion Factor and Displacement Factor:}
  \begin{align*}
  \mathbf{K_{\text{dist}}} &= \frac{I_{s1}}{I_s} = \frac{10\text{ A}}{13.47\text{ A}} = \mathbf{0.7424} \notag\\
  \mathbf{\text{DPF}} &= \cos\phi_1 = \cos(18^\circ) = \mathbf{0.9511}
  \end{align*}

  \item \textbf{True Power Factor and Real Power:}
  Using equation~\eqref{eq:true_pf}:
  \begin{equation*}
  \mathbf{\text{PF}} = K_{\text{dist}} \times \text{DPF} = 0.7424 \times 0.9511 = \mathbf{0.706\text{ (lagging)}}
  \end{equation*}
  Verification using equation~\eqref{eq:pf_from_thd}:
  \begin{equation*}
  \text{PF} = \frac{\cos(18^\circ)}{\sqrt{1 + (0.9028)^2}} = \frac{0.9511}{\sqrt{1 + 0.815}} = \frac{0.9511}{\sqrt{1.815}} = \frac{0.9511}{1.3472} = 0.706\text{ (Exact match!)}
  \end{equation*}
  Real active power consumed:
  \begin{equation*}
  \mathbf{P} = V_s I_{s1} \cos\phi_1 = 230 \times 10 \times 0.9511 = \mathbf{2187.5\text{ W} = 2.188\text{ kW}}
  \end{equation*}
  Apparent power: $S = V_s I_s = 230 \times 13.47 = 3098\text{ VA}$. $\text{PF} = 2187.5 / 3098 = 0.706$.
\end{enumerate}
\end{examplebox}

\subsection{Problem 10: Active Power Factor Correction (PFC) Boost Converter Design}
\begin{examplebox}[Problem 10: Active PFC Boost Inductor Sizing \& IEEE 519 Check]
\textbf{Statement:} A $1.5\text{ kW}$ single-phase Active PFC boost converter is connected to a $230\text{ V}_{\text{rms}}$, $50\text{ Hz}$ AC line. The regulated DC bus voltage is $V_d = 400\text{ V}$, switching frequency is $f_s = 100\text{ kHz}$, and target converter efficiency is $\eta = 95\%$.
\begin{enumerate}
  \item Determine the peak and RMS fundamental input currents drawn from the AC line.
  \item Calculate the maximum peak-to-peak inductor ripple current $\Delta I_{L,\text{max}}$ if ripple is limited to $20\%$ of peak input current.
  \item Calculate the required boost inductance $L$.
  \item At the customer Point of Common Coupling (PCC), the available short-circuit current is $I_{sc} = 650\text{ A}$. What is the maximum permissible total demand distortion (TDD) specified by IEEE 519?
\end{enumerate}

\tcblower
\textbf{Solution:}
\begin{enumerate}
  \item \textbf{Input Line Currents:}
  Input active power drawn from the mains:
  \begin{equation*}
  P_{\text{in}} = \frac{P_{\text{out}}}{\eta} = \frac{1500\text{ W}}{0.95} = 1578.9\text{ W}
  \end{equation*}
  Since the PFC converter shapes current to achieve near-unity power factor ($\text{PF} \approx 1.0$):
  \begin{align*}
  \mathbf{I_{s(rms)}} &= \frac{P_{\text{in}}}{V_s} = \frac{1578.9\text{ W}}{230\text{ V}} = \mathbf{6.86\text{ A}} \notag\\
  \mathbf{\hat{I}_s} &= \sqrt{2} \times I_{s(rms)} = \sqrt{2} \times 6.86 = \mathbf{9.71\text{ A}}
  \end{align*}

  \item \textbf{Maximum Inductor Ripple Current ($\Delta I_{L,\text{max}}$):}
  \begin{equation*}
  \mathbf{\Delta I_{L,\text{max}}} = 20\% \times \hat{I}_s = 0.20 \times 9.71\text{ A} = \mathbf{1.942\text{ A}}
  \end{equation*}

  \item \textbf{Boost Inductance Sizing ($L$):}
  In a boost PFC converter, the duty cycle varies continuously across the line cycle: $d(t) = 1 - \frac{|v_s(t)|}{V_d}$. The ripple current is:
  \begin{equation*}
  \Delta i_L = \frac{|v_s| \cdot d}{f_s L} = \frac{|v_s|}{f_s L} \left(1 - \frac{|v_s|}{V_d}\right)
  \end{equation*}
  Differentiating with respect to $|v_s|$ shows that maximum ripple occurs precisely when $|v_s| = \frac{V_d}{2} = \frac{400}{2} = 200\text{ V}$ (where duty cycle $d = 0.5$):
  \begin{equation*}
  \Delta I_{L,\text{max}} = \frac{V_d / 2 \cdot 0.5}{f_s L} = \frac{V_d}{4 f_s L}
  \end{equation*}
  Rearranging to solve for inductance $L$:
  \begin{align*}
  \mathbf{L} &= \frac{V_d}{4 f_s \Delta I_{L,\text{max}}} = \frac{400\text{ V}}{4 \times (100 \times 10^3\text{ Hz}) \times 1.942\text{ A}} \notag\\
  &= \frac{400}{776,800} = 5.15 \times 10^{-4}\text{ H} = \mathbf{0.515\text{ mH} \approx 520\,\mu\text{H}}
  \end{align*}

  \item \textbf{IEEE 519 TDD Limit Evaluation:}
  The maximum fundamental load current is $I_L = I_{s(rms)} = 6.86\text{ A}$. The Short-Circuit Ratio (SCR) at the PCC is:
  \begin{equation*}
  \mathbf{\text{SCR}} = \frac{I_{sc}}{I_L} = \frac{650\text{ A}}{6.86\text{ A}} = \mathbf{94.75}
  \end{equation*}
  From Table~\ref{tab:ieee519_limits}, for $50 < \frac{I_{sc}}{I_L} < 100$:
  \begin{equation*}
  \mathbf{\text{Maximum Permissible TDD}} = \mathbf{12.0\%}
  \end{equation*}
  Since active PFC achieves $\text{THD}_i < 5\%$, the installation effortlessly complies with IEEE 519 with massive safety margins!
\end{enumerate}
\end{examplebox}
'''
