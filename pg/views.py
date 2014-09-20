from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import *
from forms import *
from django.contrib.auth.decorators import login_required

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

@login_required()
def list_contacts(request):
	user_profile = UserProfile.objects.get(user=request.user)
	contacts = Contact.objects.filter(user=user_profile)
	context = {'user_profile':user_profile, 'contacts':contacts}
	return render(request, 'list_contacts.html', context)