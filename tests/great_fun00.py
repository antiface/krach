import krach
from krach.source import frequency, oscillator
from krach.sink.alsa import AlsaSink
from krach.ext.plot import plot

osc = oscillator.square(
            frequency.periodic(0.5, [
                frequency.oscillating(frequency.constant(110), 3, 2),
                frequency.constant(220)
            ])
    )
sink = AlsaSink()
sink.sink([osc])
