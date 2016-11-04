from django.http import *
def view_name(func):
	def wrapper(request,*arges,**kw):
		dic={}
		if request.session.has_key('uname'):
			uname = request.session['uname']
			dic = {
				'data':uname
			}
			return func(request,dic,*arges,**kw)
		return func(request,dic,*arges,**kw)
	
	return wrapper

def name_yz(func):
	def wrapper(request,*arges,**kw):
		if request.session.has_key('unmme'):
			return func(request,*arges,**kw)
		return redirect(reverse('main:login'))
	return wrapper

