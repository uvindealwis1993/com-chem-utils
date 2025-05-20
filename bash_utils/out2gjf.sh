#Convert geometry (final, input orientation) in all Gaussian .out files in current folder to .gjf file by Multiwfn
#!/bin/bash
icc=0
nfile=`ls *.log|wc -l`
for inf in *.log
do
((icc++))
echo Converting ${inf} to ${inf//log/gjf} ... \($icc of $nfile\)
Multiwfn ${inf} << EOF > /dev/null
100
2
10
${inf//log/gjf}
0
q
EOF
done
