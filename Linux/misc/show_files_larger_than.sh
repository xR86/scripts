
# ### Alternative 1 ### #
#one liner that finds file over a size, and redirects STDERR (hides it)
#[[ $(find /usr/bin -type f -size +51200c 2>/dev/null ]]

# ### Alternative 2 ### #
#shows files larger than 5MB
# for file in /usr/bin
# do
# 	#FILESTAT = $(du -h $file | cut -f1)
# 	FILESTAT = $(du -sm $file | awk '$1 > 5' | cut -f1) 
# 	if [ filestat ]
# 	then
# 		echo $file $FILESTAT
# done

# ### Obs: #
#cd /usr/bin | ll | du -h | cut -f1
	#without the if

# ### Main solution ### #
#searches in /usr/bin for files larger than 5MB
find /usr/bin -size +5M #simplest
