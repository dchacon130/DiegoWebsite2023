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
        'GLOBAL_VAR_DEV': True
    }
    return render(request, 'app/developer.html', context)

def tester(request):
    context = {
        'titleTab': '.: Diego Tester :.',
        'titleName':'Diego Chacon Tester',
        'GLOBAL_VAR_QA': True,
    }
    return render(request, 'app/tester.html', context)


def expQA(request):
    context = {
        'titleTab': '.: Diego Tester :.',
        'titleName':'Diego Chacon Tester',
        'GLOBAL_VAR_QA': True,
    }
    return render(request, 'app/expQA.html', context)

def knowledgeQa(request):
    context = {
        'titleTab': '.: Diego Tester :.',
        'titleName':'Diego Chacon Tester',
        'GLOBAL_VAR_QA': True,
    }
    return render(request, 'app/knowledgeQA.html', context)

def aboutDev(request):
    
    return render(request, 'app/aboutDEV.html')

def projectsDev(request):
    
    return render(request, 'app/projectsDEV.html')