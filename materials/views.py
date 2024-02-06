# materials/views.py
from django.shortcuts import render
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Material
from .helpers import fooness
from .serializers import MaterialSerializer
from .decorators import exception_handler
from .helpers import validate_search_parameters
import logging
from functools import reduce
from operator import or_

logger = logging.getLogger(__name__)


class HomeView(APIView):
    def get(self, request):
        """
        Render the home page.
        """
        try:
            return render(request, 'index.html')
        except Exception as e:
            logger.exception(e)
            return Response({"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class MaterialCreateView(APIView):
    @exception_handler
    def post(self, request):
        """
        Create a new material.
        """
        serializer = MaterialSerializer(data=request.data)
        if serializer.is_valid():
            material = serializer.save()
            return Response({"id": material.id}, status=status.HTTP_201_CREATED)
        logger.error(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MaterialRetrieveView(APIView):
    @exception_handler
    def get(self, request, id):
        """
        Retrieve details of a material by ID.
        """
        material = Material.objects.get(id=id)
        serializer = MaterialSerializer(material)
        return Response(serializer.data)


class MaterialSearchView(APIView):
    @exception_handler
    def get(self, request):
        """
        Search for materials based on query parameters.
        """
        min_density = request.query_params.get('min-density')
        max_density = request.query_params.get('max-density')
        include_elements_param = request.query_params.get('include-elements')
        include_elements = include_elements_param.strip('[]').split(',') if include_elements_param else []
        exclude_elements_param = request.query_params.get('exclude-elements')
        exclude_elements = exclude_elements_param.strip('[]').split(',') if exclude_elements_param else []

        try:
            validate_search_parameters(min_density, max_density, include_elements, exclude_elements)
        except ValueError as e:
            logger.exception(e)
            return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        query = Material.objects.all()
        if min_density:
            query = query.filter(density__gte=float(min_density))
        if max_density:
            query = query.filter(density__lte=float(max_density))
        if include_elements:
            q_objects = [Q(formula__contains=element) for element in include_elements]
            conditions = reduce(or_, q_objects)
            query = query.filter(conditions)
        if exclude_elements:
            conditions = [~Q(formula__contains=element) for element in exclude_elements]
            query = query.filter(*conditions)

        serializer = MaterialSerializer(query, many=True)
        return Response(serializer.data)

        
class AdvancedMaterialPropertyView(APIView):
    @exception_handler
    def get(self, request, id):
        """
        Get advanced property value for a material by ID.
        """
        material = Material.objects.get(id=id)
        property_value = fooness(material.formula)
        return Response({"property_value": property_value})
