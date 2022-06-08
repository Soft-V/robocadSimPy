# from robocadSim.robots import festo
# import time
#
#
# robot = festo.Festo()
#
# robot.connect()
#
# robot.right_motor_speed = 10
# robot.left_motor_speed = -10
#
# time.sleep(1)
#
# while robot.ir_1 > 14:
#     pass
#
# robot.right_motor_speed = 0
# robot.left_motor_speed = 0
# robot.back_motor_speed = 0
#
# time.sleep(5)
#
# robot.right_motor_speed = 8
# robot.left_motor_speed = 8
# robot.back_motor_speed = 8
#
# while robot.imu >= -90:
#     pass
#
# robot.right_motor_speed = 0
# robot.left_motor_speed = 0
# robot.back_motor_speed = 0
#
# time.sleep(5)
#
# robot.grip_servo_pos = -1
# time.sleep(3)
# robot.grip_servo_pos = 1
# time.sleep(3)
#
# robot.right_motor_speed = 0
# robot.left_motor_speed = 0
# robot.back_motor_speed = 0
#
# time.sleep(1)
#
# robot.disconnect()
