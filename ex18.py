def print_two(*args):
    arg1, arg2= args
    print(f"arg1:{arg1} and arg2:{arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1:{arg1} and arg2:{arg2}")

def print_one(args):
    print(f"arg1:{args}")

def print_none():
    print("My name is Soundharya")

print_two("Soundharya","AM")
print_two_again("Huda","komok")
print_one("Soundharya")
print_none()