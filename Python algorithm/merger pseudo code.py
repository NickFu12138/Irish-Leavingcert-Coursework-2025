START
    IMPORT csv library
    
    DEFINE list variables 'paths' containing  cleaned CSV files

    DEFINE empty list 'merged'
    SET 'merged_file' to "house_cost_overburden_.csv"
    SET 'header_written' to False

    FOR LOOP each file in 'paths':
        OPEN file in read mode
        CREATE a CSV reader
        READ the header row

        SET first column of header to an empty string

        IF header has not been written to 'merged' list:
            APPEND header to 'merged' list + SET 'header_written' to True

        FOR each remaining row in file:
            APPEND row to 'merged' list

    OPEN 'merged_file' in write mode with newline handling
    CREATE a CSV writer
    WRITE all rows from 'merged' list to 'merged_file'
END