from uiautomator import Device
from adb_utils import read_device
from datetime import datetime
from ui_utils import adb_ui_calculator
from twilio_utils import make_call

make_call("hola hola hola hola hola hola hola hola hola hola hola hola hola hola hola hola hola",
          '+524494269026',
          '+12183327195')
"""
device = Device(read_device())
device.open.notification()
if device(text='New voicemail', className='android.widget.TextView').exists:
    print 'yay'
else:
    print ':c'
"""