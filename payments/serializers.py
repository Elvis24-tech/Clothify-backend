from rest_framework import serializers

class LipaNaMpesaSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=12)
    amount = serializers.IntegerField()
