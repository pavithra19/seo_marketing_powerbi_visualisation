# EVAGO SEO/SEA Marketing Data Dashboard

This project generates comprehensive marketing data for EVAGO (event infrastructure rental company) to create 10 different Power BI dashboard charts.

## 🎯 Project Overview

EVAGO is a company that rents event infrastructure like barriers, fencing, and crowd control equipment. This project simulates realistic marketing data across multiple channels to build comprehensive Power BI dashboards.

## 📊 10 Power BI Charts

1. **Website Traffic Overview** - Line chart showing daily traffic trends
2. **Geographic Performance** - Map/Bar chart showing performance by country
3. **Campaign Performance** - Bar chart comparing different marketing campaigns
4. **Conversion Funnel** - Funnel chart showing conversion stages
5. **Device Performance** - Pie/Bar chart showing performance by device type
6. **SEO Keyword Rankings** - Line chart showing keyword performance over time
7. **Social Media Performance** - Bar chart comparing social platforms
8. **Competitor Analysis** - Bar chart showing competitor rankings
9. **Revenue Trends** - Line chart showing revenue growth over time
10. **KPI Dashboard** - Cards/Gauges showing key performance indicators

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Generate Marketing Data

```bash
python evago_marketing_data_simulator.py
```

This will create 10 CSV files with simulated marketing data:
- `evago_google_analytics_data.csv`
- `evago_google_ads_data.csv`
- `evago_seo_keywords_data.csv`
- `evago_social_media_data.csv`
- `evago_competitor_analysis_data.csv`
- `evago_conversion_funnel_data.csv`
- `evago_device_performance_data.csv`
- `evago_campaign_performance_data.csv`
- `evago_geographic_performance_data.csv`
- `evago_time_series_data.csv`

### 3. Prepare Data for Power BI

```bash
python powerbi_data_preparation.py
```

This will create 10 optimized CSV files specifically for Power BI:
- `powerbi_chart1_traffic_overview.csv`
- `powerbi_chart2_geographic_performance.csv`
- `powerbi_chart3_campaign_performance.csv`
- `powerbi_chart4_conversion_funnel.csv`
- `powerbi_chart5_device_performance.csv`
- `powerbi_chart6_seo_keywords.csv`
- `powerbi_chart7_social_media.csv`
- `powerbi_chart8_competitor_analysis.csv`
- `powerbi_chart9_revenue_trends.csv`
- `powerbi_chart10_kpi_dashboard.csv`

## 📈 Data Sources Simulated

### Google Analytics Data
- Sessions, users, pageviews
- Bounce rate and session duration
- Conversion rates and revenue
- Geographic breakdown

### Google Ads Data
- Campaign performance metrics
- Ad group performance
- CTR, CPC, conversion rates
- ROAS and budget utilization

### SEO Data
- Keyword rankings and search volume
- Organic traffic and impressions
- Click-through rates
- Position tracking

### Social Media Data
- Platform-specific metrics
- Reach, impressions, engagement
- Conversion tracking
- Cost per engagement

### Competitor Analysis
- Competitor keyword rankings
- Market share analysis
- Traffic estimation
- Performance comparison

## 🎨 Power BI Implementation Guide

### Step 1: Import Data
1. Open Power BI Desktop
2. Import each `powerbi_chart*.csv` file as separate data sources
3. Ensure date columns are properly formatted as dates

### Step 2: Create Relationships
Create relationships between datasets using common fields:
- Date fields for time-based analysis
- Country fields for geographic analysis
- Campaign fields for campaign analysis

### Step 3: Build Charts

#### Chart 1: Traffic Overview
- **Chart Type**: Line Chart
- **X-Axis**: Date
- **Y-Axis**: Sessions, Users, Pageviews
- **Add**: Moving averages for trend analysis

#### Chart 2: Geographic Performance
- **Chart Type**: Map or Bar Chart
- **X-Axis**: Country
- **Y-Axis**: Revenue, Conversions, ROAS
- **Use**: Country codes for map visualization

#### Chart 3: Campaign Performance
- **Chart Type**: Bar Chart
- **X-Axis**: Campaign
- **Y-Axis**: ROAS, Conversion Rate, Spend
- **Add**: Color coding by performance

#### Chart 4: Conversion Funnel
- **Chart Type**: Funnel Chart
- **Stages**: Website Visitors → Service Page Views → Contact Form Views → Contact Form Submits → Qualified Leads → Project Discussions → Contracts Signed
- **Show**: Conversion rates between stages

#### Chart 5: Device Performance
- **Chart Type**: Pie Chart or Bar Chart
- **Categories**: Desktop, Mobile, Tablet
- **Metrics**: Sessions, Conversions, Revenue

#### Chart 6: SEO Keywords
- **Chart Type**: Line Chart
- **X-Axis**: Date
- **Y-Axis**: Ranking, Search Volume
- **Filter**: By keyword

#### Chart 7: Social Media
- **Chart Type**: Bar Chart
- **X-Axis**: Platform
- **Y-Axis**: Engagement Rate, Reach, Conversions

#### Chart 8: Competitor Analysis
- **Chart Type**: Bar Chart
- **X-Axis**: Competitor
- **Y-Axis**: Average Ranking, Market Share

#### Chart 9: Revenue Trends
- **Chart Type**: Line Chart
- **X-Axis**: Date
- **Y-Axis**: Revenue, Growth Rate
- **Add**: Trend lines and forecasts

#### Chart 10: KPI Dashboard
- **Chart Type**: Cards and Gauges
- **Metrics**: Total Sessions, Revenue, Conversion Rate, ROAS
- **Add**: Goal indicators and thresholds

### Step 4: Create Dashboard Layout
1. Arrange charts in a logical flow
2. Add filters for date range, country, campaign
3. Include slicers for interactive filtering
4. Add titles and descriptions

## 🔧 Customization Options

### Modify Data Generation
Edit `evago_marketing_data_simulator.py` to:
- Change date ranges
- Add/remove countries
- Modify campaign names
- Adjust performance metrics

### Adjust Data Preparation
Edit `powerbi_data_preparation.py` to:
- Change aggregation periods (daily, weekly, monthly)
- Add new calculated fields
- Modify chart data structures

## 📋 Data Dictionary

### Common Fields
- `date`: Date of the data point
- `country`: Geographic location
- `campaign`: Marketing campaign name
- `platform`: Social media platform

### Key Metrics
- `sessions`: Website sessions
- `conversions`: Successful conversions
- `revenue`: Generated revenue
- `roas`: Return on ad spend
- `ctr`: Click-through rate
- `cpc`: Cost per click

## 🎯 Business Insights

This dashboard will help EVAGO:
- Track marketing performance across channels
- Identify high-performing campaigns and keywords
- Monitor geographic performance
- Analyze conversion funnel optimization
- Compare against competitors
- Make data-driven marketing decisions

## 📁 File Structure

```
evago_seo_project/
├── evago_marketing_data_simulator.py    # Main data generator
├── powerbi_data_preparation.py          # Power BI data preparation
├── seo_trends_collector.py              # Original Google Trends collector
├── requirements.txt                     # Python dependencies
├── README.md                           # This file
├── evago_*_data.csv                    # Generated raw data files
├── powerbi_chart*.csv                  # Power BI optimized files
└── *_summary.json                      # Data summaries
```

## 🚨 Troubleshooting

### Common Issues
1. **Missing dependencies**: Run `pip install -r requirements.txt`
2. **Date format issues**: Ensure Power BI recognizes date columns
3. **Large file sizes**: Consider filtering data by date range
4. **Performance issues**: Use aggregated data for large datasets

### Support
For issues or questions, check the generated summary files for data validation.

## 📊 Expected Output

After running both scripts, you should have:
- 10 raw data files (evago_*.csv)
- 10 Power BI optimized files (powerbi_*.csv)
- 2 summary files (*_summary.json)
- Ready-to-use data for 10 different Power BI charts

This comprehensive dataset will provide EVAGO with actionable insights for their SEA/SEO marketing strategies.

- All Power BI datasets for campaign, funnel, and device performance now include a `country` field for market-level analysis.
- Device metrics are now realistic: Mobile, Desktop, and Tablet have different session, conversion, and revenue patterns.
- SEO keyword data is now market-appropriate and localized by country (German, Dutch, English, Croatian), with common event industry terms included for all markets.
- Only relevant keywords appear for each country in the Power BI chart. 