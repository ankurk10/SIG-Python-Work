side_one = input("Enter the length of the first side ")
side_two = input("Enter the length of the second side ")
side_three = input("Enter the length of the third side ")
if side_one == side_two == side_three :
    print("The triangle is an equilateral triangle")

elif side_one == side_two or side_one == side_three or side_two == side_three :
     print("The triangle is an isocesles triangle")

else :
    print("The triangle is a scalen triangle")

