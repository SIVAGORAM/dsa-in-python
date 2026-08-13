def main():
    # Question 20: Take a month number (1-12) and print the number of days
    # in that month (ignore leap years).
    month = 2

    if month == 2:
        print("28 days")
    elif month == 4 or month == 6 or month == 9 or month == 11:
        print("30 days")
    elif 1 <= month <= 12:
        print("31 days")
    else:
        print("Invalid month")


if __name__ == "__main__":
    main()


"""
Explanation:
The value stored in `month` is the input that the conditions work on.

The condition `month == 2` checks whether the month is February.
February has 28 days because leap years are ignored.

The condition `month == 4 or month == 6 or month == 9 or month == 11`
checks the months that have 30 days.

The remaining valid months have 31 days.

If the month is not between 1 and 12, "Invalid month" is printed.
"""