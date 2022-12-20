from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from .forms import ContactForm, ApplyForm
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

            print('**************', messages)

        else:
            print('Form is invalid')

    context = {
            'form': form,
    }
    return render(request, 'contact.html', context)

def apply(request):

    form = ApplyForm()
    if request.method == 'POST':
        contact_data = request.POST
        form = ApplyForm(data=contact_data)
        # submitted = True
        if form.is_valid():
            form.save()
            messages.success(request, 'Qeyde alindi')

            print(messages)

        else:
            print(form.errors)
            print('Form is invalid')

    context = {
            'form': form,
    }
    return render(request, 'apply.html', context)