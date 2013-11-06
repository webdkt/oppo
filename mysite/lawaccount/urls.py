from django.conf.urls import patterns, url


from lawaccount import views

urlpatterns = patterns('',
    #url(r'^$', views.ClientListView.as_view(), name='mainView'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^login.do/$', views.loginAction, name='loginAction'),
    url(r'^view/list/(?P<model_name>\D+)/$' , views.genericListView, name='genericListView'),
    url(r'^ajax/list/$' , views.getDataTable, name='ajaxDataTable'),
    url(r'^create/Customer/(?P<customer_id>\d+)/File/$' , views.FileCreate.as_view(), name='createFile'),
    url(r'^create/File/$' , views.FileCreate.as_view(), name='createFile'),
    url(r'^edit/Customer/(?P<customer_id>\d+)/File/(?P<pk>\d+)/$' , views.FileUpdate.as_view(), name='updateFile'),
    url(r'^edit/File/(?P<pk>\d+)/$' , views.FileUpdate.as_view(), name='updateFile'),
    url(r'^edit/(?P<model_name>\D+)/(?P<pk>\d+)/$' , views.GenericEdit.as_view(), name='genericEdit'),
    url(r'^create/(?P<model_name>\D+)/$' , views.GenericCreate.as_view(), name='genericCreate'),
    url(r'^ajax/create/(?P<model_name>\D+)/$' , views.GenericCreateAjax.as_view(), name='genericCreateAjax'),
    url(r'^batchdelete/$' , views.genericBatchDelete, name='genericBatchDelete'),
    url(r'^ajax/batchdelete/$' , views.genericBatchDeleteAjax, name='genericBatchDeleteAjax'),
    url(r'^ajax/template/(?P<template>\D+.html)/$' , views.ajaxLoadTemplate, name='ajaxLoadTemplate'),
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

