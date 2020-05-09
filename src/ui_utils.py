from subprocess import check_call, check_output
from uiautomator import Device
import time
from constants import dict_keyboard_call, dict_keyboard_calculator, dict_ui_status, set_operators


def adb_ui_call(phone_number, seconds, device, serial, debug=True):
    for i in range(len(phone_number)):
        if not (phone_number[i] in dict_keyboard_call):
            raise ValueError('Numero de telefono invalido')
    if len(phone_number) == 0:
        raise ValueError('Numero de telefono invalido')
    if debug:
        print ('Llamando a {}'.format(phone_number))
    device(text='Phone', className='android.widget.TextView').click()
    device(text='Keypad', className='android.widget.TextView').click()
    for i in range(len(phone_number)):
        if phone_number[i] == '+':
            device(text='+', className='android.widget.TextView').long_click()
        else:
            device(resourceId='com.samsung.android.dialer:id/{}'.format(dict_keyboard_call[phone_number[i]])).click()
    device(resourceId='com.samsung.android.dialer:id/dialButton').click()
    time.sleep(seconds)
    if device(resourceId='com.samsung.android.incallui:id/disconnect_button').exists and debug:
        print "Llamada realizada exitosamente"
    device(resourceId='com.samsung.android.incallui:id/disconnect_button').click()
    device.press.home()


def adb_ui_wifi(status, device, serial, debug=True):
    if not (status in dict_ui_status):
        raise ValueError('Valor de estatus invalido')
    device(text='Settings', className='android.widget.TextView').click()
    device(text='Connections', className='android.widget.TextView').click()
    device(text='Wi-Fi', className='android.widget.TextView').click()
    if device(text='Wi-Fi, {}'.format(dict_ui_status[status]), className='android.widget.Switch').exists:
        if debug:
            print ("Estatus de Wifi es {}".format(dict_ui_status[status]))
        device(text='Wi-Fi, {}'.format(dict_ui_status[status]), className='android.widget.Switch').click()
        if device(text='Wi-Fi, {}'.format(dict_ui_status[status ^ 1]), className='android.widget.Switch').exists \
                and debug:
            print ("Estatus de Wifi cambiado a {}".format(dict_ui_status[(status ^ 1)]))
    else:
        raise ValueError("Wifi se encuentra {0} - No es necesario Turn {0}".format(dict_ui_status[status ^ 1]))
    device.press.home()


def adb_ui_calculator(operand1, operator, operand2, device, serial, debug=True):
    device(text='Calculator', className='android.widget.TextView').click()
    if not (operator in set_operators):
        raise ValueError('Operador invalido')
    try:
        i = 1
        _operand1 = float(operand1)
        i = 2
        _operand2 = float(operand2)
    except Exception as ex:
        raise ValueError('El valor del operando {} no es valido'.format(i))
    if operator == '/' and operand2 == 0:
        raise ValueError('No se puede dividir entre 0')
    str_operand1 = str(_operand1)
    str_operand2 = str(_operand2)
    for i in range(len(str_operand1)):
        device(text=str_operand1[i], className='android.widget.Button').click()
    device(resourceId='com.sec.android.app.popupcalculator:id/calc_keypad_btn_{}'
           .format(dict_keyboard_calculator[operator])).click()
    for i in range(len(str_operand2)):
        device(text=str_operand2[i], className='android.widget.Button').click()
    device(resourceId='com.sec.android.app.popupcalculator:id/calc_keypad_btn_{}'
           .format(dict_keyboard_calculator['='])).click()
    if operator == '+':
        result = _operand1 + _operand2
    elif operator == '-':
        result = _operand1 - _operand2
    elif operator == '*':
        result = _operand1 * _operand2
    elif operator == '/':
        result = _operand1 / _operand2
    data = device(resourceId='com.sec.android.app.popupcalculator:id/calc_edt_formula').info
    text = str(data['text'])
    str_ui_result = ''
    for i in range(len(text)):
        if text[i] != ',':
            str_ui_result += text[i]
    float_ui_result = float(str_ui_result)
    if abs(result-float_ui_result) < 1e-6 and debug:
        print "Resultado correcto de operacion"
    device.press.home()

