import time
import datetime

f = datetime.datetime.utcnow()
print(str(f) + " UTC")

with open("C:/Users/arodriguez/Documents/elevator.csv", "a+", newline="") as file:
    print(file.read())
    
    
    