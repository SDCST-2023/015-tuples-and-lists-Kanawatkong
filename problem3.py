#! python3
"""
Ask the user to enter a maximum of 10 positive integers.
After each entry, add the number to a list
If the entry is -1 then stop adding numbers to the list
Sort the list and display the highest number added

inputs:
as many integers as needed

outputs:
Display the largest number:

examples:
Enter an integer:3
Enter an integer:2
Enter an integer:8
Enter an integer:92
Enter an integer:48
Enter an integer:13
Enter an integer:24
Enter an integer:-1

The largest number you entered is 92
"""

List = (3, 2, 8, 92, 48, 13, 24, -1, 5, 79)

print(List[0])
print(List[1])
print(List[2])
print(List[3])
print(List[4])
print(List[5])
print(List[6])
print(List[7])
print(List[8])
print("The largest number you entered is ",end="")
print(List[3])