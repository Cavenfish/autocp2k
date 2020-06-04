import os
import sys
import numpy  as np
import pandas as pd
import basis_set_exchange as bse
from copy import deepcopy

#Dictionary key names
atm      = 'Atoms'
pos      = 'Positions'

#Error messages
error_head   = "\n*****uh oh spaghettios*****\n"
error_tail   = "\n*****Ponder this, then return to me*****\n"

#Basic input file parameters for optimization calculation
#basic_params = ()

#class Input:
#    'Parameters for the CP2K input file'

#Class for storing molecules in a cell
class Cell:
    'The cell with all molecules to be studied'
    molCount = 0

    def __init__(self, molecule, cell_size):
        self.mols      = deepcopy(molecule)
        self.size      = cell_size
        self.molCount += 1

    def add_molecule(self, molecule):
        atm      = 'Atoms'
        pos      = 'Positions'
        #Check if any atoms overlap
        if check_distance(self.mols[pos], molecule[pos]):
            return

        #Check if molecule in cell bounds
        if any(i >= j for x in molecule[pos] for i,j in zip(x, self.size)):
            return

        self.mols[atm] += molecule[atm]
        self.mols[pos] += molecule[pos]
        self.molCount  += 1
        return

    def make_xzy(self, save_name):
        xyz = []
        spa = '        '
        for i,j in zip(self.mols[atm], self.mols[pos]):
            xyz.append(str(i) + spa + str(j[0]) +
                       spa + str(j[1]) + spa + str(j[2]) + '\n')

        f = open(save_name, 'w')
        f.writelines(xyz)
        f.close()
        return


#Basic functions used throughout code-----------------------------------
def read_molecule(molecule):
    atm = 'Atoms'
    pos = 'Positions'

    mol = {atm:[], pos:[]}

    for line in molecule:
        mol[atm].append(line.split()[0])
        x   = np.float64(line.split()[1])
        y   = np.float64(line.split()[2])
        z   = np.float64(line.split()[3])
        xyz = (x,y,z)
        mol[pos].append(xyz)

    return mol

def check_distance(atoms, mol):
    for i in range(len(mol)):
        for j in range(len(atoms)):
            x1,y1,z1 = mol[i][0],mol[i][1],mol[i][2]
            x2,y2,z2 = atoms[j][0], atoms[j][1], atoms[j][2]
            d = np.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
            if d < 2.00:
                return True
    return False
