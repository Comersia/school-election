from django.urls import path, include
from . import views


app_name = 'election'
urlpatterns = [
	path('accounts/', include('django.contrib.auth.urls')),
    path('candidat/<int:pk>/', views.DetailView.as_view(), name='candidat_detail'),
    path('', views.ListView.as_view(), name='candidat_list'),
    path('vote/', views.voting, name='vote'),
    path('simple_upload/', views.simple_upload, name='simple_upload')
]
