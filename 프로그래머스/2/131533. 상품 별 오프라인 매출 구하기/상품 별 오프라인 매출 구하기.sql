-- 코드를 입력하세요
SELECT
    T1.PRODUCT_CODE
    , SUM(T2.SALES_AMOUNT) * T1.PRICE AS SALES
FROM
    PRODUCT AS T1
    JOIN OFFLINE_SALE AS T2
    ON T1.PRODUCT_ID = T2.PRODUCT_ID
GROUP BY
    T1.PRODUCT_ID
ORDER BY
    SALES DESC, T1.PRODUCT_CODE
