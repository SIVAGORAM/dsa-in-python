# Python Fundamentals - Complete Beginner Notes

# 1. Introduction to Python

## What is Python?

Python is a high-level, interpreted, general-purpose programming language created by **Guido van Rossum** and first released in **1991**.

Python is designed to be simple, readable, and easy to learn, making it one of the most popular programming languages in the world.

---

# 2. Hello World Program

### Python

```python
print("Hello, World!")
```

### C

```c
#include <stdio.h>

int main() {
    printf("Hello, World!");
    return 0;
}
```

### Java

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

### JavaScript

```javascript
console.log("Hello, World!");
```

---

# 3. Why Python?

Python is popular because it is:

- Easy to learn
- Easy to read
- Easy to write
- Beginner-friendly
- Cross-platform
- Open source
- Large community support
- Huge ecosystem of libraries
- Highly productive
- Widely used in industry

---

# 4. Python is a Multi-Purpose Language

Python can be used for:

- Web Development
- Desktop Application Development
- Mobile Application Development
- Automation & Scripting
- Artificial Intelligence (AI)
- Machine Learning (ML)
- Data Science
- Data Analysis
- Deep Learning
- Cyber Security & Ethical Hacking
- DevOps
- Cloud Computing
- Networking
- Game Development
- IoT (Internet of Things)
- API Development
- Testing & Automation

---

# 5. Advantages of Python

## High-Level Language

Python is easy for humans to understand because it hides complex low-level details.

## Cross-Platform

Python programs run on Windows, Linux, and macOS with little or no modification.

## Large Ecosystem

Python provides thousands of built-in modules and third-party libraries.

Examples:

- NumPy
- Pandas
- Django
- Flask
- FastAPI
- TensorFlow
- PyTorch
- OpenCV

## Huge Community

Millions of developers contribute tutorials, libraries, and open-source projects.

---

# 6. Installing Python

1. Download the latest Python version from the official website.
2. Install Python.
3. During installation, select:

✅ Add Python to PATH

4. Finish the installation.

---

# 7. Verify Installation

Open Command Prompt or Terminal.

Check Python version:

```bash
python --version
```

or

```bash
python3 --version
```

Example:

```bash
Python 3.13.7
```

---

# 8. Python Interactive Shell

Start the Python shell:

```bash
python
```

Example:

```python
>>> 2 + 2
4

>>> 2 > 1
True

>>> 2 > 5
False

>>> 2 >
SyntaxError
```

The Python shell is useful for quickly testing code.

Exit using:

```python
exit()
```

or

```python
quit()
```

---

# 9. Code Editor vs IDE

## Code Editor

A Code Editor is a lightweight application used to write source code.

Examples:

- VS Code
- Sublime Text
- Atom

---

## IDE (Integrated Development Environment)

An IDE provides everything needed for software development.

Common IDE features:

- Intelligent Auto-completion
- Syntax Highlighting
- Debugging
- Unit Testing
- Code Navigation
- Refactoring
- Git Integration
- Terminal
- Linting
- Code Formatting
- Extensions

Examples:

- PyCharm
- VS Code
- IntelliJ IDEA

---

# 10. Install Visual Studio Code

Download and install the latest version of Visual Studio Code.

Recommended extensions:

- Python (Microsoft)
- Pylance
- Python Debugger
- autopep8
- Black Formatter
- Code Runner
- GitLens

---

# 11. Built-in Functions

Python provides many built-in functions.

Examples:

```python
print()

input()

type()

len()

id()

help()

max()

min()

sum()

range()

abs()

round()

sorted()
```

---

# 12. Linting

Linting checks your code for:

- Syntax errors
- Style violations
- Possible bugs
- Unused variables
- Missing imports

Popular linters:

- Pylint
- Flake8
- Ruff

---

# 13. Code Formatting

Code formatting automatically improves code readability.

Popular formatters:

- autopep8
- Black

Install autopep8:

```bash
pip install autopep8
```

---

# 14. Python PEPs

PEP stands for **Python Enhancement Proposal**.

The most important is:

**PEP 8**

It defines the official Python coding style.

Examples:

- 4 spaces for indentation
- Meaningful variable names
- Proper spacing around operators
- Maximum recommended line length

Following PEP 8 makes code clean and maintainable.

---

# 15. Python Implementations

Python has multiple implementations.

## CPython

- Official implementation
- Written in C
- Most widely used
- Downloads from python.org install CPython

Execution Flow:

```
Python Source Code
        ↓
CPython Compiler
        ↓
Python Bytecode (.pyc)
        ↓
Python Virtual Machine (PVM)
        ↓
Machine Code
        ↓
Processor
```

---

## PyPy

- Written in Python
- Faster than CPython for many programs
- Uses Just-In-Time (JIT) compilation

---

## Jython

- Implemented in Java
- Runs on the Java Virtual Machine (JVM)

Execution Flow:

```
Python Code
      ↓
Jython
      ↓
Java Bytecode
      ↓
JVM
      ↓
Machine Code
```

---

## IronPython

- Implemented using .NET
- Integrates with C#
- Runs on the Common Language Runtime (CLR)

---

# 16. Program Execution Comparison

## C

```
C Source Code
      ↓
Compiler
      ↓
Machine Code
      ↓
Processor
```

---

## Java

```
Java Source Code
       ↓
Java Compiler
       ↓
Java Bytecode
       ↓
Java Virtual Machine (JVM)
       ↓
Machine Code
       ↓
Processor
```

---

## Python

```
Python Source Code
        ↓
CPython Compiler
        ↓
Python Bytecode
        ↓
Python Virtual Machine (PVM)
        ↓
Machine Code
        ↓
Processor
```

---

# 17. Variables

A variable is a named memory location used to store data.

Example:

```python
name = "Siva"
age = 22
salary = 50000
```

Rules:

- Variable names are case-sensitive.
- Variable names cannot start with a number.
- Variable names cannot contain spaces.
- Use meaningful variable names.

Examples:

```python
name = "John"

student_name = "Rahul"

total_marks = 500
```

Invalid:

```python
1name = "John"

student name = "John"
```

---

# 18. Python is Case Sensitive

Python treats uppercase and lowercase letters as different.

Example:

```python
age = 20

Age = 30

AGE = 40
```

These are **three different variables**.

---

# 19. Everything in Python is an Object

Python follows an object-oriented approach.

Every value is an object.

Examples:

```python
x = 10

name = "Python"

marks = [10, 20, 30]

flag = True
```

All of these are objects with their own type and identity.

You can check the type:

```python
print(type(x))

print(type(name))

print(type(flag))
```

---

# Key Takeaways

- Python is a high-level, interpreted, general-purpose programming language.
- Python is widely used in AI, ML, Data Science, Web Development, Automation, DevOps, Testing, and more.
- CPython is the official and most commonly used Python implementation.
- Python source code is compiled into bytecode and executed by the Python Virtual Machine (PVM).
- Python is case-sensitive.
- Everything in Python is an object.
- Variables are used to store data.
- Follow PEP 8 coding standards for writing clean, readable code.
- Use VS Code or PyCharm for Python development.
- Use linting and formatting tools to improve code quality.
