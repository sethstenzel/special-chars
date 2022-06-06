from model import model as model
from view import view as view
from controller import controller as controller
from queue import Queue
from threading import Thread

model_msg_queue = Queue(1)
view_msg_queue = Queue(1)
controller_msg_queue = Queue(1)
termination_flag = Queue(1)

threads = []
m = Thread(name = "view", target = model, args =(model_msg_queue, controller_msg_queue, termination_flag, ))
threads.append(m)

# v = Thread(name = "view", target = view, args =(view_msg_queue, termination_flag, ))
# threads.append(v)

# c = Thread(name = "view", target = view, args =(model_msg_queue, view_msg_queue,controller_msg_queue, termination_flag, ))
# threads.append(c)

# Start all threads
for thread in threads:
    thread.start()

try:
    while True:
        if not termination_flag.empty():
            print("Termination flag set, exiting...")
            break        
        mq = input("mq: ")
        if mq != "":
            view_msg_queue.put(mq)
        tf = input("tf: ")

        if tf != "" and int(tf) == 1:
            termination_flag.put(True)
except:
    termination_flag.put(True)

