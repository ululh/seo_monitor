Pull MySQL docker image :
docker pull mysql

Launch MySQL server :
docker run --name mdr-mysql -e MYSQL_ROOT_PASSWORD=xxxx -d mysql:latest

Below is a command to launch a mysql client container
docker run -it --network bridge --rm mysql mysql -h172.17.0.2 -uroot -pxxxx
If using the default bridge network we can't use the DNS name of the mysql server container 
To run sql scripts located in the docker volume it is easier to exec bash in the mysql container:
docker exec -it mdr-mysql bash
cd /var/lib/mysql # /var/lib/mysql being the directory where the docker volume is mounted within the container
then mysql -uroot -pxxxx < create_table_mdr.sql

Grafana : 
docker run -d -p 3000:3030 grafana/grafana
