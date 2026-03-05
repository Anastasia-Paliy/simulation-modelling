from prng import LinearCongruentialPRNG
import matplotlib.pyplot as plt
from scipy.stats import kstest, uniform
from numpy import mean, var

rnd = LinearCongruentialPRNG()
print(f'seed = {rnd.get_seed()}')
a, b = 5, 10
# sequence = rnd.get_sequence(20)
# sequence = [rnd.random() for _ in range(25)]
sequence = [rnd.uniform(a, b) for _ in range(100)]

print(sequence[:5])
pre_period, period = rnd.get_period()
print(f'pre_period = {pre_period}, period = {period}')
print(f'Mean: {mean(sequence)}')
print(f'Variance: {var(sequence)}')
print(f"Критерий Колмогорова-Смирнова (pvalue > 0.05): "
      f"{kstest(sequence, uniform(loc=a, scale=b-a).cdf).pvalue > 0.05}")
plt.hist(sequence, bins=20, range=(a, b), density=True, color='lightblue', edgecolor='black')
plt.title('Гистограмма относительных частот')
plt.xlabel('Значения')
plt.ylabel('Относительная частота')
plt.show()

