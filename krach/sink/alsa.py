import alsaaudio
import struct

class AlsaSink(object):
    def __init__(self, sample_rate=44100, format=alsaaudio.PCM_FORMAT_S16_LE, period_size=32, card='default'):
        self.device = alsaaudio.PCM(card=card)
        self.sample_rate = sample_rate
        self.format = format
        self.period_size = period_size

    def sink(self, oscillators):
        self.device.setchannels(len(oscillators))
        self.device.setrate(self.sample_rate)
        self.device.setformat(self.format)
        self.device.setperiodsize(self.period_size)

        sample_rate = self.sample_rate
        period_size = self.period_size
        frame = 0
        buf = ''
        while 1:
            t = float(frame) / sample_rate
            amplitudes = [osc(t) for osc in oscillators]
            assert self.format == alsaaudio.PCM_FORMAT_S16_LE # TODO: other formats
            for amp in amplitudes:
                if amp is None:
                    return # TODO: the right way?
                amp = int(amp * (2 ** 15 - 1))
                buf += struct.pack('<h', amp) # TODO: sample width
            frame += 1
            if frame % self.period_size == 0:
                self.device.write(buf)
                buf = ''

