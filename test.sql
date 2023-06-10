create table A (a int,b int,c int,primary key (a));
create table B (a int,d int,e int,primary key (a));
insert into A (a, b, c) values (1, 2, 3);
insert into A ( a, b) values (2, 2);
insert into A (a, c, b) values (4, 6, 5);
insert into B (a, d) values (1, 3);
insert into B (a, e, d) values (3, 4, 4);
insert into B (a, e) values (2, 7);
select * from B where a > 2;
select * from A join B where a != 2;
select * from A join B;
select a, b, c from A join B where a != 1;
select * from A left outer join B;
select * from A right outer join B;


