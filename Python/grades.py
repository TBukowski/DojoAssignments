import random

def scoreGrade(students):
    print 'Scores and Grades'
    for i in range(0, students):
        score = random.randint(60, 100)
        if score <= 69:
            print 'Score:', score, 'Your grade is D'
        elif score <= 79:
            print 'Score:', score, 'Your grade is C'
        elif score <= 89:
            print 'Score:', score, 'Your grade is B'
        elif score <= 100:
            print 'Score:', score, 'Your grade is A'
    print 'End of the program, Bye!'
scoreGrade(10)