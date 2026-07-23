# Nassau Candy Distributor - Shipping Optimization & Reallocation System

## Project Overview
This project focuses on transforming Nassau Candy Distributor’s legacy shipping operations into a data-driven, intelligent decision-making engine. By utilizing geospatial analytics and predictive modeling, the system identifies the optimal factory for each order, minimizing shipping distances and reducing lead times.

## Problem Statement
The current logistics framework relied on static, rule-based processes, leading to:
- High average lead times (approx. 14 days).
- Inefficient shipping routes from distant facilities.
- Margin erosion due to logistics inefficiencies.

## Methodology
- **Data Cleaning:** Normalized shipment dates and calculated "True Lead Time".
- **Geospatial Analysis:** Implemented the **Haversine formula** to map customer cities to their nearest manufacturing facility using coordinates.
- **Recommendation Engine:** Developed a logic-based system to reallocate order fulfillment to the most cost-efficient/nearest factory.
- **Interactive Dashboard:** Built a live dashboard using **Streamlit** for real-time scenario simulation.

## Tech Stack
- **Languages:** Python
- **Data Analysis:** Pandas, NumPy
- **Algorithm:** Haversine (Geospatial distance mapping)
- **Deployment:** Streamlit Cloud
- **Tools:** VS Code, Git, GitHub

## How to Run
1. Clone this repository: `git clone https://github.com/your-username/Nassau-Candy-Optimization.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the dashboard: `streamlit run app.py`

## Screenshots
![Dashboard Screenshot](https://github.com/mohit8059/Nassau-Candy-Optimization/blob/main/Screenshot%202026-07-23%20121103.pngz
,)


## Results
- Successfully automated the "Nearest Factory" identification.
- Provided a scalable simulation tool for management to optimize supply chain performance.
