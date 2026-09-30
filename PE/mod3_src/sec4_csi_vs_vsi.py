# -*- coding: utf-8 -*-
"""Section 4: Current Source Inverters (CSI) and Comparison with VSI"""

def get_section():
    return r'''
\section{Current Source Inverters (CSI) and Detailed Comparison with VSI}

\subsection{Operating Principle of Single-Phase Current Source Inverters (CSI)}

In contrast to a Voltage Source Inverter (which is fed from a stiff, low-impedance DC voltage source), a \textbf{Current Source Inverter (CSI)} is fed from an adjustable direct current source possessing \textbf{high internal impedance}. In practice, this is realized by placing a large smoothing choke ($L_{dc}$) in series with a controlled DC power supply or phase-controlled thyristor rectifier.

\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.95, every node/.style={transform shape}]
  % DC Current Source representation
  \draw[thick] (0, 3.5) -- (1.5, 3.5);
  \draw[thick] (0, 0.5) -- (1.5, 0.5);
  \draw[thick, fill=cardbg] (0, 1.5) rectangle (1.2, 2.5);
  \draw[thick, ->] (0.6, 1.7) -- (0.6, 2.3);
  \node[right, font=\footnotesize\bfseries] at (1.2, 2.0) {$I_{dc}$};
  \draw[thick] (0.6, 3.5) -- (0.6, 2.5);
  \draw[thick] (0.6, 0.5) -- (0.6, 1.5);
  
  % Large DC Inductor
  \draw[thick] (1.5, 3.5) to[decoration={coil,aspect=0.5,segment length=2mm,amplitude=2.5mm},decorate] (3.0, 3.5);
  \node[above, font=\footnotesize\bfseries, color=navyprimary] at (2.25, 3.8) {Large Choke $L_{dc}$};
  \draw[thick] (3.0, 3.5) -- (4.0, 3.5);
  \draw[thick] (1.5, 0.5) -- (4.0, 0.5);
  
  % H-Bridge Switches with Series Diodes
  % Leg 1: S1, D1 and S4, D4
  \draw[thick] (4.0, 3.5) -- (5.0, 3.5) -- (5.0, 3.0);
  % Switch S1
  \draw[thick, fill=cardbg] (4.6, 2.3) rectangle (5.4, 2.9);
  \node[font=\footnotesize\bfseries] at (5.0, 2.6) {$S_1$};
  % Diode D1
  \draw[thick] (5.0, 2.3) -- (5.0, 1.9);
  \draw[thick, fill=navyprimary] (4.75, 1.9) -- (5.25, 1.9) -- (5.0, 1.5) -- cycle;
  \draw[thick] (4.75, 1.5) -- (5.25, 1.5);
  \node[right, font=\tiny\bfseries] at (5.25, 1.7) {$D_1$};
  \draw[thick] (5.0, 1.5) -- (5.0, 1.2);
  
  % Leg 2: S3, D3 and S2, D2
  \draw[thick] (5.0, 3.5) -- (8.0, 3.5) -- (8.0, 3.0);
  % Switch S3
  \draw[thick, fill=cardbg] (7.6, 2.3) rectangle (8.4, 2.9);
  \node[font=\footnotesize\bfseries] at (8.0, 2.6) {$S_3$};
  % Diode D3
  \draw[thick] (8.0, 2.3) -- (8.0, 1.9);
  \draw[thick, fill=navyprimary] (7.75, 1.9) -- (8.25, 1.9) -- (8.0, 1.5) -- cycle;
  \draw[thick] (7.75, 1.5) -- (8.25, 1.5);
  \node[right, font=\tiny\bfseries] at (8.25, 1.7) {$D_3$};
  \draw[thick] (8.0, 1.5) -- (8.0, 1.2);
  
  % Output Load Terminals
  \draw[thick] (5.0, 1.2) -- (6.0, 1.2);
  \draw[thick] (8.0, 1.2) -- (7.0, 1.2);
  \draw[thick, fill=formulabg] (6.0, 0.9) rectangle (7.0, 1.5);
  \node[font=\footnotesize\bfseries, color=navyprimary] at (6.5, 1.2) {Load};
  
  % Lower Switches
  % S4, D4
  \draw[thick] (5.0, 1.2) -- (5.0, 0.9);
  \draw[thick, fill=navyprimary] (4.75, 0.9) -- (5.25, 0.9) -- (5.0, 0.5) -- cycle;
  \draw[thick] (4.75, 0.5) -- (5.25, 0.5);
  \node[right, font=\tiny\bfseries] at (5.25, 0.7) {$D_4$};
  \draw[thick] (5.0, 0.5) -- (5.0, 0.1);
  \draw[thick, fill=cardbg] (4.6, -0.5) rectangle (5.4, 0.1);
  \node[font=\footnotesize\bfseries] at (5.0, -0.2) {$S_4$};
  \draw[thick] (5.0, -0.5) -- (5.0, -0.8) -- (4.0, -0.8) -- (4.0, 0.5);
  
  % S2, D2
  \draw[thick] (8.0, 1.2) -- (8.0, 0.9);
  \draw[thick, fill=navyprimary] (7.75, 0.9) -- (8.25, 0.9) -- (8.0, 0.5) -- cycle;
  \draw[thick] (7.75, 0.5) -- (8.25, 0.5);
  \node[right, font=\tiny\bfseries] at (8.25, 0.7) {$D_2$};
  \draw[thick] (8.0, 0.5) -- (8.0, 0.1);
  \draw[thick, fill=cardbg] (7.6, -0.5) rectangle (8.4, 0.1);
  \node[font=\footnotesize\bfseries] at (8.0, -0.2) {$S_2$};
  \draw[thick] (8.0, -0.5) -- (8.0, -0.8) -- (5.0, -0.8);
\end{tikzpicture}
\caption{Single-phase IGBT-based Current Source Inverter (CSI) with series blocking diodes and massive DC smoothing inductor $L_{dc}$.}
\label{fig:csi_circuit}
\end{figure}

\subsubsection{Circuit Characteristics of the CSI}
\begin{enumerate}[leftmargin=*]
  \item \textbf{Constant Input Current ($I_{dc}$):} Due to the large inductance $L_{dc}$, the DC link current cannot change instantaneously:
  \begin{equation}
  i_{dc}(t) \approx I_{dc} = \text{constant (ripple-free)}
  \end{equation}
  \item \textbf{Square-Wave Output Current Waveform:} Gating switch pair $(S_1, S_2)$ directs $+I_{dc}$ through the load, while gating $(S_3, S_4)$ directs $-I_{dc}$ through the load. The output current $i_o(t)$ is therefore a \textbf{clean square wave alternating between $+I_{dc}$ and $-I_{dc}$}.
  \item \textbf{Need for Series Blocking Diodes ($D_1 - D_4$):}
  \begin{itemize}
    \item Standard power MOSFETs and IGBTs have anti-parallel body diodes or low reverse-blocking voltage ratings ($< 20\text{ V}$).
    \item In a CSI, the load voltage is alternating AC, meaning the switches must withstand \textbf{large reverse voltages}.
    \item Fast-recovery diodes are placed strictly in \textbf{series} with each controlled switch to provide the necessary reverse voltage blocking capability!
  \end{itemize}
  \item \textbf{Inherent Short-Circuit Immunity:} In a VSI, accidental simultaneous conduction of upper and lower switches causes an explosive shoot-through short circuit. In sharp contrast, in a CSI, \textbf{simultaneous conduction of upper and lower switches merely circulates the constant DC current $I_{dc}$ without any current spike!}
  \item \textbf{Open-Circuit Danger:} In a CSI, an open circuit in the load or DC path is catastrophic ($L \frac{di}{dt} \to \infty$, generating thousands of volts of inductive overvoltage arc breakdown). An overlap period is mandatory during commutation!
\end{enumerate}

\subsection{Comprehensive Technical Comparison: VSI vs. CSI}

The comparison between Voltage Source Inverters and Current Source Inverters is a quintessential KTU university examination question (often awarded 6 to 9 marks). Table~\ref{tab:vsi_vs_csi} provides an exhaustive, multi-dimensional comparison.

\begin{table}[htbp]
\centering
\small
\caption{Definitive Technical Comparison: Voltage Source Inverter (VSI) vs. Current Source Inverter (CSI)}
\label{tab:vsi_vs_csi}
\begin{tabularx}{\textwidth}{l p{6.5cm} X}
\toprule
\textbf{Feature / Parameter} & \textbf{Voltage Source Inverter (VSI)} & \textbf{Current Source Inverter (CSI)} \\
\midrule
\textbf{DC Source Characteristic} & Stiff DC voltage source with very small internal impedance & Stiff DC current source with very high internal impedance \\
\textbf{Energy Storage Element} & Large DC-link capacitor bank ($C_{dc}$) across input terminals & Large DC-link smoothing inductor / choke ($L_{dc}$) in series \\
\textbf{Output Voltage Waveform} & Controlled square wave or PWM pulsed waveform (independent of load) & Determined entirely by load impedance and current \\
\textbf{Output Current Waveform} & Determined entirely by the connected load impedance & Pure square wave or PWM current waveform (independent of load) \\
\textbf{Freewheeling / Blocking Diodes} & Requires freewheeling diodes in \textbf{anti-parallel} with switches & Requires blocking diodes in \textbf{series} with switches \\
\textbf{Regeneration Capability} & Requires a four-quadrant dual converter or active front-end rectifier & Natural and simple: just reverse the DC voltage polarity while $I_{dc}$ remains unidirectional \\
\textbf{Short-Circuit Behavior} & Highly vulnerable: leg shoot-through creates catastrophic short circuit & Inherent short-circuit ride-through; fault current limited by $I_{dc}$ \\
\textbf{Open-Circuit Behavior} & Safe: open circuit causes no damage & Extremely hazardous: open-circuit produces destructive inductive $L \frac{di}{dt}$ voltage spikes \\
\textbf{Switching Overlap Requirements} & Strict \textbf{blanking time (dead-time)} mandatory to avoid shoot-through & Strict \textbf{overlap time} mandatory to avoid open-circuiting the DC choke \\
\textbf{Switch Ratings} & High current rating, unidirectional voltage blocking & High reverse voltage blocking capability required \\
\textbf{Dynamic Response} & Extremely fast (voltage switched instantaneously) & Slower due to large magnetic time constant of $L_{dc}$ \\
\textbf{Size, Weight \& Cost} & Compact and lightweight (uses electrolytic/film capacitors) & Bulky, heavy, and expensive due to massive iron-core DC reactor \\
\textbf{Primary Industrial Use} & General-purpose industrial VFDs, solar inverters, EV traction, UPS & High-power multi-megawatt synchronous motor drives, induction heating \\
\bottomrule
\end{tabularx}
\end{table}
'''
