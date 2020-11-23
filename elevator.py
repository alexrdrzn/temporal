import time
import csv
import datetime
import os
from gpiozero import Button


up = Button(23, pull_up=True, bounce_time=0.1)
down = Button(24, pull_up=True, bounce_time=0.1)
state = "RUNNING"

def pressed():
    toCSV = ["3", "06:45"]
    with open("settings/elevator.csv", "a+", newline="") as file:
        writerCSV = csv.writer(file)
        writerCSV.writerow(toCSV)
    return

up.when_pressed = pressed
down.when_pressed = pressed

def main():
    try:
        if not os.path.exists("settings/elevator.csv"):
            with open("settings/elevator.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Triggered", "Time"])
                writer.writerow(["2", "05:29"])


        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("Bye")

if __name__ == __name__ == "__main__":
    main()   