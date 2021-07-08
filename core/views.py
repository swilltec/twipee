from django.shortcuts import render
from django.views.generic import ListView

from .models import Tweet


class HomeView(ListView):
    template_name = 'index.html'
    paginate_by = 20
    
    def get_queryset(self, *args, **kwargs):
        return Tweet.objects.all().prefetch_related('link_set')


class TagsView(ListView):
    template_name = 'tags.html'
    paginate_by = 20
    
    def get_queryset(self, *args, **kwargs):
        tag = f"#{self.kwargs.get('tag')}"
        return Tweet.objects.filter(tip__contains=tag).prefetch_related('link_set')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.kwargs.get('tag')
        return context
        
    
