from django.shortcuts import render
from django.views import View


# Create your views here.

class ProductsList(View):

    def get(self, request):
        title = "RVONNET - Products List"

        # files_list = STATICFILES_DIRS

        return render(request, 'products_list.html', locals())


