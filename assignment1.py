import pigpio
import time
#runs a loops that completes the assignment
#- turns off all leds
# delay 1 second
# over 1 second ramp up R, G, B values then back down
# over 1 second ramp W values up then down
#loop again
#red is pin 13
#green is pin 19
#blue is pin 26
def loop():
    DELAY =
    pi1 = pigpio.pi()
    pi1.set_PWM_range(9, 100)
    #turn all off
    pi1.write(13,0)
    pi1.write(19,0)
    pi1.write(26,0)
    time.sleep(1)
    #begin ramping R value
    for i in range(9,100):
        pi1.set_PWM_dutycycle(i)
        time.sleep(DELAY)
