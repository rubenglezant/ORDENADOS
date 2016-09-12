mysql> create database piu;
Query OK, 1 row affected (0.13 sec)

mysql> use piu;
Database changed
mysql> create table horas(buslinea as VARCHAR(25), minutos as INTEGER);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'as VARCHAR(25), minutos as INTEGER)' at line 1
mysql> create table horas(buslinea VARCHAR(25), minutos INTEGER);
Query OK, 0 rows affected (0.26 sec)

mysql> insert into horas values ('123 - Callao',3);
Query OK, 1 row affected (0.07 sec)

mysql> insert into horas values ('263 - Sol',7);
Query OK, 1 row affected (0.05 sec)

mysql> insert into horas values ('345 - Sevilla',10);
Query OK, 1 row affected (0.10 sec)

mysql> insert into horas values ('45 - Cuzco',15);
Query OK, 1 row affected (0.06 sec)

mysql> insert into horas values ('675 - Cibeles',45);
Query OK, 1 row affected (0.04 sec)

