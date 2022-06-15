from queue import Queue
from threading import Thread
import traceback
from model import model as model
from view import view as view
from controller import controller as controller
import time
import sys


def main(model, view, controller):
    try:
        threads = []
        model_msg_queue = Queue(1)
        view_msg_queue = Queue(1)
        controller_msg_queue = Queue(1)
        termination_flag = Queue(1)
        has_focus = Queue(1)

        m = Thread(name = "model", target = model, args =(
            model_msg_queue,
            controller_msg_queue,
            termination_flag,
            has_focus, 
            ))
        threads.append(m)

        v = Thread(name = "view", target = view, args =(
            view_msg_queue,
            termination_flag,
            has_focus, 
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
    except Exception:
        traceback.print_exc()
        termination_flag.put(True)
        time.sleep(1)
        sys.exit()

if __name__ == '__main__':
    main(model, view, controller)