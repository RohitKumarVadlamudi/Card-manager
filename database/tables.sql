-- Create card table
CREATE TABLE IF NOT EXISTS card (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    max_limit INT NOT NULL,
    used DECIMAL(10,2) NOT NULL,
    available DECIMAL(10,2) NOT NULL,
    due_date DATE NOT NULL,
    minimum_payment DECIMAL(10, 2) NOT NULL,
    paid BOOLEAN DEFAULT FALSE
);
