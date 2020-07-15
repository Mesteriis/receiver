from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json, requests



@csrf_exempt
@require_POST
def bx24(request):
    data = request.POST
    key = data['auth[application_token]']             # ключ исходящего хука
    lead_id = data['data[FIELDS][ID]']                # id лида, который был обновлен
    response = requests.get('https://<Your_bitrix24_domain_name>/rest/<user_id>/<autorization_code>/crm.lead.get/', {'id': lead_id}) # исходящий хук к обновленному лиду
    print()
    if key == '**********':    # ключи хуков
        print(response.json()['result']['STATUS_ID']) # статус обновленного лида
    else:
        print('Fail!')
    print()
    return HttpResponse('success')

