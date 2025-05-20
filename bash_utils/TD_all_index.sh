#!/bin/bash
cat << EOF > calcall.txt
18
1
tddft.log
EOF
for ((i=1;i<=200;i=i+1))  #Range of excited states
do
cat << EOF >> calcall.txt
$i
1
2
0
0
1
EOF
done

 Multiwfn tddft.chk < calcall.txt |tee log.txt  #Running command
 rm ./calcall.txt ./excited_result.txt -f

grep "Sr index" ./log.txt |nl >> excited_result.txt;echo >> excited_result.txt
grep "D index" ./log.txt |nl >> excited_result.txt;echo >> excited_result.txt
grep "RMSD of hole in" ./log.txt |nl >> excited_result.txt;echo >> excited_result.txt
grep "RMSD of electron in" ./log.txt |nl >> excited_result.txt;echo >> excited_result.txt
grep "H index" ./log.txt |nl >> excited_result.txt;echo >> excited_result.txt
grep "t index" ./log.txt |nl >> excited_result.txt
echo
echo "Finished!"
