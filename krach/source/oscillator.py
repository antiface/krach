import math

def sine(freq):
    def f(t):
        return math.sin(2 * math.pi * freq(t) * t)
    return f
