-- Create card table
CREATE TABLE IF NOT EXISTS card (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    max_limit INT NOT NULL,
    used INT NOT NULL,
    available INT NOT NULL,
    due_date DATE NOT NULL,
    minimum_payment DECIMAL(10, 2) NOT NULL,
    paid BOOLEAN DEFAULT FALSE
);
