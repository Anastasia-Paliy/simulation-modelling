from prng import LinearCongruentialPRNG
import matplotlib.pyplot as plt


class Request:
    def __init__(self, arrival_time: int | float):
        self.arrival_time = arrival_time
        self.time_in_queue = None
        self.time_in_service = None


class QueueingSystem:
    def __init__(self,
                 source_distr=LinearCongruentialPRNG().triangle,
                 source_params=(2, 8, 15),
                 service_distr=LinearCongruentialPRNG().triangle,
                 service_params=(3, 7, 10)
                 ):
        self.source_distr = source_distr
        self.service_distr = service_distr
        self.source_params = source_params
        self.service_params = service_params

        self.requests = []
        self.prev_arrival = 0
        self.prev_departure = 0
        self.queue_length = 0

        # statistics
        self.n_arrived = 0
        self.n_served = 0
        self.time = 0
        self.max_queue_length = 0
        self.total_waiting = 0
        self.total_service = 0
        self.total_in_system = 0
        self.total_idle = 0

    def request_processing(self):
        source_interval = self.source_distr(*self.source_params)
        request = Request(self.prev_arrival + source_interval)
        self.prev_arrival += source_interval
        self.n_arrived += 1

        waiting_interval = max(request.arrival_time, self.prev_departure) - request.arrival_time
        request.time_in_queue = waiting_interval
        self.total_waiting += waiting_interval
        self.total_idle += max(0, request.arrival_time - self.prev_departure)

        delay_interval = self.service_distr(*self.service_params)
        request.time_in_service = delay_interval
        self.total_service += delay_interval
        self.total_in_system += waiting_interval + delay_interval
        self.n_served += 1
        self.prev_departure = request.arrival_time + request.time_in_queue + request.time_in_service
        self.time = self.prev_departure
        self.requests.append(request)

    def print_statistics(self):
        print(f'Время: {self.time}')
        print(f'Количество поступивших заявок: {self.n_arrived}')
        print(f'Количество обслуженных заявок: {self.n_served}')
        print(f'Среднее время ожидания в очереди: {self.total_waiting / self.n_served}')
        print(f'Среднее время обслуживания: {self.total_service / self.n_served}')
        print(f'Среднее время в системе: {self.total_in_system / self.n_served}')
        print(f'Пропускная способность: {self.n_served / self.time}')
        print(f'Общее время простоя: {self.total_idle}')
        print(f'Коэффициент простоя: {self.total_idle / self.time}')


def show_hist(data, n_bins=20):
    plt.hist(data, bins=n_bins, density=True, color='lightblue', edgecolor='black')
    plt.title('Гистограмма относительных частот')
    plt.xlabel('Значения')
    plt.ylabel('Относительная частота')
    plt.show()
