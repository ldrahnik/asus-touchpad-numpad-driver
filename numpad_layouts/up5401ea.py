from libevdev import EV_KEY

# Number of tries to identify the interface number
try_times = 10
try_sleep = 0.1

cols = 5
rows = 4

#top_left_icon_is_suppressed_brightness_function = True
top_left_icon_is_suppressed = True
top_left_icon_width = 200
top_left_icon_height = 200

top_right_icon_width = 200
top_right_icon_height = 200
top_right_icon_activation_time = 0.5 # in seconds [s] 

top_offset = 200
right_offset = 200
left_offset = 200
bottom_offset = 80

touchpad_left_button_keys = [
    EV_KEY.KEY_LEFTSHIFT,
    EV_KEY.KEY_LEFTMETA,
    EV_KEY.KEY_K
]

# Including off (first value of array)
backlight_levels = [
    "0x00",
    "0x41",
    "0x42",
    "0x43",
    "0x44",
    "0x45",
    "0x46"
]
# default has to be value from array above ^^!
default_backlight_level = "0x41"

keys = [
    [EV_KEY.KEY_KP7, EV_KEY.KEY_KP8, EV_KEY.KEY_KP9, EV_KEY.KEY_KPSLASH, EV_KEY.KEY_BACKSPACE],
    [EV_KEY.KEY_KP4, EV_KEY.KEY_KP5, EV_KEY.KEY_KP6, EV_KEY.KEY_KPASTERISK, EV_KEY.KEY_BACKSPACE],
    [EV_KEY.KEY_KP1, EV_KEY.KEY_KP2, EV_KEY.KEY_KP3, EV_KEY.KEY_KPMINUS, EV_KEY.KEY_5],
    [EV_KEY.KEY_KP0, EV_KEY.KEY_KPDOT, EV_KEY.KEY_KPENTER, EV_KEY.KEY_KPPLUS, EV_KEY.KEY_KPEQUAL]
]
