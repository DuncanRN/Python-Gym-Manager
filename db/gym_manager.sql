DROP TABLE bookings;
DROP TABLE gym_classes;
DROP TABLE members;

-- members
CREATE TABLE members (
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    id SERIAL PRIMARY KEY
);

-- classes renamed - gym_classes
CREATE TABLE gym_classes (
    name VARCHAR(255),
    date_start TIMESTAMP,
    repeating VARCHAR(255),
    end_date TIMESTAMP,
    capacity INT,
    id SERIAL PRIMARY KEY
);

-- bookings
CREATE TABLE bookings (
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    gym_class_id INT REFERENCES gym_classes(id) ON DELETE CASCADE,
    id SERIAL PRIMARY KEY
);
