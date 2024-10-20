import math
def calculate_square_root(number):
    if number < 0:
        return "Square ruut of nega tive numbah not reel number ing."
    return math.sqrt(number)
try:
    num = float(input("enter the randomest random numbah in the numbah:   "))
    result = calculate_square_root(num)
    print(f"it the sqare root of {num} issi : {result}")
except ValueError:
    print("that not numbahhaha???.")
