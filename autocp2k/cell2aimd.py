from .config import *

def geo2cell(cellfile, posfile, outfile):
    """
    This function take a geometry optimization file and converts it to
    a cell optimization file.

    cellfile: string
        This should be a string that points to the input file of an
        already run cell optimization file. (FULL DIRECTORY STRING REQUIRED)
    posfile: string
        This should be a string that points to the position trace file produced
        by the cell optimization file ran. (FULL DIRECTORY STRING REQUIRED)
    outfile: string
        This should be a string that points to the output file produced
        by the cell optimization file ran. (FULL DIRECTORY STRING REQUIRED)
    """
