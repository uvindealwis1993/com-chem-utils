#!/bin/bash
#Uvin De Alwis
#Execute Multiwfn with folloiwng commands
/home/dealwisu/bin/Multiwfn_3.8_dev_bin_Linux/Multiwfn tddft.log << EOF
11
-3
1
10
1
8
0.1
2
EOF
mv spectrum_curve.txt spectrum_curve_x.txt
mv  spectrum_line.txt spectrum_line_x.txt
/home/dealwisu/bin/Multiwfn_3.8_dev_bin_Linux/Multiwfn tddft.log << EOF
11
-3
2
10
1
8
0.1
2
EOF
mv spectrum_curve.txt spectrum_curve_y.txt
mv spectrum_line.txt spectrum_line_y.txt
/home/dealwisu/bin/Multiwfn_3.8_dev_bin_Linux/Multiwfn tddft.log << EOF
11
-3
3
10
1
8
0.1
2
EOF
mv spectrum_curve.txt spectrum_curve_z.txt
mv spectrum_line.txt spectrum_line_z.txt
/home/dealwisu/bin/Multiwfn_3.8_dev_bin_Linux/Multiwfn tddft.log << EOF
11
-3
0
10
1
8
0.1
2
EOF
#column -t will format the spacing between columns to a single space or tab
paste spectrum_curve.txt spectrum_curve_x.txt spectrum_curve_y.txt spectrum_curve_z.txt | awk '{print $1,$2,$4,$6,$8}' | column -t > uv_vis.txt




