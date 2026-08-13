def main():
    # Question 15: Take the hour of the day (0-23) and print
    # "Good Morning", "Good Afternoon", "Good Evening", or "Good Night".
    hour = 16

    if hour >= 5 and hour < 12:
        print("Good Morning")
    elif hour >= 12 and hour < 17:
        print("Good Afternoon")
    elif hour >= 17 and hour < 21:
        print("Good Evening")
    else:
        print("Good Night")


if __name__ == "__main__":
    main()


"""
Explanation:
The value stored in `hour` is the input that the conditions work on.

The conditions check the hour in order:
- `5 <= hour < 12` → Good Morning
- `12 <= hour < 17` → Good Afternoon
- `17 <= hour < 21` → Good Evening
- Otherwise → Good Night

Only the branch whose condition becomes true prints its message.
"""