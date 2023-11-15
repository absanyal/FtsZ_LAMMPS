import numpy as np

fname_str = 'polymer_embedded.data'

system_size = 100  # Angstrom
bondlength = 0.1

frequency_linker = 0.25

n_atoms = 50
n_chains = 2
n_bonds = n_atoms - 1
n_angles = n_bonds - 1

atom_types = 3
bond_types = 1
angle_types = 1

xlo, xhi = 0.0, system_size
ylo, yhi = 0.0, system_size
zlo, zhi = 0.0, system_size

# ---Setup mass---
mass = [
    [1, 1.0, "monomer_chain1"],
    [2, 1.0, "monomer_chain2"],
    [3, 1.0, "linker"]
]

# ---Setup positions---
positions = []

chain = 1
normalatom = 1
for i in range(n_atoms):
    thisatom = normalatom

    # r = np.random.uniform(0, 1)
    # if (r < frequency_linker):
    #     thisatom = 3

    if ((i+1) % 4 == 0):
        thisatom = 3

    px = system_size/2.0
    py = system_size/2.0
    pz = (i * bondlength) - (zhi - zlo)/2
    positions.append([chain, thisatom, px, py, pz])


chain = 2
normalatom = 2
for i in range(n_atoms):
    thisatom = normalatom

    # r = np.random.uniform(0, 1)
    # if (r < frequency_linker):
    #     thisatom = 3
    

    if ((i+1) % 4 == 0):
        thisatom = 3

    px = system_size/2.0 + 10
    py = system_size/2.0
    pz = (i * bondlength) - (zhi - zlo)/2
    positions.append([chain, thisatom, px, py, pz])


# ---Setup bonds----
bonds = []

# linear bonds in chain1, bond type = 1
bond_type = 1
for i in range(n_atoms - 1):
    b_start = i+1
    b_stop = b_start + 1
    bond = [bond_type, b_start, b_stop]
    bonds.append(bond)

# linear bonds in chain2, bond type = 1
bond_type = 1
for i in range(n_atoms - 1):
    b_start = i+1+n_atoms
    b_stop = b_start + 1
    bond = [bond_type, b_start, b_stop]
    bonds.append(bond)

# ---Setup angles---
angles = []

# 180 degree angle between two successive bonds, chain 1, angle type=1
angle_type = 1
for i in range(n_atoms - 2):
    a_1 = i+1
    a_2 = a_1 + 1
    a_3 = a_2 + 1
    angle = [angle_type, a_1, a_2, a_3]
    angles.append(angle)

# 180 degree angle between two successive bonds, chain 2, angle type=1
angle_type = 1
for i in range(n_atoms - 2):
    a_1 = i+1+n_atoms
    a_2 = a_1 + 1
    a_3 = a_2 + 1
    angle = [angle_type, a_1, a_2, a_3]
    angles.append(angle)

with open(fname_str, 'w') as fname:

    # ---Header---
    fname.write("Random atoms in a box\n\n")

    # Numbers
    fname.write('{} atoms\n'.format(n_atoms * n_chains))
    fname.write('{} bonds\n'.format(n_bonds * n_chains))
    fname.write('{} angles\n'.format(n_angles * n_chains))

    fname.write('\n')

    # Types

    fname.write('{} atom types\n'.format(atom_types))
    fname.write('{} bond types\n'.format(bond_types))
    fname.write('{} angle types\n'.format(angle_types))

    fname.write('\n')

    # Box size
    fname.write('{} {} xlo xhi\n'.format(xlo, xhi))
    fname.write('{} {} ylo yhi\n'.format(ylo, yhi))
    fname.write('{} {} zlo zhi\n'.format(zlo, zhi))

    fname.write('\n')

    # Masses
    fname.write('Masses \n\n')

    for i in range(atom_types):
        fname.write(
            '{} {} # {}\n'.format(mass[i][0], mass[i][1], mass[i][2]))

    fname.write('\n')

    # ---Atoms---
    fname.write('Atoms\n\n')

    for i, pos in enumerate(positions):
        fname.write('{} {} {} {} {} {}\n'.format(i+1, *pos))

    fname.write('\n')

    # ---Bonds---
    fname.write('Bonds\n\n')

    for i, bond in enumerate(bonds):
        fname.write('{} {} {} {}\n'.format(i+1, *bond))

    fname.write('\n')

    # ---Angles---
    fname.write('Angles\n\n')

    for i, angle in enumerate(angles):
        fname.write('{} {} {} {} {}\n'.format(i+1, *angle))
