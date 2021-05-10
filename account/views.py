from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from oauth2_provider.models import AccessToken
from django.http import JsonResponse
import requests
import json


@csrf_exempt
def get_user(request):
    access_token=request.POST.get('access_token')
    user_id=AccessToken.objects.get(token=access_token).user_id
    user=list(User.objects.filter(id=user_id).values())
    return JsonResponse(user,safe=False)

@csrf_exempt
def send_sms(request):
    phone=request.POST.get('phone')
    authorization=request.POST.get('authorization')
    message=request.POST.get('message')
    headers = {
        'authorization': authorization,
    }
    data = {
        'sender_id': "TXTIND",
        'message': message,
        'language': 'english',
        'route': 'v3',
        'numbers': phone
    }

    response = requests.post('https://www.fast2sms.com/dev/bulkV2', headers=headers, data=data)
    messageResponse = json.loads(response.text)
    status=messageResponse['message']

    balanceResponse = requests.request("GET",
                                       url="https://www.fast2sms.com/dev/wallet?authorization=tY3qVKk2G4Ol8srpoQ5RLagdAfCwXehNEzx17UPJFiWHTZM9bmi6JojuLUkWIwYfO4hZ3QP9rKmTDpal")
    balance=json.loads(balanceResponse.text)
    result={'status':status,'balance':balance}
    return JsonResponse(result,safe=False)