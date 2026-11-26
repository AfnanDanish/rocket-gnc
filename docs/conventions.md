# Conventions

Fill this in before writing simulation code. Every module and test follows it. When you change a
convention, change it here first.

Answer each question, then delete the prompt.

## Units
- All internal quantities in SI. Angles in radians internally, degrees only for display.
- _Any exceptions? (e.g. Isp in seconds)_

## World frame
- _Which frame? (e.g. ENU: x East, y North, z Up, origin at the landing pad)_
- _Flat, non-rotating Earth with constant gravity? Write down what you're ignoring and why._

## Body frame
- _Which body axis points along the rocket, nose up? Which way do the other two point?_
- _Where's the origin: center of mass, or a fixed point that the CoM moves relative to as fuel burns?_

## Quaternions
- _Scalar-first [w, x, y, z] or scalar-last?_
- _Hamilton or JPL convention? (Solà's paper explains the difference. Pick one and never mix.)_
- _Does q rotate body→world or world→body?_

## State vectors
- _3-DOF: layout of x, e.g. [r (3), v (3), m]_
- _6-DOF: layout_

## Thrust and gimbal
- _Sign convention for gimbal angles, and the frame the thrust vector is expressed in._

## Time
- _Simulation step, controller rate, guidance re-plan rate, sensor rates. Will the sim and the controller run at different rates?_
