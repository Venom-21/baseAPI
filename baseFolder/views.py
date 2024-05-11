from django.http import JsonResponse

def apiCheck(request):
    data = {'message': 'Hey, Fuckers!'}
    return JsonResponse(data)
