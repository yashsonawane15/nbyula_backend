from json import JSONDecodeError
from django.http import JsonResponse
import json
import jwt
from django.conf import settings
from jwt import InvalidSignatureError

AUTH_HEADER = "HTTP_AURHORIZATION"

def validate_payload(func):
    def wrapper(*args, **kwargs):
        view = args[0]
        request = args[1]
        try:
            payload = json.loads(request.body.decode())
            form = view.forms[request.method](payload)

            if not form.is_valid():
                form_errors = json.loads(form.errors.as_json())

                errors = []

                for field in form_errors.keys():
                    errors.append({
                        "field": field,
                        "msg": form_errors[field][0]["message"]
                    })

                return JsonResponse({"errors": errors}, status=400)
            else:
                view.payload = payload
        except JSONDecodeError:
            return JsonResponse({"msg": "Invalid payload format"}, status=400)

        return func(*args, **kwargs)
    return wrapper


def authenticate(func):
    def wrapper(*args, **kwargs):
        view = args[0]
        request = args[1]

        headers = request.META

        if 'HTTP_AUTHORIZATION' not in headers:
            return JsonResponse({"msg": "Auth token missing!"}, status=401)

        # first component after split will be "Bearer", next will be the token
        token = headers['HTTP_AUTHORIZATION'].split()[1]

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            view.id = payload['id']
        except InvalidSignatureError:
            return JsonResponse({"msg": "You don't have permission to do that"}, status=403)

        return func(*args, **kwargs)
    return wrapper
























