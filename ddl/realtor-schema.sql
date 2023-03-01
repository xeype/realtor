CREATE SCHEMA realtor;

ALTER
SCHEMA realtor OWNER TO postgres;

CREATE TABLE public.employees
(
    id           INTEGER GENERATED ALWAYS AS IDENTITY,
    first_name   VARCHAR(255),
    second_name  VARCHAR(255),
    phone_number VARCHAR(255),
    address      TEXT,
    PRIMARY KEY (id)
);

CREATE TABLE public.customers
(
    id           INTEGER GENERATED ALWAYS AS IDENTITY,
    first_name   VARCHAR(255),
    second_name  VARCHAR(255),
    phone_number VARCHAR(255),
    address      TEXT,
    PRIMARY KEY (id)
);

CREATE TABLE public.prices
(
    id    INTEGER GENERATED ALWAYS AS IDENTITY,
    price DOUBLE PRECISION,
    PRIMARY KEY (id)
);

CREATE TABLE public.services
(
    id           INTEGER GENERATED ALWAYS AS IDENTITY,
    service_name VARCHAR(255),
    price_id     INTEGER,
    PRIMARY KEY (id),
    CONSTRAINT fk_price_id
        FOREIGN KEY (price_id)
            REFERENCES prices (id)
);

CREATE TABLE public.apartments
(
    id           INTEGER GENERATED ALWAYS AS IDENTITY,
    num_of_rooms SMALLINT,
    address      VARCHAR(255),
    manager_id   INTEGER,
    price_id     INTEGER,
    PRIMARY KEY (id),
    CONSTRAINT fk_manager_id
        FOREIGN KEY (manager_id)
            REFERENCES employees (id),
    CONSTRAINT fk_price_id
        FOREIGN KEY (price_id)
            REFERENCES prices (id)
);

CREATE TABLE public.agreements
(
    id           INTEGER GENERATED ALWAYS AS IDENTITY,
    customer_id  INTEGER,
    apartment_id INTEGER,
    employee_id  INTEGER,
    PRIMARY KEY (id),
    CONSTRAINT fk_customer_id
        FOREIGN KEY (customer_id)
            REFERENCES customers (id),
    CONSTRAINT fk_apartment_id
        FOREIGN KEY (apartment_id)
            REFERENCES apartments (id),
    CONSTRAINT fk_employee_id
        FOREIGN KEY (employee_id)
            REFERENCES employees (id)
);