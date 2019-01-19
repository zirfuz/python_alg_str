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


sum_rec_time = np.squeeze(times('sum_rec.txt'))
sum_loop_time = np.squeeze(times('sum_loop.txt'))

plt.plot(sum_rec_time, linewidth=0.3, color='red')
plt.plot(sum_loop_time, linewidth=0.3, color='blue')

plt.savefig('chart_sum.png', dpi=200)
plt.show()
