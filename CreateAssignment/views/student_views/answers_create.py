from CreateAssignment.models import *

def create_student_answer(user,subquestion,assignment):
    answer = StudentAnswer.objects.filter(user = user).filter(subquestion_id = subquestion).first()
    if answer == None:
        answer = StudentAnswer.objects.create(
            user = user,
            link = assignment,
            question_id = subquestion.question_id, 
            subquestion = subquestion,
            answer = "",
            score = 0
            ) 
    return answer
