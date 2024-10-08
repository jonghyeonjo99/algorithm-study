-- 코드를 입력하세요
SELECT
    UB.TITLE
    , UB.BOARD_ID
    , UR.REPLY_ID
    , UR.WRITER_ID
    , UR.CONTENTS
    , DATE_FORMAT(UR.CREATED_DATE, '%Y-%m-%d')
FROM
    USED_GOODS_BOARD AS UB
    JOIN USED_GOODS_REPLY AS UR
    ON UB.BOARD_ID = UR.BOARD_ID
WHERE
    UB.CREATED_DATE LIKE '2022-10%'
GROUP BY
    UB.BOARD_ID
ORDER BY
    UR.CREATED_DATE ASC
    , UB.TITLE ASC