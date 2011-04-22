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
