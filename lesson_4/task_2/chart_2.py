import matplotlib
import matplotlib.pyplot as plt
import numpy as np

font = {'weight': 'normal', 'size': 7}
matplotlib.rc('font', **font)


def times(file):
    file = open(file)
    times_str = file.read().split('\n')
    times_str.remove('')
    try:
        ret = [float(str) for str in times_str][1:]
    except:
        return []
    return ret


not_sieve_time = np.squeeze(times('not_sieve.txt'))
sieve_time = np.squeeze(times('sieve.txt'))
sieve_prepare_time = np.squeeze(times('sieve_prepare.txt'))

plt.plot(not_sieve_time, linewidth=0.3, color='red')
plt.plot(sieve_time, linewidth=0.3, color='blue')
plt.plot(sieve_prepare_time, linewidth=0.7, color='green', )

plt.savefig('primes.png', dpi=200)
plt.show()
