from django.shortcuts import render, get_object_or_404
from submissions.forms import CardSubmission
from submissions.models import magic_card
from game.models import Game
from django.views.generic import TemplateView, DetailView, ListView, FormView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model

# Create your views here.
user = get_user_model()

class WaitingSubmissions(TemplateView):
    template_name = 'submissions/waiting_submissions.html'

class CardSubmissionView(UpdateView):
    model = magic_card
    template_name = 'submissions/card_submission.html'
    success_url = reverse_lazy('submissions:waiting_submissions')
    form_class = CardSubmission

    def form_valid(self, form):
        form.instance.submitted = True
        subject = 'A card has been submitted'
        message = ('Follow the link to view the card' + "\n <href= 'http://www.nerdsconamigos.com/submissions/card_detail/" + str(form.instance.pk)+"'>")
        form.instance.game.notify_players(subject, message)
        return super().form_valid(form)

class CardDetailView(DetailView):
    context_object_name = 'card_details'
    model = magic_card
    template_name = 'submissions/card_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


