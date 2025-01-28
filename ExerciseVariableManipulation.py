#I Hope this works....

# Exercise: Variable Manipulation
# Initialize three variables of different types: int, float, and str
# Use both camel case and underscore notation for variable names
int_variable = 10
float_variable = 3.14
str_variable = "Hello, World!"

# Print the initial values of the variables
print("Initial values:")
print("int_variable:", int_variable)
print("float_variable:", float_variable)
print("str_variable:", str_variable)

# Update the values of the variables
int_variable_camelCase = int_variable + 5
float_variable_underscore = float_variable * 2
str_variable_camelCase = str_variable + " Updated"

# Print the updated values
print("\nUpdated values:")
print("int_variable_camelCase:", int_variable_camelCase)
print("float_variable_underscore:", float_variable_underscore)
print("str_variable_camelCase:", str_variable_camelCase)

# Change the type of the variable from str to int
# Note: This is just an example; the conversion might not be suitable for all cases
str_to_int_variable = int(float_variable_underscore)

# Print the final values after type conversion
print("\nFinal values after type conversion:")
print("int_variable_camelCase:", int_variable_camelCase)
print("float_variable_underscore:", float_variable_underscore)
