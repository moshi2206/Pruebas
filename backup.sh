#!/bin/bash
# vars
backups_path="/home/moshi/cron/backups"
database="mydatabase"
current_date_time="`date +%Y%m%d%H%M%S`";

# dump
pg_dump -Fc $database > $backups_path/$current_date_time.backup;

# get size of dump
size="`wc -c $backups_path/$current_date_time.backup`";
# get oldest backup
first_backup="`ls $backups_path | sort -n | head -1`"
echo 'First backup '$first_backup
# get size of oldest backup
size_first="`wc -c $backups_path/$first_backup`"
echo 'Size first '$size_first
# get backups count
backups_count="`find  $backups_path/*.backup -type f | wc -l`"
echo 'Backups count '$backups_count
# condition for remove if there is more than 4 backups
if [ $backups_count -ge 5 ] ; then
 echo 'Greather than 5'
# removing backup
 rm $backups_path/$first_backup
 first_text="`ls $backups_path | sort -n | head -1`"
# removing text of backup
 rm $backups_path/$first_text
# printing body explaining removed backup
 printf "File deleted: "$first_backup >>  $backups_path/$current_date_time.txt
 printf "Size: "$size_first >>  $backups_path/$current_date_time.txt
fi
