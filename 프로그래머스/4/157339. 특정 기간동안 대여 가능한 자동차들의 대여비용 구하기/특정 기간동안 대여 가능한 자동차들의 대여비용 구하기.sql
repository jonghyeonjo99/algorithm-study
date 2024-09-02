SELECT 
    C.CAR_ID, 
    C.CAR_TYPE, 
    FLOOR(C.DAILY_FEE * 30 * (1 - DP.DISCOUNT_RATE / 100)) AS FEE
FROM 
    CAR_RENTAL_COMPANY_CAR C
LEFT JOIN 
    CAR_RENTAL_COMPANY_RENTAL_HISTORY RH 
    ON C.CAR_ID = RH.CAR_ID 
    AND RH.START_DATE <= '2022-11-30' # 대여 시작일이 11월 30일 이전
    AND RH.END_DATE >= '2022-11-01'   # 대여 종료일이 11월 01일 이후   즉, 11월 중에 대여 중인 차량 확인 근데 AND???
JOIN 
    CAR_RENTAL_COMPANY_DISCOUNT_PLAN DP 
    ON C.CAR_TYPE = DP.CAR_TYPE 
    AND DP.DURATION_TYPE = '30일 이상'
WHERE 
    C.CAR_TYPE IN ('세단', 'SUV')
    AND RH.HISTORY_ID IS NULL  -- 2022년 11월 1일~30일 사이에 대여 이력이 없는 자동차만 선택
HAVING 
    FEE >= 500000 AND FEE < 2000000
ORDER BY 
    FEE DESC, 
    C.CAR_TYPE ASC, 
    C.CAR_ID DESC;