from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from oauth2_provider.models import AccessToken
from django.http import JsonResponse



@csrf_exempt
def get_user(request):
    access_token=request.POST.get('access_token')
    user_id=AccessToken.objects.get(token=access_token).user_id
    user=list(User.objects.filter(id=user_id).values())
    return JsonResponse(user,safe=False)