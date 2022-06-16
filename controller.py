from pynput import keyboard
import traceback
import sys
import time

def controller(
    model_msg_queue,
    view_msg_queue,
    controller_msg_queue,
    termination_flag,
    ):
    app_visibile = True
    current_level = None
    try:
        model_msg_queue.put(current_level)
        app_visibile, current_level = controller_msg_queue.get()
        view_msg_queue.put(current_level.bg)
        while not view_msg_queue.empty():
            time.sleep(0.01)
        if app_visibile:
            view_msg_queue.put("show")
        else:
            view_msg_queue.put("hide")

    except Exception:
        traceback.print_exc()
        termination_flag.put(True)
        sys.exit()

    key_log = []
    reset_key_log = 0.5
    last_pressed = time.time()

    def on_press(key):
        nonlocal key_log, last_pressed, reset_key_log, current_level, app_visibile
        try:
            current_time = time.time()
            if current_time - last_pressed > reset_key_log:
                key_log = []
            last_pressed = current_time
            key_log = key_log[-5:]
            key_log.append(key)

            for pattern in current_level.patterns:
                if (
                    pattern["key_pattern"] == key_log[-abs(len(pattern["key_pattern"])):] and
                    pattern["when_visible"] == app_visibile
                ):
                    key_log = []
                    model_msg_queue.put(pattern)
                    new_app_visibile, new_current_level = controller_msg_queue.get()
                    if current_level.name != new_current_level.name:
                        view_msg_queue.put(new_current_level.bg)
                    while not view_msg_queue.empty():
                        time.sleep(0.01)
                    if new_app_visibile != app_visibile:
                        if new_app_visibile:
                            view_msg_queue.put("show")
                        else:
                            view_msg_queue.put("hide")
                    current_level = new_current_level
                    app_visibile = new_app_visibile


        except Exception:
            traceback.print_exc()
            termination_flag.put(True)
            sys.exit()


    try:
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
    except Exception:
        traceback.print_exc()
        termination_flag.put(True)
        sys.exit()