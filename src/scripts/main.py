import os
from uiautomator import Device
from adb_utils import read_device, read_devices
from data import data
from datetime import datetime
from logger import create_file, write_file


def test_read_devices(case_data, log_result):
    read_devices(debug=True, log_file=log_result)


def test_read_device(case_data, log_result):
    read_device(case_data['parameters']['device_id'], debug=True, log_file=log_result)


def main():
    log_file = os.path.join('log', str(datetime.now().strftime("%d%m%Y %H%M%S") ) + '.csv')
    log_result = log_file[0:-4]+' result.csv'
    create_file(log_result, ['result'])
    fieldnames = ['test', 'function', 'description', 'automated', 'parameters', 'expected result', 'begin', 'end']
    create_file(log_file, fieldnames)
    i = 0
    for case in data:
        begin = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        try:
            if case['function'] == 'read_devices':
                test_read_devices(case, log_result)
        except Exception as ex:
            print ex
        end = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        i += 1
        test_number = str(i)
        while len(test_number) < 3:
            test_number = '0' + test_number
        case['test'] = 'TC' + test_number
        case['begin'] = begin
        case['end'] = end
        write_file(log_file, fieldnames, case)


if __name__ == "__main__":
    main()
