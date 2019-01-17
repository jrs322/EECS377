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
    DELAY = .01
    pi1 = pigpio.pi()
    pi1.set_PWM_range(9, 100)
    #turn all off
    pi1.write(19,0)
    pi1.write(13,0)
    pi1.write(26,0)
    time.sleep(1)
    #begin ramping R value
    pi1.write(19,1)
    pi1.set_PWM_range(19, 100)
    for i in range(9,100):
        pi1.set_PWM_dutycycle(19,i)
        time.sleep(DELAY)
    for j in range(100, 9, -1):
        pi1.set_PWM_dutycycle(19 , i)
        time.sleep(DELAY)
    pi1.write(19,0)
    time.sleep(1)
    #begin ramping up the green led
    pi1.write(13,1)
    pi1.set_PWM_range(13, 100)
    for i in range(9,100):
        pi1.set_PWM_dutycycle(13,i)
        time.sleep(DELAY)
    for j in range(100, 9, -1):
        pi1.set_PWM_dutycycle(13 , i)
        time.sleep(DELAY)
    pi1.write(13,0)
    time.sleep(1)
    #begin ramping up the blue led
    pi1.write(26,1)
    pi1.set_PWM_range(26, 100)
    for i in range(9,100):
        pi1.set_PWM_dutycycle(26,i)
        time.sleep(DELAY)
    for j in range(100, 9, -1):
        pi1.set_PWM_dutycycle(26 , i)
        time.sleep(DELAY)
    pi1.write(26,0)
    time.sleep(1)
    #begin ramping up the white led which is a mix of all
    pi1.write(26,1)
    pi1.write(19,1)
    pi1.write(13,1)    
    for i in range(9,100):
        pi1.set_PWM_dutycycle(26,i)
        pi1.set_PWM_dutycycle(19,i)
        pi1.set_PWM_dutycycle(13,i)        
        time.sleep(DELAY)
    for j in range(100, 9, -1):
        pi1.set_PWM_dutycycle(26,i)
        pi1.set_PWM_dutycycle(19,i)
        pi1.set_PWM_dutycycle(13,i)
        time.sleep(DELAY)
    pi1.write(26,0)
    time.sleep(10)
def main():
    while True:
        loop()
if __name__ == "__main__":
    main()
