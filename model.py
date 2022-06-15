from dataclasses import dataclass
import time
import sys
import traceback
import pyperclip
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

def model(model_msg_queue, controller_msg_queue, termination_flag):
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

                if pattern["action"] == "change_level" and app_visible == True:            
                    current_level = get_level(levels, level_id = pattern["action_data"])
                    controller_msg_queue.put((app_visible, current_level))
                
                elif pattern["action"] == "hide" and app_visible == True:
                    app_visible = False
                    controller_msg_queue.put((app_visible, get_level(levels, level_name="initial")))

                elif pattern["action"] == "show":
                    app_visible = True
                    controller_msg_queue.put((app_visible, get_level(levels, level_name="initial")))

                elif pattern["action"] == "exit" and app_visible == True:
                    termination_flag.put(True)
                    controller_msg_queue.put((app_visible, get_level(levels, level_name="initial")))

                elif pattern["action"] == "get_character":
                    get_character(current_level, pattern)
                    app_visible = False
                    controller_msg_queue.put((app_visible, get_level(levels, level_name="initial")))

                else:
                    controller_msg_queue.put((app_visible, get_level(levels, level_name="initial")))
    except Exception:
            traceback.print_exc()
            termination_flag.put(True)
            time.sleep(1)
            sys.exit()