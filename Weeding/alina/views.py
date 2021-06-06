from django.core.mail import message
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import *


def index(request):
    return render(request, 'alina/index.html')
#
#
# def get_context_data(self, *, object_list=None, **kwargs):
#     context = super().get_context_data(**kwargs)
#     context[''] = self.get_upper(FormView.objects.get(pk=self.kwargs['category_id']))
#     return context


def Contact(request):
    form = ContactForm
    data = {
        'form' : form
    }
    return render(request, 'alina/index.html')






# class ContactFormView(FormView):
#     form_class = ContactForm
#     template_name = 'alina/contact.html'
#     success_url = reverse_lazy('home')
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title="Обратная связь")
#         return dict(list(context.items()) + list(c_def.items()))
#
#     def form_valid(self, form):
#         print(form.cleaned_data)
#         return redirect('home')
