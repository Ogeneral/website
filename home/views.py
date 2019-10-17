from django.shortcuts import render
 
# Create your views here.
def home(request):
	  return render(request, 'new.html')
	  
def gallery(request):
	return render(request, 'gallery.html')
	           
def wywlu(request):
	return render(request, 'index.html')

def more(request):
	return render(request, 'index2.html')