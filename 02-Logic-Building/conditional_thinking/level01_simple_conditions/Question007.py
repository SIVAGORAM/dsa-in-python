def main():
    # Question 7: Take three numbers and print the largest.
    first = 20
    second = 35
    third = 12

    largest = first

    if second > largest:
        largest = second

    if third > largest:
        largest = third

    print("Largest = " + str(largest))


if __name__ == "__main__":
    main()


"""
Explanation:
The variables `first`, `second`, and `third` hold the three numbers
that need to be compared.

The variable `largest` initially stores the value of `first`.

- If `second` is greater than `largest`, `largest` is updated to `second`.
- If `third` is greater than `largest`, `largest` is updated to `third`.

After all comparisons, `largest` contains the largest number.
"""