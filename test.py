import krach
from krach.source import frequency, oscillator
from krach.sink.alsa import AlsaSink
from krach.sink.wav import WaveSink
from krach.ext.plot import plot

osc = oscillator.sine_vibrato(frequency.constant(220), 0.5, 10)
sink = AlsaSink()
sink.sink([osc])
