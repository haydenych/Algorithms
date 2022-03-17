from enum import Enum


class Direction(Enum):
    LEFT = 1
    RIGHT = 2


# User input
queue = [55, 58, 39, 18, 90, 150, 38, 184]
start_pos = 100
min_cylinder = 0
max_cylinder = 499
direction = Direction.RIGHT


def min_if_exists(q, criteria):
    try:
        return min(x for x in q if x < criteria)
    except ValueError:
        return None


def max_if_exists(q, criteria):
    try:
        return max(x for x in q if x > criteria)
    except ValueError:
        return None


def FCFS(queue, start_pos):
    q = list(queue)
    curr = start_pos
    seq = [curr]
    total_movement = 0
    num_req = len(q)

    for i in range(num_req):
        total_movement += abs(curr - q[0])
        curr = q[0]
        q.pop(0)
        seq.append(curr)

    print("FCFS: ", seq)
    print("FCFS Total Scan Distance: ", total_movement, "\n")


def SSTF(queue, start_pos):
    q = list(queue)
    curr = start_pos
    seq = [curr]
    total_movement = 0
    num_req = len(q)

    for _ in range(num_req):
        dist = [abs(curr - num) for num in q]
        total_movement += abs(curr - q[dist.index(min(dist))])
        curr = q[dist.index(min(dist))]
        q.remove(curr)
        seq.append(curr)

    print("SSTF: ", seq)
    print("SSTF Total Scan Distance: ", total_movement, "\n")


def SCAN(queue, start_pos, min_cylinder, max_cylinder, direction):
    q = list(queue)
    q.append(start_pos)
    q.sort()
    seq = []
    total_movement = 0

    if direction == Direction.LEFT:
        seq += q[q.index(start_pos)::-1] + q[q.index(start_pos) + 1:]

        if seq[0] < seq[len(seq) - 1]:
            total_movement = seq[0] - min_cylinder + seq[len(seq) - 1] - min_cylinder
        else:
            total_movement = seq[0] - seq[len(seq) - 1]
    elif direction == Direction.RIGHT:
        q.reverse()
        seq += q[q.index(start_pos)::-1] + q[q.index(start_pos) + 1:]

        if seq[0] > seq[len(seq) - 1]:
            total_movement = max_cylinder - seq[0] + max_cylinder - seq[len(seq) - 1]
        else:
            total_movement = seq[len(seq) - 1] - seq[0]

    print("SCAN: ", seq)
    print("SCAN Total Scan Distance: ", total_movement, "\n")


def C_SCAN(queue, start_pos, min_cylinder, max_cylinder, direction):
    q = list(queue)
    q.append(start_pos)
    q.sort()
    seq = []

    if direction == Direction.LEFT:
        q.reverse()
        seq += q[q.index(start_pos)::] + q[:q.index(start_pos):]
    elif direction == Direction.RIGHT:
        seq += q[q.index(start_pos)::] + q[:q.index(start_pos):]

    if seq != sorted(seq) and seq != sorted(seq, reverse=True):
        total_movement = (max_cylinder - min_cylinder) * 2 - abs(seq[0] - seq[len(seq) - 1])
    else:
        total_movement = abs(seq[len(seq) - 1] - seq[0])

    print("C_SCAN: ", seq)
    print("C_SCAN Total Scan Distance: ", total_movement, "\n")


def LOOK(queue, start_pos, direction):
    q = list(queue)
    q.append(start_pos)
    q.sort()
    seq = []
    total_movement = 0

    if direction == Direction.LEFT:
        seq += q[q.index(start_pos)::-1] + q[q.index(start_pos) + 1:]

        if seq[0] < seq[len(seq) - 1]:
            total_movement = start_pos - min(q) + max(q) - min(q)
        else:
            total_movement = seq[0] - seq[len(seq) - 1]
            
    elif direction == Direction.RIGHT:
        q.reverse()
        seq += q[q.index(start_pos)::-1] + q[q.index(start_pos) + 1:]

        if seq[0] > seq[len(seq) - 1]:
            total_movement = max(q) - start_pos + max(q) - min(q)
            print(total_movement)
        else:
            total_movement = seq[len(seq) - 1] - seq[0]
            print(total_movement)

    print("LOOK: ", seq)
    print("LOOK Total Scan Distance: ", total_movement, "\n")


def C_LOOK(queue, start_pos, direction):
    q = list(queue)
    q.append(start_pos)
    q.sort()
    seq = []

    if direction == Direction.LEFT:
        q.reverse()
        seq += q[q.index(start_pos)::] + q[:q.index(start_pos):]

    elif direction == Direction.RIGHT:
        seq += q[q.index(start_pos)::] + q[:q.index(start_pos):]

    if seq != sorted(seq) and seq != sorted(seq, reverse=True):
        total_movement = (max(q) - min(q)) * 2 - abs(seq[0] - seq[len(seq) - 1])
    else:
        total_movement = abs(seq[len(seq) - 1] - seq[0])

    print("C_LOOK: ", seq)
    print("C_LOOK Total Scan Distance: ", total_movement, "\n")


FCFS(queue, start_pos)
SSTF(queue, start_pos)
SCAN(queue, start_pos, min_cylinder, max_cylinder, direction)
C_SCAN(queue, start_pos, min_cylinder, max_cylinder, direction)
LOOK(queue, start_pos, direction)
C_LOOK(queue, start_pos, direction)
