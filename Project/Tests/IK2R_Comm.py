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
        angles = RIK3(x, y, z) #RIK3 returneaza 3 valori - unghiurile
        if (angles[0] == -1): #nu exista unghi
            pass
        #am impresia ca q2 e flipped...
        print(angles[0], ' ', angles[1], ' ', angles[2], '\n') #imi da output intre pi si -pi 

    

