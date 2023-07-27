from pymavlink import mavutil

the_connection = mavutil.mavlink_connection('/dev/pts/1', baud=57600)

the_connection.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_GCS, mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)
