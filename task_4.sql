SELECT 
    COLUMN_NAME, 
    COLUMN_TYPE, 
    IS_NULLABLE, 
    COLUMN_DEFAULT, 
    COLUMN_KEY, 
    EXTRA 
FROM 
    information_schema.COLUMNS 
WHERE 
    TABLE_NAME = 'Books' 
    AND TABLE_SCHEMA = 'alx_book_store';
