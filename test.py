import krach
from krach.source import frequency, oscillator
from krach.sink.alsa import AlsaSink
from krach.sink.wav import WaveSink
from krach.ext.plot import plot

osc = oscillator.sine(frequency.vibrato(frequency.constant(220), 0.5, 3))
sink = AlsaSink(12000)
sink.sink([osc])
