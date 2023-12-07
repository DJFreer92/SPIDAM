import numpy as np
import wave as wav
import scipy as sci
from pydub import AudioSegment
import matplotlib.pyplot as plt

class Model:
    def __init__(self):
        self.file_path = ''

    def set_file_path(self, file_path):
        if file_path.endswith(".wav"):
            sound = AudioSegment.from_wav(file_path)
            self.file_path = sound.export("NewClap.wav", format="wav")
        else:
            sound = AudioSegment.from_mp3(file_path)
            self.file_path = sound.export("NewClap.wav", format="wav")

    def set_single_channel(self):
        sound = AudioSegment.from_wav(self.file_path).set_channels(1)
        self.file_path = sound.export("NewClap.wav", format="wav")

    def compute_highest_resonance(self):
        audio_file = wav.open(self.file_path, 'r')
        signal = np.frombuffer(audio_file.readframes(-1), dtype=np.int16)
        frequencies, power = sci.signal.fftconvolve(signal, signal)
        audio_file.close()
        return frequencies[np.argmax(power)]

    def display_time_value(self):
        audio_file = wav.open(self.file_path, 'r')
        frames = audio_file.getnframes()
        rate = audio_file.getframerate()
        duration = frames / float(rate)
        audio_file.close()
        return duration

    def waveform(self):
        audio_file = wav.open(self.file_path, 'rb')
        signal = np.frombuffer(audio_file.readframes(-1), dtype=np.int16)
        plt.figure(figsize=(10, 6))
        plt.plot(signal)
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.title('Waveform')
        plt.show()

    def high_mid_low(self):
        audio_file = wav.open(self.file_path, 'rb')
        signal = np.frombuffer(audio_file.readframes(-1), dtype=np.int16)
        frequencies, power = sci.signal.welch(signal)
        high_cut = int(len(power) * 0.4)
        mid_cut = int(len(power) * 0.6)
        high_power = power[:high_cut]
        mid_power = power[high_cut:mid_cut]
        low_power = power[mid_cut:]
        plt.figure(figsize=(10, 6))
        time = np.arange(0, len(power)) * (1 / audio_file.getframerate())  # time array for x axis
        plt.plot(high_power)
        plt.plot(mid_power)
        plt.plot(low_power)
        plt.ylabel('Power')
        plt.title('High, Mid, and Low Frequencies')
        plt.show()




