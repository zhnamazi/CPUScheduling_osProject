
from threading import Event
import threading


# event = Event()
# event.clear()
# are_wait = [[False], [False]]

# def thread_func(number, is_wait):
#     while True:
#         print(number)
#         is_wait[0] = True
#         event.wait()
#         event.clear()
#         is_wait[0] = False

# print("t = ", x)
# t1 = threading.Thread(target=thread_func, args=(1, are_wait[0]))
# t2 = threading.Thread(target=thread_func, args=(2, are_wait[1]))

# x = 0
# t1.start()
# t2.start()
# while x < 5:
#     event.set()
#     while are_wait[0] == [False] or are_wait[1] == [False]:
#         pass
#     print("t = ", x)
#     x += 1
    

# t1.join()
# t2.join()

print("s")