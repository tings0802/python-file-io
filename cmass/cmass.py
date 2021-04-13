#!/usr/bin/env python3

import sys, argparse
import solution
from modules import calculate, inspect, read

def main(module, pfile, tdir):
    coor = module.readPDB(pfile)
    mass = module.readTOPs(tdir)
    molecule, missing = calculate.createMole(coor, mass)

    cenMass, totMass = calculate.calulateCM(molecule)
    inspect.printCM(cenMass, totMass)
    
    angMass = calculate.calculateMI(molecule, cenMass)
    inspect.printMI(angMass)

    return cenMass, totMass, angMass

if __name__ == "__main__":
    parser = argparse.ArgumentParser('cmass.py')
    parser.add_argument("-c", "--check", action='store_true', help="check the answer")
    parser.add_argument("--pdb", help="path to the PDB file (protein data bank)", default='pdb/receptor5_Pemirolast.pdb')
    parser.add_argument("--top", help="directory contains topology files", default='topology')
    args = parser.parse_args()

    if args.check:
        print('[My answer]')
        ans = main(read, args.pdb, args.top)

    try:
        print('\n[Your answer]')
        sol = main(solution, args.pdb, args.top)
    except:
        sol = None
        raise
    finally:
        if args.check:
            print('\nCongratulations! Your answer is correct!' if sol == ans else '\nOops! Something is wrong.', end='\n\n')
