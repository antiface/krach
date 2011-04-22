import math
import itertools

from . import CycleEnded

def constant(frequency):
    def f(t):
        return frequency
    return f

def oscillating(frequency, vibrato_frequency, modulation):
    def f(t):
        return frequency(t) + modulation * math.sin(2 * math.pi * vibrato_frequency * t)
    return f

def periodic(duration, frequencies):
    class _Periodic(object):
        def __init__(self, duration, frequencies):
            self.duration = duration
            self.frequencies = frequencies
            self.iterator = itertools.cycle(frequencies)
            self.current = None
            self.next_t = 0

        def __call__(self, t):
            if t >= self.next_t:
                self.next_t = t + self.duration
                self.current = self.iterator.next()
            return self.current(t)

    return _Periodic(duration, frequencies)

def sheet(frequencies):
    class _Sheet(object):
        def __init__(self, frequencies):
            self.frequencies = frequencies
            self.iterator = iter(frequencies)
            self.current = (0, 0)
            self.last_t = 0

        def __call__(self, t):
            if t - self.last_t >= self.current[1]:
                self.last_t = t
                try:
                    self.current = self.iterator.next()
                except StopIteration:
                    raise CycleEnded(self)
            return self.current[0](t)

    return _Sheet(frequencies)
