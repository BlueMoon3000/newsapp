from django.shortcuts import render_to_response

from django.views.generic.base import View

# Create your views here.
class WebTemplateView(View):
    def dispatch(self, request, *args, **kwargs):
        #self.process_request(request)
        context = self.get_context_data(request, *args, **kwargs)
        return self.render(request, context)
    
    def get_context_data(self, request, *args, **kwargs):
        return {}

    def render(self, request, context):
        return render_to_response(self.template_name, context)

class IndexView(WebTemplateView):
    template_name = 'index.html'

    def get_context_data(self, request, *args, **kwargs):
        import wikipedia
        from core.models import *
        from random import randint

        topic = Topic.objects.all()[randint(0,2)]
        wikidata = wikipedia.summary(topic.title)

        return {
            'topic': topic,
            'wikidata': wikidata
        }