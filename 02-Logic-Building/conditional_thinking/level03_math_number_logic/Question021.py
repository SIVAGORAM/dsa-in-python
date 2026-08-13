def main():
    # Question 21: Take a 3-digit number and check if all digits are distinct.
    number = 427

    hundreds = number // 100
    tens = (number // 10) % 10
    ones = number % 10

    if hundreds != tens and tens != ones and hundreds != ones:
        print("All digits are distinct")
    else:
        print("Digits are not distinct")


if __name__ == "__main__":
    main()


"""
Explanation:
The variables `hundreds`, `tens`, and `ones` store the three digits
of the given 3-digit number.

For 427:
- `hundreds = 4`
- `tens = 2`
- `ones = 7`

The condition checks that every pair of digits is different:
- `hundreds != tens`
- `tens != ones`
- `hundreds != ones`

All three conditions must be True for the digits to be distinct.
"""