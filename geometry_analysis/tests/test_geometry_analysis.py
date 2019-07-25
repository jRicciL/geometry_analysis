"""
Unit and regression test for the geometry_analysis package.
"""

# Import package, test suite, and other packages as needed
import geometry_analysis
import pytest
import sys
import numpy as np
import math

#---- FIXTURES
@pytest.fixture()
# Instantiate an object to work with it during the testig
def water():
    name = 'water'
    symbols = ['H', 'O', 'H']
    coordinates = np.array([[2, 0, 0], [0, 0, 0], [-2, 0, 0]])

    water = geometry_analysis.Molecule(name, symbols, coordinates)
    
    return water
#----

def test_geometry_analysis_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "geometry_analysis" in sys.modules

# Write a test for each behaviour
def test_calculate_distance():
    '''Test the calculate distan function'''
    r1 = np.array([0, 0, -1])
    r2 = np.array([0, 1, 0])

    expected_distance = np.sqrt(2.0)

    calculated_distance = geometry_analysis.calculate_distance(r1, r2)

    assert expected_distance == calculated_distance


def test_calculate_angle():
    '''Test the calculate_angle function'''
    rA = np.array([1, 0, 0])
    rB = np.array([0, 0, 0])
    rC = np.array([0, 1, 0])

    expected_angle = 90
    calculated_angle = geometry_analysis.calculate_angle(rA, rB, rC, degrees=True)

    assert expected_angle == calculated_angle
    # Second assert
    expected_angle_rad = math.radians(90)
    calculated_angle_rad = geometry_analysis.calculate_angle(rA, rB, rC, degrees=False)

    assert expected_angle_rad == calculated_angle_rad

# Using decorators (need to import pytest)
#-----
@pytest.mark.parametrize('p1, p2, p3, expected_angle', [
    (np.array([1, 0, 0]), np.array([0, 0, 0]), np.array([0, 1, 0]), 90),
    (np.array([1, 0, 0]), np.array([0, 1, 0]), np.array([0, 0, 1]), 60)
])
def test_calculate_angle(p1, p2, p3, expected_angle):
    calculated_angle = geometry_analysis.calculate_angle(p1, p2, p3, degrees=True)
    assert np.isclose(expected_angle, calculated_angle)
#-----

# Proving fixtures:
def test_molecule_setter_coords(water):

    num_bonds = len(water.bonds)

    assert num_bonds == 2

    water.coordinates = water.coordinates * 100
    new_bonds = len(water.bonds)

    assert new_bonds == 0
    #assert np.array_equal()


#-----------------------------
def test_molecules_set_coord():
    name = 25 # this will be an error
    symbols = ['H', 'O', 'H']
    coordinates = np.array([[2, 0, 0], [0, 0, 0], [-2, 0, 0]])

    # Test that the probe actualy rises an error
    with pytest.raises(TypeError):
        water = geometry_analysis.Molecule(name, symbols, coordinates)
    

#-----------------------------
# pytest with docstrings
