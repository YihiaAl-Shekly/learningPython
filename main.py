# some PID math

# the PID vals
# proportional for the present error
p = 2
# integrator for the past error
i = 1
# derivative for the future error
d = 0.1

# the angle that i want the airplane to fly at
intendedVal = float(50)
# the angle that the airplane is actual flying at
actualVal = float(0)

error = intendedVal - actualVal
oldError = error - 1
time = float(1)
# control surface control ( elevator for ex)
pid_i = 0.0  # just for python not to be mad
pid_p = error * p
pid_i = pid_i + (i * error)
pid_d = (d * oldError / time)
elevatorAngle = pid_p + pid_i + pid_d
