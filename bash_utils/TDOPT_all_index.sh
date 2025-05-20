#!/bin/bash
cat << EOF > calcall.txt
18
1
tddft-opt-trialA.log
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

 Multiwfn tddft-opt-trialA.fchk < calcall.txt |tee log.txt  #Running command
 rm ./calcall.txt ./result.txt -f

grep "Sr index" ./log.txt |nl >> result_opt.txt;echo >> result_opt.txt
grep "D index" ./log.txt |nl >> result_opt.txt;echo >> result_opt.txt
grep "RMSD of hole in" ./log.txt |nl >> result_opt.txt;echo >> result_opt.txt
grep "RMSD of electron in" ./log.txt |nl >> result_opt.txt;echo >> result_opt.txt
grep "H index" ./log.txt |nl >> result_opt.txt;echo >> result_opt.txt
grep "t index" ./log.txt |nl >> result_opt.txt
echo
echo "Finished!"
