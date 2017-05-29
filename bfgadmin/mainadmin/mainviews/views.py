from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import redirect
from django.core.cache import cache
from mainadmin.models import (TypeSentence, Categories, Regions, Sentence)


#Class MainView  - start page


class MainView(LoginRequiredMixin, TemplateView):

   template_name = 'index.html'

   # def get_context_data(self, **kwargs):
   #    content = super(MainView, self).get_context_data(**kwargs)
   #    content['count_new_sentences'] = Sentence.objects.filter(on_moderation=0).count()
   #    return content


"""
    Work with users site
"""

#Class UsersWork  - All users page

class UsersWork(LoginRequiredMixin, PermissionRequiredMixin, ListView):

   permission_required = "auth.change_user"
   template_name = 'users/users.html'
   login_url = '/'
   queryset = User.objects.using('default').all()
   context_object_name = 'users_list' #or for custom paginate page_obj in template
   paginate_by = 10


class UserDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):

    login_url = '/'
    permission_required = "auth.change_user"
    queryset = User.objects.using('default').all()
    context_object_name = 'user_detail'
    template_name = 'users/user_detail.html'


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


"""
    Work with CTR(Category, Type sentences, Regions)
"""

class CtrWork(LoginRequiredMixin, PermissionRequiredMixin, ListView):

    data_db = {'typesent':TypeSentence, 'category':Categories, 'regions':Regions}
    data_slug = {'typesent': 'Type Sentence', 'category': 'Categories', 'regions': 'Regions'}
    permission_required = "auth.change_user"
    login_url = '/'
    template_name = 'ctr/ctrwork.html'
    context_object_name = 'ctr_list'

    def get_queryset(self):
        return self.data_db[self.kwargs['type_slug']].object.all()

    def get_context_data(self, **kwargs):
        context = super(CtrWork, self).get_context_data(**kwargs)
        context['tab'] = True
        context['slug'] = self.data_slug[self.kwargs['type_slug']]
        context['key_slug'] = self.kwargs['type_slug']
        return context

class AjaxCtrActive(LoginRequiredMixin, PermissionRequiredMixin, View):

    permission_required = "auth.change_user"
    data_db = {'typesent': TypeSentence, 'category': Categories, 'regions': Regions}

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            ctr = self.data_db[self.request.GET['key_ctr']].object.get(pk=kwargs['pk'])
            if ctr.is_active:
                ctr.is_active = False
                data = {"status":False}
            else:
                ctr.is_active = True
                data = {"status": True}
        ctr.save(using='default')
        cache.set('data_ctr', '')
        return JsonResponse(data)

class AjaxCtrNew(LoginRequiredMixin, PermissionRequiredMixin, View):

    permission_required = "auth.change_user"
    data_db = {'typesent': TypeSentence, 'category': Categories, 'regions': Regions}

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            new_ctr =  self.data_db[self.request.GET['key_ctr']](
                name=self.request.GET['name'],
                link_name=self.request.GET['link'],
                is_active=False
            )
            new_ctr.save()
            cache.set('data_ctr', '')
        return JsonResponse({"status": True, 'id':new_ctr.id})

class CtrDelete(LoginRequiredMixin, PermissionRequiredMixin, View):

    permission_required = "auth.change_user"
    data_db = {'typesent': TypeSentence, 'category': Categories, 'regions': Regions}
    login_url = '/'

    def get(self, request, *args, **kwargs):
        self.data_db[self.request.GET['key_ctr']].object.get(pk=kwargs['pk']).delete()
        redirect_url = '/ctr/'+self.request.GET['key_ctr']+'/'
        cache.set('data_ctr', '')
        return redirect(redirect_url)

    def get_context_data(self, **kwargs):
        context = super(CtrDelete, self).get_context_data(**kwargs)
        context['tab'] = True
        return context

class AjaxNumNewCategories(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "auth.change_user"

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            ctr = Categories.object.get(id=self.request.GET['id'])
            if self.request.GET['name_field'] == 'max_num':
                ctr.max_num = self.request.GET['num']
            else:
                ctr.paid_num = self.request.GET['num']
            ctr.save(using='default')

            return JsonResponse({'status':True})