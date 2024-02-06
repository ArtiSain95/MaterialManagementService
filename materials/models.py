# materials/models.py
from django.db import models


class Material(models.Model):
    """
    Model representing a material with chemical properties.

    Attributes:
        formula (str): The chemical formula of the material.
        density (float): The density of the material.

    Example:
        A Material instance may have the following attributes:
        - formula: "H2O"
        - density: 1.0
    """
    formula = models.CharField(max_length=255, unique = True)
    density = models.FloatField()
