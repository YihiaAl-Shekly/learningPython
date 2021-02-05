# some PID math

# the PID vals
# proportional for the present error
p = 8
# integrator for the past error
i = 0.1
# derivative for the future error
d = 15

# the angle that i want the airplane to fly at
intendedVal = float(50)  # from input
# the angle that the airplane is actual flying at
actualVal = float(0)  # from input

error = intendedVal - actualVal
oldError = error - 1  # idk how to calculate it yet
time = float(1)  # need to be calculated
# control surface control ( elevator for ex)
pid_i = 0.0  # just for python not to be mad

# the pid math
pid_p = error * p
pid_i = pid_i + (i * error)
pid_d = (d * oldError / time)
elevatorAngle = pid_p + pid_i + pid_d
