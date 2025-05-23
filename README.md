# Netflix Overview
Netflix (founded in 1997) is a global leader in the streaming and entertainment market. It offers a variety of TV shows, movies, documentaries and original content. As of 2024, they have over **over 300 million subscribers** worldwide.

The company has significant data on its content offerings, operational efficiency, and customer retention rates that have previously been underutilised. This project thoroughly analyses and synthesises this data to uncover critical insights that will improve Netflix's customer acquisition and retention.

Insights and recommendations are provided on the following key areas:

- **Churn Analysis:** An evaluation of general churn rate activity and churn rates across various sectors.
- **Revenue Evaluation:** An investigation of Netflix's global revenue and scrutiny of their pricing tiers to see if they can be optimised.
- **Engagement Insights:** An analysis of the most popular genres by country and why this is the case.

## Key Deliverables and Navigational Links

Targeted SQL queries regarding various business questions are found [here](https://github.com/AdnanH901/Netflix_Business_Analysis/blob/main/PostgreSQL/netflix_business_analysis.sql).

The Tableau dashboards for reporting and exploring customer churn, acquisition trends and pricing optimisation are found [here](https://github.com/AdnanH901/Netflix_Business_Analysis/tree/main/TableauDashboards).

A/B testing conducted during the [Revenue Evaluation & Pricing](#revenue-evaluation) segment are found [here](https://github.com/AdnanH901/Netflix_Business_Analysis/blob/main/Python/ABtesting.py)

To quickly view the overview of findings and recommendations, click on [Overview of Findings](#overview-of-findings) and [Recommendations](#recommendations).

# Data Structure & Initial Checks
## ERD Diagram of Data

![image](https://github.com/user-attachments/assets/5bf2a110-4939-4c3d-977e-54548e9c1013)


## Summary of Data
Netflix's main database structure, as seen below, consists of three tables:
netflix_titles, consumer_data and viewing_behaviour_data with a total row count of **1,200,000**. A description of each table is as follows:
- **netflix_titles:** A catalogue of over **8,800** titles ranging from movies, shows, documentaries etc.
- **consumer_data:** A table filled with data comprising of **100,000** subscribers.
- **viewing_behaviour_data:** A table comprisng of **1,000,000** viewings from the **100,000** subscribers in consumer_data from titles in netflix_titles.

# Executive Summary
### Overview of Findings

![image](https://github.com/user-attachments/assets/824b0129-336a-4efc-8d4a-82fa970cc4e2)

Netflix is experiencing consistent revenue growth over the years, initially starting with **£130,000** in revenue to **£13,000,000**. This indicates that they have optimal pricing strategies and marketing efforts. Globally, the most popular genres that boost customer acquisition are international movies (*green*) and dramas (*blue*). The most reliable content that leads to the lowest churn rates is predominantly TV shows and shows with a lot of replayability. 

# Insights Deep Dive
### Churn Analysis:
![image](https://github.com/user-attachments/assets/59f4df20-91b9-4b92-adc3-9ddbaead6772)

- **Churn Overall:** Out of **1,000,000** subscribers, Netflix has kept its unsubscribers relatively small, with churn numbers only elevating during 2016.
  - Over its early years, Netflix has had a tiny increase in churn numbers. This suggests that they have done quite well in their startup years being able to retain a loyal customer base. This indicates Netflix has strong customer satisfaction, effective content offerings and a competitive edge in the streaming market.
  - Netflix's elevated levels of churn from 2016 onwards can be explained through a myriad of factors,
    - **Market Saturation:** By 2016, Netflix had already captured a large share of potential subscribers, making it harder to sustain high growth while naturally increasing the likelihood of cancellations.
    - **Consumer Behavior Shifts:** Viewers increasingly engaged in "subscription cycling," cancelling and resubscribing based on content availability.
    - **Increased Competition:** Especially towards the ladder years, streaming competitors like *Disney +*, *HBO Max*, *Apple TV+*, and *Amazon Prime Video* gained traction, giving consumers more alternatives.
    - **Password Sharing Crackdown:** Stricter enforcement against account sharing may have led to cancellations from users who previously relied on shared accounts.
    - **Content Changes:** Netflix lost popular shows and movies as studios like Disney pulled their content to launch streaming services, leading to greater subscriber churn.

- **Churn per Generation:** The two generations with the highest churn rates are *Baby Boomers* and *Gen X*, born between 1946-1964 and 1965-1980 respectively. This suggests that Netflix has a huge gap in its customer retention strategy, particularly among older generations who may have different viewing habits, preferences and expectations. 
  
- **Churn & Genre:** The genres associated with the lowest churn rates are defined as those that consistently retain viewers and encourage long-term subscriptions. The genre with the lowest rates by far is *TV shows*, followed by genres such as *Science & Nature TV*, *Stand-Up Comedy & Talk Shows* and *TV Comedies*.
  - Along with the other genres with low churn rates, most of them share a common trait of having a lot of replayability. This implies that Netflix subscribers prefer titles with more replayability, thus giving them an incentive to stay subscribed after they have finished titles they would only watch once.
  - By having content that can be watched repeatedly or consumed over time (e.g., episodic content), these genres ensure that subscribers stay engaged, even during gaps between new releases.

- **Churn Globally:** The countries with the highest churn counts are the USA with 464 unsubscribed, Brazil with 97 unsubscribed, closely followed by the UK and India with 93 and 89 unsubscribed, respectively. The markets with the biggest overall churners are North America and Europe.

### Revenue Evaluation:
![image](https://github.com/user-attachments/assets/516b80aa-d0e0-4e5d-8ad1-01b2f3df9dd1)

- **Steady Gains:** There has been a very steady, linear increase in revenue for Netflix over the past couple of decades.
  - Netflix started their first year by generating **£130,000** and has gone up to **£13,000,000** in revenue in 2024. This shows Netflix's stability and growth in the streaming industry and shows how its model is quite reliable.
  
- **Subscription:** The Premium option generates the highest average revenue per subscriber. This could be because:
  - Netflix's Premium option offers much more than its other options, whilst costing substantially more, which indicates that the Premium option is doing quite well overall and is well optimised.
  - The Premium plan allows up to four simultaneous streams, making it an attractive option for families, housemates, or friends who want to split the cost.
  - While Netflix has cracked down on password sharing, this plan still enables multiple users within the same household to watch at once. This explains the overall high average gains, high relative adoption ratings and thus long-term subscriptions.
  
- **Pricing Tiers:** Multiple A/B testings have proven that Netflix's monthly pricing tiers are already well optimised.
  - Experiments introducing annual pricing models with discounted rates showed no significant reduction in churn while leading to a measurable decrease in average revenue per user (ARPU).
  - These findings suggest that annual pricing tiers are deceptive in value for Netflix. They do not improve long-term retention and can negatively impact overall revenue.
### Engagement Insights:
![image](https://github.com/user-attachments/assets/ca851615-e1e3-4363-8f75-90afff28e2c1)

- **Genre Popularity Globally:** More details about the supporting analysis of this insight, including time frames, quantitative values, and observations about trends.
  
- **Yearly Genre Popularity:** The most viewed genre categories per year are International Movies, Dramas, Comedies, International TV Shows, and Documentaries.
    - These genres all have high levels of replayability, which, as mentioned in [Churn Analysis](#churn-analysis), contribute significantly to their growing viewership. Audiences likely return to these genres for their emotional depth, humour, global perspective, and thought-provoking content.
    - All genres show increasing views per year, demonstrating that audiences are broadening their preferences and seeking diverse content.
      - This increase could be fueled by improved accessibility, cultural shifts, and the rise of streaming platforms making these genres more readily available.
      - This also suggests that people have more free time during the latter parts of the year and tend to become less productive as the months go by, meaning they are more likely to binge-watch a TV show or watch another movie.

# Recommendations:

Based on the insights and findings above, we would recommend the _Financial Planning and Analysis_ and _Strategy and Analysis_ teams to consider the following: 

- **Replayability is Netflix's Bedrock:** One-time big shows and movies bolster Netflix's customer acquisition. However, customers stay subscribed to Netflix because of the many classics, comedies, and other content that is highly replayable. Netflix should consider doing some further market analysis on what specific titles customers like and buying the rights to have them on their platform.
  
- **Competitor Analysis:** While Netflix’s pricing tiers are already well-optimised, we recommend conducting a competitive analysis of major rivals such as Amazon Prime Video and HBO Max. This could uncover opportunities to refine Netflix’s pricing strategy further. Therefore, Netflix can undercut its competitors and strengthen its market position.

  - **Appeal to Older Adults:** Netflix should procure some shows that are tailored towards the *Gen X* & *Baby Boomers* audience. Topics such as "*what genres do the older generation prefer*" and "*do they prefer other streaming platforms and if so, why*", among others, should be explored.

# Assumptions and Caveats:

Throughout the analysis, multiple assumptions were made to manage challenges with the data. These assumptions and caveats are noted below:

- **Assumption 1:** The amount paid for subscribers between countries does vary depending on multiple factors. But for ease of calculations, it is assumed that each country pays the same amount per pricing tier in GBP.
  
- **Assumption 2:** Netflix only has three and only three monthly pricing tiers that have not varied in price throughout the years. Those being:
  - Standard with Ads (£5.99)
  - Standard (£12.99)
  - Premium (£18.99)

- **Assumption 3:** The synthetically generated data (see Python file [*generating_tables.py*](https://github.com/AdnanH901/Netflix_Business_Analysis/blob/main/Python/generating_tables.py) code) using Python and AI is fully accurate and a perfect representation of Netflix's real-life customer data, subscription activity and pricing tiers. 
