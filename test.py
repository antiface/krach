import krach
from krach.source import frequency, oscillator
from krach.sink.alsa import AlsaSink
from krach.sink.wav import WaveSink
from krach.controller.sheet import create_sheet, SheetController

sheet = '[c4 e4 g4] [c4 e4 g4] [ab3 c4 eb4] [ab3 c4 eb4]'

sink = AlsaSink(8000)
controller = SheetController(sink, sheet)
controller.start()
