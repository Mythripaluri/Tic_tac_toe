from scipy.io.wavfile import write
import numpy as np

# Function to generate a sound wave
def generate_sound(filename, frequency, duration=0.2, volume=0.5):
    sample_rate = 44100  # Sample rate (standard for WAV files)
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = volume * np.sin(2 * np.pi * frequency * t)

    wave = (wave * 32767).astype(np.int16)  # Convert to 16-bit PCM format
    write(filename, sample_rate, wave)
    print(f"{filename} has been created successfully!")

# Generate Tic-Tac-Toe sound effects
generate_sound("click.wav", frequency=1000, duration=0.1)  # Click sound
generate_sound("win.wav", frequency=600, duration=0.4)  # Win sound
generate_sound("draw.wav", frequency=400, duration=0.3)  # Draw sound
generate_sound("restart.wav", frequency=800, duration=0.2)  # Restart sound
