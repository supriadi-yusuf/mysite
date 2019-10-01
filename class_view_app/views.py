from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, \
                                      UpdateView, DeleteView, \
                                      FormMixin
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse_lazy
from django.urls import reverse

# Create your views here.

from .models import Author
from .forms import ContactForm, CommentForm

def my_view(request):
    return HttpResponse("result from function-based view")

class MyView(View):
    def get(self, request):
        return HttpResponse("result from class-based view")

class GreetingView(View):
    greeting = "Good day"

    def get(self, request):
        return HttpResponse(self.greeting)

class MorningGreetingView(GreetingView):
    greeting = "Good Morning"

class MyFormView(View):
    pass

class AuthorListView(ListView):
    model = Author

class AuthorListView2(AuthorListView):
    #context_object_name = 'author_list'
    template_name = 'class_view_app/author_list2.html' # template name

class AuthorListView3(AuthorListView): # use object inheritance to make it simpler
    context_object_name = 'list_of_author' # change variable name for html template
    template_name = 'class_view_app/author_list3.html' # change html template name

class AuthorListView4(ListView):
    queryset = Author.objects.all() # source of data
    context_object_name = 'authors' # name of data list
    template_name = 'class_view_app/author_list4.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AuthorListView4, self).get_context_data(*args,**kwargs)
        context['page_title'] = 'Author List 4' # pass value into template
        context['main_title'] = 'List of Author 4' # pass value into template
        return context

class AuthorListView5(ListView):
    context_object_name = 'authors' # name of data list
    template_name = 'class_view_app/author_list4.html'

    def get_context_data(self, *args, **kwargs):
        page_title = self.kwargs['page_title'] # get keyword argument from url config
        main_title = self.kwargs['main_title'] # get keyword argument from url config
        context = super(AuthorListView5, self).get_context_data(*args,**kwargs)
        context['page_title'] = page_title
        context['main_title'] = main_title
        return context

    def get_queryset(self, *args, **kwargs):
        word = self.args[0] # get positional argument from url config
        return Author.objects.filter(name__icontains = word )

class AuthorListView6(AuthorListView5):
    def get_queryset(self, *args, **kwargs):
        word = self.kwargs['word'] # get keyword argument from url config
        return Author.objects.filter(name__icontains = word )

class AuthorDetailView(DetailView):
    model = Author

class ContactView(FormView):
    template_name = 'class_view_app/contact.html'
    form_class = ContactForm
    success_url = '/class-view/thanks/'

    def form_valid(self, form):
        #print(dir(self))
        form.send_email()
        return super(ContactView, self).form_valid(form)

class ThankView(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Thank you')

class AuthorCreate(CreateView):
    model = Author
    fields = ['salutation', 'name', 'email']

class AuthorUpdate(UpdateView):
    model = Author
    fields = ['salutation', 'name', 'email']

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('class-view-app:author-list')

class CommentView(DetailView):
    form_class = CommentForm
    model = Author
    template_name_suffix = '_with_comment'

    def get_context_data(self, **kwargs):
        context = super(CommentView, self).get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context

class CommentView2(DetailView):
    form_class = CommentForm
    model = Author
    template_name_suffix = '_with_comment'

    def get_context_data(self, **kwargs):
        context = super(CommentView2, self).get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object() # mandatory before calling mixing method
        params = self.get_context_data()
        form = self.form_class( request.POST)
        if form.is_valid():
            params['comment'] = form.cleaned_data['comment']

        params['form'] = form
        return render( request, self.get_template_names(), params)

class CommentView3(FormMixin,DetailView):
    form_class = CommentForm
    model = Author
    template_name_suffix = '_with_comment'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object() # mandatory before calling mixing method
        params = self.get_context_data()
        form = params['form']
        if form.is_valid():
            params['comment'] = form.cleaned_data['comment']

        return render(request, self.get_template_names(), params)

class GetCommentView(DetailView):
    form_class = CommentForm
    model = Author
    template_name_suffix = '_with_comment'

    def get_context_data(self, **kwargs):
        context = super(GetCommentView, self).get_context_data(**kwargs)

        if 'comment' in self.kwargs.keys():
            context['comment'] = self.kwargs['comment']
        else:
            context['form'] = self.form_class()

        return context

class ShowCommentView(SingleObjectMixin, FormView):
    form_class = CommentForm
    model = Author
    template_name_suffix = '_with_comment'

    def post(self, request, *args, **kwargs):
        print(dir(self))
        self.object = self.get_object()
        return super( ShowCommentView, self).post(request, *args, **kwargs)

    def form_valid(self,form):
        self.comment = form.cleaned_data['comment']
        return super(ShowCommentView, self).form_valid(form)

    def get_template_names(self):
        return ['class_view_app/' + self.model.__name__.lower() + self.template_name_suffix + '.html',]

    def get_success_url(self):
        return reverse('class-view-app:display-comment',
        kwargs={'pk' : self.object.pk, 'comment' : self.comment})

class CommentView4(View):
    def get(self, request, *args, **kwargs):
        view = GetCommentView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ShowCommentView.as_view()
        return view(request, *args, **kwargs)
