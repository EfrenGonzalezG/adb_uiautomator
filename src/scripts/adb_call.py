from uiautomator import Device
from adb_utils import read_device, adb_call
from datetime import datetime

if __name__ == "__main__":
    phone_number = raw_input("Ingresa un numero telefonico : ")
    print("Llamada con Adb")
    print("Empezar Prueba")
    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    try:
        _serial = read_device()
        adb_call(phone_number, 3, _serial)
    except Exception as ex:
        print("Error: {}".format(ex))
    finally:
        print("Prueba finalizada")
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))