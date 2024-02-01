import threading
from heapq import *
import queue

resources = [0, 0, 0]
mutex = threading.Lock()
status = [None, None, None, None]
tasks = []
ready= []
waiting = []
terminated = []


class Task:
    def __init__(self, name, task_type, duration):
        self.name = name
        self.type = task_type
        self.duration = duration
        self.state = "ready"  # Initial state is 'ready'
        self.remaining_time = duration


def get_resources(task :Task):
    match task.type:
        case 'x':
            return (0,1)
        case 'y':
            return (1,2)
        case 'z':
            return (0,2)
        

def get_priority(task :Task):
    match task.type:
        case 'x':
            return 3
        case 'y':
            return 2
        case 'z':
            return 1


def update_queue(): # update state
    for t in ready:
        r = get_resources(t)
        p = get_priority(t)
        if resources[r[0]] == 0 and resources[r[1]] == 0:
            ready.remove(t)
            heappush(waiting, (p, t))
            t.state = "waiting"
    for t in waiting:
        r = get_resources(t)
        if resources[r[0]] > 0 and resources[r[1]] > 0:
            waiting.remove(t)
            ready.append(t)
            t.state = "ready"



def process_t():
    has_task = 0
    curTask = None
    curR = None
    while True:
        if has_task==0:
            mutex.acquire()
            # pick a task
            curTask = ready.pop()
            curTask.state = "running"
            # allocate resources
            curR = get_resources(curTask)
            resources[curR[0]] -= 1
            resources[curR[1]] -= 1
            #check ready and waiting
            update_queue()
            has_task = 1
            mutex.release()
        curTask.remaining_time -= 1
        if curTask.remaining_time == 0:
            mutex.acquire()
            terminated.append(curTask)
            curTask.state = "terminated"
            resources[curR[0]] += 1
            resources[curR[1]] += 1
            has_task = 0
            mutex.release()
        #wait for an event
        
        


each_resources = input()
resources[0] = int(each_resources[0])
resources[1] = int(each_resources[2])
resources[2] = int(each_resources[4])
num_of_tasks = int(input())
for i in range(num_of_tasks):
    task = input()
    tasks.append(Task(task[:2], task[3], int(task[5])))
    ready.append(tasks[-1])

p1 = threading.Thread(target=process_t, args=())
p2 = threading.Thread(target=process_t, args=())
p3 = threading.Thread(target=process_t, args=())
p4 = threading.Thread(target=process_t, args=())

#print_thread = 

while len(terminated) < num_of_tasks:
    #wait for threads and print
    #next loop


# check prints
# for t in tasks:
#     print(t.name, t.type, t.duration)
# print(resources)
