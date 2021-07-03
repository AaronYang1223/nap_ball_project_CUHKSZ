import RPi.GPIO as GPIO
import time
import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate(r'/boot/exalted-skein-310719-7cda86669645.json') # The secret key for connecting with google firebase
firebase_admin.initialize_app(cred)

db = firestore.client() #Initialize google cloud platform

TRIG = 11  #send-pin
ECHO = 12  #receive-pin

def setup(): # Set up the connection between Raspberry Pi and the sensors
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(TRIG, GPIO.OUT, initial = GPIO.LOW)
    GPIO.setup(ECHO, GPIO.IN)

def distance(): # Return the value of the detected real-time distance 

    GPIO.output(TRIG, 1) 
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)

    
    while GPIO.input(ECHO) == 0:  
        pass
    time1 = time.time()  
    

    while GPIO.input(ECHO) == 1:  
        pass
    time2 = time.time() 

    during = time2 - time1   

    return during * 340 / 2 * 100  

def firebase(): # The main function to send real-time data to firebase
    sequenceNumber = 1 # Original sequence_number
    while True:

            dis1 = distance() # Get 5 latest real-time distances that are valid (<=200) 
            if dis1 > 200:
                time.sleep(0.04)
                continue   # If not valid, detect again until the distance is in the range of valid distance 
            
            time.sleep(0.04)

            dis2 = distance()
            if dis2 > 200:
                time.sleep(0.04)
                continue
            
            time.sleep(0.04)

            dis3 = distance()
            if dis3 > 200:
                time.sleep(0.04)
                continue

            time.sleep(0.04)

            dis4 = distance()
            if dis4 > 200:
                time.sleep(0.04)
                continue

            time.sleep(0.04)

            dis5 = distance()
            if dis5 > 200:
                time.sleep(0.04)
                continue

            time.sleep(0.04)
            
            average_dis=(dis1+dis2+dis3+dis4+dis5)/5  # Take average of every five distances detected to make the distances more accurate

            print('status1',average_dis, 'cm')
            
            if average_dis >= 59 or average_dis <= 54: # The distance is out of range (there's something or somebody in the nap-ball).

                print("occupy")

                print('sequence_number',sequenceNumber)

                sequenceNumber_str = str(sequenceNumber)
                A = time.time()
                B = time.localtime(A)
                X = time.strftime('%Y-%m-%d %H:%M:%S', B) # Get the time 


                Y = time.strftime('%Y', B)
                m = time.strftime('%m', B)
                d = time.strftime('%d', B)
                H = time.strftime('%H', B)
                M = time.strftime('%M', B)
                S = time.strftime('%S', B)

                Y_1 = int(Y)
                m_1 = int(m)
                d_1 = int(d)
                H_1 = int(H)
                M_1 = int(M)
                S_1 = int(S) # Convert the format of time into integer for conveniently computing


                doc_ref = db.collection(u'monitor').document(sequenceNumber_str)
                doc_ref.set({
                    u'sequence_number': sequenceNumber,
                    u'start_time_1': Y_1,
                    u'start_time_2': m_1,
                    u'start_time_3': d_1,
                    u'start_time_4': H_1,
                    u'start_time_5': M_1,
                    u'start_time_6': S_1,   
                    u'end_time_1': u'x',
                    u'end_time_2': u'x',
                    u'end_time_3': u'x',
                    u'end_time_4': u'x',
                    u'end_time_5': u'x',
                    u'end_time_6': u'x', 
                    u'duration': 0,
                    u'status': u'occupied'})  # Send the data to firebase
                
                print("occupy1, update")
                
                while True:

                    dis1 = distance()
                    if dis1 > 200:
                        time.sleep(0.04)
                        continue
                    
                    time.sleep(0.04)

                    dis2 = distance()
                    if dis2 > 200:
                        time.sleep(0.04)
                        continue
                    
                    time.sleep(0.04)

                    dis3 = distance()
                    if dis3 > 200:
                        time.sleep(0.04)
                        continue

                    time.sleep(0.04)

                    dis4 = distance()
                    if dis4 > 200:
                        time.sleep(0.04)
                        continue

                    time.sleep(0.04)

                    dis5 = distance()
                    if dis5 > 200:
                        time.sleep(0.04)
                        continue

                    time.sleep(0.04)
                    
                    average_dis=(dis1+dis2+dis3+dis4+dis5)/5

                    print(average_dis, 'cm')
                    print("status2, occupy")
                    print('sequence_number',sequenceNumber)

                    time.sleep(3.0)

                    if not(average_dis >= 59 or average_dis <= 54):

                        print("occupy-free")  # Convertion of status
                        break

                C = time.time()
                D = time.localtime(C)
                Z = time.strftime('%Y-%m-%d %H:%M:%S', D)
                print(X)
                print(Z)
                D1 = datetime.datetime.strptime(str(X),'%Y-%m-%d %H:%M:%S')
                D2 = datetime.datetime.strptime(str(Z),'%Y-%m-%d %H:%M:%S')
                delta = D2 - D1
                print(delta)
                string = str(delta)
                X1= string[0]
                X2= string[2:4]
                X3= string[5:]
                print(X1,X2,X3)
                X4 = int(X1)
                X5 = int(X2)
                X6 = int(X3)
                X7 = X6 + 60*X5 + 3600*X4 # Convert the unit of time to seconds

                Y_ = time.strftime('%Y', D)
                m_ = time.strftime('%m', D)
                d_ = time.strftime('%d', D)
                H_ = time.strftime('%H', D)
                M_ = time.strftime('%M', D)
                S_ = time.strftime('%S', D)

                Y_2 = int(Y_)
                m_2 = int(m_)
                d_2 = int(d_)
                H_2 = int(H_)
                M_2 = int(M_)
                S_2 = int(S_)

                doc_ref = db.collection(u'monitor').document(sequenceNumber_str)
                doc_ref.set({
                    u'sequence_number': sequenceNumber,
                    u'start_time_1': Y_1,
                    u'start_time_2': m_1,
                    u'start_time_3': d_1,
                    u'start_time_4': H_1,
                    u'start_time_5': M_1,
                    u'start_time_6': S_1,  
                    u'end_time_1': Y_2,
                    u'end_time_2': m_2,
                    u'end_time_3': d_2,
                    u'end_time_4': H_2,
                    u'end_time_5': M_2,
                    u'end_time_6': S_2,  
                    u'duration_1': X4,
                    u'duration_2': X5,
                    u'duration_3': X6,
                    u'duration': X7,
                    u'status': u'occupied'})   

                print("occupy_update")             

                sequenceNumber+=1 
                print('sequence_number',sequenceNumber)

            else: # another initial status (free)

                print("free")

                print('sequence_number',sequenceNumber)

                sequenceNumber_str = str(sequenceNumber)

                A = time.time()
                B = time.localtime(A)
                X = time.strftime('%Y-%m-%d %H:%M:%S', B)


                Y = time.strftime('%Y', B)
                m = time.strftime('%m', B)
                d = time.strftime('%d', B)
                H = time.strftime('%H', B)
                M = time.strftime('%M', B)
                S = time.strftime('%S', B)

                Y_1 = int(Y)
                m_1 = int(m)
                d_1 = int(d)
                H_1 = int(H)
                M_1 = int(M)
                S_1 = int(S)

                doc_ref = db.collection(u'monitor').document(sequenceNumber_str)
                doc_ref.set({
                    u'sequence_number': sequenceNumber,
                    u'start_time_1': Y_1,
                    u'start_time_2': m_1,
                    u'start_time_3': d_1,
                    u'start_time_4': H_1,
                    u'start_time_5': M_1,
                    u'start_time_6': S_1,   
                    u'end_time_1': u'x',
                    u'end_time_2': u'x',
                    u'end_time_3': u'x',
                    u'end_time_4': u'x',
                    u'end_time_5': u'x',
                    u'end_time_6': u'x', 
                    U'duration': 0,
                    u'status': u'free'})
                
                while True:

                    dis1 = distance()
                    if dis1 > 200:
                        time.sleep(0.04)
                        continue
                    
                    time.sleep(0.04)

                    dis2 = distance()
                    if dis2 > 200:
                        time.sleep(0.04)
                        continue
                    
                    time.sleep(0.04)

                    dis3 = distance()
                    if dis3 > 200:
                        time.sleep(0.04)
                        continue

                    time.sleep(0.04)

                    dis4 = distance()
                    if dis4 > 200:
                        time.sleep(0.04)
                        continue

                    time.sleep(0.04)

                    dis5 = distance()
                    if dis5 > 200:
                        time.sleep(0.04)
                        continue

                    time.sleep(0.04)
                    
                    average_dis=(dis1+dis2+dis3+dis4+dis5)/5

                    print(average_dis, 'cm')
                    print("status3, free")
                    print('sequence_number',sequenceNumber)

                    time.sleep(3.0)

                    if average_dis >= 59 or average_dis <= 54:
                        print("free-occupy")
                        break

                C = time.time()
                D = time.localtime(C)
                Z = time.strftime('%Y-%m-%d %H:%M:%S', D)
                print(X)
                print(Z)
                D1 = datetime.datetime.strptime(str(X),'%Y-%m-%d %H:%M:%S')
                D2 = datetime.datetime.strptime(str(Z),'%Y-%m-%d %H:%M:%S')
                delta = D2 - D1
                print(delta)
                string = str(delta)
                X1= string[0]
                X2= string[2:4]
                X3= string[5:]
                print(X1,X2,X3)
                X4 = int(X1)
                X5 = int(X2)
                X6 = int(X3)
                X7 = X6 + 60*X5 + 3600*X4

                Y_ = time.strftime('%Y', D)
                m_ = time.strftime('%m', D)
                d_ = time.strftime('%d', D)
                H_ = time.strftime('%H', D)
                M_ = time.strftime('%M', D)
                S_ = time.strftime('%S', D)

                Y_2 = int(Y_)
                m_2 = int(m_)
                d_2 = int(d_)
                H_2 = int(H_)
                M_2 = int(M_)
                S_2 = int(S_)

                doc_ref = db.collection(u'monitor').document(sequenceNumber_str)
                doc_ref.set({
                    u'sequence_number': sequenceNumber,
                    u'start_time_1': Y_1,
                    u'start_time_2': m_1,
                    u'start_time_3': d_1,
                    u'start_time_4': H_1,
                    u'start_time_5': M_1,
                    u'start_time_6': S_1,  
                    u'end_time_1': Y_2,
                    u'end_time_2': m_2,
                    u'end_time_3': d_2,
                    u'end_time_4': H_2,
                    u'end_time_5': M_2,
                    u'end_time_6': S_2,  
                    u'duration_1': X4,
                    u'duration_2': X5,
                    u'duration_3': X6,  
                    u'duration': X7,                                      
                    u'status': u'free'})                       

                sequenceNumber+=1 

                    
def destroy(): # Interrupt the process
    GPIO.cleanup()

if __name__ == "__main__":
    setup()
    try:
        firebase()
    except KeyboardInterrupt:
        destroy() 