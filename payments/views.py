import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings
import base64
from datetime import datetime
import json
def generate_password():
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    data_to_encode = f"{settings.MPESA_SHORTCODE}{settings.MPESA_PASSKEY}{timestamp}"
    encoded_string = base64.b64encode(data_to_encode.encode()).decode('utf-8')
    return encoded_string, timestamp

@csrf_exempt
def lipa_na_mpesa(request):
    if request.method == "POST":
        body = json.loads(request.body)
        amount = body.get("amount")
        phone_number = body.get("phone_number")

        if not amount or not phone_number:
            return JsonResponse({"error": "Amount and phone number required"}, status=400)
        auth_response = requests.get(
            f"{settings.MPESA_BASE_URL}/oauth/v1/generate?grant_type=client_credentials",
            auth=(settings.MPESA_CONSUMER_KEY, settings.MPESA_CONSUMER_SECRET)
        )
        access_token = auth_response.json().get("access_token")

        password, timestamp = generate_password()

        stk_push_payload = {
            "BusinessShortCode": settings.MPESA_SHORTCODE,
            "Password": password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone_number,
            "PartyB": settings.MPESA_SHORTCODE,
            "PhoneNumber": phone_number,
            "CallBackURL": "https://your-ngrok-url.com/mpesa/callback/",
            "AccountReference": "Order Payment",
            "TransactionDesc": "Payment for order"
        }

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

        response = requests.post(f"{settings.MPESA_BASE_URL}/mpesa/stkpush/v1/processrequest",
                                 json=stk_push_payload, headers=headers)

        return JsonResponse(response.json())
    return JsonResponse({"error": "Invalid method"}, status=405)


@csrf_exempt
def mpesa_callback(request):
    data = json.loads(request.body)
    # TODO: 
    print("MPESA callback:", data)
    return JsonResponse({"status": "success"})
