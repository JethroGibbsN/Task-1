from django.shortcuts import render

from .forms import SignupForm


# Create your views here.

def signupform(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            return render(request, 'result.html', {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'choices': form.cleaned_data['plan_choices']
            })

    else:
       form = SignupForm()

    # returning form
    return render(request, 'signupform.html', {'form': form});