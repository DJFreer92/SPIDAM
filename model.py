import numpy as np
import wave as wav
import scipy as sci
import matplotlib.pyplot as plt
import os


class Model:
    def __init__(self):
        self.file_path = ''

    def set_file_path(self, file_path):
        if file_path.endswith(".wav"):
            self.file_path = file_path
        else:
            new_file_path = os.path.splitext(file_path)[0] + ".wav"
            with wav.open(new_file_path, 'wb') as wf:
                with wav.open(file_path, 'rb') as rf:
                    wf.setnchannels(rf.getnchannels())
                    wf.setsampwidth(rf.getsampwidth())
                    wf.setframerate(rf.getframerate())
                    wf.writeframes(rf.readframes(rf.getnframes()))
            self.file_path = new_file_path

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

    def compute_high_mid_low_frequency(self):
        with wav.open(self.file_path, 'rb') as audio_file:
            sampling_frequency = audio_file.getframerate()
            number_of_frames = audio_file.getnframes()
            raw_data = audio_file.readframes(number_of_frames)
            audio_file.close()
            data = np.frombuffer(raw_data, dtype='int16')
        return data, sampling_frequency

