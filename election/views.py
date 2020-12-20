from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from .models import Candidat, Election 
from .forms import VoteForm
from django.utils import timezone
from django.conf import settings
from . import logik

class DetailView(generic.DetailView):
	model = Candidat


class ListView(generic.ListView):
	model = Candidat


def voting(request):
	elections = Election.objects.all()
	for election in elections:
		if election.start_time <= timezone.now() <= election.end_time:
			now_election = election
			break
	else:
		return render(request, 'election/no_elections_now.html')

	if request.method == "POST":
		form = VoteForm(request.POST)
		if form.is_valid():
			vote = form.save(commit=False)
			vote.voted_time = timezone.now()
			vote.user = request.user.profile
			vote.save()
			request.user.profile.is_voted = True
			request.user.save()
			return redirect('election:vote')
	else:
		form = VoteForm()
	return render(request, 'election/voting.html', {'form': form, 'election': now_election})


def simple_upload(request):
	if request.method == 'POST' and request.FILES['myfile']:
		myfile = request.FILES['myfile']
		uploaded_file_url = logik.register_file(myfile)
		return render(request, 'election/simple_upload.html', {
			'uploaded_file_url': uploaded_file_url
		})
	return render(request, 'election/simple_upload.html')
