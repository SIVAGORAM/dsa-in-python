def main():
    # Question 8: Take a temperature value and print "Cold", "Warm", or "Hot" using range conditions.
    temperature = 31

    if temperature < 15:
        print("Cold")
    elif temperature <= 30:
        print("Warm")
    else:
        print("Hot")


if __name__ == "__main__":
    main()


"""
Explanation:
The value stored in `temperature` is the input that the conditions work on.

The conditions check the temperature in order:
- `temperature < 15` → Cold
- `temperature <= 30` → Warm
- Otherwise → Hot

Only the branch whose condition becomes true prints its message.
"""