import re
from . import materialsData as _md
import time
import random
    

def get_melting_point(material_formula):
    """
    Get the melting point of a material based on its chemical formula.

    Args:
        material_formula (str): The chemical formula of the material.

    Returns:
        float or None: The melting point if available, else None.
    """
    material_properties = _md.MaterialPropertiesDatabase.properties.get(material_formula, {})
    return material_properties.get("melting_point", None)


def remains_solid_at_room_temp(material_formula):
    """
    Check if a material remains solid at room temperature based on its chemical formula.

    Args:
        material_formula (str): The chemical formula of the material.

    Returns:
        bool: True if the material is solid at room temperature, False otherwise.
    """
    material_properties = _md.MaterialPropertiesDatabase.properties.get(material_formula, {})
    state_at_room_temp = material_properties.get("state_at_room_temp", None)
    return state_at_room_temp == "solid"


def get_boiling_point(material_formula):
    """
    Get the boiling point of a material based on its chemical formula.

    Args:
        material_formula (str): The chemical formula of the material.

    Returns:
        float or None: The boiling point if available, else None.
    """
    material_properties = _md.MaterialPropertiesDatabase.properties.get(material_formula, {})
    return material_properties.get("boiling_point", None)


def get_gas_properties(material_formula):
    """
    Get gas properties of a material based on its chemical formula.

    Args:
        material_formula (str): The chemical formula of the material.

    Returns:
        dict or None: Dictionary containing gas properties if the material is a gas, else None.
    """
    material_properties = _md.MaterialPropertiesDatabase.properties.get(material_formula, {})
    return {"gas_property": "gas"} if material_properties.get("state_at_room_temp") == "gas" else None


def determine_material_state(material_formula):
    """
    Determine the state of a material (crystalline, solid, liquid, gas, or unknown) based on its properties.

    Args:
        material_formula (str): The chemical formula of the material.

    Returns:
        str: The determined state of the material.
    """
    melting_point = get_melting_point(material_formula)
    if melting_point is not None:
        return 'crystalline'

    if remains_solid_at_room_temp(material_formula):
        return 'solid'

    boiling_point = get_boiling_point(material_formula)
    if boiling_point is not None:
        return 'liquid'

    gas_properties = get_gas_properties(material_formula)
    if gas_properties is not None:
        return 'gas'

    return 'unknown'


def get_element_weights():
    """
    Get a dictionary mapping chemical elements to their atomic weights.

    Returns:
        dict: Dictionary containing element-weight mappings.
    """
    return {
        'H': 1.008,
        'He': 4.0026,
        'Li': 6.94,
        'Be': 9.0122,
        'B': 10.81,
        'C': 12.011,
        'N': 14.007,
        'O': 15.999,
        'F': 18.998,
        'Ne': 20.180,
        'Na': 22.990,
        'Mg': 24.305,
        'Al': 26.982,
        'Si': 28.085,
        'P': 30.974,
        'S': 32.06,
        'Cl': 35.45,
        'K': 39.098,
        'Ar': 39.95,
    }


def calculate_molecular_weight(formula):
    """
    Calculate the molecular weight of a material based on its chemical formula.

    Args:
        formula (str): The chemical formula of the material.

    Returns:
        float: The calculated molecular weight.
    """
    elem_weight = get_element_weights()

    s = re.findall('([A-Z][a-z]?)([0-9]*)', formula)

    total_weight = 0
    for elem, count in s:
        if count == '':
            count = 1

        total_weight += int(count) * elem_weight.get(elem, 0)

    return total_weight


def calculate_density(formula, molar_volume):
    """
    Calculate the density of a material.

    Args:
        formula (str): The chemical formula of the material.
        molar_volume (float): The molar volume of the material.

    Returns:
        float or None: The calculated density if the inputs are valid, else None.
    """
    molecular_weight = calculate_molecular_weight(formula)
    if molecular_weight is not None and molar_volume != 0:
        density = molecular_weight / molar_volume
        return density
    else:
        return None


def calculate_molar_volume(material_state):
    """
    Calculate the molar volume of a material based on its state.

    Args:
        material_state (str): The state of the material (gas, liquid, crystalline).

    Returns:
        float or None: The calculated molar volume if the state is valid, else None.
    """
    if material_state == 'gas':
        R = 0.0821
        T_stp = 273.15
        P_stp = 1.0
        molar_volume_gas = (R * T_stp) / P_stp
        return molar_volume_gas
    elif material_state == 'liquid' or material_state == 'crystalline':
        return 24.465  # Hypothetical molar volume for liquids or crystalline solids
    else:
        return None


def fooness(formula):
    """
    Simulate an advanced material property calculation.

    Args:
        formula (str): The chemical formula of the material.

    Returns:
        float or None: The simulated property value if available, else None.
    """
    sleep_duration = random.uniform(1.0, 5.0)
    time.sleep(sleep_duration)
    state = determine_material_state(formula)
    molar_volume = calculate_molar_volume(state)
    density = calculate_density(formula, molar_volume)
    return density


def validate_search_parameters(min_density, max_density, include_elements, exclude_elements):
    """ Check if min_density and max_density are valid numbers """

    try:
        min_density = float(min_density) if min_density is not None else None
        max_density = float(max_density) if max_density is not None else None
    except ValueError:
        raise ValueError("Invalid density values. Please provide valid numeric values.")
    # Validate min_density is greater than max_density if both are provided
    if min_density is not None and max_density is not None and min_density >= max_density:
        raise ValueError("Minimum density should not be greater than maximum density.")

    # Validate that include_elements and exclude_elements do not contain the same elements
    common_elements = set(include_elements) & set(exclude_elements)
    if common_elements:
        raise ValueError(f"Elements cannot be both included and excluded: {', '.join(common_elements)}")
