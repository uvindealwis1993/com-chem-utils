#!/bin/bash
#Uvin De Alwis
#the forlder where the file is located
fpath=$(find $PWD -type d -name "step2")
#go to where the file 
for i in ${fpath}; do
#the path to the file
molpath=${i}
cd ${molpath}
if grep -q "Voluntary" OUTCAR; then
mkdir scf2
cp CONTCAR POTCAR KPOINTS run_vasp.pbs scf2
cd scf2
mv CONTCAR POSCAR

# Create the INCAR file
        cat << EOF > INCAR
# This file contains the parameters of the calculation

# Start Parameters for run
# name of calculation
SYSTEM = Antimexene
# ISTART : 0 -from scratch; 1 - restart with constant energy cut-off ( WAVECAR file needed); 2 - restart with constant basis set ( needs WAVECAR file)
ISTART = 0
LCHARG = .TRUE.
LWAVE  = .FALSE.
# Detail level of output use 3 as default and 4 for debugging only
#NWRITE = 3
# Parallelization: determines numbr of cores/Orbitals  - wrong setting may result in "Segmentation Fault" error - fallback: NPAR = 1; Else: NPAR = Number of NODES
# Spinpolarized: 1 - No; 2 - Yes
#NPAR = 2
#NUPDOWN = 8
ISPIN  = 2
#MAGMON = 26*0.0 8*0.1 20*0.0
# Difference between e- with differrent spins - If 0 - singlet (closed shell); 1 - doublet etc. ; if "-1" - spin is optimized during SCF
#NUPDOWN = 16
# Define Initial magnetic Moment - Spin is optimized during calculation; good starting guess is 2*Atoms
#MAGMOM = 2*1.0
## Number of electrons in system - if commented out neutral system is used
#NELECT = 2
NCORE = 4
# Electronic Relaxation
############################################################
# GGA type: PW91 - 91; PBE - PE; RPBE - RP;
############################################################
#GGA =BF
#GGA = RP
#IVDW = 4
#F
###########################################################
## Uncomment for BEEF-vdW + GGA=BF
############################################################
     #luse_vdw = True
    #zab_vdw   = -1.8867
     #lbeefens = True

###########################################################
## VASP SOL keywords
###########################################################

#LSOL = .TRUE.
#EB_K = 80

#############################################################################################
# Uncomment for HSE06 and use together with GGA=PE + PBE PAW
#############################################################################################
#   LHFCALC   = .TRUE.
#   TIME      = 0.4
#   HFSCREEN  = 0.2
#   PRECFOCK  = N
###############################
# GGA+U
##############################
# LDA+U .TRUE. or .FALSE.
# LDAU=.TRUE
# LDA+U implementation 1 - rotationally invariant LSDA+U introduced by Liechtenstein; 2 - simplified (rotationally invariant) approach to the LSDA+U, introduced by Dudarev
#LDAUTYPE=1
# Quantum number to which the U is added: Array containing 1 value/species; -1 - no U added; 1 - p; 2 - d; 3 - f
#LDAUL= 2 -1
# On site Coulomb Interaction value (Hubbard U) 1 vallue/species
#LDAUU= 4.5 0
# effective on-site Exchange interaction parameters (J)
#DAUJ= 0.86 0
# correct for aspherical charge densities at d and f elements
#LASPH = .TRUE.
#####################################################################################################
# MetaGGA - TPSS | RTPSS | M06L | MBJ; comment out if any other functional is used
#####################################################################################################
#METAGGA = TPSS
##########################################################################
#vdW Correction 12-DFT-D3 method with Becke-Jonson damping (available as of VASP.5.3.4); 21-Tkatchenko-Scheffler method with Hitshfeld partitioning (available as of VASP.5.3.5); 4-dDsC (from version 5.4.1) 
############################################################################
IVDW = 12
# Maximum number of SCF steps 
NELM = 100
# Add "Delay", i.e. number of non-self consistent steps in the beginning; important for purely converging systems. X > 0 - for all ionic steps X < 0 - only for the fist step
#NELMDL = 0
# Plane Wave cutoff
#KPAR = 4
ENCUT = 450 eV
# Energy convergence for SCF [eV]
EDIFF = 1.0E-8
EDIFFG = -0.001
# Precision of FFT grid - Influence on nENCUT? Options: LOW - Normal (=Default) - HIGH
PREC = Accurate #HIGH
# Number of bands in calc; Default for closed shell: NELECT/2 + NIONS/2; spin polarized: 0.6ENLECT + NMAGMOMS
#NBANDS = 500
# Smearing type: -5: Tetrahedron method -1 - Fermi Smearing; 0 - Gaussian smaearing; X > 0 Methfesselpaxton smearing of Xth order (recommended for metals)
ISMEAR = 0
# Smearing in [eV]
SIGMA = 0.01
# Optimisation in Realspace? - FALSE = reciprocal space (cell < 20 atoms); AUTO - real space (cell > 20 atoms
LREAL = .FALSE.
# SCF Algorithm: Fast - Davidson follolwed by DIIS; Normal - Davidson; Conjugate - Conjugate Gradient
ALGO = Normal
# Mixing settings in case of poor convergence:
# Mixer type: 1 - Kerker mixing; 4 - Broyden mixing
# IMIX = 4
# linear mixing parameter; default: 0.4
# AMIX = 0.1
# initial mixing parameter; default: 1.0, try almost 0 for poor converging systems (molecules, insulators, etc)
# BMIX = 0.0001
# Weight factor for Broyden mixing; default: 1000
# WC = 50
#
############################################################
# Symmetry Options
############################################################
# Turn Symmetry on - 1 /off - 0
ISYM = 1
# Precision for symmetry determination default 1E-5
#SYMPREC = 1.0E-8

# Geometry Optimisation
# Maximum number of geometry steps; set to 0 for single point calculation
NSW = 0 
# Algorithm type: 1 -quasi-newton 2 -conjugate-gradient
IBRION = -1
#POTIM = 0.01
# What is optimized? 2 - only relax ionic positions; 3 - relax positions cell shape and cell volume; 4 - relax position and cell shape
ISIF = 2
# Geometry Convergence if > 0: Geo opt stopped if Energyy change smaller; if < 0: Geo opt stopped if forces are smaller
#EDIFFG = -0.01

#############################################################
# TS search
# Use: set IBRION = 3 and POTIM=0
#############################################################
# Optimizers 0 -VASP default; 1 - LBFGS; 2 - CG; 7 - FIRE
#IOPT = 0
# Number of images -> enforces NEB; Note: number of cores must be dividable by numbr of images; if segmentation fault error then use 1node/image as fallback
#IMAGES = 8
# Spring constant ; if < 0 nudging is turned on
#Spring = -5.0
# Turn on climbing algorithm -> preconvergence with normal NEB recommended .TRUE./.FALSE.
#LCLIMB = .FALSE
#ICHAIN = 0
######################################################################
# for DOS only
######################################################################
# LORBIT - Which information to print? 12 - PSO, PDOS and LDOS
# #EMIN =  minimum energy for evaluation of DOS
# #EMAX =  maximum energy for evaluation of DOS
# #NEDOS=  number of grid points in DOS
# LORBIT = 12
# EMIN = -15 eV
# EMAX = 15 eV
# NEDOS = 2000

###########################################################################################
# Uncomment for IR calcs + set IBRION = 7 NSW = 1 NWRITE = 3 and LREAL = .FALSE. + dont use Gamma point only calcs
############################################################################################
# LEPSILON = .TRUE.
# ISYM = 0
# NELMIN = 10

#################################################
# Uncomment for STM
# Requires fully converged WAVECAR file + ISTART = 1
#################################################
# LPARD  Generate Partial charge density .TRUE./.FALSE.
#  LPARD = .TRUE.
#  LWAVE =.FALSE.
#  LCHARG = .TRUE.
# LSEPK/LSEPB - separate partial charge density into k-points/bands
#  LSEPK = .FALSE.
#  LSEPB = .FALSE.
# EINT = Int1 Int2 -> corresponds to the range of energy in which the electrons are included; equivalent to bias applied during STM
#  EINT = 0 1.8
# NBMOD = -3 : Offsets EINT with respect to Fermi level
#  NBMOD = -3
#
###################################################################
# Uncomment for core level shifts
# Note: compute corelevel shifts as E(not excited) - E(excited) and state core level shifts relative to a reference state!
# Input: NSW = 0 + normal inpput from DFT calc
# atom on shich core level shift shallbe computed must be singled out in POTCAR file 8e.g. by using a unic element name and in the POTCAR the normal PAW must be used for this element
###################################################################
# ICORELEVEL - activates core level shift calc; 1 - use initial density (only if excitationis short lifed and ther eis not sufficient time for relaxation; 2 - relax electron density to compute core level shifts
#ICORELEVEL = 2
# CLNT - Species (state as number of species in POSCAR file; e.g. if Zn O Ocore then CLNT = 3)
#CLNT = 3 
# CLN - main quantum number of orbital from which electron is excited from
#CLN = 1
# CLL - l quantum number from which electron is taken from
#CLL = 0
# CLZ - electron count; defines number of electrons which are excited from core usually either 0.5 or 1
#CLZ = 1
EOF
qsub run_vasp.pbs
fi
done

