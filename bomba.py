import sys
import time

i = int(sys.argv[1]) 
while i > 0:
    print(i)
    time.sleep(1)
    i -= 1
print("!!!!!!!!BOOM!!!!!!!!!")
print("You are dead") 