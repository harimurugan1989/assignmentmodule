import random
from CreateAssignment.models import *
import json


def create_random (user, question):
    randoms = StudentRandom.objects.filter(question = question).filter(user = user).first()
    if randoms == None:
        randoms = StudentRandom.objects.create(question = question,user = user,randoms = "")
        random_data = RandomNumber.objects.filter(question = question).all()
        re = []
        for i in range(len(random_data)):
            re.append(-1)
        for i in range(len(random_data)):
            if random_data[i].integers_only:
                re[random_data[i].var_number-1] = random.randint(random_data[i].min_num,random_data[i].max_num)
            else:
                re[random_data[i].var_number-1] = round(random.uniform(random_data[i].min_num,random_data[i].max_num),4)
        randoms.randoms = json.dumps(re)
        randoms.save()
    return randoms