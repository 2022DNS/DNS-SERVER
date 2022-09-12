from .models import Road
from .serializers import RoadSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView


class RoadDetailAPIView(RetrieveAPIView):
    serializer_class = RoadSerializer

    def get_queryset(self):
        print(self.request)
        id = self.kwargs['pk']

        return Road.objects.filter(id=id)


class RoadListAPIView(ListAPIView):
    serializer_class = RoadSerializer

    def get_queryset(self):
        return Road.objects.all().order_by('-count')


class RoadCreateAPIView(CreateAPIView):
    serializer_class = RoadSerializer

    def post(self, request, *args, **kwargs):
        return super(RoadCreateAPIView, self).post(request, *args, **kwargs)