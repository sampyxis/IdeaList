from django.views.generic.base import TemplateView

from TaskLists.models import *

class HomePageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['tasks'] = Tasks.objects.all()[:5]
        return context