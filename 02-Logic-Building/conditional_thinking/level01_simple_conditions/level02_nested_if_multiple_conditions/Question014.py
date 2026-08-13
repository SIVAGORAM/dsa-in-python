def main():
    # Question 14: Check if one of two given numbers is a multiple of the other.
    first = 12
    second = 36

    if first != 0 and second % first == 0:
        print("Second is a multiple of first")
    elif second != 0 and first % second == 0:
        print("First is a multiple of second")
    else:
        print("No number is a multiple of the other")


if __name__ == "__main__":
    main()


"""
Explanation:
The variables `first` and `second` store the two numbers being checked.

The first condition checks whether `second` is a multiple of `first`:
`first != 0 and second % first == 0`

The second condition checks whether `first` is a multiple of `second`:
`second != 0 and first % second == 0`

The `!= 0` checks prevent division by zero.

If neither condition is true, neither number is a multiple of the other.
"""