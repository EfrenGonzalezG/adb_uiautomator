from uiautomator import Device
from adb_utils import read_device
from datetime import datetime
from ui_utils import adb_ui_calculator

try:
    _serial = read_device(5)
    _device = Device(_serial)
except Exception as ex:
    print ex
#adb_ui_calculator(1000000, '*', 1000, _device, _serial)
