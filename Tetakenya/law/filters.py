import django_filters
from .models import *


class LawyerFilter(django_filters.FilterSet):
    class Meta:
        model = Lawyer
        fields = ['county']
