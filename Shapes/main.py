from circle import Circle

# circle_radius = input("Enter the Radius of the Circle: ")

# circle_1 = Circle()

# if circle_radius != "":
#     circle_1.radius = float(circle_radius)

# area = circle_1.area()
# perimeter = circle_1.perimeter()

# print(f"Radius: {circle_1.radius:.2f}\nArea: {area:.2f}\nPerimeter: {perimeter:.2f}")

circles = {}

circle_qty = int(input("Enter the number of circles: "))
for i in range(circle_qty):
    while True:
        try:
            # input 
            circle_radius = input("Enter the Radius of the Circle: ")
            
            # validation
            if circle_radius == "":
                print("Invalid Input. Please Try Again.")
                continue
            
            # convertion
            raidus_value = float(circle_radius)
            
            # creating Object
            circles[i] = Circle(raidus_value)
            
            # output
            area = circles[i].area()
            perimeter = circles[i].perimeter()
            
            print(f"Radius: {circles[i].radius:.2f}\nArea: {area:.2f}\nPerimeter: {perimeter:.2f}")
            break
        except ValueError as e:
            print(f"ValueError: {e}")
        except Exception as e:
            print(f"Error: {e}")