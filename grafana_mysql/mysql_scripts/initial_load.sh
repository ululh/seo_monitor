#!/bin/bash

PASS=$1
mysql -uroot -p$PASS < /mysql_scripts/create_table_mdr.sql

for file in $(ls /var/lib/mysql/CSVs)
do
	sed -e "s/TOTO/$file/" /mysql_scripts/load_csv.sql.template > /mysql_scripts/load_csv.sql
	#cat /mysql_scripts/load_csv.sql
	mysql -uroot -p$PASS < /mysql_scripts/load_csv.sql
done
