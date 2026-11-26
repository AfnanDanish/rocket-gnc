"""Numerical integrators.

Write RK4 yourself (no scipy.integrate here). Derive the update on paper first
and put the scan in docs/derivations/.
"""

from collections.abc import Callable

import numpy as np

Derivative = Callable[[float, np.ndarray], np.ndarray]
"""f(t, x) -> dx/dt"""


def rk4_step(f: Derivative, t: float, x: np.ndarray, dt: float) -> np.ndarray:
    """Advance the state x at time t by one classic 4th-order Runge-Kutta step of size dt.

    Returns the new state at t + dt. Must not modify x in place.
    """
    raise NotImplementedError("TODO: implement RK4")


def integrate(
    f: Derivative, x0: np.ndarray, t0: float, t_end: float, dt: float
) -> tuple[np.ndarray, np.ndarray]:
    """Integrate from t0 to t_end with fixed steps of dt.

    Returns (t, X) where t has shape (N,) and X has shape (N, len(x0)); X[0] == x0.
    Decide how to handle a last step that doesn't divide evenly, and document it here.
    """
    raise NotImplementedError("TODO: implement the fixed-step loop")
