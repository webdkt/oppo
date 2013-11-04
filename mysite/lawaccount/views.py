# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse,reverse_lazy
from django.views import generic
import json
import lawaccount.models
from lawaccount.models import *
from lawaccount.forms import ClientForm

from django.contrib.auth import authenticate, login
import logging
import sys

CURRENT_APP = 'lawaccount'
logger = logging.getLogger(__name__)

class LoginView(generic.TemplateView):
    template_name = CURRENT_APP +"/login.html"


def genericListView(request, model_name):
    template_name =CURRENT_APP + '/' + model_name.lower() + '_list.html'  #eg. if model_name= 'Account', tempalte name will be account_list.html
    return render(request,template_name)


class GenericEdit(generic.UpdateView):
    model = None
    #context_object_name = 'object'
    template_name = None

    def dispatch(self,*args, **kwargs):
        model_name=kwargs['model_name'].capitalize()
        self.model = eval(model_name)
        self.template_name = CURRENT_APP + '/' + model_name.lower() + '_edit.html'
        self.context_object_name = model_name.lower()
        print >>sys.stderr, 'Loading: ' + self.template_name
        return super(GenericEdit,self).dispatch(*args, **kwargs)

class GenericCreate(generic.CreateView):

    model = None
    template_name = None
    #template_name = CURRENT_APP + '/' + modelName + '_create.html'
    def dispatch(self, *args, **kwargs):
        model_name=kwargs['model_name']
        self.model = getattr(lawaccount.models,model_name)
        if self.request.REQUEST.has_key('return_url'):
            this.success_url = self.request.REQUEST['return_url']
        self.template_name = CURRENT_APP + '/' + model_name.lower() + '_create.html'
        self.context_object_name = model_name.lower()
        #return generic.CreateView.dispatch(request, *args, **kwargs)
        return super(GenericCreate,self).dispatch(*args, **kwargs)


class GenericDelete(generic.DeleteView):
    print >>sys.stderr, 'we are here!!!!!!!!!!'

    model = None
    def dispatch(request, *args, **kwargs):
        model_name=self.request.REQUEST['model_name']
        self.model = eval(model_name)
        success_url = reverse_lazy(CURRENT_APP+':deleteSuccess',kwargs={'model_name':model_name})
        return super(GenericDelete,self).dispatch(request, *args, **kwargs)


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




class AccountUpdate(generic.UpdateView):
    model = Account
    context_object_name = 'account'
    template_name = CURRENT_APP + '/accountUpdate.html'

class AccountCreate(generic.CreateView):
    model = Account
    template_name = CURRENT_APP + '/accountCreate.html'

class AccountDelete(generic.DeleteView):
    print >>sys.stderr, 'we are here!!!!!!!!!!'
    model = Account
    success_url = reverse_lazy(CURRENT_APP+':accountListView')

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
    context_object_name = 'accountDetail'
    template_name = CURRENT_APP + '/accountEdit.html'


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
    Account.objects.filter(id__in = ids).delete()

    return HttpResponseRedirect(reverse(CURRENT_APP+':accountListView',current_app=CURRENT_APP))

def genericBatchDelete(request):
    print >>sys.stderr, 'deleting batch'
    #id = request.POST['deleteFormIDs']
    ids = request.POST.getlist('selected_item')
    print >>sys.stderr, ids
    #print >>sys.stderr, id
    model_name = request.POST['model_name'].capitalize()
    obj_class = eval(model_name)
    obj_class.objects.filter(id__in = ids).delete()

    return HttpResponseRedirect(reverse(CURRENT_APP+':genericListView',current_app=CURRENT_APP, kwargs={'model_name': model_name}))



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
    if request.GET.has_key('iDisplayLength'):
        defaultPageSize = int(request.GET['iDisplayLength'])

    startIndex = 0
    if request.GET.has_key('iDisplayStart'):
        startIndex = int(request.GET['iDisplayStart'])
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
    response_dict['iTotalDisplayRecords'] = total
    aaData = [ dict(dict(zip(col_idx, [getattr(row,colname) for colname in cols] )).items() + {'DT_RowClass':'Account', 'DT_RowId': str(row.id)}.items()) for row in result ]

    #aaData =[ [ col_idx[cols.index(colname)] + ":" + str(getattr(row,colname)) for colname in cols] for row  in result ]
    #[]
    #     for row in result:
#        aaData.append([row.acc_name,row.primary_phone, row.mobile,row.email,row.fax])
    response_dict['aaData']=aaData
    print >> sys.stderr, json.dumps(response_dict)
    return HttpResponse(json.dumps(response_dict), mimetype='application/json')


def getDataTable(request):
    '''
        通用查询方法，配合JQuery Datatables plugin, 来获取某个表。初始化datatable时需要传入3个额外的参数：modelName, cols 和searchCols
    '''
    #cols = ['acc_name','primary_phone','mobile','email','fax','id']

    cols = request.GET.getlist('cols')
    print >>sys.stderr, len(cols)
    col_idx = range(len(cols))
    defaultPageSize = 10
    modelName = request.GET['modelName']
    searchCols = request.GET.getlist('searchCols')
    if request.GET.has_key('iDisplayLength'):
        defaultPageSize = int(request.GET['iDisplayLength'])

    startIndex = 0
    if request.GET.has_key('iDisplayStart'):
        startIndex = int(request.GET['iDisplayStart'])
    endIndex = startIndex + defaultPageSize
    modelClass = eval(modelName.capitalize())#getattr(lawaccount.models, modelName)
    q = modelClass.objects.all()
    #print >>sys.stderr, q.query
    query_condition_list = []
    #print >>sys.stderr, 'q genereated !'
    if (request.GET.has_key('sSearch') ):
        if request.GET['sSearch']:
            searchString =  request.GET['sSearch'].capitalize()
            print >>sys.stderr, '======================searching: '+ searchString +'====================='
            #searchColName = searchCols[0]
            query_condition = ""
            #query_condition = [Q({'{0}__istartswith'.format(searchColName):searchString}) for searchColName in searchCols]

            for i in range(len(searchCols)):
                searchColName = searchCols[i]
                if (i ==0 ):
                    query_condition = searchColName + " LIKE '" + searchString +  "%%'"
                else:
                    query_condition += " OR " + searchColName + " LIKE '" + searchString +  "%%'"
            query_condition_list = [query_condition]

    if (request.GET.has_key('parent_model')):
        q_cond = request.GET['parent_model']+'_id = ' +request.GET['parent_id']
        query_condition_list.append(q_cond)


    if len(query_condition_list)>0:
        q = q.extra(where=query_condition_list)
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
    print >>sys.stderr, str(q.query)
    total = q.count()
    result = q[startIndex:endIndex]


    response_dict = {'sEcho':'','iTotalRecords':'','iTotalDisplayRecords':'', 'aaData':''}
    response_dict['sEcho']= request.GET['sEcho']
    response_dict['iTotalRecords']= total
    response_dict['iTotalDisplayRecords'] = total
    aaData = [ dict(dict(zip(col_idx, [getattr(row,colname) for colname in cols] )).items() + {'DT_RowClass':modelName, 'DT_RowId': str(row.id)}.items()) for row in result ]

    #aaData =[ [ col_idx[cols.index(colname)] + ":" + str(getattr(row,colname)) for colname in cols] for row  in result ]
    #[]
    #     for row in result:
#        aaData.append([row.acc_name,row.primary_phone, row.mobile,row.email,row.fax])
    response_dict['aaData']=aaData
    print >> sys.stderr, json.dumps(response_dict)
    return HttpResponse(json.dumps(response_dict), mimetype='application/json')