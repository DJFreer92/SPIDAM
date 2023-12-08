import numpy as np
import wave as wav
import scipy as sci
from pydub import AudioSegment
import matplotlib.pyplot as plt


class Model:

    def __init__(self):
        self.file_path, self.sample_rate, self.data, self.spectrum, self.freqs, self.t, self.im \
            = '', '', '', '', '', '', ''

    def set_values(self, sound):
        self.file_path = sound.export("NewClap.wav", format="wav")
        self.sample_rate, self.data = sci.io.wavfile.read(self.file_path)
        self.spectrum, self.freqs, self.t, self.im = plt.specgram(self.data, Fs=self.sample_rate, NFFT=1024,
                                                                  cmap=plt.get_cmap('autumn_r'))

    def set_file_path(self, file_path):
        if file_path.endswith(".wav"):
            sound = AudioSegment.from_wav(file_path)
            self.set_values(sound)
        else:
            sound = AudioSegment.from_mp3(file_path)
            self.set_values(sound)

    def set_single_channel(self):
        sound = AudioSegment.from_wav(self.file_path).set_channels(1)
        self.set_values(sound)

    def compute_highest_resonance(self):
        with wav.open(self.file_path, 'rb') as audio_file:
            signal_data = np.frombuffer(audio_file.readframes(-1), dtype=np.int16)
        frequencies, power = sci.signal.welch(signal_data, fs=audio_file.getframerate(), nperseg=1024)
        audio_file.close()
        highest_resonance_index = np.argmax(power)
        highest_resonance_frequency = frequencies[highest_resonance_index]
        print('%.3f' % highest_resonance_frequency)
        return highest_resonance_frequency

    def display_time_value(self):
        with wav.open(self.file_path, 'rb') as audio_file:
            frames = audio_file.getnframes()
            rate = audio_file.getframerate()
        duration = frames / float(rate)
        print('%.3f' % duration)
        return duration

    def waveform(self):
        with wav.open(self.file_path, 'rb') as audio_file:
            signal = np.frombuffer(audio_file.readframes(-1), dtype=np.int16)
        plt.figure(figsize=(10, 6))
        plt.plot(signal)
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.title('Waveform')
        plt.show()

    def high_mid_low(self):
        with wav.open(self.file_path, 'r') as audio_file:
            signal = np.frombuffer(audio_file.readframes(-1), dtype=np.int16)
        frequencies, power = sci.signal.welch(signal)
        high_cut = int(len(power) * 0.4)
        mid_cut = int(len(power) * 0.6)
        high_power = power[:high_cut]
        mid_power = power[high_cut:mid_cut]
        low_power = power[mid_cut:]

        plt.figure(figsize=(10, 6))
        plt.plot(high_power, 'g')
        plt.plot(mid_power, 'y')
        plt.plot(low_power, 'r')

        plt.ylabel('Power')
        plt.xlabel('Time')
        plt.title('High, Mid, and Low Frequencies')
        plt.show()

    def find_target_frequency(self, freqs):
        for x in freqs:
            if x > 1000:
                break
        return x

    def frequency_check(self):
        target_frequency = self.find_target_frequency(self.freqs)
        index_of_frequency = np.where(self.freqs == target_frequency)[0][0]
        data_for_frequency = self.spectrum[index_of_frequency]
        data_in_db_fun = 10 * np.log10(data_for_frequency)
        return data_in_db_fun

    def find_nearest_value(self,array,value):
        array = np.asarray(array)
        idx = (np.abs(array-value)).argmin()
        return array[idx]

    def plot_rt60(self):
        data_in_db = self.frequency_check()
        plt.figure()
        plt.plot(self.t, data_in_db)
        plt.xlabel('Time')
        plt.ylabel('Power')
        index_of_max = np.argmax(data_in_db)
        value_of_max = data_in_db[index_of_max]
        plt.plot(self.t[index_of_max], data_in_db[index_of_max], 'go')
        sliced_array = data_in_db[index_of_max:]
        value_of_max_less_5 = value_of_max - 5
        value_of_max_less_5 = self.find_nearest_value(sliced_array, value_of_max_less_5)
        index_of_max_less_5 = np.where(data_in_db == value_of_max_less_5)
        plt.plot(self.t[index_of_max_less_5], data_in_db[index_of_max_less_5], 'yo')
        value_of_max_less_25 = value_of_max - 25
        value_of_max_less_25 = self.find_nearest_value(sliced_array, value_of_max_less_25)
        index_of_max_less_25 = np.where(data_in_db == value_of_max_less_25)
        plt.plot(self.t[index_of_max_less_25], data_in_db[index_of_max_less_25], 'ro')
        rt20 = (self.t[index_of_max_less_5] - self.t[index_of_max_less_25])[0]
        rt60 = rt20*3
        plt.show()
        print('%.3f' % abs(rt60))
        return abs(rt60)
