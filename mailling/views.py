import random

from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.models import Blog
from mailling.forms import MaillingForm, MessageForm, ClientForm
from mailling.models import Mailling, Message, Client, Logs
from mailling.services import send_mailling, get_cache_clients, get_cache_messages


class MainView(TemplateView):
    template_name = 'mailling/main.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Главная'

        context_data['mailling'] = len(Mailling.objects.all())
        context_data['started_mailling'] = Mailling.objects.filter(status=True).count()
        context_data['client'] = len(Client.objects.all())
        # context_data['object_list'] = random.sample(list(Blog.objects.all()), 3)
        return context_data


class MaillingCreateView(CreateView):
    model = Mailling
    form_class = MaillingForm
    success_url = reverse_lazy('mailling:maillings')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'uid': self.request.user.id})
        return kwargs


class MaillingListView(ListView):
    model = Mailling

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список рассылок'
        return context


class MaillingDetailView(DetailView):
    model = Mailling


class MaillingUpdateView(UpdateView):
    model = Mailling
    form_class = MaillingForm
    success_url = reverse_lazy('mailling:maillings')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'uid': self.request.user.id})
        return kwargs

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object


class MaillingDeleteView(DeleteView):
    model = Mailling
    success_url = reverse_lazy('mailling:maillings')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailling:messages')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class MessageListView(ListView):
    model = Message

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = get_cache_messages()
        context['title'] = 'Список сообщений'
        return context


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailling:messages')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailling:messages')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailling:clients')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ClientListView(ListView):
    model = Client

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = get_cache_clients()
        context_data['title'] = 'Список клиентов'
        return context_data


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailling:clients')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailling:clients')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object


class LogsListView(ListView):
    model = Logs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Отчет об отправленных рассылках'
        return context
