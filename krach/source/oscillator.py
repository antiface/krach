import math

def sine(freq):
    def f(t):
        return math.sin(2 * math.pi * freq(t) * t)
    return f

def sine_vibrato(freq, vibrato_freq, modulation):
    def f(t):
        return math.sin(2 * math.pi * freq(t) * t + modulation * math.sin(2 * math.pi * vibrato_freq * t))
    return f
