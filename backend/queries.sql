-- To run use: 
-- psql -U postgres -d csQuestions -f queries.sql

-- SELECT * FROM Question

-- Meant for inserting questions
-- INSERT INTO Question(question, difficulty)
-- VALUES('Tell me about a time you worked well within a team', 'Medium')

-- Rename ID to Question_ID
-- ALTER TABLE Question RENAME COLUMN ID TO Question_ID;

-- Add category column
-- ALTER TABLE Question ADD COLUMN category VARCHAR(255);

-- UPDATE Question SET category = 'Computer Science' WHERE category IS NULL;
-- ALTER TABLE Question ALTER COLUMN category SET NOT NULL;
