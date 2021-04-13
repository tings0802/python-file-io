def readPDB(pfile):
    ''' read a pdb file and return coordinates of atoms (2D list) '''
    atomicCoor = []     # [[name, x, y, z]]

    with open(pfile, 'r') as ifile:
        rawData = ifile.readlines()
    
    for row in rawData:
        data = row.split()
        if data[0] == 'ATOM':
            atomicCoor.append([row[13], float(data[6]), float(data[7]), float(data[8])])
    
    return atomicCoor

def readTOP(tfile):
    ''' read a topology file and return atomic masses (dict) '''
    atomicMass = {}     # {name: mass}
 
    with open(tfile, 'r') as ifile:
        rawData = ifile.readlines()

    for row in rawData:
        data = row.split()
        try:
            if data[0] == 'MASS':
                atomicMass[data[4]] = float(data[3])
        except:
            pass
        
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
