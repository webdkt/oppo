# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from lawaccount.models import Client

from django.contrib.auth import authenticate, login


CURRENT_APP = 'lawaccount'

class LoginView(generic.TemplateView):
    template_name = CURRENT_APP +"/login.html"


#class MainView(generic.ListView):
#    template_name= 'lawaccount/index.html'
    #context_object_name = ''

#    def get_queryset(self):
#        """Return the last five published polls. """
#        return Client.objects.order_by('-pub_date')[:5]


def loginAction(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            #return HttpResponseRedirect(reverse('login',current_app=CURRENT_APP,kwargs={'error_message:Login Success'}))
            return render(request, CURRENT_APP +'/login.html',{'error_message': 'Login Success'})
        else:
            return HttpResponseRedirect(reverse('login',current_app=CURRENT_APP,kwargs={'error_message:User Account Locked'}))
            # Return a 'disabled account' error message
    else:
        # Return an 'invalid login' error message.
        return HttpResponseRedirect(reverse('login',current_app='lawaccount',kwargs={'error_message:Invalid User/Password'}))