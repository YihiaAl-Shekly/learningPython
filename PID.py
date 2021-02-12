"""
PID Class
a specific class for controlling UAV control_surfaces

"""

"""
how to tune the PID values manually 
    increase the d until the position (error) is stable (not changing a lot)
    increase the p slowly  until the error is almost to 0 (+or- 5ish%)
    increase the i by relatively very small increment until the error is 0
"""


def calc(intended_Val, actual_Val, time):

    # the PID values
    # proportional for the present error
    p = 8
    # integrator for the past error
    i = 0.1
    # derivative for the future error
    d = 15

    # the angle that i want the airplane to fly at
    #intended_Val # from input
    # the angle that the airplane is actual flying at
    #actual_Val # from input

    error = intended_Val - actual_Val
    old_Error = error - 1  # idk how to calculate it yet
    #time  # need to be calculated
    # control surface control ( elevator for ex)
    pid_i = 0.0  # just for python not to be mad

    # the pid math
    pid_p = error * p
    pid_i = pid_i + (i * error)
    pid_d = (d * old_Error / time)
    # the sum is the output
    PID_out = pid_p + pid_i + pid_d

    # the pid val should never be more that the motor output (so we need to implement filters)
    if PID_out > 2000:  # 2000 is the highest value
        PID_out = 2000
    if PID_out < 1000:  # 1000 is the lowest value
        PID_out = 1000
    # there should be a filter for unexpected error values (noise) for the PID_d <<


