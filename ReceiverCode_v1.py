from pymavlink import mavutil
from custom import custom_mavlink_1 as mavlink

the_connection = mavutil.mavlink_connection('/dev/pts/6', baud=57600)
#custom_mav = mavlink.MAVLink(None)

the_connection.wait_heartbeat()

print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_component))

while True:
    message = the_connection.recv_match()
    if message != None:
        print(message)
    #custom_mav = mavlink.
    #custom_msg = custom_mav.decode(message.get_payload())
    #print(f"Received MyCustomMessage: field1={custom_msg.message_sent_1}, field2={custom_msg.message_sent_2}")    
