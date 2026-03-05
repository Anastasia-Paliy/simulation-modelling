from prng import LinearCongruentialPRNG
import matplotlib.pyplot as plt
from scipy.stats import kstest, triang
from numpy import mean, var

rnd = LinearCongruentialPRNG()
print(f'seed = {rnd.get_seed()}')
a, c, b = 5, 10, 20
sequence = [rnd.triangle(a, c, b) for _ in range(100)]

print(sequence[:5])
pre_period, period = rnd.get_period()
print(f'pre_period = {pre_period}, period = {period}')
print(f'Mean: {mean(sequence)}')
print(f'Variance: {var(sequence)}')
print(f"Критерий Колмогорова-Смирнова (pvalue > 0.05): "
      f"{kstest(sequence, triang(c=(c-a)/(b-a), loc=a, scale=b-a).cdf).pvalue > 0.05}")
plt.hist(sequence, bins=20, range=(a, b), density=True, color='lightblue', edgecolor='black')
plt.title('Гистограмма относительных частот')
plt.xlabel('Значения')
plt.ylabel('Относительная частота')
plt.show()

