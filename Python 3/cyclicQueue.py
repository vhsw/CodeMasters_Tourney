# You are working with a machine that resembles a queue. It supports two operations: add an element to the back of the queue and remove an element from the front of the queue. The machine recognizes the following commands:
# 
# "+N" (N ≥ 0) - add N to the back of the queue;
# "-" - remove an element from the front of the queue.
# Given an array of commands, return an array of sums of all elements in the queue after each operation the machine performs.
# 
# It is guaranteed that the second type operation is never applied to an empty queue. Sum of an empty queue is equal to 0.
# It is guaranteed that each command is recognizable by the machine.
# It is also guaranteed that the queue will not have more than 10 elements in it at any moment.


def cyclicQueue(commands):

    maxSize = 10
    queue = [0] * maxSize
    answer = []
    head = 0
    tail = 0
    currentSum = 0

    for i in range(len(commands)):
        if commands[i] == '-':
            currentSum -= queue[head];
            head = (head + 1) % maxSize;

        else:
            value = 0
            for j in range(1, len(commands[i])):
                value = value * 10 + ord(commands[i][j]) - ord('0')
            currentSum += value
            queue[tail] = value
            tail = (tail + 1) % maxSize
        answer.append(currentSum)

    return answer

