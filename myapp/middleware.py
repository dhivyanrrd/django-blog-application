from django.urls import reverse
from django.shortcuts import redirect

class RedirectAuthenticatedUserMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self, request):
        # check if user is authenticated and trying to access login or register page
        if request.user.is_authenticated:
            # list of paths to restrict for authenticated users
            paths_to_redirect =[reverse('blog:login'), reverse('blog:register')] 
            if request.path in paths_to_redirect:
                return redirect('blog:index')  # redirect to home page
        response = self.get_response(request)
        return response
    
class RedirectUnauthenticatedUserMiddleware:
    def  __init__(self,get_response):
        self.get_response=get_response
    def __call__(self, request):
       restricted_paths=[reverse('blog:dashboard')]
       if not request.user.is_authenticated and request.path in restricted_paths:
           return redirect(reverse('blog:login'))  # redirect to login page
       response = self.get_response(request)
       return response
          