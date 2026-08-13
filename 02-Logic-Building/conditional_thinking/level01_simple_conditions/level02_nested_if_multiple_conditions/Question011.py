def main():
    # Question 11: Take three sides and check if they form a valid triangle.
    a = 3
    b = 4
    c = 5

    if a + b > c and a + c > b and b + c > a:
        print("Valid triangle")
    else:
        print("Invalid triangle")


if __name__ == "__main__":
    main()


"""
Explanation:
The variables `a`, `b`, and `c` store the three side lengths.

For three sides to form a valid triangle, the sum of any two sides
must be greater than the third side.

The conditions check:
- `a + b > c`
- `a + c > b`
- `b + c > a`

All three conditions must be True, so we use the `and` operator.

If all conditions are True, the triangle is valid. Otherwise, it is invalid.
"""