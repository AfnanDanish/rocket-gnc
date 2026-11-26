"""3-DOF point-mass rocket dynamics.

State and frame conventions live in docs/conventions.md. Fill that in first, then make the
docstrings below match it.
"""

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class Vehicle3DOF:
    """Vehicle parameters. Units: SI."""

    dry_mass: float  # [kg]
    isp: float  # specific impulse [s]
    thrust_max: float  # [N]
    thrust_min: float  # [N]; the engine can't throttle below this while lit


def derivative(t: float, x: np.ndarray, thrust: np.ndarray, vehicle: Vehicle3DOF) -> np.ndarray:
    """Time derivative of the state under a commanded thrust vector (world frame, [N]).

    Suggested state layout: x = [r (3), v (3), m (1)]. Decide in docs/conventions.md.
    Include: gravity, thrust acceleration, and mass flow mdot = -|T| / (Isp * G0).
    """
    raise NotImplementedError("TODO: implement point-mass dynamics")
