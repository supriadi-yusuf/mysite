from django.shortcuts import render, redirect

from django.contrib.auth.mixins import LoginRequiredMixin, \
     UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout, \
                                update_session_auth_hash

# Create your views here.

from . import forms

class MyLoginView(View):
    def get(self, request):
        form = forms.LoginForm(initial={'dest_url':request.GET['next']})
        return render( request, 'authenticate_app/login.html', {'form':form})

    def post(self, request):
        error_msg = None

        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                dest_url = form.cleaned_data['dest_url']
                login( request, user)
                #return HttpResponseRedirect(dest_url)
                return redirect(dest_url)
            else:
                error_msg = 'user name or password does not match'

        return render( request,'authenticate_app/login.html',
                       {'form':form, 'error_msg':error_msg})

class MyLoginRequiredView(LoginRequiredMixin, View):
    login_url = reverse_lazy('authenticate-app:login')
    #redirect_field_name = 'next' # default

    #def get_login_url(self):
    #    return reverse('authenticate-app:login')

    def get(self, request):
        #print(dir(self))
        return render( request, 'authenticate_app/login-required.html')

class MyLoginRequiredView2(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request):
        #print(dir(self))
        return render( request, 'authenticate_app/login-required.html')

class MyLoginRequiredView3(LoginRequiredMixin, View):
    raise_exception = True

    def handle_no_permission(self):
        return HttpResponse('handle no permission in %s' % self.request.path)

    def get(self, request):
        #print(dir(self))
        return render( request, 'authenticate_app/login-required.html')

class MyLogoutView(View):
    def get(self, request):
        logout(request)
        #return redirect(reverse_lazy('authenticate-app:login-required'))
        return redirect(reverse('authenticate-app:login-required'))

def test_email(view_obj):
    if view_obj.request.user.is_authenticated:
        if view_obj.request.user.email.endswith('yahoo.com'):
            return True
        else:
            logout(view_obj.request)

    return False

class MyUserPassesTestView( UserPassesTestMixin, View):
    login_url = reverse_lazy('authenticate-app:login')
    #redirect_field_name = 'next' # default
    #test_func = test_email # we can use this
    #test_func = [test1, test2, ...] # we can use this

    #def test_func(self): # we can use this
    #    return test_email(self)

    def get_test_func(self): # we can use this
        return lambda : test_email(self)

    def get(self, request):
        return HttpResponse('ok ... user passes test ... thanks')

class MyPermissionRequiredView( PermissionRequiredMixin, View):
    login_url = reverse_lazy('authenticate-app:login')
    #redirect_field_name = 'next' # default
    permission_required = 'mymodel.can_print'
    #permission_required = ['mymodel.can_print', 'mymodel.can_publish']

    def get(self, request):
        return HttpResponse('ok ... permission required ... thanks')

class MyChangePasswordView(View):
    def get(self, request, username, password, newpassword):
        logout(request)

        user = authenticate(username=username, password=password)
        if user is not None :
            login(request, user)
            user.set_password(newpassword) # change password
            user.save()
            return redirect(reverse('authenticate-app:login-required'))
        else:
            return HttpResponse("Username or password error")

class MyChangePasswordView2(View):
    def get(self, request, username, password, newpassword):
        logout(request)

        user = authenticate(username=username, password=password)
        if user :
            login(request, user)
            user.set_password(newpassword) # change password
            user.save() # save changing
            update_session_auth_hash( request, user) # update session hash
            return redirect(reverse('authenticate-app:login-required'))
        else:
            return HttpResponse("Username or password error")

class MyAuthFormView(View):
    form = None
    def get(self, request):
        myform = self.form()
        return render(request, 'authenticate_app/auth-form.html', {'form':myform})
