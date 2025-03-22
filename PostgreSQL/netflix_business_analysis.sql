-------- 1. CHURN ANALYSIS --------
---- 1.1 Churn rate percentage.
-- Calculates the churn rate as a percentage of total subscribers.
WITH
	CTE AS (
		SELECT COUNT(*) AS TOTAL_SUBSCRIBERS
		FROM CONSUMER_DATA
	),
	CTE2 AS (
		SELECT COUNT(*) AS CHURNS
		FROM CONSUMER_DATA
		WHERE SUBSCRIPTION_END_DATE IS NOT NULL
	)
SELECT
	'Churn Rate' AS label, ROUND((CHURNS * 1.0 / TOTAL_SUBSCRIBERS) * 100, 2) AS CHURN_RATE,
FROM CTE, CTE2;

SELECT 'Churn Rate' AS lable, 1.8 AS CHURN_RATE
UNION
SELECT 'Subscriber Retention Rate', 100-1.8;

---- 1.2 Churn activity in general.
-- Counts the number of churns per year and month.
SELECT
	EXTRACT(YEAR FROM SUBSCRIPTION_END_DATE) AS YEAR,
	EXTRACT(MONTH FROM SUBSCRIPTION_END_DATE) AS MONTH,
	COUNT(*)
FROM CONSUMER_DATA
WHERE SUBSCRIPTION_END_DATE IS NOT NULL
GROUP BY YEAR, MONTH
ORDER BY YEAR, MONTH;

---- 1.3 Churn numbers per country.
-- Counts the number of churns per country.
SELECT
	COUNTRY,
	COUNT(*)
FROM CONSUMER_DATA CD
WHERE SUBSCRIPTION_END_DATE IS NOT NULL
GROUP BY COUNTRY
ORDER BY COUNT DESC, COUNTRY;

---- 1.4 Churn rates per gender.
-- Counts the number of churns per gender per year.
SELECT
	GENDER,
	EXTRACT(YEAR FROM SUBSCRIPTION_END_DATE) AS YEAR,
	COUNT(GENDER) AS CHURN_COUNT
FROM CONSUMER_DATA
WHERE SUBSCRIPTION_END_DATE IS NOT NULL
GROUP BY GENDER, YEAR
ORDER BY GENDER, YEAR;

---- 1.5 Mean churn rates per age range.
-- Categorizes users into generations and calculates churn rate per generation.
WITH CTE AS (
    SELECT
        CUSTOMER_ID,
        AGE,
        CASE
            WHEN AGE BETWEEN 10 AND 25 THEN 'Gen Z'
            WHEN AGE BETWEEN 26 AND 41 THEN 'Millennials'
            WHEN AGE BETWEEN 42 AND 57 THEN 'Gen X'
            WHEN AGE BETWEEN 58 AND 76 THEN 'Baby Boomers'
            ELSE 'Silent Generation'
        END AS GENERATION,
        CASE 
            WHEN SUBSCRIPTION_END_DATE IS NULL THEN 0 
            ELSE 1 
        END AS CHURNED
    FROM CONSUMER_DATA
)
SELECT 
    GENERATION,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) AS CHURN_RATE
FROM CTE
WHERE CHURNED = 1
GROUP BY GENERATION
ORDER BY 
CASE GENERATION
	WHEN 'Gen Z' THEN 1
	WHEN 'Millennials' THEN 2
	WHEN 'Gen X' THEN 3
	WHEN 'Baby Boomers' THEN 4
	WHEN 'Silent Generation' THEN 5
END
;

---- 1.6 Churn rates per country.
-- Counts churns per country per year.
SELECT
	COUNTRY,
	EXTRACT(YEAR FROM SUBSCRIPTION_END_DATE) AS YEAR,
	COUNT(COUNTRY) AS CHURN_COUNT
FROM CONSUMER_DATA
WHERE SUBSCRIPTION_END_DATE IS NOT NULL
GROUP BY YEAR, COUNTRY
ORDER BY YEAR, COUNTRY;

---- 1.7.1 Genres associated with the most amount of churns
-- Identifies the top 10 genres linked to churned users.
WITH
	CTE AS (
		SELECT
			VBD.CONTENT_ID,
			TITLE,
			LISTED_IN
		FROM
			VIEWING_BEHAVIOUR_DATA VBD
			JOIN NETFLIX_TITLES NT ON NT.SHOW_ID = VBD.CONTENT_ID
			JOIN CONSUMER_DATA CD ON CD.CUSTOMER_ID = VBD.CUSTOMER_ID
		WHERE SUBSCRIPTION_END_DATE IS NOT NULL
	)
SELECT
	BTRIM(UNNEST(STRING_TO_ARRAY(LISTED_IN, ','))) AS GENRE,
	COUNT(*)
FROM CTE
GROUP BY GENRE
ORDER BY COUNT(*) DESC
LIMIT 10;

---- 1.7.2 Genres associated with the lowest churn rates.
-- Identifies the bottom 10 genres linked to churned users.
WITH CTE AS (
	SELECT
		VBD.CONTENT_ID,
		TITLE,
		LISTED_IN
	FROM
		VIEWING_BEHAVIOUR_DATA VBD
		JOIN NETFLIX_TITLES NT ON NT.SHOW_ID = VBD.CONTENT_ID
		JOIN CONSUMER_DATA CD ON CD.CUSTOMER_ID = VBD.CUSTOMER_ID
	WHERE SUBSCRIPTION_END_DATE IS NOT NULL
),
CTE2 AS (
	SELECT
		BTRIM(UNNEST(STRING_TO_ARRAY(CTE.LISTED_IN, ','))) AS GENRE,
		COUNT(*) AS churned_watchers
	FROM CTE
	GROUP BY GENRE
),
CTE3 AS (
	SELECT 
		BTRIM(UNNEST(STRING_TO_ARRAY(LISTED_IN, ','))) AS GENRE, 
		COUNT(*) AS total_watchers
	FROM 
		VIEWING_BEHAVIOUR_DATA VBD
		JOIN NETFLIX_TITLES NT ON NT.SHOW_ID = VBD.CONTENT_ID
		JOIN CONSUMER_DATA CD ON CD.CUSTOMER_ID = VBD.CUSTOMER_ID
	GROUP BY GENRE
)
SELECT 
	CTE3.GENRE,
	CHURNED_WATCHERS,
	TOTAL_WATCHERS,
	ROUND(CHURNED_WATCHERS * 100.0/ TOTAL_WATCHERS, 4) AS churn_percent
FROM CTE2
JOIN CTE3 ON CTE2.GENRE = CTE3.GENRE
ORDER BY churn_percent ASC
LIMIT 10;

---- 1.8.1 & 1.8.2 Correlation with payment methods and churn ----
-- Counts churns per payment method and groups by year.
SELECT 
	PAYMENT_METHOD,
	COUNT(*)
FROM CONSUMER_DATA
WHERE SUBSCRIPTION_END_DATE IS NOT NULL
GROUP BY PAYMENT_METHOD;

SELECT
	PAYMENT_METHOD,
	EXTRACT(YEAR FROM SUBSCRIPTION_END_DATE) AS YEAR,
	COUNT(PAYMENT_METHOD) AS CHURN_COUNT
FROM CONSUMER_DATA
WHERE SUBSCRIPTION_END_DATE IS NOT NULL
GROUP BY YEAR, PAYMENT_METHOD
ORDER BY YEAR, PAYMENT_METHOD;

-------- 2. PRICING OPTIMISATION --------
---- 2.1.1 Average Revenue per User (ARPU) for each plan.
-- Calculates revenue gained per subscription plan.
WITH CTE AS (
	SELECT 
	    customer_id,
	    SUBSCRIPTION_START_DATE,
	    SUBSCRIPTION_END_DATE,
		AGE,
		-- Categorises customers into generational cohorts based on age.
		CASE
            WHEN AGE BETWEEN 10 AND 25 THEN 'Gen Z'
            WHEN AGE BETWEEN 26 AND 41 THEN 'Millennials'
            WHEN AGE BETWEEN 42 AND 57 THEN 'Gen X'
            WHEN AGE BETWEEN 58 AND 76 THEN 'Baby Boomers'
            ELSE 'Silent Generation'
        END AS GENERATION,
		COUNTRY,
		-- Calculates the total number of months a customer was subscribed.
		CASE
			WHEN SUBSCRIPTION_END_DATE IS NULL THEN EXTRACT(YEAR FROM AGE(CURRENT_DATE, SUBSCRIPTION_START_DATE)) * 12 + EXTRACT(MONTH FROM AGE(CURRENT_DATE, SUBSCRIPTION_START_DATE))
			ELSE EXTRACT(YEAR FROM AGE(SUBSCRIPTION_END_DATE, SUBSCRIPTION_START_DATE)) * 12 + EXTRACT(MONTH FROM AGE(SUBSCRIPTION_END_DATE, SUBSCRIPTION_START_DATE))
		END AS MONTH_DIFF,
		SUBSCRIPTION_PLAN,
		-- Assigns a fixed price for each subscription plan.
		CASE
	        WHEN subscription_plan = 'Standard (with adverts)' THEN 5.99
	        WHEN subscription_plan = 'Standard' THEN 12.99
	        WHEN subscription_plan = 'Premium' THEN 18.99
	        ELSE NULL
	    END AS pricing
	FROM consumer_data
	ORDER BY customer_id
)
-- Calculates the average revenue gained per subscription plan.
SELECT SUBSCRIPTION_PLAN, ROUND(AVG(MONTH_DIFF * PRICING), 2) AS REVENUE_GAINED
FROM CTE
GROUP BY SUBSCRIPTION_PLAN;

---- 2.1.2 Average Revenue per User (ARPU) for each generation.
-- Calculates the average revenue gained per generational group. 
WITH CTE AS (
	SELECT 
	    customer_id,
	    SUBSCRIPTION_START_DATE,
	    SUBSCRIPTION_END_DATE,
		AGE,
		-- Assigns a generation category based on age.
		CASE
            WHEN AGE BETWEEN 10 AND 25 THEN 'Gen Z'
            WHEN AGE BETWEEN 26 AND 41 THEN 'Millennials'
            WHEN AGE BETWEEN 42 AND 57 THEN 'Gen X'
            WHEN AGE BETWEEN 58 AND 76 THEN 'Baby Boomers'
            ELSE 'Silent Generation'
        END AS GENERATION,
		COUNTRY,
		-- Calculates the subscription duration in months.
		CASE
			WHEN SUBSCRIPTION_END_DATE IS NULL THEN EXTRACT(YEAR FROM AGE(CURRENT_DATE, SUBSCRIPTION_START_DATE)) * 12 + EXTRACT(MONTH FROM AGE(CURRENT_DATE, SUBSCRIPTION_START_DATE))
			ELSE EXTRACT(YEAR FROM AGE(SUBSCRIPTION_END_DATE, SUBSCRIPTION_START_DATE)) * 12 + EXTRACT(MONTH FROM AGE(SUBSCRIPTION_END_DATE, SUBSCRIPTION_START_DATE))
		END AS MONTH_DIFF,
		SUBSCRIPTION_PLAN,
		-- Assignes pricing for each subscription plan.
		CASE
	        WHEN SUBSCRIPTION_PLAN = 'Standard (with adverts)' THEN 5.99
	        WHEN SUBSCRIPTION_PLAN = 'Standard' THEN 12.99
	        WHEN SUBSCRIPTION_PLAN = 'Premium' THEN 18.99
	        ELSE NULL
	    END AS PRICING
	FROM CONSUMER_DATA
	ORDER BY CUSTOMER_ID
)
-- Aggregates and calculates the average revenue per generation.
SELECT GENERATION, ROUND(AVG(MONTH_DIFF * PRICING), 2) AS REVENUE_GAINED
FROM CTE
GROUP BY GENERATION
ORDER BY REVENUE_GAINED DESC;


---- 2.1.3 Average Revenue per User (ARPU) for each USAGE GROUP.
-- Categorises users into usage groups based on their viewing behavior and calculates ARPU.
WITH CTE AS (
	SELECT
		VBA.CUSTOMER_ID,
		COUNT(VBA.CUSTOMER_ID) AS VIEWING_COUNT,
		-- Assigns a percentile rank based on viewing count.
		PERCENT_RANK() OVER (ORDER BY COUNT(VBA.CUSTOMER_ID)) * 100 AS USAGE,
		SUBSCRIPTION_PLAN,
		-- Calculates the total months of subscription.
		CASE
			WHEN SUBSCRIPTION_END_DATE IS NULL THEN EXTRACT(YEAR FROM AGE(CURRENT_DATE, SUBSCRIPTION_START_DATE)) * 12 + EXTRACT(MONTH FROM AGE(CURRENT_DATE, SUBSCRIPTION_START_DATE))
			ELSE EXTRACT(YEAR FROM AGE(SUBSCRIPTION_END_DATE, SUBSCRIPTION_START_DATE)) * 12 + EXTRACT(MONTH FROM AGE(SUBSCRIPTION_END_DATE, SUBSCRIPTION_START_DATE))
		END AS MONTH_DIFF,
		-- Assigns pricing for each subscription plan.
		CASE
			WHEN SUBSCRIPTION_PLAN = 'Standard (with adverts)' THEN 5.99
			WHEN SUBSCRIPTION_PLAN = 'Standard' THEN 12.99
			WHEN SUBSCRIPTION_PLAN = 'Premium' THEN 18.99
			ELSE NULL
		END AS PRICING
	FROM VIEWING_BEHAVIOUR_DATA VBA
	JOIN CONSUMER_DATA CD ON VBA.CUSTOMER_ID = CD.CUSTOMER_ID
	GROUP BY VBA.CUSTOMER_ID, SUBSCRIPTION_PLAN, SUBSCRIPTION_START_DATE, SUBSCRIPTION_END_DATE
	ORDER BY VBA.CUSTOMER_ID, USAGE
)
-- Categorises users into Low, Medium, and High usage groups and calculating average revenue.
SELECT 
    CASE
        WHEN USAGE >= 0  AND USAGE < 33 THEN 'Low'
        WHEN USAGE >= 33 AND USAGE < 66 THEN 'Medium'
        WHEN USAGE >= 66 AND USAGE <= 100 THEN 'High'
    END AS USAGE_RATING,
	ROUND(AVG(MONTH_DIFF * PRICING), 2) AS REVENUE_GAINED
FROM CTE
GROUP BY USAGE_RATING
ORDER BY REVENUE_GAINED DESC;

---- 2.2.1 Yearly revenue breakdown
-- Calculate yearly revenue from Netflix subscriptions
WITH revenue_data AS (
    SELECT
        EXTRACT(YEAR FROM generate_series) AS year,
        customer_id,
        subscription_plan,
        -- Assign the correct price based on subscription plan
        CASE 
            WHEN subscription_plan = 'Standard (with adverts)' THEN 8.99
            WHEN subscription_plan = 'Standard' THEN 12.99
            WHEN subscription_plan = 'Premium' THEN 18.99
            ELSE 0
        END AS monthly_price
    FROM consumer_data,
    -- Generate a series of months from subscription start to end (or current date if active)
    LATERAL generate_series(
        subscription_start_date, 
        COALESCE(subscription_end_date, CURRENT_DATE), 
        INTERVAL '1 month'
    )
)
SELECT
    year,
    ROUND(SUM(monthly_price), 2) AS total_revenue
FROM revenue_data
WHERE YEAR <> 2025
GROUP BY year
ORDER BY year;

---- 2.2.2 Monthly revenue breakdown
-- Calculate monthly revenue from Netflix subscriptions
WITH revenue_data AS (
    SELECT
        EXTRACT(YEAR FROM generate_series) AS year,
        EXTRACT(MONTH FROM generate_series) AS month,
        customer_id,
        subscription_plan,
        -- Assign the correct price based on subscription plan
        CASE 
            WHEN subscription_plan = 'Standard (with adverts)' THEN 8.99
            WHEN subscription_plan = 'Standard' THEN 12.99
            WHEN subscription_plan = 'Premium' THEN 18.99
            ELSE 0
        END AS monthly_price
    FROM consumer_data,
    -- Generate a series of months from subscription start to end (or current date if active)
    LATERAL generate_series(
        subscription_start_date, 
        COALESCE(subscription_end_date, CURRENT_DATE), 
        INTERVAL '1 month'
    )
)
SELECT
    year,
    month,
    ROUND(SUM(monthly_price), 2) AS total_revenue
FROM revenue_data
GROUP BY year, month
ORDER BY year, month;

-------- 3. ENGAGEMENT ANALYSIS ---------
---- 3.1 Most popular genre (measured by average ratings per genre).
-- Identifies the most popular genres based on average ratings.
SELECT 
	BTRIM(UNNEST(STRING_TO_ARRAY(LISTED_IN, ','))) AS GENRE,
	ROUND(AVG(SHOW_RATING), 5) * 100 AS GENRE_RATING,
	COUNT(SHOW_RATING)
FROM VIEWING_BEHAVIOUR_DATA VBA
JOIN NETFLIX_TITLES NT ON VBA.CONTENT_ID = NT.SHOW_ID
GROUP BY GENRE
ORDER BY GENRE_RATING DESC, COUNT DESC;

---- 3.2 Identify popular regional content.
-- Identifies the most popular genre in each country.
WITH CTE AS (
    SELECT
        BTRIM(UNNEST(STRING_TO_ARRAY(COUNTRY, ','))) AS COUNTRY,
        BTRIM(UNNEST(STRING_TO_ARRAY(LISTED_IN, ','))) AS GENRE,
        COUNT(*) AS COUNT
    FROM VIEWING_BEHAVIOUR_DATA VBA
    JOIN NETFLIX_TITLES NT ON VBA.CONTENT_ID = NT.SHOW_ID
    WHERE COUNTRY IS NOT NULL	
    GROUP BY COUNTRY, GENRE
),
CTE2 AS (
SELECT 
    COUNTRY,
    GENRE,
	-- To account for repeats in genres.
    SUM(COUNT) AS TOTAL_COUNT
FROM CTE
WHERE COUNTRY <> ''
GROUP BY COUNTRY, GENRE
ORDER BY COUNTRY, TOTAL_COUNT DESC
),
CTE3 AS (
	SELECT
	    COUNTRY,
	    GENRE,
	    TOTAL_COUNT,
	    DENSE_RANK() OVER (PARTITION BY COUNTRY ORDER BY TOTAL_COUNT DESC) AS ROW_NUM
	FROM CTE2
)
SELECT 
	COUNTRY,
	GENRE,
	TOTAL_COUNT
FROM CTE3
WHERE ROW_NUM = 1;

---- 3.3 Identify genre fluctuations for a given year.
-- Generate all distinct genres.
WITH DistinctGenres AS (
    SELECT DISTINCT BTRIM(UNNEST(STRING_TO_ARRAY(LISTED_IN, ','))) AS GENRE
    FROM NETFLIX_TITLES
),
-- Generate all possible year-month combinations.
YearMonthCombinations AS (
    SELECT 
        EXTRACT(YEAR FROM WATCH_DATE) AS YEAR,
        EXTRACT(MONTH FROM WATCH_DATE) AS MONTH
    FROM VIEWING_BEHAVIOUR_DATA
    GROUP BY YEAR, MONTH
),
-- Cross join genres and year-month combinations to get all possible combinations.
AllCombinations AS (
    SELECT 
        DG.GENRE,
        YMC.YEAR,
        YMC.MONTH
    FROM DistinctGenres DG
    CROSS JOIN YearMonthCombinations YMC
)
-- Left join the original query with AllCombinations to ensure all combinations are present.
SELECT 
    AC.GENRE,
    AC.YEAR,
    AC.MONTH,
    COALESCE(COUNT(VBA.CONTENT_ID), 0) AS COUNT
FROM AllCombinations AC
LEFT JOIN (
    SELECT 
        BTRIM(UNNEST(STRING_TO_ARRAY(LISTED_IN, ','))) AS GENRE,
        EXTRACT(YEAR FROM WATCH_DATE) AS YEAR,
        EXTRACT(MONTH FROM WATCH_DATE) AS MONTH,
        VBA.CONTENT_ID
    FROM VIEWING_BEHAVIOUR_DATA VBA
    JOIN NETFLIX_TITLES NT ON NT.SHOW_ID = VBA.CONTENT_ID
) VBA ON AC.GENRE = VBA.GENRE AND AC.YEAR = VBA.YEAR AND AC.MONTH = VBA.MONTH
GROUP BY AC.GENRE, AC.YEAR, AC.MONTH
ORDER BY AC.GENRE, AC.YEAR, AC.MONTH;

