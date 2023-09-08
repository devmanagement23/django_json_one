from django.http import HttpResponse,JsonResponse

def index(request):
    comments =[
        {'name':'Ram Suryavanshi',
         'username':'rama',
         'text':'I will rule',
         },
         {'name':'Lakshman Kumar',
         'username':'Lakshman',
         'text':'Patience is the key to clear thought',
         },
    ]

    return JsonResponse({'comments':comments})