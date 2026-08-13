def main():
    # Question 29: Take two angles of a triangle and compute the third angle.
    first_angle = 50
    second_angle = 60

    third_angle = 180 - first_angle - second_angle

    print("Third angle =", third_angle)


if __name__ == "__main__":
    main()


"""
Explanation:

The question gives us two angles of a triangle and asks us to
calculate the third angle.

The total angle of a triangle is 180 degrees.

Therefore:

third angle = 180 - first angle - second angle


Example:

first_angle = 50
second_angle = 60

Step 1:
Start with the total angle of a triangle:

180 degrees


Step 2:
Subtract the first angle:

180 - 50 = 130


Step 3:
Subtract the second angle:

130 - 60 = 70


Therefore:

third_angle = 70

Output:

Third angle = 70


Another Example:

first_angle = 90
second_angle = 45

third_angle = 180 - 90 - 45
third_angle = 45

Output:

Third angle = 45


Another Example:

first_angle = 30
second_angle = 80

third_angle = 180 - 30 - 80
third_angle = 70

Output:

Third angle = 70


Test Cases:

1. Input:
   first_angle = 50
   second_angle = 60

   Output:
   Third angle = 70


2. Input:
   first_angle = 90
   second_angle = 45

   Output:
   Third angle = 45


3. Input:
   first_angle = 30
   second_angle = 80

   Output:
   Third angle = 70


4. Input:
   first_angle = 60
   second_angle = 60

   Output:
   Third angle = 60


5. Input:
   first_angle = 100
   second_angle = 30

   Output:
   Third angle = 50


Key Concepts:

`-` → Subtraction

The formula is:

third angle = 180 - first angle - second angle

Important:

This question only asks us to compute the third angle.
It does not ask us to validate whether the given two angles
can form a valid triangle, so no additional validation is needed
for this question.
"""