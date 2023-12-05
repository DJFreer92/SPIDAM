import numpy as np
import wave as wav
import scipy as sci
from scipy.io.wavfile import read
from pydub import AudioSegment
import matplotlib.pyplot as plt
import os


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
        with wav.open(self.file_path, 'r') as audio_file:
            signal = np.frombuffer(audio_file.readframes(-1), dtype=np.int16)
            sample_rate = audio_file.getframerate()
            frequencies, power = sci.signal.fftconvolve(signal, signal)
        return frequencies[np.argmax(power)]

    def display_time_value(self):
        with wav.open(self.file_path, 'r') as audio_file:
            frames = audio_file.getnframes()
            rate = audio_file.getframerate()
            duration = frames / float(rate)
        return duration

    @staticmethod
    def plot_waveform(self):
        input_data = read(self.file_path)
        audio = input_data[1]
        plt.plot(audio[0:1024])
        plt.ylabel("Amplitude")
        plt.xlabel("Time")
        plt.title(self.file_path.split("/")[-1])
        plt.show()

    def compute_high_mid_low_frequency(self):
        with wav.open(self.file_path, 'rb') as audio_file:
            sampling_frequency = audio_file.getframerate()
            number_of_frames = audio_file.getnframes()
            raw_data = audio_file.readframes(number_of_frames)
            audio_file.close()
            data = np.frombuffer(raw_data, dtype='int16')
        return data, sampling_frequency



