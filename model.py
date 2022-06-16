from dataclasses import dataclass
import time
import sys
import traceback
import pyperclip
from pynput.keyboard import Key, Controller
from special_chars import special_character_mappings
from level_data import level_data

@dataclass
class Level:
        level_id: int
        name: str
        bg: str
        patterns: list


def get_levels():
    levels = []
    
    for level in level_data:
        levels.append(
            Level(
                level["level_id"],
                level["name"],
                level["bg"],
                level["patterns"],
            )
        )
    return levels

def get_level(levels, level_name=None, level_id=None):
    for level in levels:
        if level_id and level.level_id == level_id:
            return level
        if level_name and level.name == level_name:
            return level

def get_character(current_level, pattern):
    special_character = special_character_mappings[current_level.name][pattern["action_data"]]
    pyperclip.copy(special_character)


def paste():
    time.sleep(0.1)
    keyboard = Controller()
    keyboard.press(Key.ctrl.value)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.ctrl.value)

def model(model_msg_queue, controller_msg_queue, termination_flag, has_focus):
    try:
        app_visible = True
        levels = get_levels()
        current_level = model_msg_queue.get()
        if current_level is None:
            current_level = get_level(levels, level_name = "initial")
            controller_msg_queue.put((app_visible, current_level))
            while not model_msg_queue.empty():
                time.sleep(0.01)

        while True:
            time.sleep(0.01)
            if not termination_flag.empty():
                break

            if not model_msg_queue.empty():
                pattern = model_msg_queue.get()
                if type(pattern) == Level:
                    controller_msg_queue.put((app_visible, current_level))
                    time.sleep(0.025)

                if (
                    pattern["action"] == "change_level" and
                    app_visible == True and
                    not has_focus.empty()
                ):            
                    current_level = get_level(levels, level_id = pattern["action_data"])
                    controller_msg_queue.put((app_visible, current_level))
                
                elif pattern["action"] == "hide" and app_visible == True and not has_focus.empty():
                    app_visible = False
                    current_level = get_level(levels, level_name="initial")
                    controller_msg_queue.put((app_visible, current_level))

                elif pattern["action"] == "show":
                    app_visible = True
                    current_level = get_level(levels, level_name="initial")
                    controller_msg_queue.put((app_visible, current_level))

                elif pattern["action"] == "exit" and app_visible == True and not has_focus.empty():
                    termination_flag.put(True)
                    current_level = get_level(levels, level_name="initial")
                    controller_msg_queue.put((app_visible, current_level))

                elif (
                    pattern["action"] == "get_character" and 
                    not has_focus.empty()
                ):
                    get_character(current_level, pattern)
                    app_visible = False
                    controller_msg_queue.put((app_visible, get_level(levels, level_name="initial")))
                    paste()
                else:
                    controller_msg_queue.put((app_visible, current_level))
    except Exception:
            traceback.print_exc()
            termination_flag.put(True)
            sys.exit()