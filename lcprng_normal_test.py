from prng import LinearCongruentialPRNG
import matplotlib.pyplot as plt
from scipy.stats import kstest, norm
from numpy import mean, var

rnd = LinearCongruentialPRNG()
print(f'seed = {rnd.get_seed()}')
mu, sigma = 0, 1
sequence = [rnd.normal(mu, sigma, method='Box-Muller') for _ in range(100)]
print(sequence[:5])
pre_period, period = rnd.get_period()
print(f'pre_period = {pre_period}, period = {period}')
print(f'Mean: {mean(sequence)}')
print(f'Variance: {var(sequence)}')

print(f"Критерий Колмогорова-Смирнова (pvalue > 0.05): "
      f"{kstest(sequence, norm(loc=mu, scale=sigma).cdf).pvalue > 0.05}")
plt.hist(sequence, bins=15, density=True, color='lightblue', edgecolor='black')
plt.title('Гистограмма относительных частот')
plt.xlabel('Значения')
plt.ylabel('Относительная частота')
plt.show()

