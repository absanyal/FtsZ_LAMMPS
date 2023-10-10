import numpy as np

n_atoms = 1000
system_size = 20  # Angstrom
atom_types = 1
xlo, xhi = 0.0, system_size
ylo, yhi = 0.0, system_size
zlo, zhi = 0.0, system_size

positions = []

for i in range(n_atoms):
    positions.append(np.random.rand(3) * system_size)

#fname = open('random_atoms.data', 'w')

with open('random_atoms.data', 'w') as fname:

    #---Header---
    fname.write("Random atoms in a box\n\n")

    #Number and type
    fname.write('{} atoms\n'.format(n_atoms))
    fname.write('{} atom types\n'.format(atom_types))

    #Box size
    fname.write('{} {} xlo xhi\n'.format(xlo, xhi))
    fname.write('{} {} ylo yhi\n'.format(ylo, yhi))
    fname.write('{} {} zlo zhi\n'.format(zlo, zhi))

    fname.write('\n')

    #---Atoms---
    fname.write('Atoms\n\n')

    #Positions of atoms
    for i, pos in enumerate(positions):
        fname.write('{} 1 {} {} {}\n'.format(i+1, *pos))


