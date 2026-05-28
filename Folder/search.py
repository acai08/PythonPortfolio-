# Annie
# Search
# Generate a random secret number between 1 and 100.

import random

secret_number = random.randint (1, 100)
print (f"The Secret Number is: {secret_number}")

def linear_search():
    global secret_number
    print("--- Starting Linear Search Bot ---")
    attempts = 0
    for guess in range (1, 101):
        if guess == secret_number:
            print (f"The number of attempts is: {attempts}")
        else:
            attempts = attempts + 1

def binary_search():
    low = 1
    high = 100
    found = False
    attempts1 = 0
    while found == False:
        mid = (low + high) // 2
        if mid < secret_number:
            low = mid + 1
            attempts1 = attempts1 + 1
        elif mid > secret_number:
            high = mid - 1
            attempts1 = attempts1 + 1
        else:
            found = True
            break
    print(f"The number of attempts is: {attempts1}")

binary_search()
