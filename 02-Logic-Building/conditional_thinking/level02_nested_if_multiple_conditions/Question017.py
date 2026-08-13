def main():
    # Question 17: Take two numbers and determine whether both are even,
    # both are odd, or one is even and one is odd.
    first = 12
    second = 18

    if first % 2 == 0 and second % 2 == 0:
        print("Both are even")
    elif first % 2 != 0 and second % 2 != 0:
        print("Both are odd")
    else:
        print("One is even and one is odd")


if __name__ == "__main__":
    main()


"""
Explanation:
The variables `first` and `second` store the two numbers being checked.

The first condition checks whether both numbers are even:
`first % 2 == 0 and second % 2 == 0`

The second condition checks whether both numbers are odd:
`first % 2 != 0 and second % 2 != 0`

If neither condition is true, one number is even and the other is odd.

Only the branch whose condition becomes true prints its message.
"""