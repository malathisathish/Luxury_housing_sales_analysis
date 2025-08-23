
# 🏠 Luxury Housing Sales Analysis – Market Intelligence Dashboard (Bengaluru)

## 📌 Project Overview
The **Luxury Housing Sales Analysis Project** focuses on analyzing Bengaluru's luxury housing market by studying sales, demand, buyer preferences, builder performance, and booking efficiency.  
This project leverages **Python (data cleaning & preprocessing)**, **SQL (data warehousing)**, and **Power BI (visualization & dashboarding)** to generate actionable insights for real-estate developers, investors, and buyers.

---

## 🏷️ Problem Statement
The luxury housing market faces challenges such as:
- Lack of consolidated insights on **market demand & sales patterns**.  
- Difficulty in measuring the impact of **amenities and configurations** on booking conversions.  
- Unclear understanding of **buyer types and possession preferences**.  
- Fragmented data, making it hard to analyze **geographical trends and builder performance**.  

---

## 🎯 Project Objectives
- Analyze **luxury housing demand trends** across micro-markets.  
- Evaluate **builder performance** (revenue, ticket size, efficiency).  
- Study the **impact of amenities and configurations** on booking conversions.  
- Understand **buyer preferences** for possession status (Ready-to-Move vs Under-Construction).  
- Develop an **interactive Power BI dashboard** for decision-making.  

---

## 📂 Dataset
- The dataset contains **100,000+ housing sales records** including attributes like:  
  - Project ID, Micro-Market, Developer, Ticket Price, Unit Size, Amenity Score, Booking Flag, Buyer Type, Possession Status, Sales Channel, etc.  

🔗 **Uncleaned CSV File Download** – [Click Here](./data/uncleaned_luxury_housing.csv) (ensure dataset is placed in the `data/` folder).  

---

## 🧹 Data Cleaning & Preprocessing
1. Removed duplicates and missing values.  
2. Standardized data types (e.g., dates, numerical fields).  
3. Created calculated metrics:  
   - **Price per Sqft**  
   - **Amenity Score Range**  
   - **Booking Conversion Rate**  
4. Normalized categorical fields for SQL warehousing.  

---

## 🗄️ SQL Warehousing & Schema
- A **SQL data warehouse** was designed to store cleaned housing data.  
- Schema includes:  
  - **Fact_Sales** (sales transactions)  
  - **Dim_Projects** (project details)  
  - **Dim_Developers** (builder information)  
  - **Dim_Buyers** (buyer segmentation)  
  - **Dim_Locations** (micro-market details)  

---

## 📊 Power BI Usage
- Imported **cleaned dataset** into Power BI.  
- Built interactive dashboard with filters for:  
  - Buyer Type  
  - Possession Status  
  - Micro-Market  
  - Sales Channel  
  - Amenity Score  

---

## 📈 Detailed Visualization Questions & Insights

### 📊 1. Market Trends (Line Chart)
**Bookings by Quarter & Micro-Market**  
- Whitefield leads in bookings (1200+ in Q3 2024).  
- Sarjapur Road shows steady growth.  
- Indiranagar peaks in Q4 2023 (seasonal launches).  
💡 *Whitefield & Sarjapur Road = most dynamic markets.*  

### 📊 2. Builder Performance (Bar Chart)
**Revenue vs Avg Ticket Size**  
- Total Environment leads in revenue.  
- Prestige = premium pricing (₹14.9 Cr avg).  
- Brigade = high volume, lower ticket size.  
💡 *Total Environment = volume, Prestige = premium.*  

### 📊 3. Amenity Impact (Scatter Plot)
**Amenity Score vs Booking Conversion**  
- Amenity >8.0 = 72–78% conversion.  
- Low amenities (<6.0) = <30% conversion.  
💡 *Invest in gyms, pools, and security.*  

### 📊 4. Booking Conversion (Stacked Column)
**Bookings by Micro-Market**  
- Whitefield = 72% booking rate.  
- Domlur = only 48% conversion.  
💡 *Whitefield strongest; Domlur needs improvement.*  

### 📊 5. Configuration Demand (Donut Chart)
**Most In-Demand Configurations**  
- 5BHK+ = 38% demand.  
- 3BHK = 32%.  
💡 *Buyers prefer larger homes.*  

### 📊 6. Sales Channel Efficiency (100% Stacked Column)
- NRI Desk = 72% conversion (best).  
- Broker = only 54% conversion.  
💡 *Scale up NRI Desk channel.*  

### 📊 7. Quarterly Builder Contribution (Matrix)
- Total Environment dominated Q2 2024 (₹68.2 Cr).  
- Puravankara surged in Q3 2024.  
- Brigade declined in Q4 2024.  
💡 *Total Environment consistent; Puravankara rising.*  

### 📊 8. Possession Status Analysis (Clustered Column)
- NRIs → 78% bookings in under-construction projects.  
- HNIs/CXOs → 72% bookings in ready-to-move.  
💡 *Tailor projects by buyer type.*  

### 📊 9. Geographical Insights (Map)
- Whitefield = 28% of luxury projects.  
- Sarjapur & Hebbal emerging hubs.  
💡 *Whitefield = epicenter of luxury housing.*  

### 📊 10. Top Performers (KPI Cards)
- Total Environment = revenue leader.  
- Prestige = premium leader.  
- Sobha = best conversion rate.  
💡 *Three different success models.*  

---

## ⚠️ Problems Identified
- Uneven performance across micro-markets.  
- Some builders relying on high volume, others struggling with positioning.  
- Low-amenity projects failing to convert.  
- Inefficient sales channels (brokers).  

## ✅ Solutions
- Developers must **prioritize Whitefield & Sarjapur launches**.  
- Invest in **high-quality amenities** to improve conversion.  
- Strengthen **NRI Desk & online channels**.  
- Builders should balance **premium vs volume strategies**.  

---

## 🛠️ Tech Stack
- **Python**: Data cleaning & preprocessing.  
- **SQL**: Data warehousing & schema creation.  
- **Power BI**: Visualization & dashboards.  
- **Excel/CSV**: Raw dataset management.  

---

## 📌 Dashboard Features
- 📊 Market demand trends.  
- 👷 Builder performance metrics.  
- 🏢 Possession status preferences by buyer type.  
- 🌍 Geographical insights.  
- 💰 Revenue & booking KPIs.  
- 🔍 Configurations & amenity impact.  

---

## 🚀 Future Enhancements
- Apply **machine learning** for booking probability prediction.  
- Add **geospatial heatmaps** of buyer demand.  
- Integrate **external datasets** (interest rates, demographics).  
- Deploy **real-time dashboards** using Power BI Service / Streamlit.  

---

## 🙌 Acknowledgement
This project is inspired by real-world real-estate challenges in Bengaluru's luxury market. Special thanks to mentors and peers for valuable guidance.  

---

## 📚 Conclusion
The Luxury Housing Sales Analysis project delivers **data-driven insights** into the Bengaluru luxury housing segment.  
It helps developers, investors, and marketers align strategies with **buyer demand, amenities, and market trends**.  

---

## 🙏 Thank You Note
Thank you for reviewing this project. Your feedback is welcome!  

---

## ✍️ Author Details
👩‍💻 **Author**: Malathi.y 
🎓 **Role**: Data Science Enthusiast  
📧 **Contact**: [your-email@example.com]  
📌 **GitHub**: [your-github-link]  

---

## 📸 Project Screenshots

### Page 1 – Market Trends, Builder Performance, Amenity Impact
![Dashboard Page 1](./assets/Screenshot1.png)

### Page 2 – Sales Channel, Geographical Insights, Top Performers
![Dashboard Page 2](./assets/Screenshot2.png)

### Page 3 – Insights Summary
![Dashboard Page 3](./assets/Screenshot3.png)
