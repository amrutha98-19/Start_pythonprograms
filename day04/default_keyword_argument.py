# Function with default argument and keyword argument
# Default Argument -> Uses a default value if no value is provided.
# Keyword Argument -> Passes a value using the parameter name.


def employee(name,job="tester"):

    # Print employee name and role
    print(name,"-",job)

employee("arun") # Uses default argument  # No value is given for 'job',so the default value "tester" is used.
employee("anna",job="devolper") # Uses keyword argument # A value is given using the parameter name 'job', so it overrides the default value.