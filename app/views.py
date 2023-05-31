from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'titleTab': '.: Diego Website :.',
        'titleName':'Diego Chacon Gonzalez',
        'GLOBAL_VAR_QA': False,
        'GLOBAL_VAR_DEV': False,
    }
    return render(request, 'app/index.html', context)

def developer(request):
    context = {
        'titleTab': '.: Diego Developer :.',
        'titleName':'Diego Chacon Developer',
        'GLOBAL_VAR_QA': False,
        'GLOBAL_VAR_DEV': True,
    }
    return render(request, 'app/developer.html', context)

def tester(request):
    context = {
        'titleTab': '.: Diego Tester :.',
        'titleName':'Diego Chacon Tester',
        'GLOBAL_VAR_QA': True,
        'GLOBAL_VAR_DEV': False,
    }
    return render(request, 'app/tester.html', context)

def knowledge(request):
    context = {
        'titleTab': '.: Diego Tester :.',
        'titleName':'Diego Chacon Tester',
        'GLOBAL_VAR_QA': True,
        'GLOBAL_VAR_DEV': False,
    }
    return render(request, 'app/knowledge.html', context)

def experience(request):
    context = {
        'titleTab': '.: Diego Tester :.',
        'titleName':'Diego Chacon Tester',
        'GLOBAL_VAR_QA': True,
        'GLOBAL_VAR_DEV': False,
    }
    return render(request, 'app/experience.html', context)

def knowledgeDev(request):
    context = {
        'titleTab': '.: Diego Tester :.',
        'titleName':'Diego Chacon Tester',
        'GLOBAL_VAR_QA': False,
        'GLOBAL_VAR_DEV': True,
    }
    return render(request, 'app/knowledgeDev.html', context)

def experienceDev(request):
    context = {
        'titleTab': '.: Diego Tester :.',
        'titleName':'Diego Chacon Tester',
        'GLOBAL_VAR_QA': False,
        'GLOBAL_VAR_DEV': True,
    }
    return render(request, 'app/experienceDev.html', context)



