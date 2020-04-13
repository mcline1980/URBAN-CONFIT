# Basic String Operations

number_string = "0123456"
# Remember number_string is a STRING value representing the index values
# 0123456
# 0123456 index values

# String Operations Slicing using the defined numbers
# When determining what to print. Slicing does not return the last index. I.E, index 2 will only return 0 through 1.
print("Slicing")
print("===")
print(number_string[0:2])  # Print the first two characters. Starting at index 0 to include index 0,1, but not 2.
print(number_string[0:3])  # Print the first three characters. Starting at index 0 to include index 0,1,2, but not 3.
print(number_string[1:1])  # Print the first  characters after '1'. Starting at index '1' print up to index 1. - null
print(number_string[1:2])  # Print the first characters after '1' to include index 0,1, but not 2.

# String Operations Stride
print("Stride Method")
print("===")
print(type(number_string))  # Display String Type
print(number_string[::2])  # Return every second character

# String Operations Find
# Note that find locates and returns the INDEX value of the first character of the requested string.
# Not the string itself.
print("Find Method")
print("===")
print(number_string.find('1'))  # Find '1' in the string. Return index location.
print(number_string.find('3'))  # Find '3' in the string. Return index location.
string_a = "Gus" # To demonstrate using characters other than numbers.
# Gus
# 012 <- index values
print(string_a.find('G'))  # Note that 'G' finds and returns the index location of 'G' in the string.
print(string_a.find('us'))  # finds 'us' in the string and returns the index value of the first char 'u' in string_a
test_a = string_a.find('G')
print(type(test_a))  # Note that the value returned is an integer


# Test String test_string = "Gus Keller"
test_string = "Gus Keller"
# Gus Keller
# 0123456789


# String Operations. CASE methods
print("String Operations. Upper Method")
print("===")
print(test_string)
a = test_string  # set temp variable 'a' to the test_string
b = a.upper()  # set temp variable 'b' to a only all upper case
print(b)  # print variable 'b'
print(a.upper())  # print variable 'a' all upper

# String Operations. REPLACE method
print("String Operations. Replace Method")
print("===")
print(test_string)
a = test_string
print(a.replace('Gus', 'Matt'))  # Replace 'Gus' in test_string (assigned to 'a') with 'Matt'
print(a)  # Note that the above method did NOT change variable 'a'

# String Operations. FIND method
print("String Operations. Find Method")
print("===")
print(test_string)
a = test_string
print(a.find('Gus'))  # Returns the INDEX value of the location of the first substring element (Gus) is at 0
print(a.find('Kel'))  # Will return 4
print(a.find('JDS'))  # Will return -1

# String Operations. ESCAPE character and formatting uses.
# \ is a backslash. It is the escape character. Not /.
print("String Operations. Escape character.")
print ("\\") # Prints \
print("Gus \nKeller") # Prints Gus and Keller on two different lines
