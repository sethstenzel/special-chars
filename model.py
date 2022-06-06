from pynput.keyboard import Key
from dataclasses import dataclass

class Level:
        name: str
        bg: str
        patterns: list
        key_map: dict

def build_levels():
    levels = []
    level_data = [
        {
            "name":"initial",
            "bg":"initial.bmp",
            "patterns":[
                {
                    "id":1,
                    "pattern":[Key.ctrl, Key.shift, Key.shift], 
                    "action":"show",
                    "data":"",
                }
            ],
            "key_map":dict(),
        },
    ]

    for level in level_data:
        levels.append(
            Level(level["name"],level["bg"],level["patterns"],level["key_map"])
        )
    return levels

def model(msg_queue, termination_flag):
    current_level = None
    levels = build_levels()
    for level in levels:
        if level.name == "initial":
            current_level = level