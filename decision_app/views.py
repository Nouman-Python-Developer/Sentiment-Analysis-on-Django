from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View
# from .models import Analyzer
from .forms import InputForm
from .sentiment_analyses import SentimentAnalysis


# Create your views here.

class MainPageView(View):
    template_name = 'decision_app/main_page.html'
    form_class = InputForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        # print(form)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            sentiment_analysis = SentimentAnalysis(form.data["input_field"])
            result = sentiment_analysis.sentiment()
            return HttpResponse(f"<h1>{result}</h1>")

        return render(request, self.template_name, {'form': form})
