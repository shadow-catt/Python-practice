import time
import random

print("Welcome to Self Timer")
print('\n')
print("Everybody stand up")
print("Stay standing until you think the tiome has ended")
print("Then sit dowm")
print("Anyone still standing when the time ends loses")
print("The last person to sit down before the time ended will win")
a=1
time.sleep(a)
stand_time = random.randint(5,20)
print('Standing for',stand_time,'seconds')
time.sleep(stand_time)
print("*****TIME UP*****")
