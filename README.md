# rocket-gnc

[![CI](https://github.com/AfnanDanish/rocket-gnc/actions/workflows/ci.yml/badge.svg)](https://github.com/AfnanDanish/rocket-gnc/actions/workflows/ci.yml)

Guidance, navigation and control for a propulsive rocket landing, written from scratch.

A 6-DOF booster comes back through wind, sensor noise and engine dispersions and lands itself on a pad, using:

- **Guidance:** convex-optimization powered-descent guidance (lossless convexification, Açıkmeşe & Ploen 2007)
- **Control:** thrust-vector control, with LQR attitude control and MPC-style re-planning
- **Navigation:** an error-state extended Kalman filter fusing IMU, GPS and a radar altimeter
- **Verification:** a 1,000-run Monte Carlo dispersion analysis
- **Flight core:** a C++ port with timing benchmarks

## Quickstart

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate    macOS/Linux: source .venv/bin/activate
pip install -e ".[dev]"
pytest
ruff check .
```

## Layout

```
src/rocketgnc/
  constants.py        physical constants
  sim/                dynamics, integrators, environment (gravity, wind, drag)
  gnc/guidance/       hoverslam baseline, convex powered-descent guidance
  gnc/control/        position and attitude controllers
  gnc/nav/            sensor models, error-state EKF
  montecarlo/         dispersion setup, parallel runner, statistics
  viz/                plots and animations
tests/                unit and acceptance tests
docs/
  conventions.md      frames, units, quaternion convention (read this first)
  derivations/        hand derivations behind the code
DEVLOG.md             running log of what was built and learned
```

## References

- B. Açıkmeşe, S. R. Ploen, *Convex Programming Approach to Powered Descent Guidance for Mars Landing*, JGCD, 2007
- L. Blackmore, B. Açıkmeşe, D. P. Scharf, *Minimum-Landing-Error Powered-Descent Guidance for Mars Landing Using Convex Optimization*, JGCD, 2010
- M. Szmuk, B. Açıkmeşe, *Successive Convexification for 6-DoF Mars Rocket Powered Landing with Free-Final-Time*, AIAA SciTech, 2018
- D. Malyuta et al., *Convex Optimization for Trajectory Generation*, IEEE Control Systems Magazine, 2022
- J. Solà, *Quaternion kinematics for the error-state Kalman filter*, arXiv:1711.02508
- R. Labbe, *Kalman and Bayesian Filters in Python*

## License

MIT
