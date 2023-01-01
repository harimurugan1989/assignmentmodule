from CreateAssignment.models import RandomNumber
from django.http import JsonResponse


def RandomNumberDelete(request,link,qno):
    var_num = int(request.POST["var_num"])
    print(var_num)
    randoms = RandomNumber.objects.filter(question_id = qno).all()
    for each in randoms:
        if each.var_number == var_num:
            each.delete()
    for each in randoms:
        if each.var_number > var_num:
            each.var_number -= 1
            each.save()
    return JsonResponse({
        "status": True,
    })