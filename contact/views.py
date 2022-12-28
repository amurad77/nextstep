from django.shortcuts import render, get_object_or_404, HttpResponseRedirect,HttpResponse, redirect
from .forms import ContactForm, ApplyForm
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
            messages.success(request, 'Thank you for your interest! We will reply to you within 2-3 working days.')
            print('Form save')
        else:
            print('Form is invalid')

    context = {
            'form': form,
    }
    return render(request, 'contact.html', context)

def apply(request):

    # form = ApplyForm()
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        
        # submitted = True
        if form.is_valid():
            name = form.cleaned_data['name']
            surname =form.cleaned_data['surname']
            email = form.cleaned_data['email']
            number = form.cleaned_data['number']
            what_idea = form.cleaned_data['what_idea']
            hours = form.cleaned_data['hours']
            idea = form.cleaned_data['idea']
            describe = form.cleaned_data['describe']
            people = form.cleaned_data['people']
            more_information = form.cleaned_data['more_information']
            industries1 = form.cleaned_data['industries1']
            industries2 = form.cleaned_data['industries2']
            areas1 = form.cleaned_data['areas1']
            areas2 = form.cleaned_data['areas2']
            file = form.cleaned_data['file']
            Apply(name=name, surname=surname, email=email, number=number, what_idea=what_idea, hours=hours, idea=idea, describe=describe, people=people, more_information=more_information, industries1=industries1, industries2=industries2, areas1=areas1, areas2=areas2, file=file).save()
            
            return HttpResponseRedirect('/upload')
        else:
            print(form)
            return HttpResponse('error')

                        # messages.success(request, 'Thank you for your interest! We will reply to you within 2-3 working days.')
    else:
        context = {
            'form': ApplyForm(),
        }
        return render(request, 'apply.html', context)

def upload(request):
    return render (request, 'upload.html')

# def send_files(request):
#     if request.method == 'POST':
#         name_surname = request.POST.get('name')
#         email = request.POST.get('mail')
#         number = request.POST.get('number')
#         project_name = request.POST.get('project_name')
#         project_des = request.POST.get('project_des')
#         team_members = request.POST.get('members')
#         project_level = request.POST.get('what')
#         file = request.FILES.getlist('file')

#         for f in file:
#             Apply(name_surname=name_surname, email=email, number=number, project_name=project_name, project_des=project_des, team_members=team_members, project_level=project_level, file=f).save()

#         print(Apply)
#         messages.success(request, 'Thank you for your interest! We will reply to you within 2-3 working days.')

#         return HttpResponseRedirect('')