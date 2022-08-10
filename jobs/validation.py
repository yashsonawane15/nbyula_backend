from json import JSONDecodeError
from django.http import JsonResponse
import json


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