from .models import Road
from .serializers import RoadSerializer, RoadDetailSerializer, RoadCreateSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.exceptions import NotFound
from .service import run
from django.http import HttpResponse

class RoadDetailAPIView(RetrieveAPIView):
    serializer_class = RoadDetailSerializer

    def get_queryset(self):
        lo = self.kwargs['pk']
        la = self.kwargs['post_pk']
        try:
            resp = Road.objects.filter(longitude=lo, latitude=la).get()
        except Road.DoesNotExist:
            raise NotFound()
        return resp

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
        images = request.get('images')
        la = request.get('la')
        lo = request.get('lo')

        la = converter(la)
        lo = converter(lo)

        resp = run(images, la, lo)

        return resp

def index(request):
    return HttpResponse("asdf")
