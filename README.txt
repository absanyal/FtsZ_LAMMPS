Run with:

python3 polymer_free.py; time mpirun -n 8 lmp -i input_free.lammps > out.run

Syntax:

LJ Potential
------------
pair_coeff (atom type 1) (atom type 2) (epsilon) (sigma) (cutoff)

FENE Bond
---------
bond_coeff (bond type) (K) (R0) 1(episilon) (sigma)

Harmonic angle
--------------
angle_coeff (angle type) (Spring constant) (theta_0)