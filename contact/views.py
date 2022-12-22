from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from .forms import ContactForm
from django.contrib import messages
from .models import Apply

# Create your views here.

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        contact_data = request.POST
        form = ContactForm(data=contact_data)
        # submitted = True
        if form.is_valid():
            form.save()
            messages.success(request, 'Mesajınız qeydə alındı.')
            print('Form save')
        else:
            print('Form is invalid')

    context = {
            'form': form,
    }
    return render(request, 'contact.html', context)

def apply(request):
    return render(request, 'apply.html')

def send_files(request):
    if request.method == 'POST':
        name_surname = request.POST.get('name')
        email = request.POST.get('mail')
        number = request.POST.get('number')
        project_name = request.POST.get('project_name')
        project_des = request.POST.get('project_des')
        team_members = request.POST.get('members')
        project_level = request.POST.get('what')
        file = request.FILES.getlist('file')

        for f in file:
            Apply(name_surname=name_surname, email=email, number=number, project_name=project_name, project_des=project_des, team_members=team_members, project_level=project_level, file=f).save()

        print(Apply)
        messages.success(request, 'Thank you for your interest! We will reply to you within 2-3 working days.')

        return HttpResponseRedirect('')