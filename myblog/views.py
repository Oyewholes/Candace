from django.views.generic import ListView, DetailView, TemplateView, FormView
from .models import Post, Comment
from .forms import CommentForm, SubscriberForm
from django.shortcuts import get_list_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy


class Homepage(TemplateView):
    template_name = 'myblog/index.html'

class PostListView(ListView):
    model = Post
    template_name = 'myblog/post_list.html'
    context_object_name = 'posts'


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'myblog/post_detail.html'
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['comment_form'] = CommentForm()
        return context
    
    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            # Redirect to the same page after successful form submission
            return redirect('myblog:post_detail', pk=post.pk)
        else:
            # If the form is not valid, re-render the template with form errors
            context = self.get_context_data(**kwargs)
            context['comment_form'] = form
            return self.render_to_response(context)

    

class SubscribeView(FormView):
    template_name = 'myblog/index.html'
    form_class = SubscriberForm
    success_url= reverse_lazy('myblog:subscribe_success')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class SubscribeSuccessView(TemplateView):
    template_name = 'myblog/subscribe_success.html'





# def subscribe(request):
#     if request.method == 'POST':
#         form = SubscriberForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # Add logic for sending confirmation email, etc.
#             return redirect('subscribe_success')
#     else:
#         form = SubscriberForm()
#     return render(request, 'index.html', {'form': form})

# def subscribe_success(request):
#     return JsonResponse({'success':True})
