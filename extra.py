#area of triangle 
b = float(input ("enter value of base:"))
h = float(input("enter value of height:" ))
area= 1/2*b*h
print (f"the area is {area}cm")
#area of square 
def square_area(width, height):
    area = width * height 
    return area

result= square_area(5,10)
print (f"the area is {result}")