from subprocess import check_call, check_output
from uiautomator import Device
import os
import time
from constants import dict_keyboard_call, dict_keyboard_calculator, dict_ui_status, set_operators
from logger import write_file


def adb_ui_call(phone_number, seconds, device, debug=False, log_file=os.path.join('log', 'log.csv')):
    for i in range(len(phone_number)):
        if not (phone_number[i] in dict_keyboard_call):
            if debug:
                write_file(log_file, ['result'], {'result': 'Numero de telefono invalido'})
            raise ValueError('Numero de telefono invalido')
    if len(phone_number) == 0:
        if debug:
            write_file(log_file, ['result'], {'result': 'Numero de telefono invalido'})
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
        if debug:
            write_file(log_file, ['result'], {'result': "Llamada realizada exitosamente"})
        print "Llamada realizada exitosamente"
    device(resourceId='com.samsung.android.incallui:id/disconnect_button').click()
    device.press.home()


def adb_ui_wifi(status, device, debug=False, log_file=os.path.join('log', 'log.csv')):
    if not (status in dict_ui_status):
        if debug:
            write_file(log_file, ['result'], {'result': "Valor de estatus invalido"})
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
            write_file(log_file, ['result'],
                       {'result': "Estatus de Wifi cambiado a {}".format(dict_ui_status[(status ^ 1)])})
            print ("Estatus de Wifi cambiado a {}".format(dict_ui_status[(status ^ 1)]))
    else:
        if debug:
            write_file(log_file, ['result'],
                       {'result': "Wifi se encuentra {0} - No es necesario Turn {0}".format(
                           dict_ui_status[status ^ 1])})
        device.press.home()
        raise ValueError("Wifi se encuentra {0} - No es necesario Turn {0}".format(dict_ui_status[status ^ 1]))
    device.press.home()


def adb_ui_calculator(operand1, operator, operand2, device,
                      debug=False, log_file=os.path.join('log', 'log.csv')):
    if not (operator in set_operators):
        if debug:
            write_file(log_file, ['result'], {'result': 'Operador invalido'})
        raise ValueError('Operador invalido')
    try:
        i = 1
        _operand1 = float(operand1)
        i = 2
        _operand2 = float(operand2)
    except Exception as ex:
        if debug:
            write_file(log_file, ['result'], {'result': 'El valor del operando {} no es valido'.format(i)})
        raise ValueError('El valor del operando {} no es valido'.format(i))
    if operator == '/' and _operand2 < 1e-6:
        if debug:
            write_file(log_file, ['result'], {'result': 'No se puede dividir entre 0'})
        raise ValueError('No se puede dividir entre 0')
    device(text='Calculator', className='android.widget.TextView').click()
    str_operand1 = str(_operand1)
    str_operand2 = str(_operand2)
    negative = False
    for i in range(len(str_operand1)):
        if str_operand1[i] == '-':
            negative = True
            device(resourceId='com.sec.android.app.popupcalculator:id/calc_keypad_btn_{}'
                   .format(dict_keyboard_calculator['('])).click()
            device(resourceId='com.sec.android.app.popupcalculator:id/calc_keypad_btn_{}'
                   .format(dict_keyboard_calculator['-'])).click()
        else:
            device(text=str_operand1[i], className='android.widget.Button').click()
    if negative:
        device(resourceId='com.sec.android.app.popupcalculator:id/calc_keypad_btn_{}'
               .format(dict_keyboard_calculator[')'])).click()
    device(resourceId='com.sec.android.app.popupcalculator:id/calc_keypad_btn_{}'
           .format(dict_keyboard_calculator[operator])).click()
    negative = False
    for i in range(len(str_operand2)):
        if str_operand1[i] == '-':
            negative = True
            device(resourceId='com.sec.android.app.popupcalculator:id/calc_keypad_btn_{}'
                   .format(dict_keyboard_calculator['('])).click()
            device(resourceId='com.sec.android.app.popupcalculator:id/calc_keypad_btn_{}'
                   .format(dict_keyboard_calculator['-'])).click()
        else:
            device(text=str_operand2[i], className='android.widget.Button').click()
    if negative:
        device(resourceId='com.sec.android.app.popupcalculator:id/calc_keypad_btn_{}'
               .format(dict_keyboard_calculator[')'])).click()
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
    text = data['text'].replace(u"\u2212", '-')
    str_ui_result = ''
    for i in range(len(text)):
        if text[i] != ',':
            str_ui_result += text[i]
    float_ui_result = float(str_ui_result)
    if abs(result - float_ui_result) < 1e-6 and debug:
        if debug:
            write_file(log_file, ['result'], {'result': "Resultado correcto de operacion"})
        print "Resultado correcto de operacion"
    else:
        if debug:
            write_file(log_file, ['result'], {'result': "Resultado incorrecto"})
        device.press.home()
        raise ValueError("Resultado incorrecto")
    device.press.home()


def adb_ui_voice_message(device, debug=False, log_file=os.path.join('log', 'log.csv')):
    device.open.notification()
    if device(text='New voicemail', className='android.widget.TextView').exists:
        if debug:
            print("Mensaje de voz encontrado")
            write_file(log_file, ['result'], {'result': "Mensaje de voz encontrado"})
    else:
        if debug:
            print("No se encontro mensaje de voz")
            write_file(log_file, ['result'], {'result': "No se encontro mensaje de voz"})
    device.press.home()
