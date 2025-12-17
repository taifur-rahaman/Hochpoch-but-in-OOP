# Multi-Number Calculator

A Python program that performs basic arithmetic operations on multiple numbers using object-oriented programming. The calculator supports addition, subtraction, multiplication, and division with a menu-driven interface.

## Features

1. **Multiple Number Support**
   - Perform operations on any quantity of numbers.
   - Uses `*args` for flexible input handling.
   - Space-separated input for easy number entry.

2. **Four Basic Operations**
   - **Addition**: Sum of all input numbers
   - **Subtraction**: Sequential subtraction from zero
   - **Multiplication**: Product of all input numbers
   - **Division**: Division of first number by second (binary operation)

3. **Menu-Driven Interface**
   - Interactive console menu with numbered options.
   - Clear operation descriptions.
   - Easy-to-use navigation system.

4. **Error Prevention**
   - Zero division check built into division method.
   - Raises `ZeroDivisionError` with descriptive message.
   - Match-case for invalid menu choices.

5. **Variadic Arguments**
   - Uses `*args` to accept variable number of arguments.
   - Flexible input processing with unpacking operator.
   - Demonstrates advanced Python function parameters.

## How It Works

### Calculator Class Structure

```python
class Calculator:
    def __init__(self, *args):
        self.args = args  # Stores all input numbers as tuple
```

**Key Components:**
- **Variadic Constructor**: Accepts any number of arguments via `*args`
- **Tuple Storage**: Arguments stored in `self.args` tuple
- **Instance Methods**: Each operation is a separate method

### Operation Implementations

**Addition (uses built-in sum):**
```python
def addition(self):
    return sum(self.args)
# Example: (5, 10, 15) → 30
```

**Subtraction (sequential from zero):**
```python
def subtraction(self):
    self.sum = 0
    for arg in self.args:
        self.sum -= arg
    return self.sum
# Example: (5, 10, 15) → 0 - 5 - 10 - 15 = -30
```

**Multiplication (iterative product):**
```python
def multiplication(self):
    self.product = 1
    for arg in self.args:
        self.product *= arg
    return self.product
# Example: (5, 10, 2) → 100
```

**Division (binary operation with validation):**
```python
def division(self):
    if self.args[1] == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return self.args[0] / self.args[1]
# Example: (20, 4) → 5.0
```

### Input Processing Pipeline

```python
input("Enter numbers: ")           # "5 10 15"
.split()                           # ['5', '10', '15']
map(int, ...)                      # [5, 10, 15]
list(...)                          # [5, 10, 15]
Calculator(*num)                   # Calculator(5, 10, 15)
```

## Usage

**Run the script:**
```bash
python main.py
```

**Follow the menu:**
1. Select an operation (1-4)
2. Enter numbers separated by spaces
3. View the result
4. Repeat or exit (0)

## Sample Output

### Addition Example
```
1. Addition
2. Subtraction
3. Multiplication
4. Division
0. Exit
Enter Your Choice: 1
Enter numbers separated by spaces: 10 20 30 40
100
```

### Subtraction Example
```
Enter Your Choice: 2
Enter numbers separated by spaces: 5 10 15
-30
```

### Multiplication Example
```
Enter Your Choice: 3
Enter numbers separated by spaces: 2 3 4 5
120
```

### Division Example
```
Enter Your Choice: 4
Enter numbers separated by spaces: 100 5
20.0
```

### Zero Division Error
```
Enter Your Choice: 4
Enter numbers separated by spaces: 50 0
Traceback (most recent call last):
  ...
ZeroDivisionError: Cannot divide by zero.
```

### Exit
```
Enter Your Choice: 0
Exiting the program. Goodbye!
```

## Project Structure

```
project/
├── main.py              # Main program with menu interface
└── calculation.py       # Calculator class definition
```

## Key Concepts Demonstrated

### Variadic Arguments (*args)
```python
def __init__(self, *args):
    self.args = args
```
- Accepts any number of positional arguments
- Stored as a tuple
- Enables flexible function interfaces

### Unpacking Operator (*)
```python
num = [5, 10, 15]
Calculator(*num)  # Unpacks to Calculator(5, 10, 15)
```
- Expands list/tuple into individual arguments
- Essential for passing dynamic argument lists
- Works with any iterable

### Match-Case Statement (Python 3.10+)
```python
match choice:
    case "1":
        # Addition
    case "0":
        break
    case _:
        # Default case
```
- Modern alternative to if-elif chains
- More readable for menu systems
- Pattern matching capabilities

### List Comprehension with map()
```python
list(map(int, input().split()))
```
- Converts string input to integer list
- Functional programming approach
- Concise and efficient

### Exception Raising
```python
raise ZeroDivisionError("Cannot divide by zero.")
```
- Prevents invalid operations
- Provides clear error messages
- Can be caught by calling code

## Operation Behaviors

### Addition
- **Input**: Any quantity of numbers
- **Logic**: Sums all numbers
- **Example**: `5 + 10 + 15 = 30`

### Subtraction
- **Input**: Any quantity of numbers
- **Logic**: Subtracts all from zero (0 - n1 - n2 - n3...)
- **Example**: `0 - 5 - 10 - 15 = -30`
- **Note**: This is sequential subtraction from zero, not left-to-right

### Multiplication
- **Input**: Any quantity of numbers
- **Logic**: Multiplies all numbers together
- **Example**: `5 × 10 × 2 = 100`

### Division
- **Input**: Exactly 2 numbers expected (only uses first two)
- **Logic**: Divides first by second (a ÷ b)
- **Example**: `20 ÷ 4 = 5.0`
- **Limitation**: Only processes first two numbers if more provided

## Notes

- **No External Libraries Required** - Uses only Python standard library features.
- **Python Version**: Match-case requires Python 3.10+
- Division always returns a float (even for whole number results)
- Division only uses the first two numbers from input
- Subtraction starts from zero and subtracts all numbers sequentially
- No error handling for invalid numeric input (will crash on non-numbers)
- Calculator object is recreated for each operation
- Test code included but commented out in `calculation.py`

## Limitations and Considerations

### Division Behavior
- Only performs binary division (two numbers)
- If more than 2 numbers entered, extras are ignored
- No warning given for extra numbers

### Subtraction Behavior
- Current implementation: `0 - n1 - n2 - n3`
- Alternative approach could be: `n1 - n2 - n3 - n4` (left-to-right)

### Error Handling Gaps
- No handling for non-numeric input
- No validation for empty input
- No minimum number requirements per operation
- Division doesn't check if enough numbers provided

### Division Zero Check
```python
if self.args[1] == 0:  # Checks second number
```
- Only checks second number (divisor)
- Doesn't validate that two numbers exist
- Could cause IndexError if only one number provided

## Educational Value

This program is excellent for learning:
- Object-oriented programming in Python
- Variadic arguments (`*args`)
- Unpacking operators (`*`)
- Match-case statements (structural pattern matching)
- Built-in functions (`sum()`, `map()`)
- List comprehensions and functional programming
- Menu-driven program design
- Exception raising and error handling
- Method organization in classes
- Input processing pipelines

## Potential Enhancements

### Input Validation
```python
try:
    num = list(map(int, input().split()))
    if not num:
        print("No numbers entered!")
        continue
except ValueError:
    print("Invalid input! Enter numbers only.")
    continue
```

### Improved Division
```python
def division(self):
    if len(self.args) < 2:
        raise ValueError("Division requires at least 2 numbers.")
    if self.args[1] == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return self.args[0] / self.args[1]
```

### Alternative Subtraction
```python
def subtraction(self):
    if not self.args:
        return 0
    result = self.args[0]
    for arg in self.args[1:]:
        result -= arg
    return result
# Example: (20, 5, 3) → 20 - 5 - 3 = 12
```

### Additional Features
- Add modulo operation
- Add exponentiation
- Support floating-point input
- Add operation history
- Implement memory functions (store/recall)
- Add parentheses support for complex expressions
- Create GUI version with Tkinter
- Add scientific calculator functions
- Implement unit conversion
- Add result formatting options
- Support for fractions and decimals
- Add calculation history saving to file

## Alternative Implementation Ideas

### Functional Approach
```python
from functools import reduce
import operator

def division(self):
    if len(self.args) < 2:
        raise ValueError("Need at least 2 numbers")
    if 0 in self.args[1:]:
        raise ZeroDivisionError("Cannot divide by zero")
    return reduce(operator.truediv, self.args)
```

### Using reduce for All Operations
```python
from functools import reduce
import operator

def subtraction(self):
    return reduce(operator.sub, self.args, 0)

def multiplication(self):
    return reduce(operator.mul, self.args, 1)
```

## Code Quality Features

✅ Object-oriented design with clear separation  
✅ Variadic arguments for flexibility  
✅ Menu-driven interface for user-friendliness  
✅ Built-in function usage (`sum()`)  
✅ Zero division protection  
✅ Match-case for clean control flow  
✅ Modular code structure  
⚠️ Missing comprehensive error handling  
⚠️ No input validation for empty/invalid input  
⚠️ Division limitation to two numbers not documented in UI

## Testing Suggestions

Run these test cases to verify functionality:

**Addition:**
- `5 10 15` → Expected: `30`
- `100` → Expected: `100`
- `-5 -10` → Expected: `-15`

**Subtraction:**
- `5 10 15` → Expected: `-30`
- `100` → Expected: `-100`
- `-5 -10` → Expected: `15`

**Multiplication:**
- `2 3 4` → Expected: `24`
- `5` → Expected: `5`
- `-2 5` → Expected: `-10`

**Division:**
- `20 4` → Expected: `5.0`
- `100 10` → Expected: `10.0`
- `50 0` → Expected: `ZeroDivisionError`
- `10` → Expected: `IndexError` (bug to fix!)