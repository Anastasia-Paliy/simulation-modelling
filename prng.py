from time import time
from math import sqrt, log, sin, cos, pi


class PseudoRandomNumberGenerator:
    def __init__(self):
        self._seed = None
        self._state = None

    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state

    def get_seed(self):
        return self._seed

    def set_seed(self, seed):
        self._seed = seed
        self._reset()

    def _reset(self):
        raise NotImplementedError

    def get_next(self):
        """
        Updates current state of generator and returns the new one
        :return: current state of generator
        """
        raise NotImplementedError

    def get_sequence(self, length: int):
        return [self.get_next() for _ in range(length)]

    def get_period(self, max_attempts=10**6):
        saved_state = self.get_state()
        self._reset()
        pre_period = 0
        found = False
        current_state = self.get_state()
        seen = {current_state}
        for _ in range(max_attempts):
            pre_period += 1
            self.get_next()
            current_state = self.get_state()
            if current_state in seen:
                found = True
                break
            seen.add(current_state)

        if found:
            period = 1
            start_state = current_state
            self.get_next()
            while self.get_state() != start_state:
                self.get_next()
                period += 1
            pre_period -= period
        else:
            pre_period = None
            period = None
        self.set_state(saved_state)
        return pre_period, period

    # def print_period
    def max_value(self):
        # max_value + 1
        raise NotImplementedError

    def random(self):
        """
        Returns pseudorandom number in [0, 1)
        :return:
        """
        return self.get_next() / self.max_value

    def uniform(self, a: int | float, b: int | float) -> float:
        """
        Returns pseudorandom number in [a, b)
        :param a: left endpoint
        :param b: right endpoint
        :return:
        """
        return a + (b - a) * self.random()

    def triangle(self, a, c, b):
        a, c, b = sorted((a, c, b))
        alpha = self.random()
        alpha_crit = (c - a) / (b - a)
        if alpha < alpha_crit:
            x = a + sqrt(alpha * (b - a) * (c - a))
        else:
            x = b - sqrt((1 - alpha) * (b - a) * (b - c))
        return x

    def exponential(self, lmbda):
        alpha = self.random()
        x = -log(1 - alpha) / lmbda
        return x

    def normal(self, mu=0, sigma=1, n=12, method='Box-Muller'):
        if method == 'CLT':
            z = sqrt(12 / n) * (sum(self.random() for _ in range(n)) - (n / 2))
        elif method == 'Box-Muller':
            r, phi = self.random(), self.random()
            z = cos(2 * pi * phi) * sqrt(-2 * log(r))
            # z = sin(2 * pi * phi) * sqrt(-2 * log(r))
        else:
            raise ValueError("method options are 'CLT' and 'Box-Muller'")
        x = mu + sigma * z
        return x


class MiddleSquarePRNG(PseudoRandomNumberGenerator):
    def __init__(self, n_digits: int):
        super().__init__()
        if n_digits % 2 != 0:
            raise Exception("Number of digits must be even")
        self.digits = n_digits
        self.set_seed(int(time() * 10**6) % (10**self.digits))

    def _reset(self):
        self._state = self._seed

    def get_next(self):
        p = 10 ** (self.digits // 2)
        self._state = (self._state * self._state // p) % (p * p)
        return self._state

    @property
    def max_value(self):
        return 10 ** self.digits


class MiddleProductPRNG(PseudoRandomNumberGenerator):
    def __init__(self, n_digits: int):
        super().__init__()
        if n_digits % 2 != 0:
            raise Exception("Number of digits must be even")
        self.digits = n_digits
        self.set_seed(int(time() * 10**6) % (10**self.digits))

    def set_seed(self, seed):
        if isinstance(seed, tuple):
            self._seed = seed
        else:
            # if seed: int|float
            p = 10 ** (self.digits // 2)
            self._seed = (seed, (seed * seed // p) % (p * p))
        self._reset()

    def _reset(self):
        self._state = self._seed

    def get_next(self):
        p = 10 ** (self.digits // 2)
        prev = self._state[0]
        current = self._state[1]
        self._state = current, (prev * current // p) % (p * p)
        return self._state[1]

    @property
    def max_value(self):
        return 10 ** self.digits


class LinearCongruentialPRNG(PseudoRandomNumberGenerator):
    def __init__(self, k=106, b=1283, m=6075):
        super().__init__()
        self.k = k
        self.b = b
        self.m = m
        self.set_seed(int(time() * 10**6) % self.m)

    def _reset(self):
        self._state = self._seed

    def get_next(self):
        self._state = (self.k * self._state + self.b) % self.m
        return self._state

    @property
    def max_value(self):
        return self.m
