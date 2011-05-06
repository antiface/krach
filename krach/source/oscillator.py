import math

from . import CycleEnded

def sine(freq):
    def f(t):
        return math.sin(2 * math.pi * freq(t) * t)
    return f

def sine_vibrato(freq, vibrato_freq, modulation):
    def f(t):
        return math.sin(2 * math.pi * freq(t) * t + modulation * math.sin(2 * math.pi * vibrato_freq * t))
    return f

def sawtooth(freq):
    def f(t):
        return 2 * (t * freq(t) - math.floor(t * freq(t) + 1./2))
    return f

def square(freq):
    simple_sine = sine(freq)
    def f(t):
        return 1 if simple_sine(t) > 0 else -1
    return f

def silence(): # (i kill you)
    def f(t):
        return 0
    return f

def cut_after(osc, cut_delta):
    class CutAfter(object):
        def __init__(self, osc, cut_delta):
            self.osc = osc
            self.cut_delta = cut_delta
            self.cut_t = None

        def __call__(self, t):
            if self.cut_t is None:
                self.cut_t = t + self.cut_delta
            if t >= self.cut_t:
                raise CycleEnded()
            else:
                return self.osc(t)

    return CutAfter(osc, cut_delta)
        
def combine_simple(osc):
    osc = osc[:]
    def f(t):
        amps = []
        for o in osc[:]:
            try:
                amps.append(o(t))
            except CycleEnded:
                osc.remove(o)
        if not amps:
            raise CycleEnded(f)
        return sum(amps) / float(len(amps))
    return f
