from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView

#Class MainView  - start page
class MainView(LoginRequiredMixin, TemplateView):

   template_name = 'index.html'