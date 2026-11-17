from django.shortcuts import render
from django.http import Http404

def home(request):
    students = ['Anu', 'Rahul', 'Meera', 'Arun', 'Neha']

    return render(request, 'great/home.html', {
        'students': students
    })


def view_result(request, name):

    results = {
        'Anu': {'english': 85, 'maths': 90, 'science': 88},
        'Rahul': {'english': 78, 'maths': 82, 'science': 75},
        'Meera': {'english': 92, 'maths': 95, 'science': 90},
        'Arun': {'english': 70, 'maths': 76, 'science': 80},
        'Neha': {'english': 88, 'maths': 84, 'science': 91},
    }

    if name not in results:
        raise Http404("Student not found")

    return render(request, 'great/result.html', {
        'name': name,
        'result': results[name]
    })

# Create your views here.
