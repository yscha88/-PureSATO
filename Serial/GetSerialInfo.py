import serial
import serial.tools.list_ports as sp



def get_serial_list():
    list = sp.comports()
    connected = []

    for i in list:
        connected.append(i.device)

    print("Connected COM posts: " + str(connected))
    return connected


