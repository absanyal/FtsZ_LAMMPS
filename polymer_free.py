import numpy as np

fname_str = 'polymer_free.data'

# system_size = 200
bondlength = 0.1

# Chain info (only count polymer chain)
n_chains = 2
chain_offset = 10

# Per chain numbers
n_atoms = 50
n_bonds = n_atoms - 1
n_angles = n_bonds - 1

# Linker numbers
n_linkers_cross = 400
n_linkers_membrane = 200


# Types
atom_types = 4
bond_types = 1
angle_types = 1

# Box dimensions
xlo, xhi = 0.0, 100
ylo, yhi = 0.0, 350
zlo, zhi = 0.0, 350

# ---Setup mass---
mass = [
    [1, 1.0, "monomer_chain1"],
    [2, 1.0, "monomer_chain2"],
    [3, 1.1, "linker_cross"],
    [4, 1.1, "linker_membrane"]
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

    # if ((i+1) % 4 == 0):
    #     thisatom = 3

    px = (xhi - xlo)/2.0
    py = (yhi - ylo)/2.0
    pz = (i * bondlength) - (zhi - zlo)/2
    positions.append([chain, thisatom, px, py, pz])


chain = 2
normalatom = 2
for i in range(n_atoms):
    thisatom = normalatom

    # r = np.random.uniform(0, 1)
    # if (r < frequency_linker):
    #     thisatom = 3

    # if ((i+1) % 4 == 0):
    #     thisatom = 3

    px = (xhi - xlo)/2.0 + chain_offset
    py = (yhi - ylo)/2.0
    pz = (i * bondlength) - (zhi - zlo)/2
    positions.append([chain, thisatom, px, py, pz])

# Linkers
thisatom = 3
chain = 3
for i in range(n_linkers_cross):
    px = np.random.uniform(xlo, xhi)
    py = np.random.uniform(ylo, yhi)
    pz = np.random.uniform(zlo, zhi)
    positions.append([chain, thisatom, px, py, pz])

thisatom = 4
chain = 4
for i in range(n_linkers_membrane):
    px = np.random.uniform(xlo, xhi)
    py = np.random.uniform(ylo, yhi)
    pz = np.random.uniform(zlo, zhi)
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
    fname.write("Two chains and floating linkers\n\n")

    # Numbers
    fname.write('{} atoms\n'.format(n_atoms * n_chains +
                n_linkers_membrane + n_linkers_cross))
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
