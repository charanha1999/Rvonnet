from django.shortcuts import render
from django.views import View

# from rv.settings import STATICFILES_DIRS


# Create your views here.

class Index(View):

    def get(self, request):

        title = 'RVONNET - Home Page'

        user = request.user.id

        # files = STATICFILES_DIRS

        return render(request, 'index.html', locals())



class LogoutUser(View):

    def post(self, request):

        user = request.user.id

