# rocket-gnc

[![CI](https://github.com/AfnanDanish/rocket-gnc/actions/workflows/ci.yml/badge.svg)](https://github.com/AfnanDanish/rocket-gnc/actions/workflows/ci.yml)

I'm teaching myself guidance, navigation and control by building the whole stack for a rocket that
lands itself, from an empty folder. No GNC library, no copied flight code. The physics, the
guidance, the controller and the state estimator are all written here, and every one gets checked
against something I can derive on paper.

The guidance is the part I find most interesting. Landing a rocket with the least fuel, without
hitting the ground sideways, can be posed as a convex optimization problem and solved fast enough to
run on board. That's the idea in Açıkmeşe & Ploen (2007), and building up to it properly is most of
the point of this repo.

It's early. Right now there's a skeleton, conventions to pin down, and failing tests waiting for
code. I'd rather the history show that honestly than pretend it arrived finished.

## Running it

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate    macOS/Linux: source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

Tests marked as skipped are the ones I haven't written yet. Each one says in its docstring what it
has to prove.

## How it's laid out

```
src/rocketgnc/
  sim/              dynamics and integrators
  gnc/guidance/     where the rocket should go
  gnc/control/      how to make it go there
  gnc/nav/          where it thinks it is
  montecarlo/       the same landing a thousand times with things going wrong
  viz/              plots
docs/conventions.md frames, units, quaternion convention. Decided before any code, on purpose
docs/derivations/   the paper working behind each piece of code
DEVLOG.md           what I did, what broke, what I learned
```

Conventions come first because half the bugs in this kind of code are a frame or a sign that two
files disagree about.

## Reading I'm working from

- B. Açıkmeşe, S. R. Ploen, *Convex Programming Approach to Powered Descent Guidance for Mars Landing*, JGCD, 2007
- L. Blackmore, B. Açıkmeşe, D. P. Scharf, *Minimum-Landing-Error Powered-Descent Guidance for Mars Landing Using Convex Optimization*, JGCD, 2010
- M. Szmuk, B. Açıkmeşe, *Successive Convexification for 6-DoF Mars Rocket Powered Landing with Free-Final-Time*, AIAA SciTech, 2018
- D. Malyuta et al., *Convex Optimization for Trajectory Generation*, IEEE Control Systems Magazine, 2022
- J. Solà, *Quaternion kinematics for the error-state Kalman filter*, arXiv:1711.02508
- R. Labbe, *Kalman and Bayesian Filters in Python*

## License

MIT
