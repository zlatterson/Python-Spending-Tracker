DROP TABLE transactions;
DROP TABLE users;
DROP TABLE items;
DROP TABLE merchants;
DROP TABLE tags;

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
-- ----------v
CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    times_used INT
);

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    cost INT,
    tag_id INT REFERENCES tags(id) ON DELETE CASCADE,
    merchant_id INT REFERENCES merchants(id) ON DELETE CASCADE
);
-- --------^

CREATE TABLE transactions(
    id SERIAL PRIMARY KEY,
    merchant_id SERIAL REFERENCES merchants(id) ON DELETE CASCADE,
    user_id SERIAL REFERENCES users(id) ON DELETE CASCADE,
    item_id SERIAL REFERENCES items(id) ON DELETE CASCADE,
    cost INT
    -- rating INT
    -- time DATE
);


