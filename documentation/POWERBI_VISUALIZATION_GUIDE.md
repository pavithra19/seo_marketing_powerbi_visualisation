# Power BI Visualization Guide for EVAGO Global Marketing Dashboard

## Overview
This guide will help you create the correct visuals with proper data from each CSV file in your Power BI dashboard. Each CSV file is designed for specific chart types and contains the appropriate data fields.

## 1. Global Traffic Overview (Line Chart)
**File:** `powerbi_chart1_global_traffic_overview.csv`

### Chart Type: Line Chart
### Fields to Use:
- **Axis (X):** `date` (Date field)
- **Values (Y):** `sessions` (or `users`, `pageviews`, `revenue`)
- **Legend:** `country` (for multiple lines by country)
- **Tooltip:** Include `sessions`, `users`, `pageviews`, `revenue`

### Steps:
1. Drag `date` to Axis
2. Drag `sessions` to Values
3. Drag `country` to Legend
4. Format: Add data labels, adjust colors per country

## 2. Geographic Performance Map (Map Chart)
**File:** `powerbi_chart2_geographic_performance_map.csv`

### Chart Type: Map (Filled Map)
### Fields to Use:
- **Location:** `country_code` (AUS, GBR, DEU, NLD, USA)
- **Values:** `revenue` or `conversions` or `ctr`
- **Tooltip:** Include `impressions`, `clicks`, `conversions`, `revenue`, `ctr`, `roas`

### Steps:
1. Drag `country_code` to Location
2. Drag `revenue` to Values
3. Format: Choose appropriate color scale (green to red)
4. Add tooltip with all relevant metrics

## 3. Campaign Performance Comparison (Bar Chart)
**File:** `powerbi_chart3_campaign_performance_comparison.csv`

### Chart Type: Clustered Bar Chart
### Fields to Use:
- **Axis (X):** `campaign_name`
- **Values (Y):** `clicks`, `conversions`, `revenue`
- **Legend:** `partner` (EVAGO vs Mojo)
- **Tooltip:** Include all performance metrics

### Steps:
1. Drag `campaign_name` to Axis
2. Drag `clicks` to Values
3. Drag `partner` to Legend
4. Add multiple measures: `conversions`, `revenue`

## 4. Conversion Funnel Analysis (Funnel Chart)
**File:** `powerbi_chart4_conversion_funnel_analysis.csv`

### Chart Type: Funnel Chart
### Fields to Use:
- **Category:** `funnel_stage` (Sessions → Page Views → Add to Cart → Purchase)
- **Values:** `count`
- **Breakdown:** `location_type` (Primary vs Expansion Markets)

### Steps:
1. Drag `funnel_stage` to Category
2. Drag `count` to Values
3. Drag `location_type` to Breakdown
4. Format: Adjust colors and add data labels

## 5. Device Performance Breakdown (Pie/Bar Chart)
**File:** `powerbi_chart5_device_performance_breakdown.csv`

### Chart Type: Pie Chart or Bar Chart
### Fields to Use:
- **Legend:** `device_category` (Desktop, Mobile, Tablet)
- **Values:** `sessions` or `revenue`
- **Tooltip:** Include `sessions`, `pageviews`, `revenue`, `bounce_rate`

### Steps:
1. Drag `device_category` to Legend
2. Drag `sessions` to Values
3. Format: Add data labels with percentages
4. Consider using Bar Chart for better comparison

## 6. SEO Keyword Rankings Trends (Line Chart)
**File:** `powerbi_chart6_seo_keyword_rankings_trends.csv`

- **Keywords are now market-appropriate and localized:**
  - German keywords for Germany
  - Dutch keywords for Netherlands
  - English keywords for England, North America, Australia
  - Croatian keywords for Croatia
  - Common event industry terms (e.g., "event infrastructure", "event equipment rental", "crowd management") are included for all markets
  - Brand/group keywords (e.g., Mojo, Terraplas, Entertee, No Fuss, Talos, EVAGO Group) are present in all markets
- **Only relevant keywords appear for each country in the chart.**

#### Recommended Visual Setup
- **X-axis:** `date`
- **Y-axis:** `ranking` (lower is better)
- **Legend:** `keyword` (limit to a few for clarity)
- **Small multiples:** `country` (see each country's trend in a grid)
- **Slicers:** Add slicers for `country`, `keyword`, and `keyword_type` for focused analysis.

### Steps:
1. Drag `date` to Axis
2. Drag `ranking` to Values
3. Drag `keyword` to Legend
4. Format: Invert Y-axis (so lower numbers appear higher)

## 7. Social Media Performance Comparison (Bar Chart)
**File:** `powerbi_chart7_social_media_performance_comparison.csv`

### Chart Type: Clustered Bar Chart
### Fields to Use:
- **Axis (X):** `platform` (Facebook, Instagram, LinkedIn, Twitter)
- **Values (Y):** `followers`, `engagement_rate`, `reach`
- **Legend:** `partner` (EVAGO vs Mojo)
- **Tooltip:** Include all social metrics

### Steps:
1. Drag `platform` to Axis
2. Drag `followers` to Values
3. Drag `partner` to Legend
4. Add multiple measures for comprehensive view

## 8. Competitor Analysis Dashboard (Bar Chart)
**File:** `powerbi_chart8_competitor_analysis_dashboard.csv`

### Chart Type: Bar Chart
### Fields to Use:
- **Axis (X):** `competitor_name`
- **Values (Y):** `market_share`, `brand_awareness`, `engagement_rate`
- **Tooltip:** Include all competitor metrics

### Steps:
1. Drag `competitor_name` to Axis
2. Drag `market_share` to Values
3. Format: Use consistent color scheme
4. Add data labels

## 9. Revenue Trends Analysis (Line Chart)
**File:** `powerbi_chart9_revenue_trends_analysis.csv`

### Chart Type: Line Chart
### Fields to Use:
- **Axis (X):** `date`
- **Values (Y):** `revenue`
- **Legend:** `traffic_source` (Organic vs Paid)
- **Tooltip:** Include `revenue`, `sessions`, `conversion_rate`

### Steps:
1. Drag `date` to Axis
2. Drag `revenue` to Values
3. Drag `traffic_source` to Legend
4. Format: Use different line styles for organic vs paid

## 10. Mojo Acquisition Impact Dashboard (Cards/Gauges)
**File:** `powerbi_chart10_mojo_acquisition_impact_dashboard.csv`

### Chart Type: Card Visuals and Gauges
### Fields to Use:
- **Cards:** `acquisition_impact_score`, `market_share_expansion`, `brand_awareness_growth`
- **Gauges:** `roas_improvement`, `ctr_improvement`
- **Tooltip:** Include all impact metrics

### Steps:
1. Create multiple Card visuals
2. Each card shows one key metric
3. Use Gauges for percentage improvements
4. Format with appropriate colors (green for positive)

## Updates for Country-Level Analysis and Device Metrics

- **Campaign Performance (Chart 3):** Now includes a `country` field. You can filter or break down campaign performance by country using slicers or the legend in Power BI.
- **Conversion Funnel (Chart 4):** Now includes a `country` field. Funnel analysis can be filtered or compared by country.
- **Device Performance (Chart 5):** Now includes a `country` field and uses realistic device splits (Mobile, Desktop, Tablet). Device metrics are no longer equal for all device types.

### How to Use Country Slicers
- Add a slicer for `country` to any of these charts to filter and compare by market.
- This enables more granular insights and better presentations for global stakeholders.

## General Tips for Better Visualizations:

### 1. Data Relationships
- Create relationships between tables using common fields like `date`, `country`, `partner`
- Use the Model view to set up proper relationships

### 2. Formatting Best Practices
- Use consistent color schemes across all charts
- Add meaningful titles and subtitles
- Include data labels where appropriate
- Use appropriate number formatting (%, $, etc.)

### 3. Interactivity
- Add slicers for `date`, `country`, `partner`
- Use cross-filtering between charts
- Add drill-down capabilities where relevant

### 4. Performance Optimization
- Use calculated columns sparingly
- Prefer measures over calculated columns
- Use appropriate data types (Date, Text, Number)

### 5. Mobile Responsiveness
- Test your dashboard on different screen sizes
- Use responsive layouts
- Ensure text is readable on mobile devices

## Common Issues and Solutions:

### Issue: Charts showing wrong data
**Solution:** Check field mappings and ensure you're using the correct CSV file for each chart type.

### Issue: Dates not displaying correctly
**Solution:** Ensure date fields are set to Date/DateTime data type in Power BI.

### Issue: Map not showing countries
**Solution:** Verify country codes are in ISO format (AUS, GBR, DEU, NLD, USA).

### Issue: Line charts showing as bars
**Solution:** Change chart type to Line Chart in the Visualizations pane.

### Issue: No data appearing
**Solution:** Check if filters are applied, refresh data, and verify field mappings.

## Next Steps:
1. Start with the Global Traffic Overview (Chart 1)
2. Add the Geographic Performance Map (Chart 2)
3. Continue with Campaign Performance (Chart 3)
4. Build the remaining charts following this guide
5. Add slicers and filters for interactivity
6. Test the dashboard with different data scenarios

This guide ensures you create the correct visuals with proper data from each CSV file, maximizing the insights from your EVAGO global marketing data. 