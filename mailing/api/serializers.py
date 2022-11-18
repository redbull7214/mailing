from rest_framework import serializers
from .models import Contact, Mailing, Message


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Contact


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Message


class MailinglistSerializer(serializers.ModelSerializer):
    send_messages = serializers.SerializerMethodField(read_only=True)
    failed_messages = serializers.SerializerMethodField(read_only=True)
    processed_messages = serializers.SerializerMethodField(read_only=True)

    class Meta:
        fields = (
            'id', 'start_send_time', 'end_send_time',
            'text', 'tag', 'code', 'send_messages', 'failed_messages', 'processed_messages'
        )
        model = Mailing

    def get_send_messages(self, obj):
        return obj.messages.filter(status='SEND').count()

    def get_failed_messages(self, obj):
        return obj.messages.filter(status='FAILED').count()

    def get_processed_messages(self, obj):
        return obj.messages.filter(status='PROCESSED').count()


class MailingSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(read_only=True, many=True)

    class Meta:
        fields = (
            'id', 'start_send_time', 'end_send_time',
            'text', 'tag', 'code', 'messages'
        )
        model = Mailing
