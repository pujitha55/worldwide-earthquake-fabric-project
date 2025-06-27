#  Earthquake Insights with Microsoft Fabric

This project analyzes global earthquake data using Microsoft Fabric's Lakehouse architecture. It demonstrates a complete data engineering workflow: ingesting real-time GeoJSON from the USGS, transforming it using PySpark, and visualizing results through Power BI.

---

## Project Objective

To build a modern, scalable, and automated data pipeline that enables real-time monitoring and analysis of global earthquakes using Microsoft Fabric and the Medallion architecture.

---

##  Business Logic / Use Case

Governments, researchers, and disaster response teams need fast, reliable earthquake data to respond to seismic events.  
This project helps:

- Monitor global seismic activity in real time  
- Understand earthquake patterns by location, magnitude, and depth  
- Visualize trends and enable quick decision-making for emergency preparedness

---

##  Medallion Architecture

This project uses the **Bronze-Silver-Gold** architecture for data refinement:

| Layer     | Purpose                                           | This Project Uses                                  |
|-----------|---------------------------------------------------|----------------------------------------------------|
| **Bronze**| Raw data ingestion                                | GeoJSON from USGS API stored in Lakehouse File     |
| **Silver**| Cleaned and flattened data                        | PySpark extracts and converts nested fields        |
| **Gold**  | Aggregated business-ready insights                | Summary data used for Power BI reporting           |

---

##  Tools & Technologies Used

- **Microsoft Fabric**
  - Lakehouse
  - Notebooks (PySpark)
  - Pipelines
  - Power BI
- **USGS GeoJSON Earthquake Feed**
- **Python / PySpark**
- **Medallion Architecture**

---

##  Features

- ✅ Ingests real-time data from USGS (7-day earthquake feed)
- ✅ Converts complex JSON into structured tables
- ✅ Converts timestamps from epoch to human-readable
- ✅ Outputs CSV/Delta for analytics
- ✅ Builds visuals like scatter plots, bar charts, and trendlines

---

##  Power BI Visuals

- Earthquake Locations (via Latitude/Longitude)
- Top Earthquake Countries
- Trend of Earthquakes Over Time
- Average Magnitude by Region

---

##  How to Use

1. Clone this repo  
2. (Optional) Run `src/fetch_latest_usgs.py` to pull latest GeoJSON  
3. Open `notebooks/` in Microsoft Fabric  
4. Use `Lakehouse` to store files and outputs  
5. Visualize using `Power BI` or export CSVs from the `Download` folder

---



- Lakehouse File view  
- Notebook with transformations  
- Flattened table  
- Final Power BI dashboard  

---

##  Folder Structure

earthquake-fabric/
├── notebooks/
│ └── 01_transform.ipynb
├── data/ (excluded)
├── src/
│ └── fetch_latest_usgs.py
├── reports/
│ └── Worldwide_Earthquake_Report.pbix
├── screenshots/
│ └── dashboard.png
├── .gitignore
└── README.md


---

##  Author

**Lakshmi Pujitha Gorantla**  
 Built as part of a Microsoft Fabric learning project  
 [LinkedIn Profile](www.linkedin.com/in/lakshmi-pujitha-gorantla)

---

## License

MIT License – feel free to reuse or adapt this project.



