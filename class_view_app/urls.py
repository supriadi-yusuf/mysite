from django.conf.urls import url

from .views import my_view, MyView, GreetingView, MorningGreetingView, \
    AuthorListView, AuthorDetailView, AuthorListView2, AuthorListView3, \
    AuthorListView4, AuthorListView5, AuthorListView6, \
    ContactView, ThankView, \
    AuthorCreate, AuthorUpdate, AuthorDelete, \
    CommentView, CommentView2, CommentView3, CommentView4,\
    GetCommentView

app_name = 'class-view-app'

urlpatterns = [
    url(r'^function/$', my_view),
    url(r'^class/$', MyView.as_view()),
    url(r'^greeting/$', GreetingView.as_view()),
    url(r'^greeting/morning/$', MorningGreetingView.as_view()),
    url(r'^greeting/afternoon/$', GreetingView.as_view(greeting="Good Afternoon")),
    url(r'^authors/$', AuthorListView.as_view(), name='author-list'),
    url(r'^author/(?P<pk>\d+)/$', AuthorDetailView.as_view(), name='author-detail'),
    url(r'^authors-2/$', AuthorListView2.as_view(), name='author-list-2'),
    url(r'^authors-3/$', AuthorListView3.as_view(), name='author-list-3'),
    url(r'^authors-4/$', AuthorListView4.as_view(), name='author-list-4'),
    url(r'^authors-5/(\w+)/$', # pass positional argument to view via url string
           AuthorListView5.as_view(),
           {'page_title':'Author List 5', 'main_title':'List of Author 5'}, # pass keyword argument to view
           name='author-list-5'),
    url(r'^authors-6/(?P<word>\w+)/$', # pass keyword argument to view via url string
           AuthorListView6.as_view(),
           {'page_title':'Author List 6', 'main_title':'List of Author 6'}, # pass keyword argument to view
           name='author-list-6'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^thanks/$', ThankView.as_view(), name='thanks'),
    url(r'^author/add/$', AuthorCreate.as_view(), name='author-add'),
    url(r'^author/(?P<pk>\d+)/edit/$', AuthorUpdate.as_view(), name='author-edit'),
    url(r'^author/(?P<pk>\d+)/delete/$', AuthorDelete.as_view(), name='author-delete'),
    url(r'^author/(?P<pk>\d+)/comment/$', CommentView.as_view(), name='comment-author'),
    url(r'^author/(?P<pk>\d+)/comment-2/$', CommentView2.as_view(), name='comment-author-2'),
    url(r'^author/(?P<pk>\d+)/comment-3/$', CommentView3.as_view(), name='comment-author-3'),
    url(r'^author/(?P<pk>\d+)/(?P<comment>.+)/show/$', GetCommentView.as_view(), name='display-comment'),
    url(r'^author/(?P<pk>\d+)/comment-4/$', CommentView4.as_view(), name='comment-author-4'),
]
