#If you want to install pyautogui,just copy the fllowing code to the cmd
#pip install pyautogui -i http://pypi.doubanio.com/simple/ --trusted-host pypi.doubanio.com

import pyautogui
import time

# get the size of screen
x,y=pyautogui.size()
print("The size of your screen is {0}*{1}".format(x,y))

time.sleep(2)
#repeat for many times
while 1:
  for a in range(400,x-400):
    for b in range(400,y-400):

      #move the mouse to the point(a,b)
      print("Move to the point ({},{})".format(a,b))
      pyautogui.moveTo(a,b,duration=5)

      #wait for 1700 second(30min - 100s)
      time.sleep(1700)
