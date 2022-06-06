from queue import Queue
from threading import Thread

from model import model as model
from view import view as view
from controller import controller as controller


def main(model, view, controller):
    threads = []
    model_msg_queue = Queue(1)
    view_msg_queue = Queue(1)
    controller_msg_queue = Queue(1)
    termination_flag = Queue(1)

    m = Thread(name = "model", target = model, args =(
        model_msg_queue,
        controller_msg_queue,
        termination_flag, 
        ))
    threads.append(m)

    v = Thread(name = "view", target = view, args =(
        view_msg_queue,
        termination_flag, 
        ))
    threads.append(v)

    c = Thread(name = "controller", target = controller, args =(
        model_msg_queue,
        view_msg_queue,
        controller_msg_queue,
        termination_flag, 
        ))
    threads.append(c)

    # Start all threads
    for thread in threads:
        thread.start()

if __name__ == '__main__':
    main(model, view, controller)