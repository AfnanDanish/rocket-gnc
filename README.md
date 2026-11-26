# rocket-gnc

[![CI](https://github.com/AfnanDanish/rocket-gnc/actions/workflows/ci.yml/badge.svg)](https://github.com/AfnanDanish/rocket-gnc/actions/workflows/ci.yml)

Guidance, navigation and control for a propulsive rocket landing, written from scratch.

A 6-DOF booster comes back through wind, sensor noise and engine dispersions and lands itself on a pad, using:

- **Guidance:** convex-optimization powered-descent guidance (lossless convexification, Açıkmeşe & Ploen 2007)
- **Control:** thrust-vector control, with LQR attitude control and MPC-style re-planning
- **Navigation:** an error-state extended Kalman filter fusing IMU, GPS and a radar altimeter
- **Verification:** a 1,000-run Monte Carlo dispersion analysis
- **Flight core:** a C++ port with timing benchmarks

> 🚧 Work in progress. Results, the landing animation and a live 3D replay will land here as each phase is finished.

## Roadmap

- [ ] **Phase 0: Setup.** Repo, CI, conventions, dev log
- [ ] **Phase 1: 3-DOF point-mass sim.** RK4, mass depletion, hoverslam baseline
- [ ] **Phase 2: Convex powered-descent guidance.** Lossless convexification, glide-slope and pointing constraints, time-of-flight search
- [ ] **Phase 3: 6-DOF dynamics.** Quaternions, TVC with gimbal limits, engine lag, drag, wind
- [ ] **Phase 4: Control.** Outer position loop, LQR attitude loop, re-planning
- [ ] **Phase 5: Navigation.** Sensor models, error-state EKF, NEES/NIS consistency
- [ ] **Phase 6: Monte Carlo.** 1,000 dispersed runs, landing CEP, failure analysis
- [ ] **Phase 7: C++ flight core.** Eigen, CVXPYgen, pybind11 cross-check, benchmarks
- [ ] **Phase 8: Demo.** three.js replay on GitHub Pages, technical report

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
tests/                one test file per phase; every phase passes before the next starts
docs/
  conventions.md      frames, units, quaternion convention (read this first)
  derivations/        hand derivations for every phase
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
