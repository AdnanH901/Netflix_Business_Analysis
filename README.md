# Project background
Netflix (founded in 1997) is a global leader in the streaming and entertainment market. It offers a variety of TV shows, movies, documentaries and original content. They have over **over 300 million subscribers** worldwide (as of 2024).

The company has a significant amount of data on its content offerings, operational efficiency and customer retention rates that have been previously underutilised. This project thoroughly analyses and synthesises this data to uncover critical insights that will improve Netflix's customer acquisition and retention.

Insights and recommendations are provided on the following key areas:

- **Churn Analysis:** An evaluation of general churn rate activity and churn rates across various sectors.
- **Revenue Evaluation:** An investigation of Netflix's global revenue and scrutinisation of their pricing tiers to see if they can be optimised.
- **Engagement Insights:** An analysis of the most popular genres by country.

Targeted SQL queries regarding various business questions are found here [link].

The Tableau dashboards for reporting and exploring customer churn, acquisition trends and pricing optimisation can be found here [link].

# Data Structure & Initial Checks

Netflix's main database structure as seen below consists of three tables:
netflix_titles, consumer_data and viewing_behaviour_data with a total row count of **1,200,000**. A description of each table is as follows:
- **netflix_titles:** A catalogue of over **8,800** titles ranging from movies, shows, documentaries etc.
- **consumer_data:** A table filled with data comprising of **100,000** subscribers.
- **viewing_behaviour_data:** A table comprisng of **1,000,000** viewings from the 100,000 subscribers in consumer_data from titles in netflix_titles.


![image](https://github.com/user-attachments/assets/fe87f594-3521-4587-8129-61f8b71948b7)

# Executive Summary
### Overview of Findings
Netflix is experiencing consistent revenue growth over the years initally starting with £130,000 in revenue to £13,000,000 in revenue. This indicates that they have optimal pricing stratergies and marketing efforts. The most popular genres globally that boost customer acquisition are international movies (green) and dramas (blue). The most reliabale content that leads to the lowest churn rates are predominatley TV shows and shows with a lot of replayability to them. 

![image](https://github.com/user-attachments/assets/824b0129-336a-4efc-8d4a-82fa970cc4e2)

# Insights Deep Dive
### Churn Analysis:
  
* **Churn Globally:** Netflix, out of a sample of 1,000,000, has been able to keep the number of unsubscribers small:
  * Over its early years, Netflix has had a very small increase in churn numbers. This suggests that they have done quite well in their startup years.
  
* **Churn & Genre:** TEXT

* **Churn Overall:** TEXT

![image](https://github.com/user-attachments/assets/59f4df20-91b9-4b92-adc3-9ddbaead6772)


### Revenue Evaluation:

* **Steady Gains:** There is a very steady, linear increase in revenue for Netflix over the past couple of decades. This shows Netflix's stability and growth in the streaming industry and show's how it's model is quite reliable.  
  
* **Subscription:** It seems that the Premium option generates the highest average revenue per subscriber. This could be because:
  * Netflix's Premium option offers much more than its other options whilst costing substantially more which indicates that the Premium option is doing quite well overall and is well optimised.
  * The Premium plan allows up to four simultaneous streams, making it an attractive option for families, housemates, or friends who want to split the cost.
  * While Netflix has cracked down on password sharing, this plan still enables multiple users within the same household to watch at once. Which explains the overall high average gains, high relative adoption ratings and thus long term subscriptions.
  
* **Pricing Tiers:** Multiple A/B testings have proven that Netflix's monthly pricing tiers are already well optimised.
  * Experiments introducing annual pricing models with discounted rates showed no significant reduction in churn while leading to a measurable decrease in average revenue per user (ARPU).
  * These findings suggest that annual pricing tiers are deceptive in value for Netflix. They do not improve on long-term retention and can negatively impact overall revenue.

![image](https://github.com/user-attachments/assets/516b80aa-d0e0-4e5d-8ad1-01b2f3df9dd1)

### Engagement Insights:

* **Genre Popularity Globally:** More detail about the supporting analysis about this insight, including time frames, quantitative values, and observations about trends.
  
* **Yearly Genre Popularity:** More detail about the supporting analysis about this insight, including time frames, quantitative values, and observations about trends.

![image](https://github.com/user-attachments/assets/ca851615-e1e3-4363-8f75-90afff28e2c1)
