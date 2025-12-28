import IK
import serial 
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer() #practic da flush
    while(True):
        x = float(input('X:'))
        y = float(input('Y:'))
        z = float(input('Z:'))
        angles = []
        angles = IK.RIK3(x, y, z) #RIK3 returneaza 3 valori - unghiurile
        if (angles[0] == -1): #nu exista unghi
            pass
        angles = IK.transform3(angles)
        for i in range(0, 3):
            serial.write(angles[i].encode('utf-8'))

    

