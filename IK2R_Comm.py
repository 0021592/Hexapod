import IK.IK.IK as IK
import serial
import struct 
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer() #practic da flush
    while(True):
        
        x = float(input('X:'))
        y = float(input('Y:'))
        z = float(input('Z:'))
        angles = [0, 0, 0]
        angles = IK.RIK3(x, y, z) #RIK3 returneaza 3 valori - unghiurile
        print(x, y, z)
        print(angles[0], angles[1], angles[2])
        if (angles[0] == -1024): #nu exista unghi
            pass
        angles = IK.transform3(angles)
        print(angles[0], angles[1], angles[2])
        ser.write(bytearray(struct.pack("B", 1))) #trimite ce fel de operatie este
        ser.write(bytearray(struct.pack("B", 0))) #trimite adresa servoului
        for i in range(0, 3):
            ser.write(bytearray(struct.pack("f", angles[i])))

    

