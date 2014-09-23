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

CreateContactFormSet = formset_factory(CreateContactForm, formset=BaseContactFormset, extra=3)