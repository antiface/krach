import krach
from krach.source import frequency, oscillator
from krach.sink.alsa import AlsaSink
from krach.sink.wav import WaveSink
from krach.controller.sheet import create_sheet, SheetController

sheet = 'a4 bb4 c5 a4 bb4 c5 d5 bb4 c5'

sink = AlsaSink(8000)
controller = SheetController(sink, sheet)
controller.start()
