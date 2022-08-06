
from m5stack import *
from m5ui import *
from uiflow import *
import time
from machine import Pin       #importing classes
from time import sleep    #Import sleep from time class
from m5stack import lcd
from machine import Timer

setScreenColor(0x111111)
 

global RPM, Rtime,end, start, state
start = 0
rev = 0
def handle_interrupt(Pin):
  global rev
  rev += 1 #defining interrupt handling function



PIR_Interrupt=Pin(26,Pin.IN) 
PIR_Interrupt.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt) 

max_RPM = 0

while True:
  wait_ms(500)
  state = machine.disable_irq()
  end = time.ticks_ms()
  Rtime = time.ticks_diff(end, start)
  RPM = int ((rev/Rtime)*60000)
  start = time.ticks_ms()
  rev = 0 
  
  if RPM > max_RPM:
    max_RPM = RPM

  lcd.clear()
  lcd.setCursor(20,20)
  lcd.print("RPM")
  lcd.setCursor(20,40)
  lcd.print(RPM)
  lcd.setCursor(10,80)
  lcd.print("Max RPM")
  lcd.setCursor(20,100)
  lcd.print(max_RPM)
  machine.enable_irq(state)
  
 
