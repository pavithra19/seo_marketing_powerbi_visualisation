# Power BI with Microsoft Fabric - Complete Setup Guide

## 🎯 Overview
This guide will walk you through creating EVAGO's global marketing dashboard using Power BI with Microsoft Fabric.

## 📋 Prerequisites
- Microsoft 365 account with Power BI Pro or Premium
- Access to Microsoft Fabric
- EVAGO data files from `powerbi_dashboards/` directory

## 🚀 Step-by-Step Setup

### Step 1: Access Microsoft Fabric
1. **Go to**: [Microsoft Fabric](https://app.fabric.microsoft.com)
2. **Sign in** with your Microsoft 365 account
3. **Create a new workspace** (if you don't have one)
   - Click "Create workspace"
   - Name it "EVAGO Marketing Dashboard"
   - Choose appropriate permissions

### Step 2: Set Up OneLake Data Lake
1. **Navigate to Data Engineering** in Fabric
2. **Create a new Lakehouse**:
   - Click "New" → "Lakehouse"
   - Name: "EVAGO_Data_Lake"
   - Description: "EVAGO Global Marketing Data"

### Step 3: Upload Data Files
1. **In your Lakehouse**:
   - Click "Upload" → "Files"
   - Upload all CSV files from `powerbi_dashboards/`:
     - `powerbi_chart1_global_traffic_overview.csv`
     - `powerbi_chart2_geographic_performance_map.csv`
     - `powerbi_chart3_campaign_performance_comparison.csv`
     - `powerbi_chart4_conversion_funnel_analysis.csv`
     - `powerbi_chart5_device_performance_breakdown.csv`
     - `powerbi_chart6_seo_keyword_rankings_trends.csv`
     - `powerbi_chart7_social_media_performance_comparison.csv`
     - `powerbi_chart8_competitor_analysis_dashboard.csv`
     - `powerbi_chart9_revenue_trends_analysis.csv`
     - `powerbi_chart10_mojo_acquisition_impact_dashboard.csv`

### Step 4: Create Power BI Dataset
1. **In Fabric, go to Power BI**:
   - Click "New" → "Power BI dataset"
   - Name: "EVAGO_Marketing_Dataset"

2. **Connect to your Lakehouse**:
   - Select your Lakehouse
   - Choose all uploaded CSV files
   - Click "Create"

### Step 5: Build Your Dashboard

#### Chart 1: Global Website Traffic Overview
1. **Create new report** in Power BI
2. **Add Line Chart**:
   - X-axis: `date`
   - Y-axis: `sessions`, `users`, `pageviews`
   - Legend: `country`
   - Add moving averages: `sessions_ma_7d`, `sessions_ma_30d`

#### Chart 2: Geographic Performance Map
1. **Add Map Visual**:
   - Location: `country_code`
   - Size: `revenue`
   - Color: `roas`
   - Tooltip: `conversions`, `ctr`

#### Chart 3: Campaign Performance Comparison
1. **Add Bar Chart**:
   - X-axis: `campaign`
   - Y-axis: `roas`, `ctr`, `cpc`
   - Color: `is_mojo_campaign`
   - Add data labels

#### Chart 4: Conversion Funnel Analysis
1. **Add Funnel Chart**:
   - Values: `website_visitors`, `service_page_views`, `contact_form_views`, `contact_form_submits`, `qualified_leads`, `project_discussions`, `contracts_signed`
   - Group by: `location_type`
   - Add conversion rates between stages

#### Chart 5: Device Performance Breakdown
1. **Add Pie Chart**:
   - Values: `sessions`
   - Legend: `device`
   - Add bar chart for `conversion_rate` by device

#### Chart 6: SEO Keyword Rankings Trends
1. **Add Line Chart**:
   - X-axis: `date`
   - Y-axis: `ranking`, `search_volume`
   - Legend: `keyword`
   - Filter by `keyword_type`

#### Chart 7: Social Media Performance Comparison
1. **Add Bar Chart**:
   - X-axis: `platform`
   - Y-axis: `engagement_rate`, `reach`, `conversions`
   - Color: `is_mojo_campaign`

#### Chart 8: Competitor Analysis Dashboard
1. **Add Bar Chart**:
   - X-axis: `competitor`
   - Y-axis: `avg_ranking`, `market_share`
   - Color: `is_mojo_competitor`

#### Chart 9: Revenue Trends Analysis
1. **Add Line Chart**:
   - X-axis: `date`
   - Y-axis: `total_revenue`, `organic_traffic`, `paid_traffic`
   - Add trend lines and forecasts

#### Chart 10: Mojo Acquisition Impact Dashboard
1. **Add Cards**:
   - Total Sessions
   - Total Revenue
   - Organic Traffic
   - ROAS
2. **Add Gauges**:
   - Market Share
   - Brand Awareness
   - Acquisition Impact Score

### Step 6: Create Relationships
1. **Go to Model view** in Power BI
2. **Create relationships**:
   - `date` fields between all tables
   - `country` fields for geographic analysis
   - `campaign` fields for campaign analysis

### Step 7: Add Filters and Slicers
1. **Add Date Range Slicer**:
   - Field: `date`
   - Type: Date range
2. **Add Country Slicer**:
   - Field: `country`
   - Type: Dropdown
3. **Add Campaign Slicer**:
   - Field: `campaign`
   - Type: Multi-select

### Step 8: Create Dashboard Layout
1. **Arrange charts** in logical order:
   - Top: KPI cards and summary metrics
   - Middle: Detailed performance charts
   - Bottom: Trend analysis and forecasts
2. **Add titles and descriptions**
3. **Set consistent color scheme**
4. **Add navigation buttons**

### Step 9: Publish and Share
1. **Save your report**
2. **Publish to workspace**
3. **Create dashboard** from report
4. **Share with stakeholders**:
   - Set appropriate permissions
   - Schedule automatic refresh
   - Set up alerts for key metrics

## 🔧 Advanced Features

### Data Refresh
1. **Set up automatic refresh**:
   - Go to dataset settings
   - Configure refresh schedule
   - Set up data source credentials

### Alerts and Notifications
1. **Create alerts** for:
   - Revenue drops below threshold
   - Conversion rate changes
   - Keyword ranking changes
   - Geographic performance issues

### Mobile Optimization
1. **Optimize for mobile**:
   - Adjust chart sizes
   - Simplify navigation
   - Ensure readability on small screens

## 📊 Dashboard Best Practices

### Visual Design
- Use consistent color scheme
- Limit charts per page (max 6-8)
- Use appropriate chart types
- Add clear titles and labels

### Performance
- Optimize data model
- Use calculated columns sparingly
- Limit data refresh frequency
- Monitor dashboard performance

### User Experience
- Add tooltips and help text
- Create intuitive navigation
- Provide drill-down capabilities
- Include export functionality

## 🎯 Key Metrics to Monitor

### Daily/Weekly
- Total sessions and revenue
- Conversion rates
- Campaign performance
- Geographic performance

### Monthly/Quarterly
- Trend analysis
- Market share changes
- Partner performance
- ROI analysis

## 🚨 Troubleshooting

### Common Issues
1. **Data not loading**: Check file formats and connections
2. **Charts not displaying**: Verify data types and relationships
3. **Performance issues**: Optimize data model and refresh schedule
4. **Access issues**: Check permissions and sharing settings

### Support Resources
- Microsoft Fabric documentation
- Power BI community forums
- Microsoft support channels

## 📈 Next Steps

1. **Customize dashboard** for your specific needs
2. **Add real data sources** when available
3. **Set up automated reporting**
4. **Train team members** on dashboard usage
5. **Gather feedback** and iterate

## 🎉 Success Metrics

Your dashboard is successful when:
- Stakeholders can access key metrics easily
- Data is updated automatically
- Insights lead to actionable decisions
- Performance improves over time
- Team adoption is high

This comprehensive setup will give EVAGO a powerful, scalable marketing analytics platform using Microsoft Fabric and Power BI. 