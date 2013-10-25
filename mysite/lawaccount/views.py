# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse,reverse_lazy
from django.views import generic
import json
import lawaccount.models
from lawaccount.models import Client, Account
from lawaccount.forms import ClientForm

from django.contrib.auth import authenticate, login
import logging
import sys

CURRENT_APP = 'lawaccount'
logger = logging.getLogger(__name__)

class LoginView(generic.TemplateView):
    template_name = CURRENT_APP +"/login.html"


class AccountList(generic.ListView):
    template_name = CURRENT_APP + '/account.html'
    context_object_name = 'account_list'
    model = Account
    defaultPageSize = 20  #default page size for account list
    startIndex = 0
    endIndex = 10

    print >>sys.stderr, '!!!!!!!!!!Action List'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(generic.ListView,self).get_context_data(**kwargs)
        # (PublisherDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        self.request.session['first_level_view_name'] = 'Account'
        return context

    def get_queryset(self):
        #startIndex = 0
        #endIndex = 10
        if not self.request:
            self.startIndex = int(self.request.session["accountStartIndex"])
            if not self.startIndex:
                self.startIndex = 0
            self.endIndex = int(self.request.session["accountStartIndex"])
            if (not self.endIndex) or self.endIndex < self.startIndex:
                self.endIndex = self.startIndex + self.defaultPageSize
        return Account.objects.all()[self.startIndex:self.endIndex]

    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)




class ClientListView(generic.ListView):
    template_name= CURRENT_APP + '/client.html'
    context_object_name = 'client_list'
    model = Client

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(generic.ListView,self).get_context_data(**kwargs)
        # (PublisherDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['first_level_view_name'] = 'Client'
        return context


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



def deleteAccounts(request):
    print >>sys.stderr, 'deleting accounts'
    #id = request.POST['deleteFormIDs']
    ids = request.POST.getlist('selected_item')
    print >>sys.stderr, ids
    #print >>sys.stderr, id
    return HttpResponseRedirect(reverse(CURRENT_APP+':login',current_app=CURRENT_APP))





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
            return HttpResponseRedirect(reverse(CURRENT_APP+':login',current_app=CURRENT_APP,kwargs={'error_message':'User Account Locked'}))
            # Return a 'disabled account' error message
    else:
        # Return an 'invalid login' error message.
        return render(request, CURRENT_APP+'/login.html', {'error_message': "Invalid User/Password",})

        #return HttpResponseRedirect(reverse(CURRENT_APP+':login',current_app='lawaccount',kwargs={'error_message:Invalid User/Password'}))

'''
配合JQuery Datatables,用Ajax GET方法在服务器端获取数据

'''
def getAccountListAction(request):
    #col_idx = ['0','1','2','3','4']
    cols = ['acc_name','primary_phone','mobile','email','fax','id']
    col_idx = range(len(cols))
    defaultPageSize = 10
    startIndex = 0
    endIndex = startIndex + defaultPageSize
    modelClass = getattr(lawaccount.models, 'Account')
    q = modelClass.objects
    #q = Account.objects
    #q = Account.objects.filter(headline__startswith="What")
    print >>sys.stderr, 'q genereated !'
    if request.GET.has_key('sSearch'):
        searchString =  request.GET['sSearch']
        print >>sys.stderr, 'addiing filter!'
        q = q.filter(acc_name__istartswith = searchString)

    if request.GET.has_key('iSortCol_0'):
        for i in range(0,int(request.GET['iSortingCols'] )):
            if request.GET['bSortable_'+ request.GET['iSortCol_'+str(i)]] == 'true':
                direction = request.GET.get('iSortDir_'+str(i),'asc')
                if direction == 'asc':
                    q = q.order_by(cols[int(request.GET['iSortCol_'+str(i)])-1])
                else:
                    q = q.order_by('-'+cols[int(request.GET['iSortCol_'+str(i)])-1])

    if request.GET.has_key('iDislayStart'):
        startIndex = request.GET['iDisplayStart']
    if request.GET.has_key('iDisplayLength'):
        endIndex = int(request.GET['iDisplayLength'])
        if endIndex <> -1:
            endIndex = startIndex + endIndex
        else:
            endIndex = startIndex + defaultPageSize
    total = q.count()
    result = q[startIndex:endIndex]


    response_dict = {'sEcho':'','iTotalRecords':'','iTotalDisplayRecords':'', 'aaData':''}
    response_dict['sEcho']= request.GET['sEcho']
    response_dict['iTotalRecords']= total
    response_dict['iTotalDisplayRecords'] = min(endIndex - startIndex, total)
    aaData = [ dict(dict(zip(col_idx, [getattr(row,colname) for colname in cols] )).items() + {'DT_RowClass':'Account', 'DT_RowId': str(row.id)}.items()) for row in result ]

    #aaData =[ [ col_idx[cols.index(colname)] + ":" + str(getattr(row,colname)) for colname in cols] for row  in result ]
    #[]
    #     for row in result:
#        aaData.append([row.acc_name,row.primary_phone, row.mobile,row.email,row.fax])
    response_dict['aaData']=aaData
    print >> sys.stderr, json.dumps(response_dict)
    return HttpResponse(json.dumps(response_dict), mimetype='application/json')


'''
通用查询方法，配合JQuery Datatables plugin, 来获取某个表。特定的表需要扩展这个Class，指定新的
'''
def getDataTable(request, modelName, cols, searchColName):
    #cols = ['acc_name','primary_phone','mobile','email','fax','id']
    col_idx = range(len(cols))
    defaultPageSize = 10
    startIndex = 0
    endIndex = startIndex + defaultPageSize
    modelClass = getattr(lawaccount.models, modelName)
    q = modelClass.objects
    #q = Account.objects.filter(headline__startswith="What")

    if request.GET.has_key('sSearch'):
        searchString =  request.GET['sSearch']
        print >>sys.stderr, 'addiing filter!'
        q = q.filter(acc_name__istartswith = searchString)

    if request.GET.has_key('iSortCol_0'):
        for i in range(0,int(request.GET['iSortingCols'] )):
            if request.GET['bSortable_'+ request.GET['iSortCol_'+str(i)]] == 'true':
                direction = request.GET.get('iSortDir_'+str(i),'asc')
                if direction == 'asc':
                    q = q.order_by(cols[int(request.GET['iSortCol_'+str(i)])-1])
                else:
                    q = q.order_by('-'+cols[int(request.GET['iSortCol_'+str(i)])-1])

    if request.GET.has_key('iDislayStart'):
        startIndex = request.GET['iDisplayStart']
    if request.GET.has_key('iDisplayLength'):
        endIndex = int(request.GET['iDisplayLength'])
        if endIndex <> -1:
            endIndex = startIndex + endIndex
        else:
            endIndex = startIndex + defaultPageSize
    total = q.count()
    result = q[startIndex:endIndex]


    response_dict = {'sEcho':'','iTotalRecords':'','iTotalDisplayRecords':'', 'aaData':''}
    response_dict['sEcho']= request.GET['sEcho']
    response_dict['iTotalRecords']= total
    response_dict['iTotalDisplayRecords'] = min(endIndex - startIndex, total)
    aaData = [ dict(dict(zip(col_idx, [getattr(row,colname) for colname in cols] )).items() + {'DT_RowClass':modelName, 'DT_RowId': 'row_'+str(row.id)}.items()) for row in result ]

    #aaData =[ [ col_idx[cols.index(colname)] + ":" + str(getattr(row,colname)) for colname in cols] for row  in result ]
    #[]
    #     for row in result:
#        aaData.append([row.acc_name,row.primary_phone, row.mobile,row.email,row.fax])
    response_dict['aaData']=aaData
    print >> sys.stderr, json.dumps(response_dict)
    return HttpResponse(json.dumps(response_dict), mimetype='application/json')