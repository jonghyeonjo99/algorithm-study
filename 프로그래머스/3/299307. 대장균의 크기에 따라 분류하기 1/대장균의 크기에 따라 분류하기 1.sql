-- 코드를 작성해주세요
SELECT
    E.ID
    , (CASE
        WHEN E.SIZE_OF_COLONY <= 100
        THEN 'LOW'
        WHEN 100 < E.SIZE_OF_COLONY AND E.SIZE_OF_COLONY <= 1000
        THEN 'MEDIUM'
        WHEN 1000 < E.SIZE_OF_COLONY
        THEN 'HIGH'
    END) AS SIZE
FROM
    ECOLI_DATA AS E
ORDER BY
    E.ID ASC