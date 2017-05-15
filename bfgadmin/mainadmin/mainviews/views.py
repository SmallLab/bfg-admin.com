from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import Permission, User
from django.http import JsonResponse


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


class AjaxUserIsActiveView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "auth.change_user"
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            user = User.objects.using('default').get(pk=kwargs['pk'])
            if user.is_active:
                user.is_active = False
                user.last_name = 'Anonimus'
                data = {"status":False}
            else:
                user.is_active = True
                user.last_name = 'Anonimus200'
                data = {"status": True}
        user.save(using='default')
        return JsonResponse(data)