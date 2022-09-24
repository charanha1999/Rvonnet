from django.shortcuts import render
from django.views import View

# Create your views here.
class ServicesList(View):

    def get(self, request):
        title = "RVONNET - Services list"
    
        user = request.user.id

        return render(request, 'services_list.html', locals())