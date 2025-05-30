#!/usr/bin/env python2.7

""" Calculate RMSD between two XYZ files
by: Jimmy Charnley Kromann <jimmy@charnley.dk> and Lars Bratholm
project: https://github.com/charnley/rmsd
license: https://github.com/charnley/rmsd/blob/master/LICENSE
"""

import numpy
import sys
import re

def fit(P, Q):
  """ Varies the distance between P and Q, and optimizes rotation for each step
  until a minimum is found.
  """
  step_size = P.max(0)
  threshold = step_size*1e-9
  rmsd_best = kabsch(P, Q)
  while True:
    for i in range(3):
      temp = numpy.zeros(3)
      temp[i] = step_size[i]
      rmsd_new = kabsch(P+temp, Q)
      if rmsd_new < rmsd_best:
        rmsd_best = rmsd_new
        P[:,i] += step_size[i]
      else:
        rmsd_new = kabsch(P-temp, Q)
        if rmsd_new < rmsd_best:
          rmsd_best = rmsd_new
          P[:,i] -= step_size[i]
        else:
          step_size[i] /= 2
    if (step_size<threshold).all():
      break
  return rmsd_best


def kabsch(P, Q):
  """ The Kabsch algorithm
  http://en.wikipedia.org/wiki/Kabsch_algorithm
  The algorithm starts with two sets of paired points P and Q.
  P and Q should already be centered on top of each other.
  Each vector set is represented as an NxD matrix, where D is the
  the dimension of the space.
  The algorithm works in three steps:
  - a translation of P and Q
  - the computation of a covariance matrix C
  - computation of the optimal rotation matrix U
  The optimal rotation matrix U is then used to
  rotate P unto Q so the RMSD can be caculated
  from a straight forward fashion.
  """

  # Computation of the covariance matrix
  C = numpy.dot(numpy.transpose(P), Q)

  # Computation of the optimal rotation matrix
  # This can be done using singular value decomposition (SVD)
  # Getting the sign of the det(V)*(W) to decide
  # whether we need to correct our rotation matrix to ensure a
  # right-handed coordinate system.
  # And finally calculating the optimal rotation matrix U
  # see http://en.wikipedia.org/wiki/Kabsch_algorithm
  V, S, W = numpy.linalg.svd(C)
  d = (numpy.linalg.det(V) * numpy.linalg.det(W)) < 0.0

  if(d):
    S[-1] = -S[-1]
    V[:,-1] = -V[:,-1]

  # Create Rotation matrix U
  U = numpy.dot(V, W)

  # Rotate P
  P = numpy.dot(P, U)

  return rmsd(P,Q)


def centroid(X):
  """ Calculate the centroid from a vectorset X """
  C = sum(X)/len(X)
  return C


def rmsd(V, W):
  """ Calculate Root-mean-square deviation from two sets of vectors V and W.
  """
  D = len(V[0])
  N = len(V)
  rmsd = 0.0
  for v, w in zip(V, W):
    rmsd += sum([(v[i]-w[i])**2.0 for i in range(D)])
  return numpy.sqrt(rmsd/N)


def get_coordinates(filename,Hs):
  """ Get coordinates from filename.
  Get coordinates from a filename.xyz and return a vectorset with all the
  coordinates.
  This function has been written to parse XYZ files, but can easily be
  written to parse others.
  """
  f = open(filename, 'r')
  V = []

  # Skip the first two lines
  for _ in xrange(2):
    f.next()

  if Hs == "noH":
    for line in f:
      v = line.strip().split()
      atom = v[0]
      if atom != "H":
        numbers = re.findall(r'[-]?\d+\.\d+', line)
        numbers = [float(number) for number in numbers]
        V.append(numpy.array(numbers))
  else:
    for line in f:
      numbers = re.findall(r'[-]?\d+\.\d+', line)
      numbers = [float(number) for number in numbers]
      V.append(numpy.array(numbers))

  f.close()
  V = numpy.array(V)
  return V


if __name__ == "__main__":

  args = sys.argv[1:]

  usage = """
Usage:
python calculate_rmsd.py <mol1.xyz> <mol2.xyz>
Calculate Root-mean-square deviation (RMSD) between two molecules, where the
two sets of xyz atoms are in the same order.
The script will return three RMSD values;
1) Normal: The RMSD calculated the straight-forward way.
2) Kabsch: The RMSD after the two coordinate sets are translated and rotated onto eachother.
3) Fitted: The RMSD after a fitting function has optimized the centers of the two coordinat sets.
"""

  if len(args) < 2:
    print usage
    sys.exit(0)

  mol1 = args[0]
  mol2 = args[1]
  if len(args) > 2:
    Hstatus = args[2]
  else:
    Hstatus = []

  P = get_coordinates(mol1,Hstatus)
  Q = get_coordinates(mol2,Hstatus)

  #print "Normal RMSD:", rmsd(P, Q)

  # Create the centroid of P and Q which is the geometric center of a
  # N-dimensional region and translate P and Q onto that center.
  # http://en.wikipedia.org/wiki/Centroid
  Pc = centroid(P)
  Qc = centroid(Q)
  P -= Pc
  Q -= Qc

  print "%-.3f" %kabsch(P, Q)
  #print kabsch(P, Q)
  #print "Kabsch RMSD:", kabsch(P, Q)
  #print "Fitted RMSD:", fit(P, Q)
  #print "Molecule1 Molecule2    Normal    Kabsch   Fitted"
  #print "--------- --------     ------    ------   ------"
  #print "%- 10s  %- 10s  %- .3f  %- .3f  %- .3f" %(mol1, mol2,  rmsd(P, Q), kabsch(P, Q), fit(P, Q))
