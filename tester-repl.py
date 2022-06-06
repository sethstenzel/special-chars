from view import view as view
from queue import Queue
from threading import Thread

msg_queue = Queue(1)
termination_flag = Queue(1)

v = Thread(name = "view", target = view, args =(msg_queue, termination_flag, ))
v.start()
try:
    while True:
        if not termination_flag.empty():
            print("Termination flag set, exiting...")
            break        
        mq = input("mq: ")
        if mq != "":
            msg_queue.put(mq)
        tf = input("tf: ")

        if tf != "" and int(tf) == 1:
            termination_flag.put(True)
except:
    termination_flag.put(True)

