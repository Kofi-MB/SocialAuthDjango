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
    headers = {
        'authorization': 'tY3qVKk2G4Ol8srpoQ5RLagdAfCwXehNEzx17UPJFiWHTZM9bmi6JojuLUkWIwYfO4hZ3QP9rKmTDpal',
    }
    data = {
        'sender_id': "TXTIND",
        'message': 'lore, ipsium kwhkvfkwb wkbf wm fkw  fekbiwb flwi fec ibwfgweefiw fwh hf9  hg fbwf8o3t4r3 99r 93t3ihh h3hh9p3hyt 3p98h ihh ho h2hih wbf bwg jiwah fqwljbfiiwbk;f',
        'language': 'english',
        'route': 'v3',
        'numbers': '9178595277'
    }

    response = requests.post('https://www.fast2sms.com/dev/bulkV2', headers=headers, data=data)
    messageResponse = json.loads(response.text)
    status=messageResponse['message']
    balanceResponse = requests.request("GET",
                                       url="https://www.fast2sms.com/dev/wallet?authorization=tY3qVKk2G4Ol8srpoQ5RLagdAfCwXehNEzx17UPJFiWHTZM9bmi6JojuLUkWIwYfO4hZ3QP9rKmTDpal")
    balance=json.loads(balanceResponse.text)
    result={'status':status,'balance':balance}
    return JsonResponse(result,safe=False)