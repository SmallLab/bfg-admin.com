from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import Permission, User
from mainadmin.models import Regions


#Class MainView  - start page


class MainView(LoginRequiredMixin, TemplateView):

   template_name = 'index.html'



"""
    Work with users site
"""

#Class UsersWork  - All users page

class UsersWork(LoginRequiredMixin, PermissionRequiredMixin, ListView):

   permission_required = "auth.change_user"
   template_name = 'users.html'
   login_url = '/'
   queryset = User.objects.using('default').all()
   context_object_name = 'users_list' #or for custom paginate page_obj in template
   paginate_by = 2

   # def get_context_data(self, **kwargs):
   #    content = super(UsersWork, self).get_context_data(**kwargs)
   #    content['users_list'] = User.objects.using('default').all()
   #    return content


class UserDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):

    login_url = '/'
    permission_required = "auth.change_user"
    queryset = User.objects.using('default').all()
    context_object_name = 'user_detail'
    template_name = 'user_detail.html'