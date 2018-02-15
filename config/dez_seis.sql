
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

create table notificacao (
	email_usuario varchar(100),
	mensagem varchar(50),
	foi_lida boolean default 'false',

	foreign key(email_usuario) references usuario(email) on delete cascade
);

create table amizade (
	email_usuario1 varchar(100),
	email_usuario2 varchar(100),

	foreign key(email_usuario1) references usuario(email) on delete cascade,
	foreign key(email_usuario2) references usuario(email) on delete cascade
)
