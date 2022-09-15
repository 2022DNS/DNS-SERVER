from .models import Road
from .serializers import RoadSerializer, RoadDetailSerializer, RoadCreateSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.exceptions import NotFound
from .service import run, flo2str, converter
from django.http import HttpResponse
from rest_framework.response import Response

class RoadDetailAPIView(RetrieveAPIView):
    serializer_class = RoadDetailSerializer

    def get_object(self):
        lo = converter(self.kwargs['pk'])
        la = converter(self.kwargs['post_pk'])
        print(lo)
        print(la)
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
        images = request.data.get('images')
        la = request.data.get('latitude')
        lo = request.data.get('longitude')

        la = flo2str(la)
        lo = flo2str(lo)

        resp = run(images, la, lo)

        print(resp)

        return Response({
            "result": resp
        })


def index(request):
    return HttpResponse("API")
