import wave
import struct

class WaveSink(object):
    def __init__(self, filename, sample_rate=44100, sample_width=2):
        self.wav = None
        self.filename = filename
        self.sample_rate = sample_rate
        self.sample_width = sample_width
        self.frame = 0

    def sink(self, oscillators):
        if self.wav is None:
            self.wav = wave.open(self.filename, 'w')
            self.wav.setnchannels(len(oscillators))
            self.wav.setframerate(self.sample_rate)
            self.wav.setsampwidth(self.sample_width)

        sample_width = self.sample_width
        sample_rate = self.sample_rate
        while 1:
            t = float(self.frame) / sample_rate
            amplitudes = [osc(t) for osc in oscillators]
            for amp in amplitudes:
                if amp is None:
                    return # TODO: the right way?
                amp = int(amp * (2 ** (self.sample_width * 8 - 1) - 1))
                self.wav.writeframes(struct.pack('<h', amp)) # TODO: sample width
            self.frame += 1

