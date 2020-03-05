CREATE table users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(256) UNIQUE,
    password VARCHAR(256) NOT NULL,
    hint VARCHAR(25) NOT NULL,
    country_code CHAR(3) NOT NULL,
    status INTEGER DEFAULT 0 NOT NULL
)

create table uk_profile (
    id            serial primary key,
    user_id       integer references users (id) not null,
    first_name    varchar(256) not null,
    last_name     varchar(256) not null,
    mobile_number varchar(25)  not null,
    address1      varchar(256) not null,
    address2      varchar(256),
    city          varchar(25)  not null,
    town          varchar(25)  not null,
    post_code     char(8)      not null,
    lat             float       not null,
    long            float       not null
)

CREATE TABLE uk_orders(
    id              SERIAL PRIMARY KEY,
    order_date      timestamp default CURRENT_TIMESTAMP,
    delivery_date   date        not null,
    invoice_number  varchar(25) not null,
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
)

create table uk_item_type(
    id serial primary key ,
    type varchar(25) not null
)

create table uk_items
(
    id        serial primary key,
    item_name varchar(50) not null,
    type_id      integer    references uk_item_type(id) not null,
    amount    decimal     not null
)

create table uk_order_detail(
    id         SERIAL PRIMARY KEY,
    order_id   integer references uk_orders (id) not null,
    item_id  integer references uk_items(id)  not null,
    unit_price decimal     not null,
    quantity   integer     not null,
    amount     decimal     not null
)

create table uk_delivery_address(
    id            serial primary key,
    order_id       integer references uk_orders (id) not null,
    mobile_number varchar(25)  not null,
    address1      varchar(256) not null,
    address2      varchar(256),
    city          varchar(25)  not null,
    town          varchar(25)  not null,
    post_code     char(8)      not null,
    lat             float       not null,
    long            float       not null
)

/*
insert into uk_item_type (type) VALUES ('Base')
insert into uk_item_type (type) VALUES ('Protein')
insert into uk_item_type (type) VALUES ('Side')
insert into uk_item_type (type) VALUES ('Dessert')

insert into uk_items (item_name, type_id, amount) VALUES ('Traditional Pulao Rice', 1, 10.00)
insert into uk_items (item_name, type_id, amount) VALUES ('Couscous', 1, 10.00)
insert into uk_items (item_name, type_id, amount) VALUES ('Quinoa', 1, 10.00)

insert into uk_items (item_name, type_id, amount) VALUES ('Chicken Malai', 2, 10.00)
insert into uk_items (item_name, type_id, amount) VALUES ('Chicken Bihari', 2, 10.00)

insert into uk_items (item_name, type_id, amount) VALUES ('Channa Chaat', 3, 10.00)
insert into uk_items (item_name, type_id, amount) VALUES ('Baked Sweet Potato', 3, 10.00)

insert into uk_items (item_name, type_id, amount) VALUES ('Ladoo', 4, 10.00)
insert into uk_items (item_name, type_id, amount) VALUES ('Cake Alaska', 4, 10.00)
*/


