import random

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.models import Blog
from mailling.forms import MaillingForm, MessageForm, ClientForm
from mailling.models import Mailling, Message, Client, Logs
from mailling.services import get_cache_clients, get_cache_messages


class MainView(LoginRequiredMixin, TemplateView):
    template_name = 'mailling/main.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Главная'

        context_data['mailling'] = len(Mailling.objects.all())
        context_data['started_mailling'] = Mailling.objects.filter(is_active=True).count()
        context_data['client'] = len(Client.objects.all())
        context_data['object_list'] = random.sample(list(Blog.objects.all()), 3)
        return context_data


class MaillingCreateView(CreateView):
    model = Mailling
    form_class = MaillingForm
    success_url = reverse_lazy('mailling:maillings')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'uid': self.request.user.id})
        return kwargs


class MaillingListView(LoginRequiredMixin, ListView):
    model = Mailling

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список рассылок'
        return context

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.has_perm('mailling.view_mailling'):
            return Mailling.objects.all()
        queryset = Mailling.objects.filter(user=self.request.user, is_active=True)
        return queryset


class MaillingDetailView(LoginRequiredMixin, DetailView):
    model = Mailling

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object


class MaillingUpdateView(LoginRequiredMixin, PermissionRequiredMixin,  UpdateView):
    model = Mailling
    form_class = MaillingForm
    success_url = reverse_lazy('mailling:maillings')
    permission_required = 'mailling.change_mailling'

    def has_permission(self):
        obj = self.get_object()
        if self.request.user == obj.user or self.request.user.is_staff:
            return True
        return super().has_permission()

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'uid': self.request.user.id})
        return kwargs

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object


class MaillingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailling
    success_url = reverse_lazy('mailling:maillings')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailling:messages')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class MessageListView(LoginRequiredMixin, ListView):
    model = Message

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = get_cache_messages()
        context['title'] = 'Список сообщений'
        return context

    def get_queryset(self):
        if self.request.user.is_staff:
            return Message.objects.all()
        queryset = Message.objects.filter(user=self.request.user)
        return queryset


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailling:messages')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('mailling:messages')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailling:clients')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class ClientListView(LoginRequiredMixin, ListView):
    model = Client

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = get_cache_clients()
        context_data['title'] = 'Список клиентов'
        return context_data

    def get_queryset(self):
        if self.request.user.is_staff:
            return Client.objects.all()
        queryset = Client.objects.filter(mailling__user=self.request.user)
        return queryset


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailling:clients')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mailling:clients')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object


class LogsListView(LoginRequiredMixin, ListView):
    model = Logs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Отчет об отправленных рассылках'
        return context

    def get_queryset(self):
        if self.request.user.is_staff:
            return Logs.objects.all()
        queryset = Logs.objects.filter(mailling__user=self.request.user)
        return queryset
