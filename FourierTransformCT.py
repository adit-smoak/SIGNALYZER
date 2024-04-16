import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import signal
def sinWaveCT(amp, freq, time):
  return amp * np.sin(2 * np.pi * freq * time)
def cosWaveCT(amp, freq, time):
  return amp * np.cos(2 * np.pi * freq * time)
def sinWaveFourierTransform(amplitude, frequency):
  omega0 = 2 * np.pi * frequency
  rounded_omega0 = round(omega0)
  print(rounded_omega0)
  x = range(-rounded_omega0 - 10, rounded_omega0 + 11)

  left_impulse_magnitude = -1 * amplitude * np.pi
  right_impulse_magnitude = amplitude * np.pi

  y = [0 for val in x]
  y[-11] = right_impulse_magnitude
  y[10] = left_impulse_magnitude

  plt.subplot(2, 1, 2)
  plt.plot(x, y, marker='o', markersize=3, markerfacecolor='blue')
  plt.title("Fourier Transform")
  plt.xlabel("Ω (rounded off to the nearest integer)")
  plt.ylabel("X(jΩ)")
  plt.tight_layout()
def cosWaveFourierTransform(amplitude, frequency):
  omega0 = 2 * np.pi * frequency
  rounded_omega0 = round(omega0)
  print(rounded_omega0)
  x = range(-rounded_omega0 - 10, rounded_omega0 + 11)

  impulse_magnitude = amplitude * np.pi

  y = [0 for val in x]
  y[-11] = impulse_magnitude
  y[10] = impulse_magnitude

  plt.subplot(2, 1, 2)
  plt.plot(x, y, marker='o', markersize=3, markerfacecolor='blue')
  plt.title("Fourier Transform")
  plt.xlabel("Ω (rounded off to the nearest integer)")
  plt.ylabel("X(jΩ)")
  plt.tight_layout()
def singleExpFourierTransform(A, a):
  print("Value at x = 0: ", A/a)
  x = np.linspace(-10, 10, 100)
  y = [A / (math.sqrt(a**2 + x**2)) for x in x]

  plt.subplot(2, 1, 2)
  plt.plot(x, y)
  plt.title("Magnitude of Fourier Transform")
  plt.xlabel("Omega (rad/s)")
  plt.ylabel("|X(jΩ)|")
  plt.tight_layout()
  plt.show()
def doubleExpFourierTransform(A, a):
  print("Value at x = 0: ", 2 * A/a)
  x = np.linspace(-10, 10, 100)
  y = [(2 * a * A) / (a**2 + x**2) for x in x]

  plt.subplot(2, 1, 2)
  plt.plot(x, y)
  plt.title("Magnitude of Fourier Transform")
  plt.xlabel("Omega (rad/s)")
  plt.ylabel("|X(jΩ)|")
  plt.tight_layout()
  plt.show()

def constantCTFourierTransform(c):
  x = np.linspace(-10, 10, 50)

  plt.subplot(2, 1, 2)
  plt.plot(0, [2 * np.pi * c], marker='o', color='red', label='y at x=0')
  plt.title("Magnitude of Fourier Transform")
  plt.xlabel("Omega (rad/s)")
  plt.ylabel("|X(jΩ)|")
  plt.tight_layout()
  plt.show()
def rectangularCTFourierTransform(edge_pt):
  x = np.linspace(-10, 10, 1000)
  t = edge_pt * 2
  y = [(t * np.sin(x * t/2)) / (x * t/2) for x in x]
  plt.subplot(2, 1, 2)
  plt.plot(x, y)
  plt.title("Magnitude of Fourier Transform")
  plt.xlabel("Omega (rad/s)")
  plt.ylabel("|X(jΩ)|")
  plt.tight_layout()
  plt.show()
def sgnFTHelper(i):
  if i == 0:
    return np.NAN
  else:
    return 2 / np.abs(i)

def sgnFourierTransform():
  x = np.linspace(-10, 10, 100)
  y = [sgnFTHelper(x) for x in x]
  plt.subplot(2, 1, 2)
  plt.plot(x, y)
  plt.title("Magnitude of Fourier Transform")
  plt.xlabel("Omega (rad/s)")
  plt.ylabel("|X(jΩ)|")
  plt.tight_layout()
  plt.show()

print("Welcome to Signalyzer: A tool for understanding how Fourier Transform works.")
print("Currently, the supported waveforms are:")
print("Constant value (type const in input box)")
print("Sine wave (type sin in input box)");
print("Cosine wave (type cos in input box)");
print("Single sided exponential wave (type single_exp in input box)");
print("Double sided exponential wave (type double_exp in input box)");
print("Rectangular pulse (type rect in input box)")
print("Signum Function (type sgn in input box)")


signal_type = input("Enter the type of signal: ")

sampling_rate = 1000
duration = 2.0

time_values = np.linspace(0, duration, int(sampling_rate * duration))

if(signal_type.lower() == "sin" or signal_type.lower() == "cos"):
  amplitude = int(input("Enter the amplitude: "))
  frequency = int(input("Enter the frequency: "))
  domain = input("Enter the domain of signal: Continuous Time[CT] or Discrete Time[DT]: ")
  if(domain.lower() == "ct" or domain.lower() == "dt"):
    pass
  else:
    print("Enter a valid domain!")

  if signal_type.lower() == "sin":
    sine_wave = sinWaveCT(amplitude, frequency, time_values)

  if signal_type.lower() == "cos":
    cos_wave = cosWaveCT(amplitude, frequency, time_values)


elif(signal_type.lower() == "single_exp" or signal_type.lower() == "double_exp"):
  init_val = int(input("Enter initial value A: "))
  decay_factor = int(input("Enter decay factor a: "))
  domain = input("Enter the domain of signal: Continuous Time[CT] or Discrete Time[DT]: ")
  if(domain.lower() == "ct" or domain.lower() == "dt"):
    pass
  else:
    print("Enter a valid domain!")
elif(signal_type.lower() == "const"):
  c = int(input("Enter the constant value: "))
elif(signal_type.lower() == "rect"):
  edge_point = int(input("Enter the positive edge point: "))
elif(signal_type.lower() == "sgn"):
  pass
else:
  print("Enter a valid choice!")


if(signal_type.lower() == "sin"):
  plt.figure(figsize=(10, 6))
  plt.subplot(2, 1, 1)
  plt.plot(time_values, sine_wave, label="Sine Wave")
  plt.xlabel("Time (s)")
  plt.ylabel("Amplitude")
  plt.title("Original Sine Wave")
  sinWaveFourierTransform(amplitude, frequency)

if(signal_type.lower() == "cos"):
  plt.figure(figsize=(10, 6))
  plt.subplot(2, 1, 1)
  plt.plot(time_values, cos_wave, label="Cos Wave")
  plt.xlabel("Time (s)")
  plt.ylabel("Amplitude")
  plt.title("Original Cosine Wave")
  cosWaveFourierTransform(amplitude, frequency)


if(signal_type.lower() == "single_exp"):
  x = np.linspace(0, 10, 100)
  y = init_val * np.exp(-1 * decay_factor * np.abs(x))
  plt.figure(figsize=(10, 6))
  plt.subplot(2, 1, 1)
  plt.plot(x, y, label="Single sided Exponential Wave")
  plt.xlabel("Time (s)")
  plt.ylabel("Amplitude")
  plt.title("Original Single sided Exponential Wave")
  singleExpFourierTransform(init_val, decay_factor)

if(signal_type.lower() == "double_exp"):
  x = np.linspace(-10, 10, 1000)
  y = np.where(x <= 0, init_val * np.exp(decay_factor * x), init_val * np.exp(-1 * decay_factor * x))

  plt.figure(figsize=(10, 6))
  plt.subplot(2, 1, 1)
  plt.plot(x, y, label="Double sided Exponential Wave")
  plt.xlabel("Time (s)")
  plt.ylabel("Amplitude")
  plt.title("Original Double sided Exponential Wave")
  doubleExpFourierTransform(init_val, decay_factor)

if(signal_type.lower() == "const"):
  x = np.linspace(-10, 10, 20)
  y = [c for x in x]
  plt.figure(figsize=(10, 6))
  plt.subplot(2, 1, 1)
  plt.plot(x, y, label="Constant Wave")
  plt.xlabel("Time (s)")
  plt.ylabel("Amplitude")
  plt.title("Original Constant Wave")
  constantCTFourierTransform(c)

if(signal_type.lower() == "rect"):
  x = np.linspace(-1 * edge_point-10, edge_point+10, 1000)
  y = np.where(np.logical_and(x > -1 * edge_point, x < edge_point), 1, 0)
  plt.figure(figsize=(10, 6))
  plt.subplot(2, 1, 1)
  plt.plot(x, y, label="Rectangular Wave")
  plt.xlabel("Time (s)")
  plt.ylabel("Amplitude")
  plt.title("Original Rectangular Wave")
  rectangularCTFourierTransform(edge_point)

if(signal_type.lower() == "sgn"):
  x = np.linspace(-10, 10, 500)
  y = np.where(x < 0, -1, 1)
  plt.figure(figsize=(10, 6))
  plt.subplot(2, 1, 1)
  plt.plot(x, y, label="Signum Wave")
  plt.xlabel("Time (s)")
  plt.ylabel("Amplitude")
  plt.title("Original Signum Wave")
  sgnFourierTransform()
