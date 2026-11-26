import rocketgnc
from rocketgnc.constants import G0


def test_package_imports():
    assert rocketgnc.__version__


def test_standard_gravity():
    assert G0 == 9.80665
