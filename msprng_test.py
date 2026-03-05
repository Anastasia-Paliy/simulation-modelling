from prng import MiddleSquarePRNG

rnd = MiddleSquarePRNG(n_digits=6)
print(f'seed = {rnd.get_seed()}')
print(rnd.get_sequence(20))
pre_period, period = rnd.get_period()
print(f'pre_period = {pre_period}, period = {period}')

