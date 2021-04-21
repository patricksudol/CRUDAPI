from rest_framework import viewsets

from src.apps.widgets.models import Widget
from src.apps.widgets.serializers import WidgetSerializer


class WidgetViewSet(viewsets.ModelViewSet):

    queryset = Widget.objects.all()

    serializer_class = WidgetSerializer
