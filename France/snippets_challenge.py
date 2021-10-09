print("Challenge 3.1: Debug code snippets")
#Debug in order each snippet

print()

print("Code Snippet 1:")

u = 5
v = 2
#I had changed to the equal comparison operator
if u * v == 10:
    print(f"The product of u ({u}) and v ({v}) is 10")
else:
    print(f"The product of u ({u}) and v ({v}) is not 10")

print()

print("Code Snippet 2:")
x = 15
y = 25

z = 30
# i had to add a colon to line 27 and line 30
if z < x:
    print("z is less than x")

elif z > x and z < y:
    print("z is between x and y")

else:
    print("z is greater than y")


print()

print("Code Snippet 3:")

#i had to modify the comparison operator below so the assert statement passes
# i had to update the print statement to reflect changes to the code

a = 1
b = 1
c = (a == b)

print(f"The value of c ({c}) is True since a ({a}) is greater than b ({b}). I changed the comparitive operater to two equal signs.")
assert(c == True) #Do not change this line

print()

print("Code Snippet 4:")

# i had to change one boolean operator in the assignment of d, so that d evaluates to False

d = (5 > 7) or not (8 < 20)
# TO DO: Explain how d is set to False in a print statement
assert(d == False) #Do not change this line
print('In order to make the statement false, I had to change the first comperative operater from less then sign to greater then sign.')
print()


print("Code Snippet 5:")

#make comparison operator so o evalutes to true
# i updated the print statement to reflect the changes

m = "GOAT"
n = "goat"

o = (m != n)

print (f"The value of o ({o}) is True since Python is case-sensitive. In order to make statement true, I had to place exclamation mark in front of the equal sign.")
assert(o == True) #Do not change this line

print()
print("CHALLENGE COMPLETE!")
