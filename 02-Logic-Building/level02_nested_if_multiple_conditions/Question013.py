def main():
    # Question 13: Take marks (0-100) and print the corresponding grade (A/B/C/D/F).
    marks = 82

    if marks >= 90:
        print("A")
    elif marks >= 75:
        print("B")
    elif marks >= 60:
        print("C")
    elif marks >= 40:
        print("D")
    else:
        print("F")


if __name__ == "__main__":
    main()


"""
Explanation:
The value stored in `marks` is the input that the conditions work on.

The conditions check the marks from the highest range to the lowest:
- `marks >= 90` → A
- `marks >= 75` → B
- `marks >= 60` → C
- `marks >= 40` → D
- Otherwise → F

The `if`, `elif`, and `else` statements ensure that only the
first matching grade is printed.
"""