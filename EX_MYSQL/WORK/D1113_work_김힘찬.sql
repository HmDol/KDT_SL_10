create database work_1113;

use work_1113;

create table tlb_work(
temp int,
is_rain int,
region varchar(10),
d_hour int,
food_kind varchar(20),
d_date datetime
);

insert into tlb_work 
values ('15', 1, '충청도', 15, '치킨', '2022-01-02'),
('25', 0, '경상남도', 13, '카페', '2025-01-03'),
('-2', 1, '서울특별시', 1, '족발', '2025-01-04'),
('-3', 0, '부산광역시', 23, '한식', '2025-01-05'),
('7', 1, '인천광역시', 8, '일식', '2025-01-06');


select * from tlb_work;