#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.iodevices import I2CDevice, LUMPDevice
from pybricks.parameters import Port
from pybricks.ev3devices import Motor
from pybricks.robotics import DriveBase
from pybricks.ev3devices import UltrasonicSensor, ColorSensor
from pybricks.parameters import Stop, Direction
from pybricks.tools import wait

# Initialize the EV3
ev3 = EV3Brick()

sensorLinha = LUMPDevice(Port.S4)
valoresSensorLinha = sensorLinha.read(2)

# sensores do vendra
# cor do sensor da esquerda do meio
def CorEsquerdaVendra():
    return sensorLinha.read(2)[1]

# cor do sensor da esquerda extrema
def CorEsquerdaEXvendra():
    return sensorLinha.read(2)[0]

# cor do sensor da direita do meio
def CorDireitaVendra():
    return sensorLinha.read(2)[2]

# cor do sensor da direita extrema
def CorDireitaEXvendra():
    return sensorLinha.read(2)[3]

print(valoresSensorLinha)
print(CorDireitaVendra())

# o index 0 é o da direita

motor_d_esquerdo = Motor(Port.A, Direction.COUNTERCLOCKWISE) #horario
motor_a_direito = Motor(Port.B, Direction.CLOCKWISE) #antihorario

robot = DriveBase(motor_a_direito, motor_d_esquerdo, 50, 123)


#     motorDireito=motor_d,
#     motorEsquerdo=motor_a,
#     diametroRoda=50,
#     distanciaEntreAsRodas=123
# )

# # Initialize the motors.
# left_motor = Motor(Port.B)
# right_motor = Motor(Port.C)

# # Initialize the color sensor.
# line_sensor = ColorSensor(Port.S3)

# # Initialize the drive base.
# robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Calculate the light threshold. Choose values based on your measurements.
BLACK = 9
WHITE = 85
threshold = (BLACK + WHITE) / 2

# Set the drive speed at 100 millimeters per second.
DRIVE_SPEED = 100

# Set the gain of the proportional line controller. This means that for every
# percentage point of light deviating from the threshold, we set the turn
# rate of the drivebase to 1.2 degrees per second.

# For example, if the light value deviates from the threshold by 10, the robot
# steers at 10*1.2 = 12 degrees per second.
PROPORTIONAL_GAIN = 5

# Start following the line endlessly.
while True:
    # Calculate the deviation from the threshold.
    deviation = CorDireitaVendra() - threshold

    # Calculate the turn rate.
    turn_rate = PROPORTIONAL_GAIN * deviation

    # Set the drive base speed and turn rate.
    robot.drive(DRIVE_SPEED, turn_rate)

    # You can wait for a short time or do other things in this loop.
    wait(10)
