from django.urls import path

from . import views


urlpatterns = [
	path('',views.Adder.as_view(), name='add'),
	path('search',views.Searcher.as_view(),name='search')
]