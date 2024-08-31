-- 코드를 작성해주세요
SELECT
    E.ID
    , E.GENOTYPE
    , E2.GENOTYPE AS PARENT_GENOTYPE
FROM
    ECOLI_DATA AS E
    LEFT JOIN ECOLI_DATA AS E2
    ON E.PARENT_ID = E2.ID
WHERE
    E.PARENT_ID IN (SELECT
                        PARENT_ID
                    FROM
                        ECOLI_DATA
                    WHERE
                        PARENT_ID IS NOT NULL
                   ) AND
# 부모의 형질을 모두 가져야하기 때문에 비트연산했을 때 부모의 형질과 값이 동일해야합니다.
# 해당 특성을 활용하여 코드 작성하였습니다.
    (E2.GENOTYPE & E.GENOTYPE) = E2.GENOTYPE
ORDER BY
    E.ID ASC