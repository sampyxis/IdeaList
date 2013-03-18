from django.views.generic.base import TemplateView
from social_auth import __version__ as version
from social_auth.utils import setting

from TaskLists.models import *

from django.http import HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.messages.api import get_messages

from django import forms

# Old code - this was the class base view - still works but not using it now
class HomePageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['tasks'] = Tasks.objects.all()[:5]
        return context

def get_idea_list_context(request):
    if request.method == 'POST':
        form = newIdeaForm(request.POST)
        if form.is_valid():
            #enter name
            #name = form.idea_name
            newIdea = Tasks(name='name', user = request.user)
            #Big bug - this doesn't stop saving to the db...
            #newIdea.save()
            return get_idea_list_context(request)
    else:

	context = {
	'tasks':Tasks.objects.all()[:150],
    'name': request.user.username,
    'newIdea': newIdeaForm()
	}
	return render_to_response('index.html', context, RequestContext(request))

def home(request):
    """Home view, displays login mechanism"""
    if request.user.is_authenticated():
        return get_idea_list_context(request)
    else:
        return render_to_response('home.html', {'version': version},
                                  RequestContext(request))
# New Idea Form
class newIdeaForm(forms.Form):
    idea_name = forms.CharField(max_length=200)

def newIdea(request):
    if request.method == 'POST':
        form = newIdeaForm(request.POST)
        if form.is_valid():
            return get_idea_list_context(request)
    else:
        form = newIdeaForm()

    return home(request)

@login_required
def user(request):
    """ Show the user acccount page """
    ctx = {
        'name': request.user.username
    }
    return render_to_response('user_account.html', ctx)

@login_required
def done(request):
    """Login complete view, displays user data"""
    ctx = {
        'version': version,
        'last_login': request.session.get('social_auth_last_login_backend')
    }
    return render_to_response('done.html', ctx, RequestContext(request))


def error(request):
    """Error view"""
    messages = get_messages(request)
    return render_to_response('error.html', {'version': version,
                                             'messages': messages},
                              RequestContext(request))


def logout(request):
    """Logs out user"""
    auth_logout(request)
    return HttpResponseRedirect('/')


def form(request):
    if request.method == 'POST' and request.POST.get('username'):
        name = setting('SOCIAL_AUTH_PARTIAL_PIPELINE_KEY', 'partial_pipeline')
        request.session['saved_username'] = request.POST['username']
        backend = request.session[name]['backend']
        return redirect('socialauth_complete', backend=backend)
    return render_to_response('form.html', {}, RequestContext(request))


def form2(request):
    if request.method == 'POST' and request.POST.get('first_name'):
        request.session['saved_first_name'] = request.POST['first_name']
        name = setting('SOCIAL_AUTH_PARTIAL_PIPELINE_KEY', 'partial_pipeline')
        backend = request.session[name]['backend']
        return redirect('socialauth_complete', backend=backend)
    return render_to_response('form2.html', {}, RequestContext(request))


def close_login_popup(request):
    return render_to_response('close_popup.html', {}, RequestContext(request))        