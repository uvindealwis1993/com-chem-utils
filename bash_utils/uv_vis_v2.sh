#!/bin/bash
#Uvin De Alwis
#Execute Multiwfn with folloiwng command
#Find tddft.log files and where they are located in current or sub directories
File=$(find $PWD -iname "tddft.log")
#runs for loop to go through each tddft.log file
for i in ${File}; do
#the path to the file
molpath=${i%/*}
#the forlder where the file is located
moldir=${molpath%/*}
#go to where the file is
cd ${molpath}
mkdir spectra
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
mv spectrum_curve.txt spectra/spectrum_curve_x.txt
mv spectrum_line.txt spectra/spectrum_line_x.txt
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
mv spectrum_curve.txt spectra/spectrum_curve_y.txt
mv spectrum_line.txt spectra/spectrum_line_y.txt
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
mv spectrum_curve.txt spectra/spectrum_curve_z.txt
mv spectrum_line.txt spectra/spectrum_line_z.txt
/home/dealwisu/bin/Multiwfn_3.8_dev_bin_Linux/Multiwfn tddft.log << EOF
11
-3
4
10
1
8
0.1
2
EOF
mv spectrum_curve.txt spectra/spectrum_curve_xy.txt
mv spectrum_line.txt spectra/spectrum_line_xy.txt
/home/dealwisu/bin/Multiwfn_3.8_dev_bin_Linux/Multiwfn tddft.log << EOF
11
-3
5
10
1
8
0.1
2
EOF
mv spectrum_curve.txt spectra/spectrum_curve_xz.txt
mv spectrum_line.txt spectra/spectrum_line_xz.txt
/home/dealwisu/bin/Multiwfn_3.8_dev_bin_Linux/Multiwfn tddft.log << EOF
11
-3
6
10
1
8
0.1
2
EOF
mv spectrum_curve.txt spectra/spectrum_curve_yz.txt
mv spectrum_line.txt spectra/spectrum_line_yz.txt
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
mv spectrum_curve.txt spectra
mv spectrum_line.txt spectra
cd spectra
#column -t will format the spacing between columns to a single space or tab
paste spectrum_curve.txt spectrum_curve_x.txt spectrum_curve_y.txt spectrum_curve_z.txt spectrum_curve_xy.txt spectrum_curve_xz.txt spectrum_curve_yz.txt| awk '{print $1,$2,$4,$6,$8,$10,$12,$14}' | column -t > uv_vis.txt
#Export MO contribution to excitations and save in tddft_exc.txt
cd ../
/home/dealwisu/bin/Multiwfn_3.8_dev_bin_Linux/Multiwfn tddft.log << EOF
18
15
y
EOF
done



