# Tableau Visualizations
Various Visualizations on Tableau. Links to my public Tableau Profile, as well as to any data processing/cleaning done on programs other than Tableau should be found here.

## 1) Exploration of SG Bus Fare Structures

- [Tableau Visualization Link](https://public.tableau.com/profile/suyash2542#!/vizhome/ExplorationofSGBusFares/ExplorationofSGBusFares)
- [Jupyter Notebook link](https://github.com/SphericalSilver/Tableau-Visualizations/blob/master/SG%20Bus%20Exploration.ipynb),  where some Data cleaning and processing was done. 

Data was acquired from the datasets found here: [Trunk Bus Data](https://data.gov.sg/dataset/fare-structure-for-trunk-bus-services), and [Express Bus Data](https://data.gov.sg/dataset/fare-for-express-bus-services)

The data was then processed and cleaned through Python, then visualized on Tableau.

### The Visualization

In particular, we looked at how Bus Fares varied for 5 different kinds of passengers:
1. Regular Adult Fares
2. Student Fares
3. Senior Citizen Fares
4. [People with Disabilities](https://www.transitlink.com.sg/PSdetail.aspx?ty=art&Id=96)
5. [Holders of Workfare Transport Concession Card](https://www.transitlink.com.sg/PSdetail.aspx?ty=art&Id=95), broadly refered to as 'Workers' in the project.

The two Bus Types we looked at were [Express Buses](https://landtransportguru.net/express-bus-services/) and [Trunk Buses](https://www.mytransport.sg/content/mytransport/home/commuting/busservices.html#Trunk_Buses).

Trunk buses navigate through an extensive network of routes, often passing through several different towns and estates. Express Bus Services are bus services that contain express sectors, by skipping bus stops or travelling by expressways, saving commuting time as compared to regular trunk services. These bus services charge Express fares.

Fares for Feeder Bus services can be found [here](https://data.gov.sg/dataset/fare-for-feeder-bus-services). Since the fares for these are completely uniform and independent of distance travelled, they were not included in the visualization.

Click the [Tableau Visualization Link](https://public.tableau.com/profile/suyash2542#!/vizhome/ExplorationofSGBusFares/ExplorationofSGBusFares) to see the Dashboard.


## 3) Customer Segmentation of Bank Customers.

The dataset used can be downloaded [here](https://sds-platform-private.s3-us-east-2.amazonaws.com/uploads/P1-UK-Bank-Customers.csv)

Data from a bank was used to analyze the demographics of its customers to find out more about how they varied in each of the 4 regions.

Some notable insights were that:

- Customers in Scotland are generally Male, above 40 years old, and predominantly Blue Collar workers. 
- Customers form England have a high proportion of white collar workers, and the age distribution leans more towards people in their 20's or 30's.
- Since Scotland and England have both the biggest customer-bases by a margin, but they are very different demographiaclly, it would make sense to adjust marketing and advertising tactics to suit each of those customer-bases differently.
    - For instance, customers in Scotland could be encouraged to save to plan ahead for retirement, and to take care of their families.
    - Customers in England could be motivated to save money for further education, and given further incentives like possibilities for loans to buy property with (since a lot of them are young people liekly just entering the workforce).

Click the [Tableau Visualization Link](https://public.tableau.com/profile/suyash2542#!/vizhome/CustomerSegmentationDashboardStory/Story1) to see the Dashboard.
