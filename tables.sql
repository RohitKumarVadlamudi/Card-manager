-- Create card table
CREATE TABLE IF NOT EXISTS cards (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    max_limit int NOT NULL,
    used int NOT NULL,
    available int NOT NULL,
    due_date DATE NOT NULL,
    minimum_payment DECIMAL(10, 2) NOT NULL
);
