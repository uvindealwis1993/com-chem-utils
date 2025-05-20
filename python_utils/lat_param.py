#!/usr/bin/env python
import numpy as np

with open("CONTCAR","r") as f:
    lines=f.readlines()

lat_mat=np.zeros((3,3))
for i in range(3):
    lat_mat[i,:]=list(map(float,lines[2+i].strip().split()))

a=np.sqrt(np.sum(lat_mat[0,:]**2))
b=np.sqrt(np.sum(lat_mat[1,:]**2))
c=np.sqrt(np.sum(lat_mat[2,:]**2))
print(a,b,c)

alpha = np.arccos(np.dot(lat_mat[1,:],lat_mat[2,:])/b/c)*360/2/np.pi
beta  = np.arccos(np.dot(lat_mat[0,:],lat_mat[2,:])/a/c)*360/2/np.pi
gamma = np.arccos(np.dot(lat_mat[0,:],lat_mat[1,:])/a/b)*360/2/np.pi
print(alpha,beta,gamma)
