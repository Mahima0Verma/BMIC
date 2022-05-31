from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings


from .models import *

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def admission(request):
    return render(request, 'admission.html')


def aim(request):
    return render(request, 'aim.html')

def book_list(request):
    all_data =  Book_list.objects.all()
    return render(request, 'book_list.html', {'key1':all_data})

def co_curriculum(request):
    return render(request, 'co-curriculum.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = 'You have a new message from User regarding ' + subject
        message_body = 'Name: ' + name + '. Email: ' + email + '. Phone: ' + phone + '. Message: ' + message

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
                email_subject,
                message_body,
                'sandeepdeveloper975@gmail.com',
                [admin_email],
                fail_silently=False,
            )
        messages.success(request, 'Thank you for contacting us. We will get back to you shortly')
        return redirect('contact')

    return render(request, 'contact.html')


def curriculum(request):
    return render(request, 'curriculum.html')




def exam(request):
    return render(request, 'exam.html')

def facilities(request):
    return render(request, 'facilities.html')

def faculty(request):
    all_data = Faculty.objects.all()
    return render(request, 'faculty.html', {'key1':all_data})

def fee(request):
    return render(request, 'fee.html')

def gallery(request):
    return render(request, 'gallery.html')

def holiday_list(request):
    return render(request, 'holiday_list.html')

def infrastructure(request):
    all_data = Infrastructure.objects.all()
    return render(request, 'infrastructure.html',{'key1':all_data})

def message(request):
    return render(request, 'message.html')

def notice(request):
    all_data = Notice.objects.all()
    return render(request, 'notice.html', {'key1':all_data})

def public_disclosure(request):
    return render(request, 'public_disclosure.html')

def rules(request):
    return render(request, 'rules.html')

def strength(request):
    all_data=Strength.objects.all()
    return render(request, 'strength.html',{'key1': all_data})

def syllabus(request):
    all_data = Syllabus.objects.all()
    return render(request, 'syllabus.html', {'key1':all_data})
