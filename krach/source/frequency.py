import math

def constant(frequency):
    def f(t):
        return frequency
    return f

def vibrato(frequency, vibrato_frequency, modulation):
    def f(t):
        return frequency(t) + modulation * math.sin(2 * math.pi * vibrato_frequency * t)
    return f

