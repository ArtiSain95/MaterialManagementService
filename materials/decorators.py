# materials/deecorators
import logging
from .models import Material
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status


logger = logging.getLogger(__name__)

def exception_handler(view_func):
    """
    Decorator to handle exceptions in views.
    """

    def wrapper(*args, **kwargs):
        try:
            return view_func(*args, **kwargs)
        except Material.DoesNotExist as e:
            logger.error("Material not found: %s", str(e))
            logger.exception(e)
            return Response({"error": "Material not foundr"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.exception("Internal Server Error: %s", str(e))
            return Response({"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return wrapper