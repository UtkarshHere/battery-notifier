from pynotifier import Notification
import psutil


battery = psutil.sensors_battery()
percent = battery.secsleft
Notification(" Battery percentage Notification ", str(percent)+ " percentage left  ", duration=10).send()
