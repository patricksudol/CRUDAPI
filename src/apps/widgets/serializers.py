from rest_framework import serializers

from src.apps.widgets.models import Widget


class WidgetSerializer(serializers.HyperlinkedModelSerializer):
    """
    Django Rest Framework serializer used to determine the fields of a Widget
    returned.
    """

    class Meta:
        model = Widget
        fields = [
            'id', 'name', 'number_of_parts', 'created_date', 'updated_date'
        ]
