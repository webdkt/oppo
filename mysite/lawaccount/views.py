# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse,reverse_lazy
from django.views import generic

from lawaccount.models import Client
from lawaccount.forms import ClientForm

from django.contrib.auth import authenticate, login


CURRENT_APP = 'lawaccount'

class LoginView(generic.TemplateView):
    template_name = CURRENT_APP +"/login.html"


class ClientListView(generic.ListView):
    template_name= CURRENT_APP + '/account.html'
    context_object_name = 'client_list'
    model = Client

class ClientCreate(generic.CreateView):
    model = Client
    template_name = CURRENT_APP + '/client_create_form.html'

class ClientUpdate(generic.UpdateView):
    model = Client


class ClientDelete(generic.DeleteView):
    model = Client
    success_url = reverse_lazy('clientListView')

class ClientDetailView(generic.DetailView):
    template_name= CURRENT_APP + '/account_detail.html'
    context_object_name = 'client'
    model = Client


'''    def get_queryset(self):
        """Return the last five published polls. """
        return Client.objects
'''

def loginAction(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect(reverse(CURRENT_APP+':clientListView',current_app=CURRENT_APP))
            #return render(request, CURRENT_APP +'/login.html',{'error_message': 'Login Success'})
        else:
            return HttpResponseRedirect(reverse(CURRENT_APP+':login',current_app=CURRENT_APP,kwargs={'error_message:User Account Locked'}))
            # Return a 'disabled account' error message
    else:
        # Return an 'invalid login' error message.
        return render(request, CURRENT_APP+'/login.html', {'error_message': "Invalid User/Password",})

        #return HttpResponseRedirect(reverse(CURRENT_APP+':login',current_app='lawaccount',kwargs={'error_message:Invalid User/Password'}))