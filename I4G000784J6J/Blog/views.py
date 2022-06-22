from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from Blog.models import Post


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "Blog/post_list"


class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url: reverse_lazy("Blog:all")
    template_name = " Blog/post_form"




class PostDetailView(DetailView):
    model = Post
    template_name = " blog/post_detail"




class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("Blog:all")
    template_name = "blog/post_form"




class PostDeleteView(DeleteView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("Blog:all")
    template_name = "blog/post_confirm_delete"

