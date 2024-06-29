#logica ck - hecktor 6/28/2024
import colorama
from colorama import Cursor
import time
colorama.init()

for  i in  range (10):
    print ("*", end="")
time.sleep(0.2)
 
for j  in range (10):
    print ()
    for i in range (10):
        if i ==9:
            print ("*", end="")
 
        else:
            print (" ", end="")
time.sleep(0.3)


for i  in range(10):
    print ("\b\b", end="")
    print ("*", end="")
 
    # Mover el cursor 2 líneas hacia arriba
print ("\b\b", end="")
time.sleep(0.1)

for i in range (10):
    print(Cursor.UP(1), end='')
    print ("\b\b", end="")
    print ("*", end =" ")
print()
time.sleep(0.5)
for i in range (8):
    print ("*", end ="")
    time.sleep(0.1)






 
 




