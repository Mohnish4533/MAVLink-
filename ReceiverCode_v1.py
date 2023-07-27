from pymavlink import mavutil

the_connection = mavutil.mavlink_connection('/dev/pts/2', baud=57600)

the_connection.wait_heartbeat()

print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_component))

while True:
    try:
        info = the_connection.messages['test_transmission']
        timestamp = the_connection.time_since('test_transmission')
        print("\n", info, timestamp, sep = "\t")
    except:
        continue
