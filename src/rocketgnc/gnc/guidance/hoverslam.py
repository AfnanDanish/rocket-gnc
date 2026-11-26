"""1D hoverslam (suicide burn) baseline.

Derive on paper first: given altitude h, downward speed v, mass m, max thrust and gravity,
at what altitude must a full-thrust burn start so that velocity reaches zero exactly at h = 0?
Start with constant mass, then decide whether (and how) to account for mass loss during the burn.
"""


def burn_start_altitude(speed: float, mass: float, thrust: float, g: float) -> float:
    """Altitude [m] at which a full-thrust burn must start to touch down at zero velocity."""
    raise NotImplementedError("TODO: derive and implement the burn-start altitude")
