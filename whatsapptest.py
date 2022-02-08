import pywhatkit
import datetime
import pyautogui as pg
import time

# Example 1: Send message to a specific number

# pywhatkit.sendwhatmsg(
#     "+5492914312803", "This message is coming from an automated Python script. Current time " + str(datetime.datetime.now()), 11, 15, 20)

# Example 2: Send message to a specific group (group id is coming from the invite link, only admins can provide that id)

QATAR22_WP_GROUP = "B9p5jiZ2vjGLqnIQ83Rw1L"

# Ejemplo: 11.20 de la mañana
HOUR = 11
MIN = 26
WAIT_TIME = 20  # Espera en segundos despues de abrir wp web antes de mandar el mensaje. Con 20 esta bien para darle tiempo de abrir

# pywhatkit.sendwhatmsg_to_group(
#     QATAR22_WP_GROUP, "Test. Current time " + str(datetime.datetime.now()), HOUR, MIN, WAIT_TIME)


# Example 3: Send message instantly

PHONE_NO = "+5492914312803"

# sendwhatmsg_instantly(phone_no: str, message: str, wait_time: int = 15, tab_close: bool = False, close_time: int = 3) -> None
pywhatkit.sendwhatmsg_instantly(
    PHONE_NO, "Mensaje instantaneo test v4", 15)
pg.press("enter")

# other option if enter doesnt work
# for i in range(10):
#     pg.press("tab")
# pg.press("enter")
