def printList(List):
    ''' print 2D list '''
    for line in List:
        for data in line:
            print(data, end='\t')
        print()

def printDict(Dict):
    ''' print key-value pairs line by line '''
    for key in Dict.keys():
        print(f'{key}\t{Dict[key]}')

def printMole(molecule, limit=-1):    # [[name, x, y, z, mass]]
    ''' print the atoms list of a molecule by the given format '''
    print(f'name\tmass\t\tcoordinates')
    for atom in molecule:
        print(f'{atom[0]}\t{atom[4]}\t\t{atom[1:4]}')
        limit -= 1
        if not limit: break
    print(f'molecule: {len(molecule)} atoms')

def printMiss(missing, limit=-1):     # [[name, x, y, z, index]]
    ''' print the missing atoms in a molecule '''
    if missing:
        print(f'name\tindex\tcoordinates')
        for atom in missing:
            print(f'{atom[0]}\t{atom[4]}\t{atom[1:4]}')
            limit -= 1
            if not limit: break
    print(f'missing: {len(missing)} atoms')

def printCM(cenMass, totMass=0, precision=4):
    ''' print center of mass and molecular mass with given presicion '''
    form = f'.{precision}f'
    print(f'center of mass: [{cenMass[0]:{form}}, {cenMass[1]:{form}}, {cenMass[2]:{form}}]')
    if totMass: print(f'molecular mass: {totMass:{form}}')

def printMI(angMass, precision=4):
    form = f'>10.{precision}f'
    print(f'moment of inertia:')
    for row in angMass:
        for col in row:
            print(f'{col:{form}}', end='')
        print()
