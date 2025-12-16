# Employee Management System

A Python program that manages employee records with automatic ID generation, random job assignment, and salary allocation. The system uses object-oriented programming with class variables to track employee counts and generate unique IDs.

## Features

1. **Automatic Employee ID Generation**
   - Unique employee IDs starting from 1001.
   - Auto-incremented for each new employee.
   - Read-only property to prevent ID modification.

2. **Random Job Assignment**
   - Job titles loaded from external text file (`jobTitles.txt`).
   - Random assignment from available positions.
   - Supports multiple job titles for variety.

3. **Random Salary Generation**
   - Salaries randomly assigned between 25,000 and 75,000.
   - Simulates realistic salary distribution.
   - Integer values for simplicity.

4. **Employee Tracking**
   - Class-level counter tracks total employees created.
   - Dictionary storage with employee count as key.
   - Complete employee roster display.

5. **Input Validation**
   - Checks for empty name input.
   - Prevents numeric-only names.
   - Continuous prompting until valid input received.

6. **Custom String Representation**
   - Formatted employee information display.
   - Includes name, salary, designation, and ID.
   - Clean, readable output format.

## How It Works

### Employee Class Structure

```python
class Employee:
    _emp_id = 1000        # Class variable for ID tracking
    count = 0             # Class variable for employee count
    
    def __init__(self, name, salary, designation):
        self._name = name
        self._salary = salary
        self._designation = designation
        Employee._emp_id += 1
        self._emp_id = Employee._emp_id
        Employee.count += 1
```

**Key Components:**
- **Class Variables**: `_emp_id` and `count` shared across all instances
- **Instance Variables**: `_name`, `_salary`, `_designation`, `_emp_id` unique to each employee
- **Auto-increment**: Each new employee increments both counters
- **Property Decorator**: Read-only access to employee ID

### ID Generation System

```python
Employee._emp_id += 1      # Increment class variable
self._emp_id = Employee._emp_id  # Assign to instance
```
- First employee gets ID 1001
- Second employee gets ID 1002
- Continues sequentially for all employees

### Random Assignment Logic

```python
emp_designation = random.choice(job_titles)  # Random job from list
emp_salary = random.randint(25000, 75000)    # Random salary in range
```

### File Loading

```python
with open("jobTitles.txt", "r") as file:
    job_titles = file.read().splitlines()
```
- Opens external file with job titles
- Reads all lines into a list
- Each line becomes one job title option

## Usage

### Prerequisites

Create a `jobTitles.txt` file in the same directory with job titles (one per line):
```
Software Engineer
Data Analyst
Project Manager
HR Manager
Marketing Specialist
Sales Executive
Accountant
Designer
Developer
Team Lead
```
### Error Handling Examples

**Empty Name Input:**
```
Enter Employee Name: 
Invalid Input. Please Try Again.
Enter Employee Name: Alice Johnson
```

**Numeric Name Input:**
```
Enter Employee Name: 12345
Must be a String. Please Try Again.
Enter Employee Name: Alice Johnson
```

**Missing File:**
```
File Not Found. Please Try Again.
```

## Project Structure

```
project/
├── main.py              # Main program with input/output logic
├── employee.py          # Employee class definition
└── jobTitles.txt        # External file with job titles (required)
```

## Key Concepts Demonstrated

### Class Variables vs Instance Variables

**Class Variables** (shared by all instances):
```python
_emp_id = 1000
count = 0
```

**Instance Variables** (unique to each object):
```python
self._name = name
self._emp_id = Employee._emp_id
```

### Property Decorator for Read-Only Access
```python
@property
def emp_id(self):
    return self._emp_id
```
- Provides read-only access to employee ID
- Prevents external modification
- Accessed like an attribute: `employee.emp_id`

### Custom String Representation
```python
def __str__(self):
    return f"Name: {self._name}\n..."
```
- Called automatically by `print()` and `str()`
- Provides formatted output
- Better than default object representation

### File Handling with Context Manager
```python
with open("jobTitles.txt", "r") as file:
    job_titles = file.read().splitlines()
```
- Automatically closes file after reading
- Exception-safe file handling
- `.splitlines()` removes newline characters

### Random Module Usage
```python
random.choice(job_titles)    # Random selection from list
random.randint(25000, 75000) # Random integer in range
```

## Data Storage Structure

```python
employees = {
    1: Employee("Alice Johnson", 52340, "Software Engineer"),
    2: Employee("Bob Smith", 68920, "Project Manager"),
    3: Employee("Carol White", 34500, "Data Analyst"),
    # ... keyed by employee count
}
```

## Validation Rules

| Input | Validation | Result |
|-------|------------|--------|
| Empty string | Check with `== ""` | "Invalid Input" message |
| Numeric string | Check with `.isdigit()` | "Must be a String" message |
| Valid name | Passes all checks | Employee created successfully |

## Configuration

### Salary Range
```python
emp_salary = random.randint(25000, 75000)
```
- Minimum: $25,000
- Maximum: $75,000
- Modify these values to adjust salary range

### Starting Employee ID
```python
_emp_id = 1000  # First employee will be 1001
```
- Change this value to start from different ID
- IDs auto-increment from this base

## Notes

- **Required File**: `jobTitles.txt` must exist in the same directory
- **Random Module**: Uses Python's built-in `random` module (no installation needed)
- The `emp_count()` static method is defined but not used in the current implementation
- Employee IDs are immutable once assigned (read-only property)
- Salary values are integers (no cents/decimals)
- Job titles are case-sensitive as stored in the file
- Empty lines in `jobTitles.txt` will be included as valid options

## Potential Enhancements

- Add employee search functionality by name or ID
- Implement salary raise/promotion methods
- Add employee removal/termination functionality
- Save employee data to persistent storage (database/JSON)
- Load existing employees from file on startup
- Add validation for duplicate names
- Implement salary ranges based on designation
- Add employee hire date tracking
- Create department grouping functionality
- Generate employee reports and statistics
- Add email generation based on name
- Implement employee filtering and sorting
- Add data export to CSV/Excel
- Create employee performance tracking
- Add employee contact information fields
- Implement role-based access control
- Add salary history tracking
- Create organizational hierarchy visualization

## Common Issues and Solutions

**FileNotFoundError when running:**
- Ensure `jobTitles.txt` exists in the same directory
- Check file name spelling (case-sensitive on some systems)
- Verify file has read permissions

**Empty job_titles list:**
- Check that `jobTitles.txt` is not empty
- Ensure file has actual content (not just whitespace)

**Same ID for multiple employees:**
- Ensure `Employee._emp_id` is a class variable (outside `__init__`)
- Verify increment happens before assignment

## Sample jobTitles.txt Content

```
Software Engineer
Senior Software Engineer
Junior Developer
Data Analyst
Data Scientist
Project Manager
Product Manager
HR Manager
Recruiter
Marketing Manager
Marketing Specialist
Sales Executive
Sales Manager
Accountant
Financial Analyst
UX Designer
UI Designer
Graphic Designer
System Administrator
Network Engineer
DevOps Engineer
Quality Assurance Engineer
Team Lead
Technical Lead
Architect
Consultant
Business Analyst
Operations Manager
Customer Support Specialist
Content Writer
```

## Code Quality Features

✅ Input validation at multiple levels  
✅ File handling with exception management  
✅ Clear separation of concerns (class vs main logic)  
✅ Read-only property for data protection  
✅ Custom string representation for readability  
✅ Auto-incrementing ID system  
✅ Random assignment for simulation  
✅ Dictionary-based storage for easy access  
✅ Descriptive variable names  
✅ Formatted output with proper spacing