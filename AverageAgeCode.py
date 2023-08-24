import time
import random

def process_queue(queue):
    total_gen_time = 0
    num_packets = len(queue)
    original_queue = queue.copy()

    while queue:
        min_gen_time = min(queue)
        print(f"Sending packet with generation time: {min_gen_time} seconds")

        randomServerTime=random.uniform(0.01,0.1)
        total_gen_time += min_gen_time +randomServerTime  # Add 1 second for time spent in server
        queue.remove(min_gen_time)
        for i in range(len(queue)):
            queue[i] += randomServerTime # Increment remaining generation times by 1

    avg_gen_time = total_gen_time / num_packets
    return avg_gen_time, original_queue

# Example usage:
queue = [1.5778513367832585, 2.7869338215303605, 1.6510538030583066, 2.7645782396705685, 1.9588457377377502, 0.4198956156759691, 0.08627844121178424, 0.9466891885964638, 3.24252187714067, 0.041372557251223276, 1.5052226973059182, 0.6051814967929559]




avg_gen_time, original_queue = process_queue(queue)
print(f"Original queue of generation times: {original_queue}")
print(f"Average age: {avg_gen_time} seconds")
