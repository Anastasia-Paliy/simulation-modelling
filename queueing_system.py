from prng import LinearCongruentialPRNG
from agents import QueueingSystem, show_hist


n_requests = 10000
rng = LinearCongruentialPRNG()
system = QueueingSystem(source_distr=rng.triangle,
                        source_params=(2, 8, 15),
                        service_distr=rng.triangle,
                        service_params=(3, 7, 10))
for i in range(n_requests):
    system.request_processing()

system.print_statistics()
show_hist([request.time_in_queue for request in system.requests])
show_hist([request.time_in_service for request in system.requests])
