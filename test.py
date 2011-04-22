import krach
from krach.source import frequency, oscillator
from krach.sink.alsa import AlsaSink
from krach.sink.wav import WaveSink
from krach.ext.plot import plot
from krach.musical.equal import get_frequency_from_name

const = frequency.constant
osc1 = oscillator.sine(
    frequency.sheet((
        [(f, 0.3) for f in map(frequency.constant, map(get_frequency_from_name, ['a4', 'bb4', 'b4', 'c5', 'c#5']))]
    ))
)
osc2 = oscillator.sine(
    frequency.sheet((
        [(f, 0.3) for f in map(const, map(get_frequency_from_name, ['f4', 'f#4', 'g4', 'ab4', 'a4']))]
    ))
)
osc = oscillator.combine_simple([osc1, osc2])
sink = AlsaSink(8000)
sink.sink([osc])
