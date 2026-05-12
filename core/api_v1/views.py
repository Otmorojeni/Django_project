from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Theme, Brand, Kit, Review
from .serializers import ThemeSerializer, BrandSerializer, KitSerializer, ReviewSerializer


@api_view(['GET', 'POST'])
def theme_list(request):
    if request.method == 'GET':
        themes = Theme.objects.all()
        serializer = ThemeSerializer(themes, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ThemeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def theme_detail(request, pk):
    try:
        theme = Theme.objects.get(pk=pk)
    except Theme.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ThemeSerializer(theme)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        theme.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class KitListCreateView(ListCreateAPIView):
    queryset = Kit.objects.all()
    serializer_class = KitSerializer


class KitDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Kit.objects.all()
    serializer_class = KitSerializer


# class BrandView(APIView):
#     def get(self, request):
#         brand = Brand.objects.all()
#         serializer = BrandSerializer(brand, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = BrandSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BrandListCreateView(ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    
class ReviewList(APIView):
    def get(self, request, kit_id=None):
        if kit_id:
            reviews = Review.objects.filter(kit_id=kit_id)
        else:
            reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ReviewDetail(APIView):
    def delete(self, request, pk):
        try:
            review = Review.objects.get(pk=pk)
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Review.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)