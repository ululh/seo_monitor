CREATE DATABASE mdr;

use mdr;

create table mdr_seo(
   date DATE NOT NULL,
   keyword VARCHAR(50) NOT NULL,
   store_rank INT,
   store_first_url VARCHAR(400),
   store_nb_occurences INT,
   facebook_rank INT,
   facebook_first_url VARCHAR(400),
   facebook_nb_occurences INT,
   pinterest_rank INT,
   pinterest_first_url VARCHAR(400),
   pinterest_nb_occurences INT,
   instagram_rank INT,
   instagram_first_url VARCHAR(400),
   instagram_nb_occurences INT,
   PRIMARY KEY ( keyword, date )
);
