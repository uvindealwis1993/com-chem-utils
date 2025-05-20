!/bin/bash
#Uvin De Alwis
#Execute Multiwfn with folloiwng commands
/home/dealwisu/bin/Multiwfn_3.8_dev_bin_Linux/Multiwfn multiple.txt << EOF
11
-3
1
20
1-5
11-200
0
10
1
8
0.1
2
EOF
mv curveall.txt curveall_x.txt
/home/dealwisu/bin/Multiwfn_3.8_dev_bin_Linux/Multiwfn multiple.txt << EOF
11
-3
2
20
1-5
11-200
0
10
1
8
0.1
2
EOF
mv curveall.txt curveall_y.txt
/home/dealwisu/bin/Multiwfn_3.8_dev_bin_Linux/Multiwfn multiple.txt << EOF
11
-3
3
20
1-5
11-200
0
10
1
8
0.1
2
EOF
mv curveall.txt curveall_z.txt
/home/dealwisu/bin/Multiwfn_3.8_dev_bin_Linux/Multiwfn multiple.txt << EOF
11
-3
0
20
1-5
11-200
0
10
1
8
0.1
2
EOF
#column -t will format the spacing between columns to a single space or tab
paste curveall.txt curveall_x.txt curveall_y.txt curveall_z.txt | awk '{print $1,$2,$3,$4,$5,$6,$8,$9,$10,$11,$12,$14,$15,$16,$17,$18,$20,$21,$22,$23,$24}' | column -t > uv_vis_multiple.txt
rm -rf spectrum_line.txt





