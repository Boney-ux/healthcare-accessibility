🗺️ Health Facility Accessibility in Nairobi

This project explores the distribution of health facilities across Nairobi constituencies and their accessibility based on population per facility.

📖 Project Overview

The goal of this analysis was to learn and apply geospatial data science techniques to a real-world inspired problem:
👉 Are health facilities evenly distributed relative to the population in Nairobi?

Using OpenStreetMap (OSM) data for health facilities and population raster data, we created a heatmap showing the ratio of people per facility by constituency.

This is for learning purposes only — not official planning data — but demonstrates how GIS tools can provide insights into healthcare accessibility.

🛠️ Tools & Libraries

GeoPandas
 → Vector data manipulation & spatial joins

Rasterio
 → Population raster extraction

Matplotlib
 → Visualization & heatmaps

OSMnx
 → Downloading health facility data from OSM

📊 Workflow Summary

Data Collection

Health facilities → from OpenStreetMap

Population data → raster covering Kenya

Preprocessing

Clipped population raster to Nairobi County

Cleaned & projected datasets into EPSG:3857

Analysis

Aggregated population counts per constituency

Counted health facilities within each constituency

Calculated population per facility ratio

Visualization

Created a choropleth heatmap of Nairobi constituencies

Overlayed health facilities for spatial context

📷 Results
People per Facility (by Constituency)

🚀 Next Steps

Explore travel-time accessibility using network analysis (e.g., OSMnx + NetworkX)

Compare with actual census health data for validation

Extend analysis to Kenya’s counties for a broader view

📌 Disclaimer

This project is for educational purposes only. Data is sourced from OSM and open population datasets, and results should not be used for official decision-making.
