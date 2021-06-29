from django.shortcuts import render
import random
import string

loop = 12
length = 8
result_str = ''
x = []

def get(request, *args, **kwargs):

    # if request.method == 'GET':
    if 'option1' == request.GET['inlineRadioOptions']:
      length = 8
    elif 'option2' == request.GET['inlineRadioOptions']:
      length = 12
    elif 'option3' == request.GET['inlineRadioOptions']:
      length = 18
    else:
      length = 12

    if len(x) == loop:
        x.clear()

    for i in range(loop):
        x.append(get_random_string(length))

    context = {
        'test': x,
    }

    # print(request.GET['inlineRadioOptions'])
    return render(request, 'index.html', context)


def get_random_string(length):
    letters = string.ascii_letters
    numbers =  string.digits
    result_str = ''.join(random.choice(letters + numbers) for i in range(length))
    return result_str


def index(request):


    if len(x) == loop:
        x.clear()

    for i in range(loop):
        x.append(get_random_string(length))


    context = {
        'test': x,
    }



    return render(request, 'index.html', context)
