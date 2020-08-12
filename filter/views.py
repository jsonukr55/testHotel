from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse

from filter.models import Filter
from account.models import Account


def filter_view(request):

	context = {}

	Filter = get_object_or_404(Filter)
	context['Filter'] = Filter

	return render(request, 'filter/filter.html', context)





def get_filter_queryset(query=None):
	queryset = []
	queries = query.split(" ") 
	for q in queries:
		posts = Filter.objects.filter(
				Q(title__icontains=q) | 
				Q(body__icontains=q)
			).distinct()

		for post in posts:
			queryset.append(post)

	return list(set(queryset))	
