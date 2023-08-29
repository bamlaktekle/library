#Bamlak Tekle
#Date: 09/26/22
#Class Section: 8
#Assignment#3
#problem 2

#ask the user to input the length for the sides three times (shortest to longest)
shortside= int(input("Enter the length of the shortest side: "))
interside= int(input("Enter the length of the intermediate side: "))
longside= int(input("Enter the length of the longest side: "))
#use the if and else function
#if all sides are equal, print that it is an equilateral triangle
#use math equations to calculate the area for the right and equilateral triangles
if shortside==interside==longside:
    print("It is an equilateral triangle")
    equiarea= (3**0.5)*(shortside**2)/4
    print(equiarea)
elif longside**2==(interside**2) + (shortside**2):
    print("It is a right triangle")
    rightarea= 0.5*(shortside*interside)
    print(rightarea)
elif longside>=shortside+interside:
    print("It is not valid triangle")
else:
    print("It is a valid triangle, but not a right triangle or an equilateral triangle")
    
