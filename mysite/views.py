
from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_http_methods


@require_http_methods(['GET'])
def redirection(request):
    ans = 'Допишите в адрес сайта /users, либо /users/by-id/?id="your_id", либо /users/by-login/?login="your_login"'
    return HttpResponse(ans)
