from django.conf.urls import patterns, url


from lawaccount import views
urlpatterns = patterns('',
    #url(r'^$', views.MainView.as_view(), name='main'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^login.do/$', views.loginAction, name='loginAction'),
    #url(r'^client/$', views.ClientListView.as_view(), name='clientList'),
    #url(r'^client/(?P<pk>\d+)/$', views.ClientDetail.as_view(), name='clientDetail'),
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

