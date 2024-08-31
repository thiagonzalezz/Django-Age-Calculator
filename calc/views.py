from django.shortcuts import render
from datetime import date

# Create your views here.
def age(request):
    if request.method == 'POST':
        day = request.POST['day']
        month = request.POST['month']
        year = request.POST['year']
        today = date.today()
        age = today.year - int(year)
        if today.month < int(month) or (today.month == int(month) and today.day < int(day)):
            age -= 1
        return render(request, 'age.html', {
            'age': age
        })
    else:
        return render(request, 'age.html')