from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from .models import Mentors, Trainers
from .forms import ContactForm
from django.contrib import messages

# Create your views here.

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        contact_data = request.POST
        form = ContactForm(data=contact_data)
        # submitted = True
        if form.is_valid():
            form.save()
            messages.success(request, 'Qeyde alindi')

            print(messages)

        else:
            print('Form is invalid')

    context = {
            'form': form,
    }
    return render(request, 'contact.html', context)


def incubation(request):
    mentors = Mentors.objects.all().order_by('-id')
    trainers = Trainers.objects.all()

    context = {
        'mentors': mentors,
        'trainers': trainers

    }
    return render(request, 'incubation-program.html', context)