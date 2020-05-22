import json

data = [
    {
        'function': 'read_devices',
        'description': 'Ningun dispositivo conectado',
        'automated': 'False',
        'parameters': {
        },
        'expected result': 'No se encontro ningun dispositivo'
    },
    {
        'function': 'read_devices',
        'description': 'Un dispositivo conectado',
        'automated': 'True',
        'parameters': {
        },
        'expected result': 'Serial 1 = R28M410479V-'
    },
    {
        'function': 'read_devices',
        'description': 'Dos o mas dispositivos conectados',
        'automated': 'False',
        'parameters': {
        },
        'expected result': '?'
    },
    {
        'function': 'read_device',
        'description': 'Un dispositivo conectado, pedir primer dispositivo',
        'automated': 'True',
        'parameters': {
            'device_id': '1'
        },
        'expected result': 'Serial = R28M410479V'
    },
    {
        'function': 'read_device',
        'description': 'Un dispositivo conectado, pedir decimo dispositivo',
        'automated': 'True',
        'parameters': {
            'device_id': '10'
        },
        'expected result': 'list index out of range'
    },
    {
        'function': 'read_device',
        'description': 'Ningun dispositivo conectado',
        'automated': 'False',
        'parameters': {
            'device_id': '10'
        },
        'expected result': 'No se encontro ningun dispositivo'
    },
    {
        'function': 'adb_call',
        'description': 'Telefono local',
        'automated': 'False',
        'parameters': {
            'device_id': '1',
            'number_phone': '4269026',
            'seconds': '3'
        },
        'expected result': 'Llamada realizada exitosamente a 4269026'
    },
    {
        'function': 'adb_call',
        'description': 'Telefono nacional',
        'automated': 'False',
        'parameters': {
            'device_id': '1',
            'number_phone': '4494269026',
            'seconds': '3'
        },
        'expected result': 'Llamada realizada exitosamente a 4494269026'
    },
    {
        'function': 'adb_call',
        'description': 'Telefono internacional',
        'automated': 'False',
        'parameters': {
            'device_id': '1',
            'number_phone': '+524494269026',
            'seconds': '3'
        },
        'expected result': 'Llamada realizada exitosamente a +524494269026'
    },
    {
        'function': 'adb_call',
        'description': 'Telefono con #',
        'automated': 'False',
        'parameters': {
            'device_id': '1',
            'number_phone': '#321',
            'seconds': '3'
        },
        'expected result': 'Llamada realizada exitosamente a #123'
    },
    {
        'function': 'adb_call',
        'description': 'Telefono con *',
        'automated': 'False',
        'parameters': {
            'device_id': '1',
            'number_phone': '*321',
            'seconds': '3'
        },
        'expected result': 'Llamada realizada exitosamente a *123'
    },
    {
        'function': 'adb_call',
        'description': 'Telefono vacio',
        'automated': 'False',
        'parameters': {
            'device_id': '1',
            'number_phone': '',
            'seconds': '3'
        },
        'expected result': 'Numero de telefono invalido'
    },
    {
        'function': 'adb_call',
        'description': 'Telefono con letras',
        'automated': 'False',
        'parameters': {
            'device_id': '1',
            'number_phone': '123abc',
            'seconds': '3'
        },
        'expected result': 'Numero de telefono invalido'
    },
    {
        'function': 'adb_call',
        'description': 'Telefono con simbolos raros',
        'automated': 'False',
        'parameters': {
            'device_id': '1',
            'number_phone': '123!%',
            'seconds': '3'
        },
        'expected result': 'Numero de telefono invalido'
    },
    {
        'function': 'adb_ui_call',
        'description': 'Telefono local',
        'automated': 'True',
        'parameters': {
            'device_id': '1',
            'number_phone': '4269026',
            'seconds': '3'
        },
        'expected result': 'Llamada realizada exitosamente a 4269026'
    },
    {
        'function': 'adb_ui_call',
        'description': 'Telefono nacional',
        'automated': 'True',
        'parameters': {
            'device_id': '1',
            'number_phone': '4494269026',
            'seconds': '3'
        },
        'expected result': 'Llamada realizada exitosamente a 4494269026'
    },
    {
        'function': 'adb_ui_call',
        'description': 'Telefono internacional',
        'automated': 'True',
        'parameters': {
            'device_id': '1',
            'number_phone': '+524494269026',
            'seconds': '3'
        },
        'expected result': 'Llamada realizada exitosamente a +524494269026'
    },
    {
        'function': 'adb_ui_call',
        'description': 'Telefono con #',
        'automated': 'True',
        'parameters': {
            'device_id': '1',
            'number_phone': '#321',
            'seconds': '3'
        },
        'expected result': 'Llamada realizada exitosamente a #123'
    },
    {
        'function': 'adb_ui_call',
        'description': 'Telefono con *',
        'automated': 'True',
        'parameters': {
            'device_id': '1',
            'number_phone': '*321',
            'seconds': '3'
        },
        'expected result': 'Llamada realizada exitosamente a *123'
    },
    {
        'function': 'adb_ui_call',
        'description': 'Telefono vacio',
        'automated': 'True',
        'parameters': {
            'device_id': '1',
            'number_phone': '',
            'seconds': '3'
        },
        'expected result': 'Numero de telefono invalido'
    },
    {
        'function': 'adb_ui_call',
        'description': 'Telefono con letras',
        'automated': 'True',
        'parameters': {
            'device_id': '1',
            'number_phone': '123abc',
            'seconds': '3'
        },
        'expected result': 'Numero de telefono invalido'
    },
    {
        'function': 'adb_ui_call',
        'description': 'Telefono con simbolos raros',
        'automated': 'True',
        'parameters': {
            'device_id': '1',
            'number_phone': '123!%',
            'seconds': '3'
        },
        'expected result': 'Numero de telefono invalido'
    },
    {
        'function': 'adb_ui_wifi',
        'description': 'Apagar wifi con wifi encendido',
        'automated': 'True',
        'parameters': {
            'device_id': '1',
            'status': '0',
        },
        'expected result': 'Estatus de Wifi cambiado a Off'
    },
    {
        'function': 'adb_ui_wifi',
        'description': 'Apagar wifi con wifi apagado',
        'automated': 'True',
        'parameters': {
            'device_id': '1',
            'status': '0',
        },
        'expected result': 'Wifi se encuentra Off - No es necesario Turn Off'
    },
    {
        'function': 'adb_ui_wifi',
        'description': 'Encender wifi con wifi apagado',
        'automated': 'True',
        'parameters': {
            'device_id': '1',
            'status': '1',
        },
        'expected result': 'Estatus de Wifi cambiado a On'
    },
    {
        'function': 'adb_ui_wifi',
        'description': 'Encender wifi con wifi encendido',
        'automated': 'True',
        'parameters': {
            'device_id': '1',
            'status': '1',
        },
        'expected result': 'Wifi se encuentra On - No es necesario Turn On'
    },
    {
        'function': 'adb_ui_calculator',
        'description': 'Sumar dos numeros negativos',
        'automated': 'True',
        'parameters': {
            'device_id': '1',
            'operand1': '-3',
            'operator': '+',
            'operand2': '-2'
        },
        'expected result': 'Resultado correcto de operacion'
    },
    {
        'function': 'adb_ui_calculator',
        'description': 'Dividir entre 0',
        'automated': 'True',
        'parameters': {
            'device_id': '1',
            'operand1': '3',
            'operator': '/',
            'operand2': '0'
        },
        'expected result': 'No se puede dividir entre 0'
    },
    {
        'function': 'adb_ui_calculator',
        'description': 'Operador invalido',
        'automated': 'True',
        'parameters': {
            'device_id': '1',
            'operand1': '3',
            'operator': 'x',
            'operand2': '0'
        },
        'expected result': 'Operador invalido'
    },
    {
        'function': 'adb_ui_calculator',
        'description': 'Operando 1 invalido',
        'automated': 'True',
        'parameters': {
            'device_id': '1',
            'operand1': '3e1',
            'operator': '+',
            'operand2': '2'
        },
        'expected result': 'El valor del operando 1 no es valido'
    },
    {
        'function': 'adb_ui_calculator',
        'description': 'Operando 1 invalido',
        'automated': 'True',
        'parameters': {
            'device_id': '1',
            'operand1': '3',
            'operator': '+',
            'operand2': '2f1'
        },
        'expected result': 'El valor del operando 2 no es valido'
    },
    {
        'function': 'adb_ui_calculator',
        'description': 'Sumar dos numeros',
        'automated': 'True',
        'parameters': {
            'device_id': '1',
            'operand1': '4',
            'operator': '+',
            'operand2': '5'
        },
        'expected result': 'Resultado correcto de operacion'
    },
    {
        'function': 'adb_ui_calculator',
        'description': 'Restar dos numeros',
        'automated': 'True',
        'parameters': {
            'device_id': '1',
            'operand1': '4',
            'operator': '-',
            'operand2': '5'
        },
        'expected result': 'Resultado correcto de operacion'
    },
    {
        'function': 'adb_ui_calculator',
        'description': 'Multiplicar dos numeros',
        'automated': 'True',
        'parameters': {
            'device_id': '1',
            'operand1': '4',
            'operator': '*',
            'operand2': '5'
        },
        'expected result': 'Resultado correcto de operacion'
    },
    {
        'function': 'adb_ui_calculator',
        'description': 'Dividir dos numeros',
        'automated': 'True',
        'parameters': {
            'device_id': '1',
            'operand1': '4',
            'operator': '/',
            'operand2': '5'
        },
        'expected result': 'Resultado correcto de operacion'
    },
    {
        'function': 'test_adb_ui_voice_message',
        'description': 'Verificar que el telefono no tenga un mensaje de voz',
        'automated': 'True',
        'parameters': {
            'device_id': '1',
            'message': '',
        },
        'expected result': 'No se encontro mensaje de voz'
    },
    {
        'function': 'test_adb_ui_voice_message',
        'description': 'Realizar una llamada desde twilio, verificar que el telefono reciba un mensaje de voz',
        'automated': 'True',
        'parameters': {
            'device_id': '1',
            'message': 'Tengo que ser siempre el mejor '
                       'Mejor que nadie mas '
                       'Atraparlos mi prueba es '
                       'Entrenarlos mi ideal '
                       'Yo viajare de aqui alla '
                       'Buscando hasta el fin '
                       'Oh pokemon yo te entendere '
                       'Tu poder interior',
            'to': '+524494269026',
            'from': '+12183327195',
        },
        'expected result': 'Mensaje de voz encontrado'
    },
    {
        'function': 'test_twilio_voice_message',
        'description': 'Verificar el contenido del mensaje de voz',
        'automated': 'False',
        'parameters': {
        },
        'expected result': 'Tengo que ser siempre el mejor '
                           'Mejor que nadie mas '
                           'Atraparlos mi prueba es '
                           'Entrenarlos mi ideal '
                           'Yo viajare de aqui alla '
                           'Buscando hasta el fin '
                           'Oh pokemon yo te entendere '
                           'Tu poder interior',
    },
]


