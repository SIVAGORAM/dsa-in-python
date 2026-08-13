def main():
    # Question 19: Take a day number (1-7) and print the corresponding day name.
    day = 3

    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    if 1 <= day <= 7:
        print(days[day - 1])
    else:
        print("Invalid day")


if __name__ == "__main__":
    main()


"""
Explanation:
The value stored in `day` represents the day number from 1 to 7.

The `days` list stores the names of the seven days.

Python list indexing starts from 0, so `day - 1` is used to get
the correct day name:
- 1 → index 0 → Monday
- 2 → index 1 → Tuesday
- 3 → index 2 → Wednesday
- ...
- 7 → index 6 → Sunday

The condition `1 <= day <= 7` checks whether the given day number
is valid.
"""