# # Define two 3x3 matrices using nested lists
# matA = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# matB = [
#     [9, 8, 7],
#     [6, 5, 4],
#     [3, 2, 1]
# ]

# # Matrix Addition
# add_result = [[matA[i][j] + matB[i][j] for j in range(3)] for i in range(3)]

# # Matrix Subtraction
# sub_result = [[matA[i][j] - matB[i][j] for j in range(3)] for i in range(3)]

# # Element-wise Matrix Multiplication
# mul_result = [[matA[i][j] * matB[i][j] for j in range(3)] for i in range(3)]

# # Display results
# print("Matrix A:")
# for row in matA:
#     print(row)

# print("\nMatrix B:")
# for row in matB:
#     print(row)

# print("\nMatrix Addition (A + B):")
# for row in add_result:
#     print(row)

# print("\nMatrix Subtraction (A - B):")
# for row in sub_result:
#     print(row)

# print("\nMatrix Multiplication (element-wise A * B):")
# for row in mul_result:
#     print(row)

# nested = (
#     (1, 2, 3),
#     (10, 5, 1),
#     (4, 4, 4),
#     (7, 8, 2),
#     (9, 9, 0)
# )

# # Sort tuples by their sum (descending order)
# sorted_tuples = sorted(nested, key=sum, reverse=True)

# # Pick the second one
# print("Tuple with second largest sum:", sorted_tuples[1])


# Nested dictionary with students and their marks
# students = {
#     "Alice": {"Maths": 90, "Science": 85, "English": 88},
#     "Bob": {"Maths": 75, "Science": 80, "English": 70},
#     "Charlie": {"Maths": 95, "Science": 78, "English": 82}
# }

# # Find all subjects
# subjects = students[next(iter(students))].keys()

# # Calculate averages per subject
# averages = {}
# for subject in subjects:
#     total = 0
#     for marks in students.values():
#         total += marks[subject]
#     averages[subject] = total / len(students)

# # Display results (simplified)
# for student, marks in students.items():
#     print(student, marks)

# for subject in averages:
#     print(subject, ":", round(averages[subject], 2))

# Create dictionary
sentence = "this is a test this test is simple this is a test"

# Step 1: convert sentence into a list of words
words = sentence.split()

# Step 2: count frequency of each word
# freq = {}
# for word in words:
#     freq[word] = freq.get(word, 0) + 1

# # Step 3: find the most occurring word(s)
# max_count = max(freq.values())
# most_occurring = [word for word, count in freq.items() if count == max_count]

# print("Word frequencies:", freq)
# print("Most occurring words:", most_occurring)
# print("Occurrence count:", max_count)

#Assignment 1
# (1) Implementation of Euclidean Algorithm

# def gcd(a,b):
#    if b == 0:
#     return a
#    return gcd(b,a % b)

# x = int(input("Enter the first number: "))
# y = int(input("Enter the second number: "))
# print("gcd of",x, "and", y, "is", gcd(x,y))

def gcd(a,b):
    n1 = a
    n2 = b
    while(n2 > 0):
        q = n1 // n2
        r = n1 - q*n2
        n1 = n2
        n2 = r
    return n1

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
print("gcd of", x, "and", y, "is", gcd(x,y))

