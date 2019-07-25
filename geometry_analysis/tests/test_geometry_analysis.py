"""
Unit and regression test for the geometry_analysis package.
"""

# Import package, test suite, and other packages as needed
import geometry_analysis
import pytest
import sys
import numpy as np
import math

def test_geometry_analysis_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "geometry_analysis" in sys.modules

# Write a test for each behaviour
def test_calculate_distance():
    '''Test the calculate distan function'''
    r1 = np.array([0, 0, -1])
    r2 = np.array([0, 1, 0])

    expectec_distance = np.sqrt(2.0)

    calculated_distance = geometry_analysis.calculate_distance(r1, r2)

    assert expectec_distance == calculated_distance


def test_calculate_angle():
    '''Test the calculate_angle function'''
    rA = np.array([1, 0, 0])
    rB = np.array([0, 0, 0])
    rC = np.array([0, 1, 0])

    expected_angle = 90
    calculated_angle = geometry_analysis.calculate_angle(rA, rB, rC, degrees=True)

    assert expected_angle == calculated_angle

    expected_angle_rad = math.radians(90)
    calculated_angle_rad = geometry_analysis.calculate_angle(rA, rB, rC, degrees=False)

    assert expected_angle_rad == calculated_angle_rad