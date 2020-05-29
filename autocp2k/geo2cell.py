from .config import *

def geo2cell(geofile, posfile):
    """
    This function take a geometry optimization file and converts it to
    a cell optimization file.

    geofile: string
        This should be a string that points to the input file of an
        already run geometry optimization file. (FULL DIRECTORY STRING REQUIRED)
    posfile: string
        This should be a string that points to the position trace file produced
        by the geometry optimization file ran. (FULL DIRECTORY STRING REQUIRED)
    """
