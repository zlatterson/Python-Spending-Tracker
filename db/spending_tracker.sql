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

-- CREATE TABLE tags (
--     id SERIAL PRIMARY KEY
--     tag_name VARCHAR(255)
-- );

CREATE TABLE transactions(
    id SERIAL PRIMARY KEY,
    merchant_id SERIAL REFERENCES merchants(id) ON DELETE CASCADE,
    item_id SERIAL REFERENCES items(id) ON DELETE CASCADE,
    user_id SERIAL REFERENCES users(id) ON DELETE CASCADE,
    cost INT
    -- rating INT
    -- time DATE
);


