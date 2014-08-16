from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView
from bow.models import Restaurant,UserBW2
from bow.forms import ResForm
from django.views.decorators.http import require_POST
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.shortcuts import render_to_response,redirect


def login_user(request):
    
    if request.method == 'POST':
    	
       	username = request.POST['username']
     	password = request.POST['password']
     	print username,password
     	user = authenticate(username=username, password=password)
     	print user
     	if user is not None:
         	if user.is_active:
           		login(request, user)
           		return HttpResponseRedirect('/about/')
    
    return render_to_response('login.html', context_instance=RequestContext(request))


@require_POST
def my_view_that_updates_plist(request):
    
    if request.method == 'POST':
        print request.POST
        if 'plist[]' in request.POST:
            plist = request.POST.getlist('plist[]')
            
            it = iter(plist)
            for rest1,rest2 in zip(it,it):
            	print str(rest1),rest2
            	#restobj1 = Restaurant.objects.filter(res_name=rest1)
            	#restobj2 = Restaurant.objects.filter(res_name__exact=str(rest2))
            	#print restobj1,restobj2
            	UserBW2.objects.create(user=request.user,btr_res=rest1,wrs_res=rest2)
            return HttpResponse('success')

    return HttpResponse('FAIL!!!!!')




class ResListView(ListView):
	template_name = 'sort.html'

	def get_queryset(self):
		self.queryset = Restaurant.objects.all()
		print self.queryset
		return self.queryset
