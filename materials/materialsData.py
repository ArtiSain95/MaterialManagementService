#materials/materialsData

class MaterialPropertiesDatabase:
    """
    Mock Database class containing properties for various materials.

    Class Attributes:
        properties (dict): A dictionary where keys are material formulas
            and values are dictionaries containing material properties.
    """
    properties = {
        "H2O": {"melting_point": None, "boiling_point": 100.0, "state_at_room_temp": "liquid"},
        "CO2": {"melting_point": None, "boiling_point": None, "state_at_room_temp": "gas"},
        "He": {"melting_point": None, "boiling_point": None, "state_at_room_temp": "gas"},
        "O3": {"melting_point": None, "boiling_point": None, "state_at_room_temp": "gas"},
    }