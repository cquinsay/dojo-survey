from django.shortcuts import render, redirect
LANGS = (
    'Python',
    'C#',
    'Java',
    'JavaScript',
    'C'
)
LOCATIONS = (
    'Burbank',
    'Chicago',
    'Dallas',
    'Seattle',
    'DC',
)

def index(request):
    context = {
        'locations': LOCATIONS,
        'languages': LANGS
    }
    return render(request, 'form.html', context)

def process(request):
    if request.method == 'POST':
        return redirect('/')
    request.session['result'] = {
        'name': request.POST['name'],
        'location': request.POST['location'],
        'language': request.POST['language']
    }
    return redirect('/result')

def result(request):
    context = {
        'result': request.session['result']
    }
    return render(request, 'result.html', context)
    

# Create your views here.
