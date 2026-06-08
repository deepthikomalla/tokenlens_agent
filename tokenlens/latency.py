# tokenlens/latency.py

import time

class LatencyTracker:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        return round(time.time() - self.start_time, 3)
    