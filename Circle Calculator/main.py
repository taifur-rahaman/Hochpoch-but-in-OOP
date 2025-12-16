from circle import Circle

circles = {} # empty dictionary to store circle objects

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
            
            # conversion
            radius_value = float(circle_radius)
            
            # creating Object
            circles[i] = Circle(radius_value)
            
            # calculation
            area = circles[i].area()
            perimeter = circles[i].perimeter()
            
            # output
            print(f"Radius: {circles[i].radius:.2f}\nArea: {area:.2f}\nPerimeter: {perimeter:.2f}")
            break
            
        except ValueError as e:
            print(f"ValueError: {e}")
        except Exception as e:
            print(f"Error: {e}")
