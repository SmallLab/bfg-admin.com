from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.base import TemplateView
from django.contrib.auth.models import Permission, User
from mainadmin.models import Regions

#Class MainView  - start page
class MainView(LoginRequiredMixin, TemplateView):

   template_name = 'index.html'

#Class UsersWork  - users page
class UsersWork(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):

   permission_required = "auth.change_user"
   template_name = 'users.html'
   login_url = '/'

   def get_context_data(self, **kwargs):
      content = super(UsersWork, self).get_context_data(**kwargs)
      content['users_list'] = User.objects.using('default').all()
      content['regions'] = Regions.objects.all()
      return content