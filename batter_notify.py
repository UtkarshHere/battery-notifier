from pynotifier import Notification
import psutil


battery = psutil.sensors_battery()
percent = battery.secsleft
Notification(" Battery percentage Notification ", float(percent)+ " seconds left ", duration=10).send()
