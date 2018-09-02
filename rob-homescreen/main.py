"""A big foobar wibble "thank you" to all our Sponsors who made this year's badge possible!"""

___name___         = "Robert and his flying trapeze"
___license___      = "MIT"
___dependencies___ = ["homescreen", "shared/logo.png", "shared/sponsors.png"]
___categories___   = ["Other"]
___bootstrapped___ = False
___launchable___   = False

import ugfx
from homescreen import *
import time

# Padding for name
intro_height = 60 # 30
intro_text = "Hi! My name is "
name_height = 70 # 60
status_height = 15 #20
info_height = 15 # 30
logo_path = "shared/logo.png"
logo_height = 150
logo_width = 56

# Maximum length of name before downscaling
max_name = 8

# Background stuff
init()
ugfx.clear(ugfx.html_color(0x073763))

# Colour stuff
style = ugfx.Style()
style.set_enabled([ugfx.WHITE, ugfx.html_color(0x073763), ugfx.html_color(0x073763), ugfx.html_color(0x073763)])
style.set_background(ugfx.html_color(0x073763))
ugfx.set_default_style(style)

# Logo stuff
ugfx.display_image(
    int((ugfx.width() - logo_width) / 2),
    int((ugfx.height() - logo_height) / 2),
    logo_path
)



# Draw for people to see
ugfx.orientation(90)
# Draw introduction
ugfx.set_default_font(ugfx.FONT_TITLE)
ugfx.Label(0, ugfx.height() - name_height - intro_height, ugfx.width(), intro_height, intro_text, justification=ugfx.Label.CENTER)
# Process name
name_setting = name("Set your name in the settings app")
if len(name_setting) <= max_name:
    ugfx.set_default_font(ugfx.FONT_NAME)
else:
    ugfx.set_default_font(ugfx.FONT_MEDIUM_BOLD)
# Draw name
ugfx.Label(0, ugfx.height() - name_height, ugfx.width(), name_height, name_setting, justification=ugfx.Label.CENTER)


# Draw for wearer to see
ugfx.orientation(270)
# Title
#ugfx.set_default_font(ugfx.FONT_TITLE)
#ugfx.Label(0, ugfx.height() - info_height * 2, ugfx.width(), info_height, "TiLDA Mk4", justification=ugfx.Label.CENTER)
# info
#ugfx.Label(0, ugfx.height() - info_height, ugfx.width(), info_height, "Press MENU", justification=ugfx.Label.CENTER)

ugfx.set_default_font(ugfx.FONT_SMALL)
status = ugfx.Label(0, ugfx.height() - info_height * 2 - status_height, ugfx.width(), status_height, "", justification=ugfx.Label.CENTER)

# update loop
while True:
    text = "";
    value_wifi_strength = wifi_strength()
    value_battery = battery()
    if value_wifi_strength:
        text += "Wi-Fi: %s%%, " % int(value_wifi_strength)
    if value_battery:
        text += "Battery: %s%%" % int(value_battery)
    status.text(text)
    sleep_or_exit(0.5)

