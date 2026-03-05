from prng import MiddleSquarePRNG, MiddleProductPRNG, LinearCongruentialPRNG

rnd = MiddleProductPRNG(n_digits=2)
#rnd = LinearCongruentialPRNG()
seed = rnd.get_seed()
print(seed)
print(rnd.get_next())
print(rnd.get_next())
print(rnd.get_next())
print(rnd.get_state())
rnd.set_seed(seed)
print(rnd.get_sequence(10))

print(rnd.get_period())
print(rnd.max_value)
rnd.set_seed(seed)
l = [rnd.random() for _ in range(10)]
print(l)

