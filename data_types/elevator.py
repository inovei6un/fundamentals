n = int(input())
p = int(input())

num_of_courses = int(n / p)
if n % p != 0:
    num_of_courses += 1

print(num_of_courses)
