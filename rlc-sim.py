import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk
from scipy.integrate import odeint

class RLCSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("RLC Circuit Simulator - AC Sinusoidal Input")
        self.root.geometry("1200x800")
        
        # Default parameters (resonance example)
        # At resonance: f0 = 1/(2*pi*sqrt(LC))
        # For L=0.1H, C=10uF: f0 ≈ 159 Hz
        self.R = 10.0      # Resistance in Ohms
        self.L = 0.1       # Inductance in Henries
        self.C = 10e-6     # Capacitance in Farads (10 μF)
        self.V0 = 10.0     # Input voltage amplitude in Volts
        self.freq = 159.15 # Frequency in Hz (set at resonance)
        
        # Create GUI
        self.create_widgets()
        
        # Initial simulation
        self.update_simulation()
    
    def create_widgets(self):
        # Control panel
        control_frame = ttk.Frame(self.root, padding="10")
        control_frame.pack(side=tk.LEFT, fill=tk.Y)
        
        ttk.Label(control_frame, text="RLC Circuit Parameters", 
                  font=('Arial', 14, 'bold')).pack(pady=10)
        
        # Resistance slider
        ttk.Label(control_frame, text="Resistance R (Ω)").pack(pady=5)
        self.R_var = tk.DoubleVar(value=self.R)
        self.R_slider = ttk.Scale(control_frame, from_=1, to=100, 
                                   variable=self.R_var, orient=tk.HORIZONTAL,
                                   command=self.on_parameter_change, length=300)
        self.R_slider.pack()
        self.R_label = ttk.Label(control_frame, text=f"{self.R:.1f} Ω")
        self.R_label.pack()
        
        # Inductance slider
        ttk.Label(control_frame, text="Inductance L (mH)").pack(pady=5)
        self.L_var = tk.DoubleVar(value=self.L * 1000)  # Display in mH
        self.L_slider = ttk.Scale(control_frame, from_=1, to=500, 
                                   variable=self.L_var, orient=tk.HORIZONTAL,
                                   command=self.on_parameter_change, length=300)
        self.L_slider.pack()
        self.L_label = ttk.Label(control_frame, text=f"{self.L*1000:.1f} mH")
        self.L_label.pack()
        
        # Capacitance slider
        ttk.Label(control_frame, text="Capacitance C (μF)").pack(pady=5)
        self.C_var = tk.DoubleVar(value=self.C * 1e6)  # Display in μF
        self.C_slider = ttk.Scale(control_frame, from_=0.1, to=100, 
                                   variable=self.C_var, orient=tk.HORIZONTAL,
                                   command=self.on_parameter_change, length=300)
        self.C_slider.pack()
        self.C_label = ttk.Label(control_frame, text=f"{self.C*1e6:.1f} μF")
        self.C_label.pack()
        
        # Voltage amplitude slider
        ttk.Label(control_frame, text="Input Voltage V₀ (V)").pack(pady=5)
        self.V0_var = tk.DoubleVar(value=self.V0)
        self.V0_slider = ttk.Scale(control_frame, from_=1, to=50, 
                                    variable=self.V0_var, orient=tk.HORIZONTAL,
                                    command=self.on_parameter_change, length=300)
        self.V0_slider.pack()
        self.V0_label = ttk.Label(control_frame, text=f"{self.V0:.1f} V")
        self.V0_label.pack()
        
        # Frequency slider
        ttk.Label(control_frame, text="Frequency f (Hz)").pack(pady=5)
        self.freq_var = tk.DoubleVar(value=self.freq)
        self.freq_slider = ttk.Scale(control_frame, from_=10, to=1000, 
                                      variable=self.freq_var, orient=tk.HORIZONTAL,
                                      command=self.on_parameter_change, length=300)
        self.freq_slider.pack()
        self.freq_label = ttk.Label(control_frame, text=f"{self.freq:.1f} Hz")
        self.freq_label.pack()
        
        # Info display
        ttk.Separator(control_frame, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=10)
        ttk.Label(control_frame, text="Circuit Information", 
                  font=('Arial', 12, 'bold')).pack(pady=5)
        
        self.info_text = tk.Text(control_frame, width=40, height=15, 
                                  font=('Courier', 9))
        self.info_text.pack(pady=5)
        
        # Buttons
        button_frame = ttk.Frame(control_frame)
        button_frame.pack(pady=10)
        
        ttk.Button(button_frame, text="Set to Resonance", 
                   command=self.set_resonance).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Reset", 
                   command=self.reset_parameters).pack(side=tk.LEFT, padx=5)
        
        # Plot area
        plot_frame = ttk.Frame(self.root)
        plot_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        self.fig = Figure(figsize=(10, 8))
        self.canvas = FigureCanvasTkAgg(self.fig, master=plot_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def rlc_derivatives(self, y, t, R, L, C, V0, omega):
        """
        Differential equations for series RLC circuit
        y[0] = charge Q on capacitor
        y[1] = dQ/dt = current I
        """
        Q, I = y
        
        # Input voltage
        V_in = V0 * np.sin(omega * t)
        
        # Kirchhoff's voltage law: V_in = V_R + V_L + V_C
        # V_in = R*I + L*dI/dt + Q/C
        # dI/dt = (V_in - R*I - Q/C) / L
        
        dQdt = I
        dIdt = (V_in - R * I - Q / C) / L
        
        return [dQdt, dIdt]
    
    def update_simulation(self):
        # Get current parameters
        self.R = self.R_var.get()
        self.L = self.L_var.get() / 1000  # Convert from mH to H
        self.C = self.C_var.get() / 1e6   # Convert from μF to F
        self.V0 = self.V0_var.get()
        self.freq = self.freq_var.get()
        
        omega = 2 * np.pi * self.freq
        
        # Calculate circuit properties
        omega0 = 1 / np.sqrt(self.L * self.C)  # Natural frequency (rad/s)
        f0 = omega0 / (2 * np.pi)              # Resonance frequency (Hz)
        Q_factor = omega0 * self.L / self.R    # Quality factor
        zeta = self.R / (2 * np.sqrt(self.L / self.C))  # Damping ratio
        Z = np.sqrt(self.R**2 + (omega * self.L - 1/(omega * self.C))**2)  # Impedance
        
        # Determine damping type
        if zeta > 1:
            damping_type = "Overdamped"
        elif zeta == 1:
            damping_type = "Critically damped"
        else:
            damping_type = "Underdamped"
        
        # Update info display
        self.info_text.delete(1.0, tk.END)
        info = f"""
Resonance frequency:
  f₀ = {f0:.2f} Hz
  ω₀ = {omega0:.2f} rad/s

Quality factor:
  Q = {Q_factor:.2f}

Damping ratio:
  ζ = {zeta:.3f}
  Type: {damping_type}

Impedance at f = {self.freq:.1f} Hz:
  Z = {Z:.2f} Ω

Current amplitude (steady-state):
  I₀ = {self.V0/Z:.4f} A

Power dissipated:
  P = {0.5 * (self.V0/Z)**2 * self.R:.4f} W
"""
        self.info_text.insert(1.0, info)
        
        # Time array for simulation
        t = np.linspace(0, 0.1, 2000)  # 100 ms simulation
        
        # Initial conditions: Q(0) = 0, I(0) = 0
        y0 = [0, 0]
        
        # Solve ODE
        solution = odeint(self.rlc_derivatives, y0, t, 
                          args=(self.R, self.L, self.C, self.V0, omega))
        
        Q = solution[:, 0]
        I = solution[:, 1]
        V_in = self.V0 * np.sin(omega * t)
        V_C = Q / self.C
        V_L = self.L * np.gradient(I, t)
        V_R = self.R * I
        
        # Clear and create new plots
        self.fig.clear()
        
        # Plot 1: Input voltage and current
        ax1 = self.fig.add_subplot(3, 1, 1)
        ax1.plot(t * 1000, V_in, 'b-', label='Input Voltage', linewidth=2)
        ax1_twin = ax1.twinx()
        ax1_twin.plot(t * 1000, I * 1000, 'r-', label='Current', linewidth=2)
        ax1.set_ylabel('Voltage (V)', color='b')
        ax1_twin.set_ylabel('Current (mA)', color='r')
        ax1.set_xlabel('Time (ms)')
        ax1.set_title('Input Voltage and Circuit Current')
        ax1.grid(True, alpha=0.3)
        ax1.legend(loc='upper left')
        ax1_twin.legend(loc='upper right')
        
        # Plot 2: Voltage across components
        ax2 = self.fig.add_subplot(3, 1, 2)
        ax2.plot(t * 1000, V_R, label='V_R (Resistor)', linewidth=1.5)
        ax2.plot(t * 1000, V_L, label='V_L (Inductor)', linewidth=1.5)
        ax2.plot(t * 1000, V_C, label='V_C (Capacitor)', linewidth=1.5)
        ax2.set_ylabel('Voltage (V)')
        ax2.set_xlabel('Time (ms)')
        ax2.set_title('Voltage Across Components')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        # Plot 3: Phasor diagram (last period)
        ax3 = self.fig.add_subplot(3, 1, 3)
        period = 1 / self.freq
        last_period_mask = t >= (t[-1] - 2 * period)
        t_last = t[last_period_mask]
        I_last = I[last_period_mask]
        V_in_last = V_in[last_period_mask]
        
        ax3.plot(t_last * 1000, V_in_last, 'b-', label='Input Voltage', linewidth=2)
        ax3_twin = ax3.twinx()
        ax3_twin.plot(t_last * 1000, I_last * 1000, 'r-', label='Current', linewidth=2)
        ax3.set_ylabel('Voltage (V)', color='b')
        ax3_twin.set_ylabel('Current (mA)', color='r')
        ax3.set_xlabel('Time (ms)')
        ax3.set_title('Steady-State Response (Last 2 Periods)')
        ax3.grid(True, alpha=0.3)
        ax3.legend(loc='upper left')
        ax3_twin.legend(loc='upper right')
        
        self.fig.tight_layout()
        self.canvas.draw()
        
        # Update labels
        self.R_label.config(text=f"{self.R:.1f} Ω")
        self.L_label.config(text=f"{self.L*1000:.1f} mH")
        self.C_label.config(text=f"{self.C*1e6:.1f} μF")
        self.V0_label.config(text=f"{self.V0:.1f} V")
        self.freq_label.config(text=f"{self.freq:.1f} Hz")
    
    def on_parameter_change(self, event=None):
        self.update_simulation()
    
    def set_resonance(self):
        """Set frequency to resonance frequency"""
        L = self.L_var.get() / 1000
        C = self.C_var.get() / 1e6
        f0 = 1 / (2 * np.pi * np.sqrt(L * C))
        self.freq_var.set(f0)
        self.update_simulation()
    
    def reset_parameters(self):
        """Reset to default parameters"""
        self.R_var.set(10.0)
        self.L_var.set(100.0)  # 100 mH
        self.C_var.set(10.0)   # 10 μF
        self.V0_var.set(10.0)
        self.freq_var.set(159.15)
        self.update_simulation()

def main():
    root = tk.Tk()
    app = RLCSimulator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
