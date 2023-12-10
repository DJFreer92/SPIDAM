import numpy as np
import wave as wav
import scipy as sci
from pydub import AudioSegment
import matplotlib.pyplot as plt

class Model:
    def __init__(self):
        # Initialize all variables needed in self
        self.file_path, self.sample_rate, self.data, self.spectrum, self.freqs, self.t, self.im \
            = '', '', '', '', '', '', ''

    def set_values(self, sound):
        # Setting the file path of the sound to be analyzed
        self.file_path = sound.export("Clap.wav", format = "wav")

        # Sets variables from L26
        self.sample_rate, self.data = sci.io.wavfile.read(self.file_path)
        self.spectrum, self.freqs, self.t, self.im = plt.specgram(self.data, Fs = self.sample_rate, NFFT = 1024,
                                                                  cmap = plt.get_cmap('autumn_r'))
        plt.close()

    def set_file_path(self, file_path):
        # Handle wav and mp3, then calling set_values to handle file_path
        if file_path.endswith(".wav"):
            sound = AudioSegment.from_wav(file_path)
            self.set_values(sound)
        elif file_path.endswith(".mp3"):
            sound = AudioSegment.from_mp3(file_path)
            self.set_values(sound)

    def set_single_channel(self):
        # Simple channel set function
        sound = AudioSegment.from_wav(self.file_path).set_channels(1)

        # Handle file_path
        self.set_values(sound)

    def compute_highest_resonance(self):
        # Opens the wav file for reading to pull signal, then closes it
        with wav.open(self.file_path, 'rb') as audio_file:
            signal_data = np.frombuffer(audio_file.readframes(-1), dtype = np.int16)

        # Pull the frequency and power from the signal
        frequencies, power = sci.signal.welch(signal_data, fs = audio_file.getframerate(), nperseg = 1024)
        highest_resonance_index = np.argmax(power)
        highest_resonance_frequency = frequencies[highest_resonance_index]

        # Reinitialize the file, as wave closes the file once the function is complete
        self.set_file_path('Clap.wav')

        # Passing the value of the resonance frequency
        return highest_resonance_frequency

    def display_time_value(self):
        # Opens the wav file for reading to get the frames and frame rate, as well as calculating the time of the file
        with wav.open(self.file_path, 'rb') as audio_file:
            frames = audio_file.getnframes()
            rate = audio_file.getframerate()
            duration = frames / float(rate)

        # Reinitialize the file, as wave closes the file once the function is complete
        self.set_file_path('Clap.wav')

        # Passing the time of the file
        return duration

    def waveform(self):
        # Opens the wav file for reading to pull signal, then closes it
        with wav.open(self.file_path, 'rb') as audio_file:
            signal = np.frombuffer(audio_file.readframes(-1), dtype = np.int16)

        # Plot the signal
        plt.figure(figsize = (10, 6))
        plt.plot(signal)
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.title('Waveform')
        plt.show()

        # Reinitialize the file, as wave closes the file once the function is complete
        self.set_file_path('Clap.wav')

        # Passing the signal for possible future use
        return signal

    def useful_waveform(self):
        # Opens the wav file for reading to pull signal, then closes it
        with wav.open(self.file_path, 'rb') as audio_file:
            signal = np.frombuffer(audio_file.readframes(-1), dtype = np.int16)

        # Cuts signify areas of the signal that represent different frequencies or power
        plt.figure(figsize = (10, 6))
        useful_cut = int(len(signal) * 0.1)
        useful_wave = signal[:useful_cut]

        # Plot the signal
        plt.plot(useful_wave)
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.title('"Useful" Waveform')
        plt.show()

        # Reinitialize the file, as wave closes the file once the function is complete
        self.set_file_path('Clap.wav')

        # Passing the modified signal for possible future use
        return signal

    def high(self):
        # Opens the wav file for reading to pull signal, then closes it
        with wav.open(self.file_path, 'r') as audio_file:
            signal = np.frombuffer(audio_file.readframes(-1), dtype = np.int16)

        # Cuts signify areas of the signal that represent different frequencies or power
        high_cut = int(len(signal) * 0.4)
        high_wave = signal[:high_cut]
        plt.figure(figsize = (10, 6))
        plt.plot(high_wave, 'g')
        plt.ylabel('Amplitude')
        plt.xlabel('Time')
        plt.title('High Waveform')
        plt.show()

        # Reinitialize the file, as wave closes the file once the function is complete
        self.set_file_path('Clap.wav')

        # Passing the modified signal for possible future use
        return high_wave

    def mid(self):
        # Opens the wav file for reading to pull signal, then closes it
        with wav.open(self.file_path, 'r') as audio_file:
            signal = np.frombuffer(audio_file.readframes(-1), dtype = np.int16)

        # Cuts signify areas of the signal that represent different frequencies or power
        high_cut = int(len(signal) * 0.4)
        mid_cut = int(len(signal) * 0.6)
        mid_wave = signal[high_cut:mid_cut]

        # Plot the signal
        plt.figure(figsize = (10, 6))
        plt.plot(mid_wave, 'y')
        plt.ylabel('Amplitude')
        plt.xlabel('Time')
        plt.title('Mid Waveform')
        plt.show()

        # Reinitialize the file, as wave closes the file once the function is complete
        self.set_file_path('Clap.wav')

        # Passing the modified signal for possible future use
        return mid_wave

    def low(self):
        # Opens the wav file for reading to pull signal, then closes it
        with wav.open(self.file_path, 'r') as audio_file:
            signal = np.frombuffer(audio_file.readframes(-1), dtype = np.int16)

        # Cuts signify areas of the signal that represent different frequencies or power
        mid_cut = int(len(signal) * 0.6)
        low_wave = signal[mid_cut:]

        # Plotting the waveform
        plt.figure(figsize = (10, 6))
        plt.plot(low_wave, 'r')
        plt.ylabel('Amplitude')
        plt.xlabel('Time')
        plt.title('Low Waveform')
        plt.show()

        # Reinitialize the file, as wave closes the file once the function is complete
        self.set_file_path('Clap.wav')

        # Passing the modified signal for possible future use
        return low_wave

    @staticmethod
    def find_target_frequency(freqs):
        for x in freqs:
            if x > 1000:
                return x

    def frequency_check(self):
        target_frequency = self.find_target_frequency(self.freqs)
        index_of_frequency = np.where(self.freqs == target_frequency)[0][0]
        data_for_frequency = self.spectrum[index_of_frequency]
        data_in_db_fun = 10 * np.log10(data_for_frequency)
        return data_in_db_fun

    @staticmethod
    def find_nearest_value(array, value):
        array = np.asarray(array)
        idx = (np.abs(array - value)).argmin()
        return array[idx]

    def plot_rt60(self):
        data_in_db = self.frequency_check()
        plt.figure()
        plt.plot(self.t, data_in_db)
        plt.xlabel('Time')
        plt.ylabel('Power')
        plt.title('RT60 Graph')
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
        rt60 = rt20 * 3
        plt.show()
        self.set_file_path('Clap.wav')

        # Returns the rt60 time for possible future use
        return abs(rt60)

    def rt60_diff(self):
        # Uses code from L26 pptx
        data_in_db = self.frequency_check()
        index_of_max = np.argmax(data_in_db)
        value_of_max = data_in_db[index_of_max]
        sliced_array = data_in_db[index_of_max:]
        value_of_max_less_5 = value_of_max - 5
        value_of_max_less_5 = self.find_nearest_value(sliced_array, value_of_max_less_5)
        index_of_max_less_5 = np.where(data_in_db == value_of_max_less_5)
        value_of_max_less_25 = value_of_max - 25
        value_of_max_less_25 = self.find_nearest_value(sliced_array, value_of_max_less_25)
        index_of_max_less_25 = np.where(data_in_db == value_of_max_less_25)
        rt20 = (self.t[index_of_max_less_5] - self.t[index_of_max_less_25])[0]
        rt60 = rt20 * 3

        # Returns the rt60 time
        return '%.3f' % (abs(rt60) - 0.5)
