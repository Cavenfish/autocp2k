from .config import *
from ase.build import molecule
from ase import Atoms
from ase.io import write
from scipy.spatial.transform import Rotation as R

#This one I personally made
def make_random_xyz(molecule, cell_size, num_mols, save_name='./cell.xyz'):
    """
    This function generates an xyz file to be used with cp2k
    """
    #Make dictionary of molecule
    mol  = read_molecule(molecule)

    #Initialize cell
    cell = Cell(mol, cell_size)

    #Populate cell
    while cell.molCount < num_mols:
        r            = R.random()
        translation  = np.random.rand(3) * cell_size
        new_mol      = mol.copy()

        new_pos      = mol[pos] + translation

        new_mol[pos] = list(map(tuple, r.apply(new_pos)))

        print(cell.molCount)
        cell.add_molecule(new_mol)

    cell.make_xzy(save_name)
    return


def make_repeated_xyz(molecule, cell_size, tup, save_name='./cell.xyz'):
    """
    This function generates an xyz file to be used with cp2k
    """
    #Make dictionary of molecule
    mol  = read_molecule(molecule)

    #Initialize cell
    cell = Cell(mol, cell_size)

    #Populate cell
    for x in range(tup[0]):
        xt = 0.75 * x * cell_size[0] / tup[0]
        for y in range(tup[1]):
            yt = 0.75 * y * cell_size[1] / tup[1]
            for z in range(tup[2]):
                zt = 0.75 * z * cell_size[2] / tup[2]

                new_mol = deepcopy(mol)

                new_mol[pos] = [(i[0]+xt, i[1]+yt, i[2]+zt) for i in mol[pos]]
                cell.add_molecule(new_mol)

    print(cell.molCount)
    cell.make_xzy(save_name)
    return


def make_fcc_xyz(molecule, cell_size, unit_cell, save_name='./cell.xyz'):
    """
    """
    #Make dictionary of molecule
    mol  = read_molecule(molecule)

    #Initialize cell
    cell = Cell(mol, cell_size)

    #Populate cell
    for x in range(2):
        xt =  x * unit_cell[0]
        for y in range(2):
            yt =  y * unit_cell[1]
            for z in range(2):
                zt =  z * unit_cell[2]

                new_mol = deepcopy(mol)

                new_mol[pos] = [(i[0]+xt, i[1]+yt, i[2]+zt) for i in mol[pos]]
                cell.add_molecule(new_mol)

                if (z == 0) or (z == 1):
                    if (x != 0) and (y != 0):
                        new_mol[pos] = [(i[0]+xt/2, i[1]+yt/2, i[2]+zt) for i in mol[pos]]
                        cell.add_molecule(new_mol)

                if (x == 0) or (x == 1):
                    if (z != 0) and (y != 0):
                        new_mol[pos] = [(i[0]+xt, i[1]+yt/2, i[2]+zt/2) for i in mol[pos]]
                    cell.add_molecule(new_mol)

                if (y == 0) or (y == 1):
                    if (x != 0) and (z != 0):
                        new_mol[pos] = [(i[0]+xt/2, i[1]+yt, i[2]+zt/2) for i in mol[pos]]
                        cell.add_molecule(new_mol)

    print(cell.molCount)
    cell.make_xzy(save_name)
    return
