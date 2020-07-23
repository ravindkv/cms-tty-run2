eosls="eos root://cmseos.fnal.gov ls"

for dir in `$eosls /store/user/npoudyal/histograms_*`;
do
#echo $dir
	for dir1 in `$eosls /store/user/npoudyal/$dir`;do
		#echo $dir/$dir1
		for dir2 in `$eosls /store/user/npoudyal/$dir/$dir1`;do
		echo $dir/$dir1/$dir2
		$eosls -lh /store/user/npoudyal/$dir/$dir1/$dir2
		done
	done
done


#if [[ -d ${dir} ]];then
#	for dir1 in `eosls /store/user/npoudyal/${dir}`:do
#		for dir2 in `eosls /store/user/npoudyal/${dir}/${dir1}`:do
#		done
#	done
#fi
