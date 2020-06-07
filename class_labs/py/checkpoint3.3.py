score = float(input('What did you get on your last exam? '))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'


print(f'Your score of {score} equates to an {grade}.')
