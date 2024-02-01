import threading
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


def process_t():
    has_task = 0
    curTask = None
    while True:
        if has_task==0:
            # pick a task
            # allocate resources
            #check ready and waiting
            has_task = 1
        curTask.remaining_time -= 1
        if curTask.remaining_time == 0:
            has_task = 0
            #lock
            terminated.append(curTask)
            #unlock
            #free resources
        #wait for an event
        
        


each_resources = input()
resources[0] = int(each_resources[0])
resources[1] = int(each_resources[2])
resources[2] = int(each_resources[4])
num_of_tasks = int(input())
for i in range(num_of_tasks):
    task = input()# for t in tasks:
#     print(t.name, t.type, t.duration)
# print(resources)
    tasks.append(Task(task[:2], task[3], int(task[5])))
    ready.append(tasks[-1])

p1 = threading.Thread(target=process_t, args=())
p2 = threading.Thread(target=process_t, args=())
p3 = threading.Thread(target=process_t, args=())
p4 = threading.Thread(target=process_t, args=())

#print_thread = 

while len(terminated) != num_of_tasks:
    #wait for threads and print
    #next loop


# check prints
# for t in tasks:
#     print(t.name, t.type, t.duration)
# print(resources)
