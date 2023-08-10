from pymavlink import mavutil
from custom import custom_mavlink_1 as mavlink 

the_connection = mavutil.mavlink_connection('/dev/pts/5', baud=57600)

the_connection.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_GCS, mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)

while True:
    a = int(input("Testcase1: "))
    b = int(input("Testcase2: "))
    
    msg = mavlink.MAVLink_test_transmission_message(message_sent_1= a, message_sent_2= b)
    
    #print("{:x}".format(msg), end= "\n\n")
    M = msg.pack(the_connection.mav)
    print(["{:x}".format(x) for x in M], end = "\n\n")
    the_connection.write(msg.pack(the_connection.mav))

    c = input("Do u want to contiue(y/n): ")
    if c == "n":
        break
