"""A big "thank you" to all our Sponsors who made this year's badge possible!"""

___name___         = "zdan"
___license___      = "MIT"
___dependencies___ = ["wifi", "http", "ugfx_helper", "sleep", "app"]
___categories___   = ["Other"]
___bootstrapped___ = False

import ugfx_helper, os, wifi, ugfx, http, time, sleep, app
from tilda import Buttons

ugfx_helper.init()
ugfx.clear()

ugfx.text(5, 5, "Loading awesomeness:", ugfx.BLACK)
try:
    image = http.get("http://www.kinyu-z.net/data/wallpapers/170/1298212.jpg").raise_for_status().content
    ugfx.display_image(0,0,bytearray(image))
except:
    ugfx.clear()
    ugfx.text(5, 5, "Couldn't download zdan", ugfx.BLACK)

while (not Buttons.is_pressed(Buttons.BTN_A)) and (not Buttons.is_pressed(Buttons.BTN_B)) and (not Buttons.is_pressed(Buttons.BTN_Menu)):
    sleep.wfi()

ugfx.clear()
app.restart_to_default()
