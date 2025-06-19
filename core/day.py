import time

from core.config import SECONDS_PER_DAY, START_TIMESTAMP

def current_day():
    with open("meta/day.txt", "r") as day_file:
        day = int(day_file.read())
    return day

def target_day():
    seconds_since_start = time.time() - START_TIMESTAMP
    day = int(seconds_since_start / SECONDS_PER_DAY)
    return day

def advance_day():
    next_day = current_day() + 1
    with open("meta/day.txt", "w") as day_file:
        day_file.write(str(next_day))
