# Dummy code for testing functionality of the IOModule

from validator.validator import Validator

val = Validator()

total = 0

while False:
    n = val.obtain_data()
    if n == None:
        break
    total += n

val.push_data(total)