from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib.auth import forms as auth_forms
from . import views

app_name = 'authenticate-app'

urlpatterns_auth_view = [
    url(r'^login/$',
        auth_views.LoginView.as_view(template_name='authenticate_app/auth/login.html')),
    url(r'^logout/$',
        auth_views.LogoutView.as_view(template_name='authenticate_app/auth/logout.html')),
    url(r'^password-change/$',
        auth_views.PasswordChangeView.as_view(template_name='authenticate_app/auth/password_change_form.html')),
    url(r'^password-change-done/$',
        auth_views.PasswordChangeDoneView.as_view(template_name='authenticate_app/auth/password_change_done.html')),
    url(r'^password-reset/$',
        auth_views.PasswordResetView.as_view(template_name='authenticate_app/auth/password_reset_form.html')),
]

urlpatterns_auth_form = [
    url(r'^authentication/$',
        views.MyAuthFormView.as_view(form=auth_forms.AuthenticationForm)),
    url(r'^user-creation/$',
        views.MyAuthFormView.as_view(form=auth_forms.UserCreationForm)),
]

urlpatterns = [
    url(r'^login/$', views.MyLoginView.as_view(), name='login'),
    url(r'^login-required/$', views.MyLoginRequiredView.as_view(), name='login-required'),
    url(r'^login-required-2/$', views.MyLoginRequiredView2.as_view(), name='login-required-2'),
    url(r'^login-required-3/$', views.MyLoginRequiredView3.as_view(), name='login-required-3'),
    url(r'^logout/$', views.MyLogoutView.as_view(), name='logout'),
    url(r'^user-passes-test/$', views.MyUserPassesTestView.as_view(), name='user-passes-test'),
    url(r'^permission-required/$', views.MyPermissionRequiredView.as_view(), name='permission-required'),
    url(r'^change-password/(?P<username>\w+)/(?P<password>\w+)/(?P<newpassword>\w+)/$',
        views.MyChangePasswordView.as_view(), name='change-password'),
    url(r'^change-password-2/(?P<username>\w+)/(?P<password>\w+)/(?P<newpassword>\w+)/$',
        views.MyChangePasswordView2.as_view(), name='change-password-2'),
    url(r'^change-password-2/(?P<username>\w+)/(?P<password>\w+)/(?P<newpassword>\w+)/$',
        views.MyChangePasswordView2.as_view(), name='change-password-2'),
    url(r'^auth/', include(urlpatterns_auth_view)),
    url(r'^auth-form/', include(urlpatterns_auth_form)),

]
