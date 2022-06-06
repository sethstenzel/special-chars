from queue import Queue
from threading import Thread

from model import model as model
from view import view as view
from controller import controller as controller


def main(model, view, controller):
    threads = []
    msg_queue = Queue(1)
    termination_flag = Queue(1)

    m = Thread(name = "model", target = model, args =(msg_queue, termination_flag, ))
    threads.append(m)

    v = Thread(name = "view", target = view, args =(msg_queue, termination_flag, ))
    threads.append(v)

    c = Thread(name = "controller", target = controller, args =(msg_queue, termination_flag, ))
    threads.append(c)

    # Start all threads
    for thread in threads:
        thread.start()

if __name__ == '__main__':
    main(model, view, controller)