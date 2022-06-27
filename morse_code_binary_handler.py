import RPi.GPIO as GPIO
import time
from morse_binary_conventions import letters

letters = {
    "A" : [0, 1],
    "B" : [1,0,0,0],
    "C" : [1,0,1,0],
    "D" : [1,0,0],
    "E" : [0],
    "F" : [0,0,1,0],
    "G" : [1,1,0],
    "H" : [0,0,0,0],
    "I" : [0,0],
    "J" : [0,1,1,1],
    "K" : [1,0,1],
    "L" : [0,1,0,0],
    "M" : [1,1],
    "N" : [1,0],
    "O" : [1,1,1],
    "P" : [0,1,1,0],
    "Q" : [1,1,0,1],
    "R" : [0,1,0],
    "S" : [0,0,0],
    "T" : [1],
    "U" : [0,0,1],
    "V" : [0,0,0,1],
    "W" : [0,1,1],
    "X" : [1,0,0,1],
    "Y" : [1,0,1,1],
    "Z" : [1,1,0,0],
    "1" : [0,1,1,1,1],
    "2" : [0,0,1,1,1],
    "3" : [0,0,0,1,1],
    "4" : [0,0,0,0,1],
    "5" : [0,0,0,0,0],
    "6" : [1,0,0,0,0],
    "7" : [1,1,0,0,0],
    "8" : [1,1,1,0,0],
    "9" : [1,1,1,1,0],
    "0" : [1,1,1,1,1],
    " " : [2],
}

def led_control(time_sleep):
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(time_sleep)
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(0.5)


PIN = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)

word = str(input("Write a word: "))
word = list(word.upper())

for letter in word:
    time.sleep(3)
    bin_letter = letters[letter]
    print(bin_letter)
    for number in bin_letter:
        if number == 1:
            led_control(0.5)
        elif number == 0:
            led_control(0.2)
        else:
            time.sleep(1)

GPIO.cleanup()