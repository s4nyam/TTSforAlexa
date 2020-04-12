a=(`wc -l file.txt`) ; lines=`echo $(($a/250)) | bc -l` ; split -l $lines -d  file.txt file
