WITH raw_messages AS (
    SELECT
        channel,
        date::TIMESTAMP AS message_date,
        message,
        views::INT
    FROM {{ source('telegram', 'raw_messages') }}
    WHERE message IS NOT NULL
)

SELECT 
    channel,
    message_date,
    message,
    views,
    EXTRACT(HOUR FROM message_date) AS message_hour
FROM raw_messages
