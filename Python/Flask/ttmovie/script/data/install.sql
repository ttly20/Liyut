create database ttmovie;
use ttmovie;
create table usr(id int not null auto_increment,username char(36) not null,password char(128) not null,email char(36) not null,sex char(4),ad char(255),primary key (id));
create table movie(id int not null auto_increment,title char(36) not null,description char(255) not null,poster char(36) not null,play char(128) not null,download char(128) not null,keywords char(255) not null,navigation char(64) not null,player char(128) not null,datetion date not null,primary key (id));
create table keywords(id int auto_increment,keywords char(16) not null,url char(36) not null,hot int not null,primary key (id));
create table station(title char(16) not null,keywords char(128) not null,url char(36) not null,description char(255) not null,ad char(255) not null,primary key (title));
create table navigation(title char(16) not null,url char(36) not null,keywords char(128) not null,description char(255) not null,logo char(36) not null,primary key (title));
create table carousel(id int not null auto_increment,imgpath char(36) not null,alt char(64) not null,caption char(255),primary key (id));
create table friend(id int auto_increment,title char(16) not null,url char(36) not null,primary key (id));
