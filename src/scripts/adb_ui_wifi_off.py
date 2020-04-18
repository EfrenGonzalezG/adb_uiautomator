from uiautomator import Device
from adb_utils import read_device
from datetime import datetime
from ui_utils import adb_ui_wifi

if __name__ == "__main__":
    print("Encender Wifi")
    print("Empezar Prueba")
    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    try:
        _serial = read_device()
        _device = Device(_serial)
        adb_ui_wifi(0, _device, _serial)
    except Exception as ex:
        print("Error: {}".format(ex))
    finally:
        print("Prueba finalizada")
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))