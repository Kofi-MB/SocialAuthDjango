from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from oauth2_provider.models import AccessToken
from django.http import JsonResponse
import requests
import json





@csrf_exempt
def get_user(request):
    access_token=request.POST.get('access_token')
    try:
        user_id=AccessToken.objects.get(token=access_token).user_id
        user=list(User.objects.filter(id=user_id).values())
        return JsonResponse(user,safe=False)
    except:
        return JsonResponse('invalidate-sessions',safe=False)

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


@csrf_exempt
def test(request):
    grant_type='authorization_code'
    code='AQT6UilUxd-rKI0twrNaKtLOL9TlAcz1XjietLMeens9pBJ_LhAo3e5zHY0eN9VmAGPm8-bfwdNHdBtDzImpaMX7_KPFZgoHYDUBBkNrsn_JhImX28Mi9v6CC4mrdspFG8vrl17YNP_2guRij-DTYSMBgxIKMP89TQXl6XdOsd9xtKHBYyi8EFBp2ksNB2c_rXIzqg1uXup4zhL8CE8'
    client_id='86bf5uhj67ssy0'
    client_secret='1Du0YxPl4wz2osAJ'
    redirect_uri='http://localhost:3000/linkedin'

    data=requests.request('GET',url=f"https://www.linkedin.com/oauth/v2/accessToken?grant_type={grant_type}&code={code}&client_id={client_id}&client_secret={client_secret}&redirect_uri={redirect_uri}")
    print(data.text)
    data=json.loads(data.text)

    url = 'http://127.0.0.1:8000/auth/convert-token'

    print(data['access_token'])
    data = {
        'token': data['access_token'],
        'backend':'linkedin-oauth2',
        'grant_type':'convert_token',
        'client_id':'9l6eJ9iiCVedDF8tsvP8SvrfOqBbPn9wA4xu93iv',
        'client_secret':'NjNuiMH2p15cuVygvl4LV9RxtmJi28J02ZBUyiSAQYQfEL4xj5SdNEs1UvLv09zCaAzWuYVNe7oQIn5TYIvoocDyO792HPLkOhiv1DrDHZnJg3HenXkXggaNZ5EqKxUP'
            }


    converttoken = requests.post(url, data=data)
    print(converttoken.text)
    return JsonResponse(True,safe=False)