from scipy.optimize import minimize_scalar
import numpy as np


def monte_carlo_integral(f, a: int | float, b: int | float, n: int, rng) -> float:
    res = minimize_scalar(lambda x: -abs(f(x)), bounds=(a, b), method='bounded')
    g = -res.fun
    x = np.array([rng.uniform(a, b) for _ in range(n)])
    y = np.array([rng.uniform(0, g) for _ in range(n)])
    f_abs = np.abs(f(x))
    n_in = np.sum(y <= f_abs)
    return (b - a) * g * n_in / n


def head_probability(n: int, rng):
    return np.mean([rng.random() < 0.5 for _ in range(n)])
