from .config import *
from ase.build import molecule
from ase import Atoms
from ase.io import write

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
        translation  = np.random.rand(3) * cell_size
        new_mol      = mol.copy()

        new_pos      = mol[pos] + translation

        new_mol[pos] = list(map(tuple, new_pos))

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
    for j in range(tup[0] + 1):
        t = 0.75 * j * cell_size[0] / tup[0]

        new_mol = mol.copy()

        new_mol[pos] = [(i[0]+t, i[1], i[2]) for i in mol[pos]]
        cell.add_molecule(new_mol)

    for j in range(tup[1] + 1):
        t = 0.75 * j * cell_size[1] / tup[1]

        new_mol = mol.copy()

        new_mol[pos] = [(i[0], i[1]+t, i[2]) for i in mol[pos]]
        cell.add_molecule(new_mol)

    for j in range(tup[2] + 1):
        t = 0.75 * j * cell_size[2] / tup[2]

        new_mol = mol.copy()

        new_mol[pos] = [(i[0], i[1], i[2]+t) for i in mol[pos]]
        cell.add_molecule(new_mol)

    cell.make_xzy(save_name)
    return
