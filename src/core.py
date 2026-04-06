import random
def run():
    print('module: low-latency-logger')
    data = [random.random() for _ in range(10)]
    print('avg:', sum(data)/len(data))
