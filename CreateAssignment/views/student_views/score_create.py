from CreateAssignment.models import *


def create_student_score(user,assignment):
    student_score = StudentScore.objects.filter(user = user).filter(link = assignment).first()
    if student_score == None:
        print("haye raam")
        student_score = StudentScore.objects.create(
            user = user,
            link = assignment,
            score = 0,
        )
    return student_score