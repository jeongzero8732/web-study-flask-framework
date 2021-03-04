SET NAMES utf8 ;
SET character_set_client = utf8mb4 ;
create database pybo;
use pybo;

create table user(
    userID varchar(20) not null,
    userPasswd varchar(150) not null,
    userName varchar(20) not null,
    userSex varchar(20) not null,
    primary key(userID)
);

create table evaluate(
    evalID int(10) not null auto_increment,
    writer varchar(20) not null,
    lec_name varchar(20) not null,
    pro_name varchar(20) not null,
    content_title varchar(20) not null,
    lec_skill varchar(20) not null,
    lec_level varchar(20) not null,
    eval_contents varchar(20) not null,
    primary key(evalID)
);