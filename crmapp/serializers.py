from rest_framework import serializers
from .models import *


class EnquiryListSerializer(serializers.ModelSerializer):

    created = serializers.ReadOnlyField()

    class Meta:
        model = Enquiry
        fields = '__all__'
        read_only_fields = ('name', 'email', 'course_interest',
                            'description', 'claimed_by')


class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = '__all__'
        read_only_fields = ('name', 'email', 'created', 'course_interest',
                            'description', 'claimed_by')
