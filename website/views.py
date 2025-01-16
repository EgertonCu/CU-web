from django.http import JsonResponse
from django.utils.timezone import now
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone
from django.urls import reverse
from .models import *
from django.contrib.auth import get_user_model


# Create your views here.
User = get_user_model()

def homepage(request):
    events = Event.objects.all()
    testimonies = Testimony.objects.all()
    context = {
        'events': events,
        'testimonies': testimonies,
    }
    return render(request, 'website/index.html', context)

@login_required(login_url = 'website:login')
def leadership(request):
    leaders = Leader.objects.all()
    context = {
    'leaders': leaders,
    }
    return render(request, 'website/Leadership.html', context)

@login_required(login_url = 'website:login')
def ministries(request):
    eteams = Eteam.objects.all()
    ministries = Ministry.objects.all()
    context = {
        'ministries': ministries,
        'eteams': eteams,
    }
    return render(request, 'website/Ministries.html', context)

def about(request):
    return render(request, 'website/about.html')

@login_required(login_url = 'website:login')
def gallery(request):
    images = Image.objects.all()
    context = {
    'images': images,
    }
    return render(request, 'website/gallery.html', context)

@login_required(login_url = 'website:login')
def library(request):
    return render(request, 'website/E-Library.html')

# def blogsingle(request):
#     return render(request, 'website/blog-single.html')

def registration(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        registrationNumber = request.POST['registrationNumber']
        phone = request.POST['phone']
        homeCounty = request.POST['homeCounty']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']

        user_data_has_error = False
        User = get_user_model()

        if User.objects.filter(registrationNumber=registrationNumber).exists():
            user_data_has_error = True
            messages.error(request, "Registration Number already exists")
        elif User.objects.filter(email=email).exists():
            user_data_has_error = True
            messages.error(request, "email already exists")
        elif len(password)<5:
            user_data_has_error = True
            messages.error(request, "Password must be at least 5 characters")
        elif password != confirmPassword:
            user_data_has_error = True
            messages.error(request, "Passwords do not match")
        elif user_data_has_error:
            return redirect('website:register')
        else:
            new_user = User.objects.create_user(
            full_name = full_name,
            username = full_name,
            registrationNumber = registrationNumber,
            homeCounty = homeCounty,
            email = email,
            phone = phone,
            password = password
            )
            messages.success(request, "Account created successfully")
            return redirect('website:login')

    return render(request, 'website/Membership_Reg.html')

def userlogin(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')

		user = authenticate(request, email=email, password=password)

		if user is not None:
			login(request, user)
			return redirect('website:home')

		else:
			messages.error(request, "Invalid credentials")
			return redirect('website:login')


	return render(request, 'website/login.html')

def forgot_password(request):
	if request.method == 'POST':
		email = request.POST.get('email')

		try:
			user = User.objects.get(email=email)
			new_password_reset = PasswordReset(user=user)
			new_password_reset.save()

			password_reset_url = reverse('website:reset', kwargs={'reset_id':new_password_reset.reset_id})
			full_password_reset_url = f"{request.scheme}://{request.get_host()}{password_reset_url}"

			email_body = f"Reset your password using the link below \n\n\n {full_password_reset_url}"

			email_message = EmailMessage(
			'Reset your password', #subject
			email_body,
			settings.EMAIL_HOST_USER, #SENDER
			[email]
			)
			email_message.fail_silently = True
			email_message.send()

			return redirect('website:reset-sent', reset_id=new_password_reset.reset_id)

		except user.DoesNotExist:
			messages.error(request, f"No user with the email '{email}' found! ")
			return redirect('website:forgot')


	return render(request, 'website/Forgot_password.html')

def password_reset_sent(request, reset_id):
	if PasswordReset.objects.filter(reset_id=reset_id).exists():
		return render(request, 'website/password_reset_sent.html')
	else:
		messages.error(request, "Invalid reset ID")
		return redirect('website:forgot')

def reset_password(request, reset_id):
    try:
        # Retrieve the PasswordReset object
        password_reset = PasswordReset.objects.get(reset_id=reset_id)

        if request.method == 'POST':
            newPassword = request.POST.get('newPassword')
            confirmPassword = request.POST.get('confirmPassword')

            passwords_have_error = False

            if newPassword != confirmPassword:
                passwords_have_error = True
                messages.error(request, "Passwords do not match")
            if len(newPassword) < 5:
                passwords_have_error = True
                messages.error(request, "Password must be 5 or more characters long")

            expiration_time = password_reset.created + timezone.timedelta(minutes=10)

            if timezone.now() > expiration_time:
                password_reset.delete()
                passwords_have_error = True
                messages.error(request, "Link expired")

            if not passwords_have_error:
                user = password_reset.user
                user.set_password(newPassword)
                user.save()

                password_reset.delete()
                messages.success(request, "Password reset successfully, proceed to login")
                return redirect('website:login')
            else:
                # Redirect back to the reset form with error messages
                return redirect('website:reset', reset_id=reset_id)

    except PasswordReset.DoesNotExist:
        messages.error(request, "Invalid reset ID")
        return redirect('website:forgot')

    return render(request, 'website/Reset_password.html')

def logout_view(request):
	logout(request)
	return redirect('website:login')

def privacyPolicy(request):
    return render(request, 'website/privacy-policy.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = Contact.objects.create(
        name=name,
        email=email,
        message=message)

        # contact.save()
        messages.success(request, "Message received")
        return redirect('website:home')
    return render(request, 'website/contact.html')
