CREATE DATABASE IF NOT EXISTS users;

create table if not exists users(
userid varchar(20) primary key,
userpw varchar(20) not null,
username varchar(20) not null,
userage int,
useremail varchar(20),users
useradd varchar(50),
usergender varchar(20),
usertel varchar(20));

insert into users values(
'hong',
'1234',
'홍길동',
50,
'koea@qf.ccc',
'한국 그 어딘가에',
'man',
'010-8282-8282');member

select * from users;

