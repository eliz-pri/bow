from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView,FormView
from bow.models import Restaurant,UserBW2,User
from bow.forms import ResForm,UserForm
from django.views.decorators.http import require_POST
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext,Context
from django.shortcuts import render_to_response,redirect
import datetime
import time

@require_POST
def my_view_that_updates_plist(request,name):
    
    if request.method == 'POST':
    	
    	print name
    	username = name
        print request.POST
        if 'plist[]' in request.POST:
            plist = request.POST.getlist('plist[]')
            
            it = iter(plist)
            for rest1,rest2 in zip(it,it):
            	print "--------",rest1
            	UserBW2.objects.create(user=username,btr_res=rest1,wrs_res=rest2)
            return HttpResponse('success')

    return HttpResponse('FAIL!!!!!')



class ResListView(ListView):
	template_name = 'sort.html'

	def get_queryset(self):
		self.queryset = Restaurant.objects.all()
		print self.queryset
		return self.queryset

	def get_context_data(self,**kwargs):
		context = super(ResListView,self).get_context_data(**kwargs)
		ts = time.time()
		print ts
		now = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M')
		print now
		
		self.username = "rand"
	
		self.username  = self.username+'-'+now		
		print self.username
                User.objects.create(name=self.username)        
		#username = self.kwargs['name']
		context['name'] = self.username
		return context

        def get_success_url(self):
		return '/rate/results/'


class ResultsView(FormView):
	template_name = 'results.html'
	form_class = UserForm

        def form_valid(self,form):
 	    	    self.object = form.save(commit=True)
                    return super(ResultsView,self).form_valid(form)

        def get_success_url(self):
           return '/rate/thanks/'

        def get_context_data(self,**kwargs):
		context = super(ResultsView,self).get_context_data(**kwargs)
		bw2_all = UserBW2.objects.all()
		res = Restaurant.objects.all()
		btr = []
		wrs = []
		score = {}
		#for restnt in res:
         #          score[restnt.res_name] = []
                
                #count_up = 1 
                #count_down = 1
                for obj in bw2_all:
                   print "==",obj.btr_res
        	   btr.append(str(obj.btr_res).strip())
        	   wrs.append(str(obj.wrs_res).strip())
        	   

                #print "score=",score
                print btr,wrs
                for restnt in res:
                	print restnt.res_name
                        score[restnt.res_name] = (btr.count(restnt.res_name),wrs.count(restnt.res_name))
                print score
	        context['score'] = score
	        return context

    


class RegisterView(FormView):
	template_name = 'index.html'
	form_class = UserForm

	def get_success_url(self):
		return '/rate/%s/'%self.username

	def form_valid(self, form):
		ts = time.time()
		print ts
		now = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M')
		print now
		self.username = form.cleaned_data['name']
		if self.username == '':
			self.username = "rand"
		self.object = form.save(commit=False)
		self.username  = self.username+'-'+now
		print self.username
                self.email = form.cleaned_data['email']
                self.object.name = self.username
                self.object = form.save(commit=True)
                return super(RegisterView,self).form_valid(form)

