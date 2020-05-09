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
        'description': 'Un dispositivo conectado',
        'automated': 'True',
        'parameters': {
            'device_id': '1'
        },
        'expected result': 'Serial = R28M410479V'
    },
    {
        'function': 'read_device',
        'description': 'Un dispositivo conectado',
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
        'parameters': {
            'device_id': '1',
            'number_phone': '123',
            'seconds': '3'
        }
    },
]


