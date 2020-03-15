/*
flask-sqlacodegen --flask --outfile models.py postgres://developer:test123@localhost/OrderBooking
*/

CREATE table users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(256) UNIQUE,
    password VARCHAR(256) NOT NULL,
    hint VARCHAR(25) NOT NULL,
    country_code CHAR(3) NOT NULL,
    status INTEGER DEFAULT 0 NOT NULL
);

CREATE TABLE orders(
    id              SERIAL PRIMARY KEY,
    order_date      timestamp default CURRENT_TIMESTAMP,
    delivery_date   date        not null,
    order_amount    decimal     not null,
    promo_code      varchar(12),
    discount_amount decimal     not null,
    tax_amount      decimal     not null,
    delivery_method integer     not null,
    delivery_amount decimal     not null,
    total_amount    decimal     not null,
    payment_method integer     not null,
    payment_status  INTEGER     not null,
    message         text
);

create table item_type(
    id serial primary key ,
    type varchar(25) not null
);

create table items (
    id               serial primary key,
    type_id          integer references item_type (id) not null,
    item_name        varchar(50)                       not null,
    item_description varchar(50)                       not null
);

create table order_detail (
    id       SERIAL PRIMARY KEY,
    order_id integer references orders (id) not null,
    box_id  integer not null,
    item_id  integer references items (id)  not null
);

create table uk_delivery_address(
    id            serial primary key,
    order_id       integer references orders (id) not null,
    mobile_number varchar(25)  not null,
    address1      varchar(256) not null,
    address2      varchar(256),
    city          varchar(25)  not null,
    town          varchar(25)  not null,
    post_code     char(8)      not null
);

create table cart
(
    id           serial primary key,
    created      timestamp default CURRENT_TIMESTAMP,
    session_id   varchar(256)         not null,
    base_id      int                 not null,
    base_name    varchar(50)         not null,
    protein_id   int                 not null,
    protein_name varchar(50)         not null,
    side1_id     int                 not null,
    side1_name   varchar(50)         not null,
    side2_id     int                 not null,
    side2_name   varchar(50)         not null,
    dessert_id   int                 not null,
    dessert_name varchar(50)         not null,
    quantity     int       default 1 not null
);

create table price
(
    id    serial primary key,
    type  varchar(25) not null,
    amount decimal         not null
);

insert into price (type,amount) VALUES ('Standard Meal',8.95);


insert into item_type (type) VALUES ('Base');
insert into item_type (type) VALUES ('Protein');
insert into item_type (type) VALUES ('Side');
insert into item_type (type) VALUES ('Dessert');

insert into items (item_name, item_description, type_id) VALUES ('Traditional Pulao Rice', 'lorem ipsum pipsum remlem emlem rim lorem ipsum pi', 1);
insert into items (item_name, item_description, type_id) VALUES ('Couscous', 'lorem ipsum pipsum remlem emlem rim lorem ipsum pi', 1);
insert into items (item_name, item_description, type_id) VALUES ('Quinoa', 'lorem ipsum pipsum remlem emlem rim lorem ipsum pi', 1);

insert into items (item_name, item_description, type_id) VALUES ('Chicken Malai', 'lorem ipsum pipsum remlem emlem rim lorem ipsum pi', 2);
insert into items (item_name, item_description, type_id) VALUES ('Chicken Bihari', 'lorem ipsum pipsum remlem emlem rim lorem ipsum pi',2);

insert into items (item_name, item_description, type_id) VALUES ('Channa Chaat', 'lorem ipsum pipsum remlem emlem rim lorem ipsum pi',3);
insert into items (item_name, item_description, type_id) VALUES ('Baked Sweet Potato', 'lorem ipsum pipsum remlem emlem rim lorem ipsum pi',3);

insert into items (item_name, item_description, type_id) VALUES ('Ladoo', 'lorem ipsum pipsum remlem emlem rim lorem ipsum pi',4);
insert into items (item_name, item_description, type_id) VALUES ('Cake Alaska', 'lorem ipsum pipsum remlem emlem rim lorem ipsum pi',4);



