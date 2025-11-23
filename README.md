# RLC Circuit Simulator Collection

A comprehensive collection of Python-based RLC (Resistor-Inductor-Capacitor) circuit simulation and analysis tools for educational and engineering purposes.

## 📋 Description

This repository contains multiple Python scripts for simulating and analyzing RLC circuits, including frequency response analysis, transient behavior, resonance phenomena, and an interactive GUI-based simulator with real-time parameter adjustment.

## 🚀 Features

### Interactive RLC Simulator (`rlc-sim.py`)
- **GUI-based simulation** with Tkinter for real-time parameter adjustment
- Adjustable parameters: Resistance (R), Inductance (L), Capacitance (C), Input Voltage (V₀), and Frequency (f)
- **Real-time visualization** of:
  - Input voltage and circuit current
  - Voltage across individual components (R, L, C)
  - Steady-state response analysis
- **Automatic calculations**:
  - Resonance frequency (f₀)
  - Quality factor (Q)
  - Damping ratio (ζ)
  - Impedance (Z)
  - Power dissipation
- One-click "Set to Resonance" button
- Default configuration demonstrates resonance behavior

### Analysis Tools

#### Bode Diagrams (`bode-diagram.py`, `bode-diagram2.py`)
- Frequency response analysis with magnitude and phase plots
- Logarithmic frequency scale
- Band-pass filter characteristics visualization
- Automatic resonance frequency marking
- -3 dB bandwidth indicators

#### Resonance Analysis (`resonance.py`)
- Resonance curves for different damping ratios
- Magnification factor visualization
- Comparison of underdamped, critically damped, and overdamped systems
- Frequency response relative to natural frequency (ω/ω₀)

#### Transient Response (`transient-response.py`)
- Step response analysis
- Comparison of underdamped, critically damped, and overdamped behaviors
- Time-domain analysis with different resistance values

#### Sinusoidal Response (`rlc-sin.py`)
- Forced oscillation analysis
- Steady-state and transient component separation
- Visualization of the transition from transient to steady-state behavior

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/FokaKefir/rlc-sim.git
cd rlc-sim
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## 🎮 Usage

### Interactive Simulator
```bash
python rlc-sim.py
```

**Controls:**
- Use sliders to adjust R, L, C, V₀, and frequency
- Click "Set to Resonance" to automatically set frequency to resonance point
- Click "Reset" to restore default parameters
- Observe real-time updates in graphs and circuit information panel

**Default Parameters:**
- R = 10 Ω
- L = 100 mH (0.1 H)
- C = 10 μF (10×10⁻⁶ F)
- V₀ = 10 V
- f = 159.15 Hz (resonance frequency)

### Analysis Scripts

**Bode Diagram (Band-pass filter):**
```bash
python bode-diagram2.py
```

**Resonance Curves:**
```bash
python resonance.py
```

**Transient Response:**
```bash
python transient-response.py
```

**Sinusoidal Response:**
```bash
python rlc-sin.py
```

## 📊 Circuit Theory

### Series RLC Circuit
The series RLC circuit is governed by Kirchhoff's voltage law:

$$V_{in}(t) = V_R + V_L + V_C = R \cdot I + L \frac{dI}{dt} + \frac{Q}{C}$$

### Key Formulas

**Resonance Frequency:**
$$f_0 = \frac{1}{2\pi\sqrt{LC}}$$

**Quality Factor:**
$$Q = \frac{\omega_0 L}{R} = \frac{1}{R}\sqrt{\frac{L}{C}}$$

**Damping Ratio:**
$$\zeta = \frac{R}{2}\sqrt{\frac{C}{L}}$$

**Impedance:**
$$Z = \sqrt{R^2 + \left(\omega L - \frac{1}{\omega C}\right)^2}$$

### Damping Types
- **Underdamped** (ζ < 1): Oscillatory decay
- **Critically damped** (ζ = 1): Fastest non-oscillatory decay
- **Overdamped** (ζ > 1): Slow non-oscillatory decay

## 📁 File Structure

```
rlc-sim/
├── rlc-sim.py              # Interactive GUI simulator (main application)
├── bode-diagram.py         # Basic Bode plot generator
├── bode-diagram2.py        # Advanced Bode plot with band-pass filter
├── resonance.py            # Resonance curve analysis
├── transient-response.py   # Step response and damping analysis
├── rlc-sin.py              # Sinusoidal forced oscillation analysis
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## 🔧 Dependencies

- **numpy**: Numerical computations and array operations
- **matplotlib**: Plotting and visualization
- **scipy**: Scientific computing, ODE solving, and signal processing

## 🎓 Educational Use

This collection is ideal for:
- Understanding RLC circuit behavior
- Visualizing frequency response and resonance
- Learning about damping and transient phenomena
- Experimenting with circuit parameter effects
- Teaching circuit analysis and control systems

## 📝 License

This project is open source and available for educational purposes.

## 👤 Author

**FokaKefir**
- GitHub: [@FokaKefir](https://github.com/FokaKefir)

## 🙏 Acknowledgments

Developed for electrical engineering and applied mathematics coursework at university.

## 🐛 Issues and Contributions

Feel free to open issues or submit pull requests for improvements and bug fixes.
