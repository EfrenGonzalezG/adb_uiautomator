from subprocess import check_call, check_output
import time
import os
from constants import dict_adb_status, dict_keyboard_call
from logger import write_file


def read_device(j, debug=True, log_file=os.path.join('log', 'log.csv')):
    i = int(j)
    if i < 1:
        if debug:
            write_file(log_file, ['result'], {'result': 'Valor invalido, i debe ser mayor a 1 y entero'})
        raise ValueError('Valor invalido, i debe ser mayor a 0 y entero')
    if len(check_output(['adb', 'devices']).splitlines()) == 2:
        if debug:
            write_file(log_file, ['result'], {'result': 'No se encontro ningun dispositivo'})
        raise ValueError('No se encontro ningun dispositivo')
    output = check_output(['adb', 'devices']).splitlines()[i]
    serial = output.split()[0]
    if debug:
        write_file(log_file, ['result'], {'result': 'Serial = {}'.format(serial)})
        print ('Serial = {}'.format(serial))
    return serial


def read_devices(debug=True, log_file=os.path.join('log', 'log.csv')):
    s = ''
    serials = []
    output = check_output(['adb', 'devices']).splitlines()
    if len(output) == 2:
        if debug:
            write_file(log_file, ['result'], {'result': 'No se encontro ningun dispositivo'})
        raise ValueError('No se encontro ningun dispositivo')
    for i in range(1, len(output) - 1):
        serials.append(output[i].split()[0])
        if debug:
            s += 'Serial {} = {}'.format(i, serials[-1])+'-'
            print ('Serial {} = {}'.format(i, serials[-1]))
    if debug:
        write_file(log_file, ['result'], {'result': s})
    return serials


def adb_call(phone_number, seconds, serial, debug=True, log_file=os.path.join('log', 'log.csv')):
    for i in range(len(phone_number)):
        if not (phone_number[i] in dict_keyboard_call):
            if debug:
                write_file(log_file, ['result'], {'result': 'Numero de telefono invalido'})
            raise ValueError('Numero de telefono invalido')
    if len(phone_number):
        if debug:
            write_file(log_file, ['result'], {'result': 'Numero de telefono invalido'})
        raise ValueError('Numero de telefono invalido')
    if debug:
        print ('Llamando a {}'.format(phone_number))
    check_call(['adb', '-s', serial, 'shell', 'am', 'start', '-a',
                'android.intent.action.CALL', '-d', 'tel:{}'.format(phone_number)])
    time.sleep(seconds)
    check_call(['adb', '-s', serial, 'shell', 'input', 'keyevent', 'KEYCODE_ENDCALL'])
    check_call(['adb', '-s', serial, 'shell', 'input', 'keyevent', 'KEYCODE_HOME'])
    if debug:
        print ('Llamada realizada exitosamente a {}'.format(phone_number))
        write_file(log_file, ['result'], {'result': 'Llamada realizada exitosamente a {}'.format(phone_number)})


def adb_wifi(status, serial):
    check_call(['adb', '-s', serial, 'shell', 'svc wifi {}'.format(dict_adb_status[status])])
