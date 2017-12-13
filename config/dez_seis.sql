
create database dez_seis;

create table usuario (
	nome varchar(50) not null,
	email varchar(100),
	idade int not null,
	senha varchar(50) not null,
	status varchar(50) default '',
	apelido varchar(50) default '',
	primary key(email)
);
