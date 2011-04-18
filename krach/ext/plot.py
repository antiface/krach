import matplotlib.pyplot as plt

def plot(func, a=0, b=5, interval=0.01):
    xes, yes = [], []
    x = a
    while x < b:
        xes.append(x)
        yes.append(func(x))
        x += interval
    plt.plot(xes, yes)
    plt.show()
