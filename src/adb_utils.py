from subprocess import check_call, check_output
import time
from constants import dict_adb_status, dict_keyboard


def read_device():
    output = check_output(['adb', 'devices']).splitlines()[1]
    if len(output.split()) == 0:
        raise ValueError('No se encontro ningun dispositivo')
    serial = output.split()[0]
    print ('Serial= {}'.format(serial))
    return serial


def adb_call(phone_number, seconds, serial):
    for i in range(len(phone_number)):
        if not (phone_number[i] in dict_keyboard):
            raise ValueError('Numero de telefono invalido')
    if len(phone_number):
        raise ValueError('Numero de telefono invalido')
    print ('Llamando a {}'.format(phone_number))
    check_call(['adb', '-s', serial, 'shell', 'am', 'start', '-a',
                'android.intent.action.CALL', '-d', 'tel:{}'.format(phone_number)])
    time.sleep(seconds)
    check_call(['adb', '-s', serial, 'shell', 'input', 'keyevent', 'KEYCODE_ENDCALL'])
    check_call(['adb', '-s', serial, 'shell', 'input', 'keyevent', 'KEYCODE_HOME'])


def adb_wifi(status, serial):
    check_call(['adb', '-s', serial, 'shell', 'svc wifi {}'.format(dict_adb_status[status])])
