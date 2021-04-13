def createMole(atomicCoor, atomicMass):
    ''' merge atomic mass into coordinates list '''
    molecule = atomicCoor   # [[name, x, y, z, mass]]
    missing = []            # [[name, x, y, z, index]]

    for i in range(len(molecule)):
        atom = molecule[i]
        try:
            atom.append(atomicMass[atom[0]])
        except:
            missing.append([*atom, i])
            atom.append(0)

    return molecule, missing

def calulateCM(molecule):   # [[name, x, y, z, mass]]
    ''' calculate the molecule's center of mass and molecular mass'''
    cenMass = [0, 0, 0]     # [x, y, z]
    totMass = 0

    for atom in molecule:
        totMass += atom[4]
        for i in range(len(cenMass)):
            cenMass[i] += atom[i + 1] * atom[4]
    
    for i in range(len(cenMass)):
        cenMass[i] /= totMass
    
    return cenMass, totMass

def calculateMI(molecule, cenMass):   # [[name, x, y, z, mass]]
    angMass = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for atom in molecule:
        x = [atom[1] - cenMass[0], atom[2] - cenMass[1], atom[3] - cenMass[2]]
        for i in range(3):
            for j in range(3):
                delta = 1 if i == j else 0
                r2 = x[0] ** 2 + x[1] ** 2 + x[2] ** 2
                angMass[i][j] = atom[4] * (r2 * delta - x[i] * x[j])

    return angMass
