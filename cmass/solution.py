def readPDB(pfile):
    ''' read a pdb file and return coordinates of atoms (2D list) '''
    atomicCoor = []     # [[name, x, y, z]]

    # your code should be here
    
    return atomicCoor

def readTOP(tfile):
    ''' read a topology file and return atomic masses (dict) '''
    atomicMass = {}     # {name: mass}
 
    # your code should be here
        
    return atomicMass

def readTOPs(tdir='./topology'):
    ''' read topology files in tdir and return atomic masses (dict) '''
    atomicMass = {}     # {name: mass}

    if tdir[-1] != '/' or '\\':
        tdir += '/'
    
    import os
    for tfile in os.listdir(tdir):
        atomicMass = {**atomicMass, **readTOP(tdir + tfile)}
        
    return atomicMass
