import serial
import time

from serial.tools.list_ports import comports


ports = zip(*comports())[0]


def get_open_port():
    for port in ports:
        try:
            ser = serial.Serial(port, 38400, timeout=1)
            time.sleep(2)
            print "opening port %s" % port
            ser.write(".")
            line = ser.readline()
            ser.close()
            return port, line
        except:
            pass

if __name__ == '__main__':
    port, line = get_open_port()
    print "test:", line
