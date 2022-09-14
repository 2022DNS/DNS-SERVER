from .models import Road
from .serializers import RoadSerializer, RoadDetailSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.exceptions import NotFound

class RoadDetailAPIView(RetrieveAPIView):
    serializer_class = RoadDetailSerializer

    def get_object(self):
        lo = self.kwargs['pk']
        la = self.kwargs['post_pk']
        try:
            resp = Road.objects.filter(longitude=lo, latitude=la).get()
        except Road.DoseNotExist:
            raise NotFound()
        return resp

    # def get_queryset(self):
        # lo = self.kwargs['pk']
        # la = self.kwargs['post_pk']
        # print(lo, la)
        # print(serializers.serialize("json",Road.objects.filter(longitude=lo, latitude=la)))
        # return Road.objects.filter(longitude=lo, latitude=la).get()

    def get(self, request, *args, **kwargs):
        return self.retrieve(self, request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)

class RoadListAPIView(ListAPIView):
    serializer_class = RoadSerializer

    def get_queryset(self):
        return Road.objects.all().order_by('-count')


class RoadCreateAPIView(CreateAPIView):
    serializer_class = RoadSerializer
    def post(self, request, *args, **kwargs):
        return super(RoadCreateAPIView, self).post(request, *args, **kwargs)