from django.shortcuts import render
import extrovertr.constants
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

#need to move these to constants.py
CLIENT_ID = "1042162482437-2mn2raldj8qee1pk2o2l9nbthk6ib4na.apps.googleusercontent.com"
CLIENT_SECRET = "hb0AtzLRMwXIQ6_AiF6mGiyE"
REDIRECT_URI = "http://localhost:8000/oauth2callback"

def check_google(request):
	return make_authorization_url()

def make_authorization_url():
	params = {"client_id": CLIENT_ID,
              "response_type": "code",
              "state": "state",
              "redirect_uri": REDIRECT_URI,
              "scope": "profile",
              "approval_prompt":"force"}    
	import urllib
	import urllib2
	url = "https://accounts.google.com/o/oauth2/auth?"+ urllib.urlencode(params)
	return url