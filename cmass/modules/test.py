def testPrint():
    printList([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print()
    printDict({'A': 4, 'B': 5, 'C': 6})
    print()
    printMole([[1, 4, 5, 3, 2], [3, 5, 2, 0, 8], [7, 1, 2, 4, 9]])

def testTOP(tdir='./topology/', tfile='top_all22_prot.rtf'):
    print(f'read a single topology file: {tdir + tfile}')
    printDict(readTOP(tdir + tfile))
    print(f'\nread topology files in directory: {tdir}')
    printDict(readTOPs(tdir))

def testPDB(pdir='./pdb/', pfile='receptor5_Pemirolast.pdb'):
    printList(readPDB(pdir + pfile))

def testMole():
    coor = readPDB('./pdb/receptor5_Pemirolast.pdb')
    mass = readTOPs('./topology/')
    molecule, missing = createMole(coor, mass)

    printMole(molecule, 18)
    print()
    printMiss(missing)

def testCM():
    coor = readPDB('./pdb/receptor5_Pemirolast.pdb')
    mass = readTOPs('./topology/')
    molecule, missing = createMole(coor, mass)
    cenMass, totMass = calulateCM(molecule)
    printCM(cenMass, totMass)

def testMI():
    coor = readPDB('./pdb/receptor5_Pemirolast.pdb')
    mass = readTOPs('./topology/')
    molecule, missing = createMole(coor, mass)
    cenMass, totMass = calulateCM(molecule)
    angMass = calculateMI(molecule, cenMass)
    printMI(angMass)
