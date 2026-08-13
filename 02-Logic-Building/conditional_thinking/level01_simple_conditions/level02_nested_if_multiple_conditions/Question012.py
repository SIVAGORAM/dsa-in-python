def main():
    # Question 12: If the sides form a valid triangle, determine
    # whether it is equilateral, isosceles, or scalene.
    a = 5
    b = 5
    c = 8

    if a + b > c and a + c > b and b + c > a:
        if a == b and b == c:
            print("Equilateral")
        elif a == b or b == c or a == c:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid triangle")


if __name__ == "__main__":
    main()


"""
Explanation:
The variables `a`, `b`, and `c` store the three side lengths.

First, the program checks whether the three sides form a valid triangle:
- `a + b > c`
- `a + c > b`
- `b + c > a`

If the triangle is valid:
- If all three sides are equal → Equilateral
- If any two sides are equal → Isosceles
- If all three sides are different → Scalene

If the triangle is not valid, it prints "Invalid triangle".
"""