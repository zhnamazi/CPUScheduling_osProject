import threading
from heapq import *


resources = [0, 0, 0]
status = [None, None, None, None]
tasks = []
ready= []
waiting = []
terminated = []
endUnit = [False,False,False,False]
mutex = threading.Lock()
endEvent = threading.Event()
printEvent = threading.Event()
time = 1


class Task:
    def __init__(self, name, task_type, duration):
        self.name = name
        self.type = task_type
        self.duration = duration
        self.state = "ready" 
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


def update_queue():
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


def process_t(task_number, pause):
    curTask = None
    curR = None
    while True:
        # pause[0] = True
        endEvent.wait()
        # pause[0] = False
        mutex.acquire()
        # pick a task
        if not ready:
            continue
        curTask = ready.pop()
        curTask.state = "running"
        # allocate resources
        curR = get_resources(curTask)
        resources[curR[0]] -= 1
        resources[curR[1]] -= 1
        #check ready and waiting
        update_queue()
        mutex.release()
        curTask.remaining_time -= 1
        status[task_number] = curTask
        mutex.acquire()
        resources[curR[0]] += 1
        resources[curR[1]] += 1
        if curTask.remaining_time == 0:
            terminated.append(curTask)
            curTask.state = "terminated"
        else:
            ready.append(curTask)
            curTask.state = "ready"
        update_queue()
        mutex.release()
        endEvent.clear()


def print_t():
    while True:
        printEvent.wait()
        printEvent.clear()
        if time ==1:
            print("----- RR -----")
        print("Time: ", time)
        for i in range(4):
            s = status[i]
            task = "Idle"
            if s != None:
                task = s.name
            print("Core: ", i+1, "Task: ", task)


each_resources = input()
resources[0] = int(each_resources[0])
resources[1] = int(each_resources[2])
resources[2] = int(each_resources[4])
num_of_tasks = int(input())
for i in range(num_of_tasks):
    task = input()
    tasks.append(Task(task[:2], task[3], int(task[5])))
    ready.append(tasks[-1])

p1 = threading.Thread(target=process_t, args=(0, endUnit[0]))
p2 = threading.Thread(target=process_t, args=(1, endUnit[1]))
p3 = threading.Thread(target=process_t, args=(2, endUnit[2]))
p4 = threading.Thread(target=process_t, args=(3, endUnit[3]))
print_thread = threading.Thread(target=print_t, args=())

p1.start()
p2.start()
p3.start()
p4.start()
print_thread.start()

while len(terminated) < num_of_tasks:
    endEvent.set()
    while not all(e[0] == True for e in endUnit):
        pass
    printEvent.set()
    time +=1


p1.join()
p2.join()
p3.join()
p4.join()
print_thread.join()

# check prints
# for t in tasks:
#     print(t.name, t.type, t.duration)
# print(resources)
