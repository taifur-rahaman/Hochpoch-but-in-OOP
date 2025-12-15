# Circle Calculator

A Python program that calculates the area and perimeter of multiple circles using object-oriented programming. The program includes robust input validation, custom property setters, and comprehensive error handling.

## Features

1. **Multiple Circle Processing**
   - Create and calculate properties for multiple circles in one session.
   - Each circle is stored as an object in a dictionary for easy access.
   - User specifies how many circles to process.

2. **Circle Class with Properties**
   - Encapsulated `Circle` class with radius property.
   - Property decorators for getter/setter validation.
   - Automatic validation on radius assignment.

3. **Comprehensive Input Validation**
   - Checks for empty input strings.
   - Validates numeric input using float conversion.
   - Prevents negative radius values (raises `ValueError`).
   - Prevents zero radius (a point, not a circle).

4. **Accurate Calculations**
   - Area calculation: π × r²
   - Perimeter calculation: 2 × π × r
   - Uses Python's `math.pi` for precision.
   - Results displayed with 2 decimal places.

5. **Robust Error Handling**
   - Catches `ValueError` for invalid numeric input and validation errors.
   - Generic exception handler for unexpected errors.
   - Continuous input loop until valid value provided.

## How It Works

### Circle Class Structure

```python
class Circle:
    def __init__(self, radius = 0):
        self.radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, new_radius):
        # Validation logic
        if new_radius < 0:
            raise ValueError("Negative Radius isn't Allowed")
        elif new_radius == 0:
            raise ValueError("You are Giving a Point")
        else:
            self._radius = new_radius
```

**Key Components:**
- **Property Decorator**: Provides controlled access to the radius attribute
- **Setter Validation**: Automatically validates radius when assigned
- **Private Attribute**: Uses `_radius` to store the actual value
- **Default Value**: Radius defaults to 0 if not provided

### Calculation Methods

**Area Formula:**
```python
def area(self):
    return pi * pow(self._radius, 2)
# Formula: A = πr²
```

**Perimeter Formula:**
```python
def perimeter(self):
    return 2 * pi * self._radius
# Formula: C = 2πr
```

### Main Program Flow

1. **Input Phase**: User specifies number of circles
2. **Circle Creation Loop**: For each circle:
   - Prompt for radius input
   - Validate input (not empty, numeric)
   - Convert to float
   - Create Circle object (triggers setter validation)
   - Calculate area and perimeter
   - Display results with 2 decimal places
3. **Error Handling**: Retry input on validation errors

### Storage Structure

```python
circles = {
    0: Circle(5.0),
    1: Circle(10.5),
    2: Circle(3.2),
    # ... indexed by creation order
}
```

## Sample Output

### Successful Execution
```
Enter the number of circles: 3
Enter the Radius of the Circle: 5
Radius: 5.00
Area: 78.54
Perimeter: 31.42
Enter the Radius of the Circle: 10.5
Radius: 10.50
Area: 346.36
Perimeter: 65.97
Enter the Radius of the Circle: 2.75
Radius: 2.75
Area: 23.76
Perimeter: 17.28
```

### Error Handling Examples

**Empty Input:**
```
Enter the Radius of the Circle: 
Invalid Input. Please Try Again.
Enter the Radius of the Circle: 5
```

**Negative Radius:**
```
Enter the Radius of the Circle: -3
ValueError: Negative Radius isn't Allowed
Enter the Radius of the Circle: 3
```

**Zero Radius:**
```
Enter the Radius of the Circle: 0
ValueError: You are Giving a Point
Enter the Radius of the Circle: 5
```

**Non-numeric Input:**
```
Enter the Radius of the Circle: abc
ValueError: could not convert string to float: 'abc'
Enter the Radius of the Circle: 5
```

## Project Structure

```
project/
├── main.py           # Main program with input/output logic
└── circle.py         # Circle class definition
```

## Key Concepts Demonstrated

### Property Decorators
```python
@property
def radius(self):
    return self._radius

@radius.setter
def radius(self, new_radius):
    # Validation logic
    self._radius = new_radius
```
- **Encapsulation**: Hide internal implementation details
- **Validation**: Automatically validate data on assignment
- **Pythonic**: Use dot notation instead of getter/setter methods

### Private Attributes
```python
self._radius  # Convention for "private" attribute
```
- Leading underscore indicates internal use
- Accessed through property methods
- Prevents direct modification without validation

### Exception Raising in Setters
```python
if new_radius < 0:
    raise ValueError("Negative Radius isn't Allowed")
```
- Validation errors raised immediately
- Prevents invalid state
- Clear error messages for debugging

### Multi-level Exception Handling
```python
try:
    # Operations
except ValueError as e:
    # Handle specific validation errors
except Exception as e:
    # Catch-all for unexpected errors
```

### Object Storage in Dictionary
```python
circles = {}
circles[i] = Circle(radius_value)
```
- Indexed storage for easy retrieval
- Maintains creation order
- Allows named access by index

## Validation Rules

| Input | Validation | Result |
|-------|------------|--------|
| Empty string | Check before conversion | "Invalid Input" message |
| Negative number | Property setter check | ValueError: "Negative Radius isn't Allowed" |
| Zero | Property setter check | ValueError: "You are Giving a Point" |
| Non-numeric | Float conversion | ValueError with conversion error |
| Positive number | All checks pass | Circle created successfully |

## Mathematical Formulas

**Circle Area:**
```
A = πr²
```
Where:
- A = Area
- π (pi) ≈ 3.14159...
- r = radius

**Circle Perimeter (Circumference):**
```
C = 2πr
```
Where:
- C = Circumference/Perimeter
- π (pi) ≈ 3.14159...
- r = radius

## Notes

- **Required Module**: Uses Python's built-in `math` module (no installation needed).
- Results are rounded to 2 decimal places for display (`.2f` formatting).
- The `count()` method in the Circle class is defined but not implemented/used.
- Radius validation occurs automatically when creating or modifying Circle objects.
- Input loop continues until valid radius is provided for each circle.
- Empty input is handled separately before type conversion to provide clearer error messages.


## Common Errors and Solutions

**AttributeError: 'Circle' object has no attribute '_radius'**
- Cause: Trying to access `_radius` before it's set
- Solution: Ensure setter is called during initialization

**ValueError in setter but object still created**
- Cause: Exception not caught in main program
- Solution: Wrap Circle creation in try-except block (already implemented)

**Float precision issues**
- Cause: Floating-point arithmetic limitations
- Solution: Use `.2f` formatting for display (already implemented)

## Code Quality Features

✅ Input validation at multiple levels  
✅ Descriptive variable names  
✅ Clear error messages  
✅ Proper exception handling  
✅ Use of Python properties for encapsulation  
✅ Separation of Circle class from main logic  
✅ Formatted output for readability  
✅ Comments explaining workflow  
✅ Modular design for reusability