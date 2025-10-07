@csrf_exempt
def validate_client(request):
    body = json.loads(request.body or '{}')
    body["mock_type"] = "payment"
    return True

@csrf_exempt
def trib_calc(request):
    body = json.loads(request.body or '{}')
    body["mock_type"] = "user"
    return True
