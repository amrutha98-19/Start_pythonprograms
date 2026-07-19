# *args -> accepts multiple positional arguments
        # -> Multiple positional arguments
        # -> Stored as a tuple
        # ->Example: 10, 20, 30
        # ->Values only.

# **kwargs -> accepts multiple keyword arguments
        # -> Multiple keyword arguments
        # -> Stored as a dictionary
        # ->Example:   name="anna", job="django developer"
        # ->key=value pairs..


def total(*numbers):
    print("sum:",sum(numbers))
total(10,20,30)

def profile(**data):
    print(data)
profile(name="anna",job="django devolper")