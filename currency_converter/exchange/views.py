import requests
import os
from dotenv import load_dotenv
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ConversionHistory

load_dotenv()
api_key = os.getenv("API_KEY")


from django.shortcuts import render


from django.conf import settings

def webapp(request):
    template_path = os.path.join(settings.BASE_DIR, 'exchange/templates/webapp/index.html')
    return render(request, "webapp/index.html")

class ConvertCurrencyView(APIView):
    def get(self, request):
        from_currency = request.GET.get("from")
        to_currency = request.GET.get("to")
        amount = request.GET.get("amount")

        if not from_currency or not to_currency or not amount:
            return Response({"error": "Missing parameters"}, status=400)

        try:
            amount = float(amount)
        except ValueError:
            return Response({"error": "Invalid amount"}, status=400)

        url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}&access_key={api_key}"
        response = requests.get(url)
        data = response.json()

        print("API Response:", data)

        if response.status_code != 200 or not data.get("success"):
            return Response({"error": "Error fetching exchange rate"}, status=500)

        if "info" not in data or "quote" not in data["info"]:
            return Response({"error": "Invalid API response"}, status=400)

        rate = data["info"]["quote"]  
        result = round(amount * rate, 2)

        ConversionHistory.objects.create(
            from_currency=from_currency,
            to_currency=to_currency,
            amount=amount,
            result=result,
        )

        return Response(
            {
                "from": from_currency,
                "to": to_currency,
                "amount": amount,
                "result": result,
                "rate": rate,
            }
        )
