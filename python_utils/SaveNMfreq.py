#!/usr/bin/python
'''
Daniel Devore
File to change freq to freq(SaveNM) to freq.com files
'''
#Initialize system
#Open opt.com file in readmode
freq = open("freq.com", "r")
#Define data within
data = ""
#Use for loop to go through file
for line in freq:
    #define what text need be replaced
    vib = line.replace("freq","freq(SaveNM)")
    #concatenate the old and new text
    data = data + vib
#Close file
freq.close()
#Open the file in write mode
freq_new = open("freq.com","w")
#Overwrite the old text with the new/replaced
freq_new.write(data)
#Close the file
freq_new.close()

