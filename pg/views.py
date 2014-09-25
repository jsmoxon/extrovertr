from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import *
from forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


def create_user_profile(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'] )
			user.save()
			UserProfile.objects.create(user=user)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			authorize_user = authenticate(username=username, password=password)
			if authorize_user is not None:
				if authorize_user.is_active:
					login(request, authorize_user)
				else:
					print "not activ"
			else:
				print "no user"
			return redirect('list_contacts')
		else:
			return HttpResponse("fail")
	else:
		form = RegistrationForm()
	return render(request, 'create_profile.html', {'form':form})		


@login_required()
def add_contacts(request):
	user_profile = UserProfile.objects.get(user=request.user)
	if request.method == 'POST':
		formset = CreateContactFormSet(request.POST)
		if formset.is_valid():
			formset.save_form(user_profile)
			return redirect('list_contacts')
		else:
			return HttpResponse("fail")
	else:
		formset = CreateContactFormSet()
	return render(request, 'add_contacts.html', {'formset':formset})		

@login_required()
def view_contact(request, contact_id):
	contact = Contact.objects.get(pk=contact_id)
	context = {'contact':contact}
	return render(request, 'view_contact.html', context)


@login_required
def edit_contact(request, contact_id):
	contact = Contact.objects.get(pk=contact_id)
	if request.method == 'POST':
		form = EditContactForm(request.POST)
		if form.is_valid():
			form.is_not_blank(contact)
			contact.name = form.cleaned_data['name']
			contact.email = form.cleaned_data['email']
			contact.cadence = form.cleaned_data['cadence']
			contact.email_next = form.cleaned_data['email_next']
			contact.save()
			return redirect('list_contacts')
		else:
			return HttpResponse("fail")
	else:
		form = EditContactForm(initial={
			'name': contact.name,
			'email': contact.email,
			'cadence': contact.cadence,
			'email_next': contact.email_next,
			})
	return render(request, 'edit_contact.html', {'form':form, 'contact':contact})


@login_required()
def list_contacts(request):
	user_profile = UserProfile.objects.get(user=request.user)
	contacts = Contact.objects.filter(user=user_profile)
	context = {'user_profile':user_profile, 'contacts':contacts}
	return render(request, 'list_contacts.html', context)