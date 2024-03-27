from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import PostCreateForm, PostUpdateForm
from .models import Post, Category
from ..services.mixins import AuthorRequiredMixin


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 3
    queryset = Post.custom.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context


class PostFromCategoryView(ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    category = None
    paginate_by = 2

    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['slug'])
        queryset = Post.custom.filter(category__slug=self.category.slug)
        if not queryset:
            sub_cat = Category.objects.filter(parent=self.category)
            queryset = Post.custom.filter(category__in=sub_cat)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.category.title
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_create.html'
    form_class = PostCreateForm
    success_url = reverse_lazy('home')
    login_url = 'home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class PostUpdateView(AuthorRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'blog/post_update.html'
    context_object_name = 'post'
    login_url = 'home'
    success_message = 'Запись успешно обновлена'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Обновление статьи {self.object.title}'
        return context

    def form_valid(self, form):
        form.instance.updater = self.request.user
        return super().form_valid(form)
