def my_decorator(f):
    def wrapper():
        print("Starting the function now...")
        f()                     # Call the original function
        print("End")            # Added after f()
    return wrapper


@my_decorator
def greet():
    print("Hello")


greet()