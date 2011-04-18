import krach
from krach.source import frequency, oscillator
from krach.sink.alsa import AlsaSink
from krach.sink.wav import WaveSink
from krach.ext.plot import plot

osc = oscillator.square(frequency.constant(110))
sink = AlsaSink()
sink.sink([osc])
