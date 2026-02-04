def score(marks):
    return sum(marks)/len(marks) 
def grade(marks):
    average = score(marks)
    if average >= 90:
        return 'A+'
    elif average >= 75:
        return 'A'
    elif average >= 60:
        return 'B'
    elif average >= 50:
        return 'C'
    else:
        return 'F'