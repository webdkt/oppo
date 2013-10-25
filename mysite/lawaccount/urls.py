from django.conf.urls import patterns, url


from lawaccount import views
urlpatterns = patterns('',
    url(r'^$', views.ClientListView.as_view(), name='mainView'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^login.do/$', views.loginAction, name='loginAction'),
    url(r'^getAccountList/$', views.getAccountListAction, name='getAccountListAction'),
    url(r'^account/$', views.AccountList.as_view(), name='accountListView'),
    url(r'^account/delete/$', views.deleteAccounts, name='deleteAccounts'),
    url(r'^account/(?P<pk>\d+)/$', views.ClientUpdate.as_view(), name='accountUpdate'),
    url(r'^client/$', views.ClientListView.as_view(), name='clientListView'),
    url(r'^client/add/$', views.ClientCreate.as_view(), name='client_add'),
    url(r'^client/(?P<pk>\d+)/$', views.ClientUpdate.as_view(), name='client_update'),
    url(r'^client/(?P<pk>\d+)/delete$', views.ClientDelete.as_view(), name='client_delete'),
    #url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)

'''
old example:
    # url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    #url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
'''

