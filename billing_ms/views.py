from django.shortcuts import render

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Invoice

@csrf_exempt  # desactiva la verificación CSRF (solo para pruebas)
def invoices(request):
    if request.method == 'GET':
        data = list(Invoice.objects.values())
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        try:
            body = json.loads(request.body)
            invoice = Invoice.objects.create(
                client_name=body['client_name'],
                amount=body['amount']
            )
            return JsonResponse({'message': 'Factura creada', 'id': invoice.id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
