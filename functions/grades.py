def grade(grade_num):

    if grade_num < 3.00:
        return "Fail"
    elif grade_num < 3.5:
        return "Poor"
    elif grade_num < 4.5:
        return "Good"
    elif grade_num < 5.5:
        return "Very Good"
    elif grade_num <= 6.00:
        return "Excellent"

current_num = float(input())

print(grade(current_num))
