from models import *
from django.forms import ModelForm, Textarea, HiddenInput
from django import forms
from django.forms.formsets import formset_factory, BaseFormSet

class RegistrationForm(ModelForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'password')
		widgets = {
			'password': forms.PasswordInput()
		}


class BaseContactFormset(BaseFormSet):
	def save_form(self, user_profile):
		for form in self.forms:
			try:
				contact = Contact()
				contact.email = form.cleaned_data['email']
				contact.name = form.cleaned_data['name']
				contact.cadence = form.cleaned_data['cadence']
				contact.email_next = form.cleaned_data['email_next']
				contact.user = user_profile
				contact.save()
			except:
				pass


class CreateContactForm(ModelForm):
	class Meta:
		model = Contact
		fields = ('name', 'email', 'cadence', 'email_next', 'user')
		widgets = {
			'user': HiddenInput(),
			'email_next': forms.TextInput(attrs={'class':'datepicker'})
		}
		labels = {
			'email_next': 'When do you want to email next? (leave blank to make it random)'
		}

CreateContactFormSet = formset_factory(CreateContactForm, formset=BaseContactFormset, extra=10)

class EditContactForm(ModelForm):
	class Meta:
		model = Contact
		exclude = ('user',)
	def is_not_blank(self, contact):
		if self.cleaned_data['name'] == "":
			self.cleaned_data['name']= contact.name
		if self.cleaned_data['email'] == "":
			self.cleaned_data['email']= contact.email
		if self.cleaned_data['cadence'] == None:
			self.cleaned_data['cadence']= contact.cadence
		if self.cleaned_data['email_next'] == None:
			self.cleaned_data['email_next']= contact.email_next










