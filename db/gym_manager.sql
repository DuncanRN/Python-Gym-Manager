DROP TABLE bookings;
DROP TABLE classes;
DROP TABLE members;

-- members
CREATE TABLE members (
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    id SERIAL PRIMARY KEY
)

-- classes
CREATE TABLE classes (
    name VARCHAR(255),
    id SERIAL PRIMARY KEY
)

-- bookings
CREATE TABLE bookings (
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    class_id INT REFERENCES classes(id) ON DELETE CASCADE,
    id SERIAL PRIMARY KEY
)

