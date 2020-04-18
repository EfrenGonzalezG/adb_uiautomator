from subprocess import check_call, check_output
from uiautomator import Device
import time
from constants import dict_keyboard, dict_ui_status


def adb_ui_call(phone_number, seconds, device, serial):
    for i in range(len(phone_number)):
        if not (phone_number[i] in dict_keyboard):
            raise ValueError('Numero de telefono invalido')
    if len(phone_number):
        raise ValueError('Numero de telefono invalido')
    print ('Llamando a {}'.format(phone_number))
    device(text='Phone', className='android.widget.TextView').click()
    device(text='Keypad', className='android.widget.TextView').click()
    for i in range(len(phone_number)):
        if phone_number[i] == '+':
            device(text='+', className='android.widget.TextView').long_click()
        else:
            device(resourceId='com.samsung.android.dialer:id/{}'.format(dict_keyboard[phone_number[i]])).click()
    device(resourceId='com.samsung.android.dialer:id/dialButton').click()
    time.sleep(seconds)
    device(resourceId='com.samsung.android.incallui:id/disconnect_button').click()
    check_call(['adb', '-s', serial, 'shell', 'input', 'keyevent', 'KEYCODE_HOME'])


def adb_ui_wifi(status, device, serial):
    if not (status in dict_ui_status):
        raise ValueError('Valor de estatus invalido')
    device(text='Settings', className='android.widget.TextView').click()
    device(text='Connections', className='android.widget.TextView').click()
    device(text='Wi-Fi', className='android.widget.TextView').click()
    if device(text='Wi-Fi, {}'.format(dict_ui_status[status]), className='android.widget.Switch').exists:
        print("Estatus de Wifi es {}".format(dict_ui_status[status]))
        device(text='Wi-Fi, {}'.format(dict_ui_status[status]), className='android.widget.Switch').click()
        print ("Estatus de Wifi cambiado a {}".format(dict_ui_status[(status ^ 1)]))
    else:
        raise ValueError("Wifi se encuentra {0} - No es necesario Turn {0}".format(dict_ui_status[status ^ 1]))
    check_call(['adb', '-s', serial, 'shell', 'input', 'keyevent', 'KEYCODE_HOME'])