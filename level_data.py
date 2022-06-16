from pynput.keyboard import Key
from pynput.keyboard._win32 import KeyCode

level_data = [
        {
            "level_id":1,
            "name":"initial",
            "bg":"initial.bmp",
            "patterns":[
                # region (initial)
                {
                    # hide gui
                    "key_pattern":[Key.esc], 
                    "action":"hide",
                    "action_data":"",
                    "when_visible":True,
                },
                {
                    # show gui
                    "key_pattern":[Key.alt_l, Key.alt_l, Key.alt_l], 
                    "action":"show",
                    "action_data":"",
                    "when_visible":False,
                },
                {
                    # exit app / shift key
                    "key_pattern":[Key.shift], 
                    "action":"hide",
                    "action_data":"",
                    "when_visible":True,
                },
                {
                    # a key
                    "key_pattern":[KeyCode(char="a")], 
                    "action":"change_level",
                    "action_data":2,
                    "when_visible":True,
                },
                {
                    # s key
                    "key_pattern":[KeyCode(char="s")], 
                    "action":"change_level",
                    "action_data":4,
                    "when_visible":True,
                },
                {
                    # d key
                    "key_pattern":[KeyCode(char="d")], 
                    "action":"change_level",
                    "action_data":6,
                    "when_visible":True,
                },
                {
                    # f key
                    "key_pattern":[KeyCode(char="f")], 
                    "action":"change_level",
                    "action_data":14,
                    "when_visible":True,
                },
                {
                    # q key
                    "key_pattern":[KeyCode(char="q")], 
                    "action":"change_level",
                    "action_data":12,
                    "when_visible":True,
                },
                {
                    # w key
                    "key_pattern":[KeyCode(char="w")], 
                    "action":"change_level",
                    "action_data":8,
                    "when_visible":True,
                },
                {
                    # e key
                    "key_pattern":[KeyCode(char="e")], 
                    "action":"change_level",
                    "action_data":10,
                    "when_visible":True,
                },
                # endregion (initial)
            ]
        },
        {
            "level_id":2,
            "name":"lower_a",
            "bg":"lower_a.bmp",
            "patterns":[
                # region (lower_a)
                {
                    # hide gui
                    "key_pattern":[Key.esc], 
                    "action":"hide",
                    "action_data":"",
                    "when_visible":True,
                },
                {
                    # shift key
                    "key_pattern":[Key.shift], 
                    "action":"change_level",
                    "action_data":3,
                    "when_visible":True,
                },
                {
                    # a key
                    "key_pattern":[KeyCode(char="a")], 
                    "action":"get_character",
                    "action_data":"a",
                    "when_visible":True,
                },
                                {
                    # s key
                    "key_pattern":[KeyCode(char="s")], 
                    "action":"get_character",
                    "action_data":"s",
                    "when_visible":True,
                },
                                {
                    # d key
                    "key_pattern":[KeyCode(char="d")], 
                    "action":"get_character",
                    "action_data":"d",
                    "when_visible":True,
                },
                                {
                    # f key
                    "key_pattern":[KeyCode(char="f")], 
                    "action":"get_character",
                    "action_data":"f",
                    "when_visible":True,
                },
                                {
                    # q key
                    "key_pattern":[KeyCode(char="q")], 
                    "action":"get_character",
                    "action_data":"q",
                    "when_visible":True,
                },
                                {
                    # w key
                    "key_pattern":[KeyCode(char="w")], 
                    "action":"get_character",
                    "action_data":"w",
                    "when_visible":True,
                },
                                {
                    # e key
                    "key_pattern":[KeyCode(char="e")], 
                    "action":"get_character",
                    "action_data":"e",
                    "when_visible":True,
                },
                # endregion (lower_a)
            ]
        },
        {
            "level_id":3,
            "name":"upper_a",
            "bg":"upper_a.bmp",
            "patterns":[
                # region (upper_a)
                {
                    # hide gui
                    "key_pattern":[Key.esc], 
                    "action":"hide",
                    "action_data":"",
                    "when_visible":True,
                },
                {
                    # shift key
                    "key_pattern":[Key.shift], 
                    "action":"change_level",
                    "action_data":2,
                    "when_visible":True,
                },
                {
                    # a key
                    "key_pattern":[KeyCode(char="a")], 
                    "action":"get_character",
                    "action_data":"a",
                    "when_visible":True,
                },
                                {
                    # s key
                    "key_pattern":[KeyCode(char="s")], 
                    "action":"get_character",
                    "action_data":"s",
                    "when_visible":True,
                },
                                {
                    # d key
                    "key_pattern":[KeyCode(char="d")], 
                    "action":"get_character",
                    "action_data":"d",
                    "when_visible":True,
                },
                                {
                    # f key
                    "key_pattern":[KeyCode(char="f")], 
                    "action":"get_character",
                    "action_data":"f",
                    "when_visible":True,
                },
                                {
                    # q key
                    "key_pattern":[KeyCode(char="q")], 
                    "action":"get_character",
                    "action_data":"q",
                    "when_visible":True,
                },
                                {
                    # w key
                    "key_pattern":[KeyCode(char="w")], 
                    "action":"get_character",
                    "action_data":"w",
                    "when_visible":True,
                },
                                {
                    # e key
                    "key_pattern":[KeyCode(char="e")], 
                    "action":"get_character",
                    "action_data":"e",
                    "when_visible":True,
                },
                # endregion (upper_a)
            ]
        },
        {
            "level_id":4,
            "name":"lower_e",
            "bg":"lower_e.bmp",
            "patterns":[
                # region (lower_e)
                {
                    # hide gui
                    "key_pattern":[Key.esc], 
                    "action":"hide",
                    "action_data":"",
                    "when_visible":True,
                },
                {
                    # shift key
                    "key_pattern":[Key.shift], 
                    "action":"change_level",
                    "action_data":5,
                    "when_visible":True,
                },
                {
                    # a key
                    "key_pattern":[KeyCode(char="a")], 
                    "action":"get_character",
                    "action_data":"a",
                    "when_visible":True,
                },
                                {
                    # s key
                    "key_pattern":[KeyCode(char="s")], 
                    "action":"get_character",
                    "action_data":"s",
                    "when_visible":True,
                },
                                {
                    # d key
                    "key_pattern":[KeyCode(char="d")], 
                    "action":"get_character",
                    "action_data":"d",
                    "when_visible":True,
                },
                                {
                    # f key
                    "key_pattern":[KeyCode(char="f")], 
                    "action":"get_character",
                    "action_data":"f",
                    "when_visible":True,
                },
                # endregion (lower_e)
            ]
        },
        {
            "level_id":5,
            "name":"upper_e",
            "bg":"upper_e.bmp",
            "patterns":[
                # region (upper_e)
                {
                    # hide gui
                    "key_pattern":[Key.esc], 
                    "action":"hide",
                    "action_data":"",
                    "when_visible":True,
                },
                {
                    # shift key
                    "key_pattern":[Key.shift], 
                    "action":"change_level",
                    "action_data":4,
                    "when_visible":True,
                },
                {
                    # a key
                    "key_pattern":[KeyCode(char="a")], 
                    "action":"get_character",
                    "action_data":"a",
                    "when_visible":True,
                },
                                {
                    # s key
                    "key_pattern":[KeyCode(char="s")], 
                    "action":"get_character",
                    "action_data":"s",
                    "when_visible":True,
                },
                                {
                    # d key
                    "key_pattern":[KeyCode(char="d")], 
                    "action":"get_character",
                    "action_data":"d",
                    "when_visible":True,
                },
                                {
                    # f key
                    "key_pattern":[KeyCode(char="f")], 
                    "action":"get_character",
                    "action_data":"f",
                    "when_visible":True,
                },

                # endregion (upper_e)
            ]
        },
        {
            "level_id":6,
            "name":"lower_i",
            "bg":"lower_i.bmp",
            "patterns":[
                # region (lower_i)
                {
                    # hide gui
                    "key_pattern":[Key.esc], 
                    "action":"hide",
                    "action_data":"",
                    "when_visible":True,
                },
                {
                    # shift key
                    "key_pattern":[Key.shift], 
                    "action":"change_level",
                    "action_data":7,
                    "when_visible":True,
                },
                {
                    # a key
                    "key_pattern":[KeyCode(char="a")], 
                    "action":"get_character",
                    "action_data":"a",
                    "when_visible":True,
                },
                                {
                    # s key
                    "key_pattern":[KeyCode(char="s")], 
                    "action":"get_character",
                    "action_data":"s",
                    "when_visible":True,
                },
                                {
                    # d key
                    "key_pattern":[KeyCode(char="d")], 
                    "action":"get_character",
                    "action_data":"d",
                    "when_visible":True,
                },
                                {
                    # f key
                    "key_pattern":[KeyCode(char="f")], 
                    "action":"get_character",
                    "action_data":"f",
                    "when_visible":True,
                },
                # endregion (lower_i)
            ]
        },
        {
            "level_id":7,
            "name":"upper_i",
            "bg":"upper_i.bmp",
            "patterns":[
                # region (lower_i)
                {
                    # hide gui
                    "key_pattern":[Key.esc], 
                    "action":"hide",
                    "action_data":"",
                    "when_visible":True,
                },
                {
                    # shift key
                    "key_pattern":[Key.shift], 
                    "action":"change_level",
                    "action_data":6,
                    "when_visible":True,
                },
                {
                    # a key
                    "key_pattern":[KeyCode(char="a")], 
                    "action":"get_character",
                    "action_data":"a",
                    "when_visible":True,
                },
                                {
                    # s key
                    "key_pattern":[KeyCode(char="s")], 
                    "action":"get_character",
                    "action_data":"s",
                    "when_visible":True,
                },
                                {
                    # d key
                    "key_pattern":[KeyCode(char="d")], 
                    "action":"get_character",
                    "action_data":"d",
                    "when_visible":True,
                },
                                {
                    # f key
                    "key_pattern":[KeyCode(char="f")], 
                    "action":"get_character",
                    "action_data":"f",
                    "when_visible":True,
                },
                # endregion (upper_i)
            ]
        },
        {
            "level_id":8,
            "name":"lower_o",
            "bg":"lower_o.bmp",
            "patterns":[
                # region (lower_o)
                {
                    # hide gui  
                    "key_pattern":[Key.esc], 
                    "action":"hide",
                    "action_data":"",
                    "when_visible":True,
                },
                {
                    # shift key
                    "key_pattern":[Key.shift], 
                    "action":"change_level",
                    "action_data":9,
                    "when_visible":True,
                },
                {
                    # a key
                    "key_pattern":[KeyCode(char="a")], 
                    "action":"get_character",
                    "action_data":"a",
                    "when_visible":True,
                },
                                {
                    # s key
                    "key_pattern":[KeyCode(char="s")], 
                    "action":"get_character",
                    "action_data":"s",
                    "when_visible":True,
                },
                                {
                    # d key
                    "key_pattern":[KeyCode(char="d")], 
                    "action":"get_character",
                    "action_data":"d",
                    "when_visible":True,
                },
                                {
                    # f key
                    "key_pattern":[KeyCode(char="f")], 
                    "action":"get_character",
                    "action_data":"f",
                    "when_visible":True,
                },
                                {
                    # q key
                    "key_pattern":[KeyCode(char="q")], 
                    "action":"get_character",
                    "action_data":"q",
                    "when_visible":True,
                },
                                {
                    # w key
                    "key_pattern":[KeyCode(char="w")], 
                    "action":"get_character",
                    "action_data":"w",
                    "when_visible":True,
                },
                                {
                    # e key
                    "key_pattern":[KeyCode(char="e")], 
                    "action":"get_character",
                    "action_data":"e",
                    "when_visible":True,
                },
                # endregion (lower_o)
            ]
        },
        {
            "level_id":9,
            "name":"upper_o",
            "bg":"upper_o.bmp",
            "patterns":[
                # region (upper_o)
                {
                    # hide gui
                    "key_pattern":[Key.esc], 
                    "action":"hide",
                    "action_data":"",
                    "when_visible":True,
                },
                {
                    # shift key
                    "key_pattern":[Key.shift], 
                    "action":"change_level",
                    "action_data":8,
                    "when_visible":True,
                },
                {
                    # a key
                    "key_pattern":[KeyCode(char="a")], 
                    "action":"get_character",
                    "action_data":"a",
                    "when_visible":True,
                },
                                {
                    # s key
                    "key_pattern":[KeyCode(char="s")], 
                    "action":"get_character",
                    "action_data":"s",
                    "when_visible":True,
                },
                                {
                    # d key
                    "key_pattern":[KeyCode(char="d")], 
                    "action":"get_character",
                    "action_data":"d",
                    "when_visible":True,
                },
                                {
                    # f key
                    "key_pattern":[KeyCode(char="f")], 
                    "action":"get_character",
                    "action_data":"f",
                    "when_visible":True,
                },
                                {
                    # q key
                    "key_pattern":[KeyCode(char="q")], 
                    "action":"get_character",
                    "action_data":"q",
                    "when_visible":True,
                },
                                {
                    # w key
                    "key_pattern":[KeyCode(char="w")], 
                    "action":"get_character",
                    "action_data":"w",
                    "when_visible":True,
                },
                                {
                    # e key
                    "key_pattern":[KeyCode(char="e")], 
                    "action":"get_character",
                    "action_data":"e",
                    "when_visible":True,
                },
                # endregion (upper_o)
            ]
        },
        {
            "level_id":10,
            "name":"lower_u",
            "bg":"lower_u.bmp",
            "patterns":[
                # region (lower_u)
                {
                    # hide gui
                    "key_pattern":[Key.esc], 
                    "action":"hide",
                    "action_data":"",
                    "when_visible":True,
                },
                {
                    # shift key
                    "key_pattern":[Key.shift], 
                    "action":"change_level",
                    "action_data":11,
                    "when_visible":True,
                },
                {
                    # a key
                    "key_pattern":[KeyCode(char="a")], 
                    "action":"get_character",
                    "action_data":"a",
                    "when_visible":True,
                },
                                {
                    # s key
                    "key_pattern":[KeyCode(char="s")], 
                    "action":"get_character",
                    "action_data":"s",
                    "when_visible":True,
                },
                                {
                    # d key
                    "key_pattern":[KeyCode(char="d")], 
                    "action":"get_character",
                    "action_data":"d",
                    "when_visible":True,
                },
                                {
                    # f key
                    "key_pattern":[KeyCode(char="f")], 
                    "action":"get_character",
                    "action_data":"f",
                    "when_visible":True,
                },
                # endregion (lower_u))
            ]
        },
        {
            "level_id":11,
            "name":"upper_u",
            "bg":"upper_u.bmp",
            "patterns":[
                # region (upper_u)
                {
                    # hide gui
                    "key_pattern":[Key.esc], 
                    "action":"hide",
                    "action_data":"",
                    "when_visible":True,
                },
                {
                    # shift key
                    "key_pattern":[Key.shift], 
                    "action":"change_level",
                    "action_data":10,
                    "when_visible":True,
                },
                {
                    # a key
                    "key_pattern":[KeyCode(char="a")], 
                    "action":"get_character",
                    "action_data":"a",
                    "when_visible":True,
                },
                {
                    # s key
                    "key_pattern":[KeyCode(char="s")], 
                    "action":"get_character",
                    "action_data":"s",
                    "when_visible":True,
                },
                {
                    # d key
                    "key_pattern":[KeyCode(char="d")], 
                    "action":"get_character",
                    "action_data":"d",
                    "when_visible":True,
                },
                {
                    # f key
                    "key_pattern":[KeyCode(char="f")], 
                    "action":"get_character",
                    "action_data":"f",
                    "when_visible":True,
                },

                # endregion (upper_u)
            ]
        },
        {
            "level_id":12,
            "name":"lower_misc",
            "bg":"lower_misc.bmp",
"patterns":[
                # region (lower_misc)
                {
                    # hide gui
                    "key_pattern":[Key.esc], 
                    "action":"hide",
                    "action_data":"",
                    "when_visible":True,
                },
                {
                    # shift key
                    "key_pattern":[Key.shift], 
                    "action":"change_level",
                    "action_data":13,
                    "when_visible":True,
                },
                {
                    # a key
                    "key_pattern":[KeyCode(char="a")], 
                    "action":"get_character",
                    "action_data":"a",
                    "when_visible":True,
                },
                                {
                    # s key
                    "key_pattern":[KeyCode(char="s")], 
                    "action":"get_character",
                    "action_data":"s",
                    "when_visible":True,
                },
                                {
                    # d key
                    "key_pattern":[KeyCode(char="d")], 
                    "action":"get_character",
                    "action_data":"d",
                    "when_visible":True,
                },
                                {
                    # f key
                    "key_pattern":[KeyCode(char="f")], 
                    "action":"get_character",
                    "action_data":"f",
                    "when_visible":True,
                },
                                {
                    # q key
                    "key_pattern":[KeyCode(char="q")], 
                    "action":"get_character",
                    "action_data":"q",
                    "when_visible":True,
                },
                                {
                    # w key
                    "key_pattern":[KeyCode(char="w")], 
                    "action":"get_character",
                    "action_data":"w",
                    "when_visible":True,
                },
                                {
                    # e key
                    "key_pattern":[KeyCode(char="e")], 
                    "action":"get_character",
                    "action_data":"e",
                    "when_visible":True,
                },
                {
                    # r key
                    "key_pattern":[KeyCode(char="r")], 
                    "action":"get_character",
                    "action_data":"e",
                    "when_visible":True,
                },
                # endregion (lower_misc)
            ]
        },
        {
            "level_id":13,
            "name":"upper_misc",
            "bg":"upper_misc.bmp",
            "patterns":[
                # region (upper_misc)
                {
                    # hide gui
                    "key_pattern":[Key.esc], 
                    "action":"hide",
                    "action_data":"",
                    "when_visible":True,
                },
                {
                    # shift key
                    "key_pattern":[Key.shift], 
                    "action":"change_level",
                    "action_data":12,
                    "when_visible":True,
                },
                {
                    # a key
                    "key_pattern":[KeyCode(char="a")], 
                    "action":"get_character",
                    "action_data":"a",
                    "when_visible":True,
                },
                                {
                    # s key
                    "key_pattern":[KeyCode(char="s")], 
                    "action":"get_character",
                    "action_data":"s",
                    "when_visible":True,
                },
                                {
                    # d key
                    "key_pattern":[KeyCode(char="d")], 
                    "action":"get_character",
                    "action_data":"d",
                    "when_visible":True,
                },
                                {
                    # f key
                    "key_pattern":[KeyCode(char="f")], 
                    "action":"get_character",
                    "action_data":"f",
                    "when_visible":True,
                },
                                {
                    # q key
                    "key_pattern":[KeyCode(char="q")], 
                    "action":"get_character",
                    "action_data":"q",
                    "when_visible":True,
                },
                                {
                    # w key
                    "key_pattern":[KeyCode(char="w")], 
                    "action":"get_character",
                    "action_data":"w",
                    "when_visible":True,
                },
                                {
                    # e key
                    "key_pattern":[KeyCode(char="e")], 
                    "action":"get_character",
                    "action_data":"e",
                    "when_visible":True,
                },
                {
                    # r key
                    "key_pattern":[KeyCode(char="r")], 
                    "action":"get_character",
                    "action_data":"e",
                    "when_visible":True,
                },
                # endregion (upper_misc)
            ]
        },
        {
            "level_id":14,
            "name":"currency",
            "bg":"currency.bmp",
            "patterns":[
                # region (upper_e)
                {
                    # hide gui
                    "key_pattern":[Key.esc], 
                    "action":"hide",
                    "action_data":"",
                    "when_visible":True,
                },
                {
                    # a key
                    "key_pattern":[KeyCode(char="a")], 
                    "action":"get_character",
                    "action_data":"a",
                    "when_visible":True,
                },
                                {
                    # s key
                    "key_pattern":[KeyCode(char="s")], 
                    "action":"get_character",
                    "action_data":"s",
                    "when_visible":True,
                },
                                {
                    # d key
                    "key_pattern":[KeyCode(char="d")], 
                    "action":"get_character",
                    "action_data":"d",
                    "when_visible":True,
                },
                                {
                    # f key
                    "key_pattern":[KeyCode(char="f")], 
                    "action":"get_character",
                    "action_data":"f",
                    "when_visible":True,
                },
                                {
                    # q key
                    "key_pattern":[KeyCode(char="q")], 
                    "action":"get_character",
                    "action_data":"q",
                    "when_visible":True,
                },
                                {
                    # w key
                    "key_pattern":[KeyCode(char="w")], 
                    "action":"get_character",
                    "action_data":"w",
                    "when_visible":True,
                },
                                {
                    # e key
                    "key_pattern":[KeyCode(char="e")], 
                    "action":"get_character",
                    "action_data":"e",
                    "when_visible":True,
                },
                # endregion (upper_e)
            ]
        },
    ]
