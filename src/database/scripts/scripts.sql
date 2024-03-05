create schema movies;
create table movies.movie (
	id char(36),
	title varchar(50),
	duration smallint,
	released date
);
alter table movies.movie add constraint pk_movie primary key (id);

delete from movies.movie;
INSERT into movies.movie values ('77849cb0-f33b-4157-b664-de7dad3fa21a', 'PULP FICTION', 30, '1995-01-01');
INSERT into movies.movie values ('77849cb0-f33b-4157-b664-de7dad3fa21b', 'INTERESTELAR', 90, '2000-01-01');
INSERT into movies.movie values ('77849cb0-f33b-4157-b664-de7dad3fa21d', 'PERROS DE RESERVA', 60, '2001-01-01');
INSERT into movies.movie values ('77849cb0-f33b-4157-b664-de7dad3fa21e', 'KILL BILL VOL. 1', 30, '2002-01-01');
INSERT into movies.movie values ('77849cb0-f33b-4157-b664-de7dad3fa21f', 'KILL BILL VOL. 2', 60, '2023-01-01');