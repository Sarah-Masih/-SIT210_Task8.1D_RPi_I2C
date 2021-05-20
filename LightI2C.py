import smbus
import time

light_sensor    = 0x23 # I2C address

Power_down = 0x00 # No active state
Power_on   = 0x01 # Power on
Reset     = 0x07 # Reset data register value

# Start measurement at 1lx resolution. Time typically 120ms
#measures at 1lx resolution, time = 120ms
#devices automacally powers down after measuring light
ONE_TIME_HIGH_RES_MODE_1 = 0x20

ONE_TIME_LOW_RES_MODE = 0x23

bus = smbus.SMBus(1)

def Light(addr=light_sensor): #collecting data from sensor
  data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE_1)
  return convertToNumber(data)


def convertToNumber(data): 
  result=(data[1] + (256 * data[0])) / 1.2
  return (result)



def main():
  while True:
    brightness=Light()
    #print(brightness)
    if(brightness>= 660):
        print("Too Bright")
    elif(brightness> 300 and brightness<550):
        print("Bright")
    elif(brightness> 100and brightness<300):
        print("Medium")
    elif(brightness<25 and brightness>10):
        print("Dark")
    elif(brightness<10):
        print("Too Dark");
   
    time.sleep(0.25)

if __name__=="__main__":
   main()
