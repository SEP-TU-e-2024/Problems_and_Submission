# Dummy code for testing functionality of the IOModule

from validator.validator import Validator

from time import sleep

val = Validator()

total = 0

while True:
    n = val.obtain_data()
    if n == None:
        break
    total += n

sleep(70)

val.push_data(total)