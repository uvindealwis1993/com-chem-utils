#!/usr/bin/python
import re

# Open the Gaussian TDDFT log file
with open('tddft.log', 'r') as f:
    log_data = f.read()

# Define a regular expression pattern to match the TDDFT excitations
excitation_pattern = r'(Excited State)\s+(\d+)(\s)\s+(\S+)\s+(\d+)\s+eV\s+(\S+)\s+nm\s+f=([\d\.]+)\s+'

# Use the pattern to extract the excitations with state number, energy and oscillator strength
excitations = re.findall(excitation_pattern, log_data)
# Convert the oscillator strengths to floats and store in a list with corresponding state number and energy
excitations_list = []
for excitation in excitations:
    state_num = int(excitation[1])
    energy = float(excitation[2])
    oscillator_strength = float(excitation[4])
    excitations_list.append((state_num, energy, oscillator_strength))

# Sort the list based on oscillator strength and select top 10 excitations
top_10_excitations = sorted(excitations_list, key=lambda x: x[2], reverse=True)[:10]

# Write the top 10 excitations to a file named 'excited_state.txt'
with open('excited_state.txt', 'w') as f:
    f.write('Excited State Number\tExcited State Energy (eV)\tOscillator Strength\n')
    for excitation in top_10_excitations:
        state_num = excitation[0]
        energy = excitation[1]
        oscillator_strength = excitation[2]
        f.write(f'{state_num}\t\t\t{energy}\t\t\t\t{oscillator_strength}\n')
