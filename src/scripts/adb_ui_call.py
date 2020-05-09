from uiautomator import Device
from adb_utils import read_device
from datetime import datetime

from ui_utils import adb_ui_call

if __name__ == "__main__":
    phone_number = raw_input("Ingresa un numero telefonico : ")
    print("Llamada con Adb y UI")
    print("Empezar Prueba")
    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    try:
        _serial = read_device()
        _device = Device(_serial)
        adb_ui_call(phone_number, 3, _device, _serial)
    except Exception as ex:
        print("Error: {}".format(ex))
    finally:
        print("Prueba finalizada")
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))