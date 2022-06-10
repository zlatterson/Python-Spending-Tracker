DROP TABLE transactions;
DROP TABLE users;
DROP TABLE items;
DROP TABLE merchants;

CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    money INT,
    daily_allowance INT
);


-- CREATE TABLE inventorys(
--     id SERIAL PRIMARY KEY,
--     merchant_id INT REFERENCES merchants(id),
--     item_id INT REFERENCES items(id)
-- );

CREATE TABLE merchants(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    money_received INT
);

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    tag VARCHAR(255),
    -- tag will allow us to search other tags
    cost INT,
    merchant_id INT REFERENCES merchants(id) ON DELETE CASCADE
);

CREATE TABLE transactions(
    id SERIAL PRIMARY KEY,
    merchant_id INT REFERENCES merchants(id) ON DELETE CASCADE,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    item_id INT REFERENCES items(id) ON DELETE CASCADE
    -- time DATETIME
);


INSERT INTO items (name,tag,cost) VALUES ('pizza','food',100);