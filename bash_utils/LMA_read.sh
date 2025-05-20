mapfile -t files < <(find . -type f -name 'job.out')
Start=$(pwd)
for i in ${!files[@]}; do
q=${files[$i-1]:1}
w=${q::-8}
cd ${Start}${w}
cur=$(pwd)
python /home/frenchk/scripts/LMA_readV2.py
gnuplot LMAHist.txt
cd ${start}
done

