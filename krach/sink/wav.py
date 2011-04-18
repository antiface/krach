import wave
import struct

class WaveSink(object):
    def __init__(self, filename, sample_rate=44100, sample_width=2):
        self.filename = filename
        self.sample_rate = sample_rate
        self.sample_width = sample_width

    def sink(self, oscillators):
        print wave
        self.wav = wave.open(self.filename, 'w')
        self.wav.setnchannels(len(oscillators))
        self.wav.setframerate(self.sample_rate)
        self.wav.setsampwidth(self.sample_width)

        frame = 0
        buf = ''
        sample_width = self.sample_width
        sample_rate = self.sample_rate
        while 1:
            t = float(frame) / sample_rate
            amplitudes = [osc(t) for osc in oscillators]
            for amp in amplitudes:
                if amp is None:
                    return # TODO: the right way?
                self.wav.writeframes(struct.pack('<h', int(amp * (sample_width ** 8) / 2 - 1))) # TODO: sample width
            frame += 1

