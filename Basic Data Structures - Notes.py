# Notes on Basic Data Structures CLASSES -- LISTS / TUPLES / DICTIONARY

# TUPLES
a = (0, 1, 2, 3)  # Define TUPLE
print("Tuples")
print("===")
print(a)  # Show TUPLE
print(type(a))  # Demonstrate class type
print(a[:3])  # Print first three tuples (SLICING)
print(a[1:])

# This is the example from the review check in the PY0101 module on tuples.
# The answer on the review is incorrect. The correct answer should be "['b', 'c']"
# The example is incorrect in the course
B = ["a", "b", "c"]
print(B[1:])

# Tuple Indexing
tuple1 = ("disco", 10, 1.2)
# "disco", 10, 1.2
#  0        1   2
#  -3       -2  -1
print("Tuple Indexing")
print("===")
print(tuple1)
print(type(tuple1))
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
print(tuple1[-1])
print(tuple1.index("disco")) # Returns the INDEX position of "DISCO". when 'finding' something in a tuple.


# Tuple Concatenate
print("Tuple Concatenate and slicing Exercise")
print("===")
tuple2 = tuple1 + ("hard rock", 10)
print(tuple2)
print("slicing")
print(tuple2[0:3])  # slice from index 0 to index 2 (original tuple1 variable)
print(tuple2[3:5])  # slice from index 2 to 4 ('added' tuple2 variable)
print(len(tuple2))

# Tuples and Sorting
print("Tuples Sorting")
print("===")
Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)
RatingsSorted = sorted(Ratings)  # Create a sorted list.. note you can not change a Tuple and need to create a new
# variable in order to store the result.
print(RatingsSorted)

# Nested Tuples
print("Nested Tuples")
print("===")
NestedT = (1, 2, ("Pop", "Rock"), (3, 4), ("Disco", (1, 2)))
# Print each element of NestedT
print("Each element of tuple")
print(NestedT[0])
print(NestedT[1])
print(NestedT[2])
print(NestedT[3])
print(NestedT[4])
# Print each element on each nested tuple
print("Elements on each index")
print(NestedT[2][0])
print(NestedT[2][1])
print(NestedT[3][0])
print(NestedT[3][1])
print(NestedT[4][0])
print(NestedT[4][1])  # Note that 1,2 is a further nested tuple
print("Elements on the third nested tuple")
print(NestedT[4][1][0])
print(NestedT[4][1][1])
print("First element in the second nested tuple")
print(NestedT[2][1][0])  # Returns 'R' the first element of "Rock", the object in second position of the nested tuple
