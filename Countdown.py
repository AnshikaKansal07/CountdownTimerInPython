import time as T
t=int(input("Enter time in seconds: "))
while t:
    minutes, sec= divmod(t,60)
    timer = '{:02d}:{:02d}'.format(minutes, sec)
    print(timer, end='\r')  
    T.sleep(1)
    t -= 1
print("Boom!!")