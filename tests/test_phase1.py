"""Phase 1 acceptance tests.

These are skipped until you get to them. For each one: delete its skip marker, write the test
body (the docstring says what it must prove), watch it fail, then make it pass.
Phase 1 is done when nothing in this file is skipped and everything passes.
"""

import pytest

todo = pytest.mark.skip(reason="Phase 1: write this test")


@todo
def test_rk4_exponential_decay():
    """dx/dt = -x from x(0) = 1 matches exp(-t) at t = 5 to within a tolerance you justify."""


@todo
def test_rk4_convergence_order():
    """Halving dt shrinks the global error by about 2**4 = 16x (RK4 is 4th order).

    Fit the slope of log(error) vs log(dt) over several step sizes, not just one pair.
    """


@todo
def test_rk4_does_not_mutate_input():
    """rk4_step must return a new array and leave the input state unchanged."""


@todo
def test_free_fall_matches_analytic():
    """With zero thrust, position and velocity match r0 + v0*t + g*t**2/2 and v0 + g*t,
    and mass stays constant."""


@todo
def test_rocket_equation_delta_v():
    """In zero gravity with constant thrust, the final speed matches Tsiolkovsky:
    dv = Isp * G0 * ln(m0 / mf)."""


@todo
def test_hoverslam_touchdown():
    """Starting a full-thrust burn at burn_start_altitude() touches down at |v| < 0.5 m/s.

    Run it through your 3-DOF sim, not just the formula.
    """
