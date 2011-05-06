from . import Controller
from krach.musical.equal import get_frequency_from_name
from krach.source import CycleEnded
from krach.source.oscillator import sine, cut_after, combine_simple
from krach.source.frequency import constant

def parse_sheet(s):
    char = None
    i = 0
    note = ''
    stack = [[]]
    while i < len(s):
        char = s[i]
        if char == '[':
            if note:
                stack[-1].append(note)
                note = ''
            stack.append([])
        elif char == ']':
            if note:
                stack[-1].append(note)
                note = ''
            l = stack.pop()
            stack[-1].append(l)
        elif char == ' ':
            if note:
                stack[-1].append(note)
                note = ''
        else:
            note += char
        i += 1
    assert len(stack) == 1
    return stack[0]

def create_sheet(parsed, duration=0.3):
    sheet = []
    for elem in parsed:
        if isinstance(elem, str):
            print 'constant frequency', elem
        elif isinstance(elem, (list, tuple)):
            print 'chord:', elem
        else:
            raise Exception(elem)
    return sheet

class SheetController(Controller):
    def __init__(self, sink, sheet, oscillator=sine, duration=0.3, get_frequency=lambda n: constant(get_frequency_from_name(n))):
        self.sink = sink
        self.parsed = parse_sheet(sheet)
        self.oscillator = oscillator
        self.get_frequency = get_frequency
        self.duration = duration

    def start(self):
        for elem in self.parsed:
            oscillators = []
            if isinstance(elem, str):
                # constant frequency, only one oscillator needed
                oscillators.append(self.oscillator(self.get_frequency(elem)), self.duration)
            elif isinstance(elem, (list, tuple)):
                for name in elem:
                    oscillators.append(self.oscillator(self.get_frequency(name)))
            try:
                osc = combine_simple([cut_after(o, self.duration) for o in oscillators])
                self.sink.sink([osc])
            except CycleEnded:
                pass
