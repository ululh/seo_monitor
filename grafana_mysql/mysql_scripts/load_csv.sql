use mdr;

LOAD DATA INFILE "/var/lib/mysql/CSVs/ref_mdr_20210112.csv" 
INTO TABLE mdr_seo 
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS

(@col1, @col2, @col3, @col4, @col5, @col6, @col7, @col8, @col9, @col10, @col11, @col12, @col13, @col14)
        SET date = nullif(@col1,''),
            keyword = nullif(@col2,''),
            store_rank = nullif(@col3,''),
            store_first_url = nullif(@col4,''),
            store_nb_occurences = nullif(@col5,''),
            facebook_rank = nullif(@col6,''),
            facebook_first_url = nullif(@col7,''),
            facebook_nb_occurences = nullif(@col8,''),
            pinterest_rank = nullif(@col9,''),
            pinterest_first_url = nullif(@col10,''),
            pinterest_nb_occurences = nullif(@col11,''),
            instagram_rank = nullif(@col12,''),
            instagram_first_url = nullif(@col13,''),
            instagram_nb_occurences = nullif(@col14,'')
; 
