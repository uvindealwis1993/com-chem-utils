#!/bin/bash
#USER BACKUP AND CHECK SCRIPT FOR KODIAK FILESYSTEM USING RSYNC
#Thomas L. Ellington
#02-08-2019

#*NOTE: CAN BE USED AS STANDALONE SCRIPT OR WITH CRON FOR AUTOMATED/SCHEDULED BACKUPS

#IMPORTANT KEYWORDS
#-c:			file comparison via checksum
#-r: 			execute recursively
#-v: 			verbose printing
#--delete		delete files existing in destination that arent in source (USE --dry-run!!!)
#--ignore-existing:	ignore files/directories existing in both areas
#--prune-empty-dirs:	ignore empty directories
#--dry-run:		print output without an executing action


#RECURSIVE DATA BACKUP FROM ~/chem
rsync -v -r --ignore-existing --prune-empty-dirs /home/ellingtont/chem /data/ellingtont

#COMPARISON OF ~/chem TO /data/ellingtont/chem VIA RECURSIVE CHECKSUM
rsync --dry-run -v -r -c --delete /home/ellingtont/chem /data/ellingtont/chem
