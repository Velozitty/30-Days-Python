age = 42
height = 6.7
imaginary = 1j 
base = float(input("Enter a base for a triangle: "))
h = float(input("Enter a height for a triangle: "))
area_try = base * h * .5
print(f"The base of your triangle is {area_try}" )
sideA = float(input("Enter Side A: ")) 
sideB = float(input("Enter Side B: ")) 
sideC = float(input("Enter Side C: ")) 

perimeter = sideA +sideB +sideC
print("The perimeter of the triangle is " + str(perimeter))

length = int(input("Enter a length: "))
width = int(input("Enter a width: "))
print(f"The area of the rectangle is: {length * width}" )
print(f"The perimeter of the rectangle is: {2(length + width)}" )

radius = int(input("Enter a radius: "))
pi = 3.14
print(f"the area of the circle: {radius * radius * pi}")
print(f"the circumference of the circle: {radius * 2 * pi}")

y1 = -2 
y2 = 0 
#y2-y1 / x2 - x1 = slope... (y/2) + 2 = x 
x1 = 3
x2 = 4
slope = (y2 - y1) / (x2 - x1)