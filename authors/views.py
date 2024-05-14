from django.shortcuts import redirect, render
from django.http import Http404
from .forms import RegisterForm

def register_view(request):
    request.session['number'] = request.session.get('number') or 1
    request.session['number'] += 1
    
    
    register_form_data = request.session.get('register_form_data')
    form = RegisterForm(register_form_data)
        
    return render(request, 'authors/pages/register_view.html', {
        'form': form
    })
    
def register_create(request):
    if not request.POST:
        raise(Http404)
    
    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(request.POST)
    
    return redirect('authors:register')
    
    # return render(request, 'authors/pages/register_view.html', {
    #     'form': form
    # })