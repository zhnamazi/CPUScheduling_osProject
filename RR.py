import threading
from heapq import *


resources = [0, 0, 0]
status = [None, None, None, None]
tasks = []
ready = []
waiting = []
terminated = []
endUnit = [False, False, False, False]
mutex = threading.Lock()
endEvent = threading.Event()
printEvent = threading.Event()
tempList = []
quantum = 3
time = 1


class Task:
    def __init__(self, name, task_type, duration):
        self.name = name
        self.type = task_type
        self.duration = duration
        self.state = "ready"
        self.remaining_time = duration
        self.last_usage = 0


def get_resources(task: Task):
    match task.type:
        case 'x':
            return (0, 1)
        case 'y':
            return (1, 2)
        case 'z':
            return (0, 2)


def get_priority(task: Task):
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
    for t in waiting:
        if (time - t.last_usage) > 3/2 * t.remaining_time:
            waiting.remove(t)
            waiting.insert(0, t)
       

def process_t(proc_number):
    global time
    has_task = 0
    curTask = None
    curR = None
    while True:
        endEvent.wait()
        endUnit[proc_number] = False
        if  has_task == 0:
            mutex.acquire()
            if (not ready):
                status[proc_number] = None
                endUnit[proc_number] = True
                if all(e for e in endUnit):
                    for i in range(len(endUnit)):
                        endUnit[i] = False
                    for i in range(len(tempList)):
                        ts = tempList.pop()
                        ready.append(ts)
                    printEvent.set()
                mutex.release()
                endEvent.clear()
                continue
            curTask = ready.pop()
            curTask.state = "running"
            # allocate resources
            curR = get_resources(curTask)
            resources[curR[0]] -= 1
            resources[curR[1]] -= 1
            # check ready and waiting
            update_queue()
            has_task = 1
            mutex.release()

        curTask.remaining_time -= 1
        status[proc_number] = curTask

        mutex.acquire()
        if curTask.remaining_time == 0:
            resources[curR[0]] += 1
            resources[curR[1]] += 1
            terminated.append(curTask)
            curTask.state = "terminated"
            has_task = 0
        elif time%quantum == 0:
            resources[curR[0]] += 1
            resources[curR[1]] += 1
            curTask.state = "ready"
            tempList.append(curTask)
            has_task = 0

        update_queue()
        mutex.release()
        endUnit[proc_number] = True
        #print(curTask.name, endUnit)
        if all(e for e in endUnit):
            for i in range(len(endUnit)):
                endUnit[i] = False
            for i in range(len(tempList)):
                ts = tempList.pop()
                ready.append(ts)
            # print("tempList:")
            # for ts in tempList:
            #     print(ts.name)
            printEvent.set()
        endEvent.clear()


def print_t():
    global time
    while True:
        printEvent.wait()
        if time == 1:
            print("----- RR -----")
        # for t in ready:
        #     print(t.name)
        print("Time: ", time)
        for i in range(4):
            s = status[i]
            task = "Idle"
            if s is not None:
                task = s.name
            print("Core: ", i+1, "Task: ", task)
        if len(terminated) < len(tasks) and time < 9:
            time += 1
            tempList.clear()
            endEvent.set()
        printEvent.clear()


each_resources = input()
resources[0] = int(each_resources[0])
resources[1] = int(each_resources[2])
resources[2] = int(each_resources[4])
num_of_tasks = int(input())
for i in range(num_of_tasks):
    task = input()
    tasks.append(Task(task[:2], task[3], int(task[5])))
    ready.append(tasks[-1])

p1 = threading.Thread(target=process_t, args=[0])
p2 = threading.Thread(target=process_t, args=[1])
p3 = threading.Thread(target=process_t, args=[2])
p4 = threading.Thread(target=process_t, args=[3])
print_thread = threading.Thread(target=print_t, args=())

p1.start()
p2.start()
p3.start()
p4.start()
print_thread.start()

endEvent.set()

# p1.join()
# p2.join()
# p3.join()
# p4.join()
# print_thread.join()import threading
from heapq import *


resources = [0, 0, 0]
status = [None, None, None, None]
tasks = []
ready = []
waiting = []
terminated = []
endUnit = [False, False, False, False]
mutex = threading.Lock()
endEvent = threading.Event()
printEvent = threading.Event()
tempList = []


class Task:
    def __init__(self, name, task_type, duration):
        self.name = name
        self.type = task_type
        self.duration = duration
        self.state = "ready"
        self.remaining_time = duration


def get_resources(task: Task):
    match task.type:
        case 'x':
            return (0, 1)
        case 'y':
            return (1, 2)
        case 'z':
            return (0, 2)


def get_priority(task: Task):
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
       

def process_t(proc_number):
    curTask = None
    curR = None
    while True:
        endEvent.wait()
        endUnit[proc_number] = False
        # pick a task
        mutex.acquire()
        if (not ready): #here  and (not tempList)
            status[proc_number] = None
            endUnit[proc_number] = True
            if all(e for e in endUnit):
                for i in range(len(endUnit)):
                    endUnit[i] = False
                for i in range(len(tempList)):
                    ts = tempList.pop()
                    ready.append(ts)
                printEvent.set()
            mutex.release()
            endEvent.clear()
            continue
        curTask = ready.pop()
        curTask.state = "running"
        # allocate resources
        curR = get_resources(curTask)
        resources[curR[0]] -= 1
        resources[curR[1]] -= 1
        # check ready and waiting
        update_queue()
        mutex.release()

        curTask.remaining_time -= 1
        status[proc_number] = curTask

        mutex.acquire()
        resources[curR[0]] += 1
        resources[curR[1]] += 1
        if curTask.remaining_time == 0:
            terminated.append(curTask)
            curTask.state = "terminated"
        else:
            curTask.state = "ready"
            tempList.append(curTask)

        update_queue()
        mutex.release()
        endUnit[proc_number] = True
        #print(curTask.name, endUnit)
        if all(e for e in endUnit):
            for i in range(len(endUnit)):
                endUnit[i] = False
            for i in range(len(tempList)):
                ts = tempList.pop()
                ready.append(ts)
            # print("tempList:")
            # for ts in tempList:
            #     print(ts.name)
            printEvent.set()
        endEvent.clear()


def print_t():
    time = 1
    while True:
        printEvent.wait()
        if time == 1:
            print("----- RR -----")
        # for t in ready:
        #     print(t.name)
        print("Time: ", time)
        for i in range(4):
            s = status[i]
            task = "Idle"
            if s is not None:
                task = s.name
            print("Core: ", i+1, "Task: ", task)
        if len(terminated) < len(tasks) and time < 9:
            time += 1
            tempList.clear()
            endEvent.set()
        printEvent.clear()


each_resources = input()
resources[0] = int(each_resources[0])
resources[1] = int(each_resources[2])
resources[2] = int(each_resources[4])
num_of_tasks = int(input())
for i in range(num_of_tasks):
    task = input()
    tasks.append(Task(task[:2], task[3], int(task[5])))
    ready.append(tasks[-1])

p1 = threading.Thread(target=process_t, args=[0])
p2 = threading.Thread(target=process_t, args=[1])
p3 = threading.Thread(target=process_t, args=[2])
p4 = threading.Thread(target=process_t, args=[3])
print_thread = threading.Thread(target=print_t, args=())

p1.start()
p2.start()
p3.start()
p4.start()
print_thread.start()

endEvent.set()

# p1.join()
# p2.join()
# p3.join()
# p4.join()
# print_thread.join()