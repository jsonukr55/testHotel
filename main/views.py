from django.shortcuts import render




def home_screen_view(request):

	return render(request,"main/home.html",{})
