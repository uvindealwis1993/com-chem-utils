#!/usr/bin/python
import re

# Define a function to convert hartrees to electron volts (eV)
def hartree_to_ev(e):
    return e * 27.2114

# Open the Gaussian log file
with open('opt.log', 'r') as f:
    log = f.read()

# Use regular expressions to extract the orbital energies
homo_re = re.compile('Alpha  occ. eigenvalues\s+(-\d+\.\d+)\s+(-\d+\.\d+)\s+(-\d+\.\d+)')
lumo_re = re.compile('Alpha virt. eigenvalues\s+(-\d+\.\d+)\s+(-\d+\.\d+)\s+(-\d+\.\d+)')
homo_match = homo_re.search(log)
lumo_match = lumo_re.search(log)

# Extract the HOMO and LUMO energies in hartrees
homo_energy = float(homo_match.group(3))
lumo_energy = float(lumo_match.group(1))

# Convert energies to eV
homo_energy_ev = hartree_to_ev(homo_energy)
lumo_energy_ev = hartree_to_ev(lumo_energy)

# Print the energies in eV
print(f'HOMO energy: {homo_energy_ev:.2f} eV')
print(f'LUMO energy: {lumo_energy_ev:.2f} eV')

# Calculate the HOMO-LUMO gap in eV
homo_lumo_gap_ev = lumo_energy_ev - homo_energy_ev

# Print the HOMO-LUMO gap in eV
print(f'HOMO-LUMO gap: {homo_lumo_gap_ev:.2f} eV')

