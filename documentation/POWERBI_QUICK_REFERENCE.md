# Power BI Quick Reference - EVAGO Dashboard

## Chart 1: Global Traffic Overview
**File:** `powerbi_chart1_global_traffic_overview.csv`
- **X-Axis:** `date`
- **Y-Values:** `sessions`
- **Legend:** `country`
- **Chart Type:** Line Chart

## Chart 2: Geographic Performance Map
**File:** `powerbi_chart2_geographic_performance_map.csv`
- **Location:** `country_code`
- **Values:** `revenue`
- **Chart Type:** Map (Filled Map)

## Chart 3: Campaign Performance
**File:** `powerbi_chart3_campaign_performance_comparison.csv`
- **X-Axis:** `campaign_name`
- **Y-Values:** `clicks`
- **Legend:** `partner`
- **Chart Type:** Clustered Bar Chart

## Chart 4: Conversion Funnel
**File:** `powerbi_chart4_conversion_funnel_analysis.csv`
- **Category:** `funnel_stage`
- **Values:** `count`
- **Chart Type:** Funnel Chart

## Chart 5: Device Performance
**File:** `powerbi_chart5_device_performance_breakdown.csv`
- **Legend:** `device_category`
- **Values:** `sessions`
- **Chart Type:** Pie Chart

## Chart 6: SEO Keywords
**File:** `powerbi_chart6_seo_keyword_rankings_trends.csv`
- **X-Axis:** `date`
- **Y-Values:** `ranking_position`
- **Legend:** `keyword`
- **Chart Type:** Line Chart
- **SEO Keyword Chart:** Uses market-appropriate, localized keywords (German, Dutch, English, Croatian) and common event industry terms for all markets. Only relevant keywords appear for each country in the chart.

## Chart 7: Social Media
**File:** `powerbi_chart7_social_media_performance_comparison.csv`
- **X-Axis:** `platform`
- **Y-Values:** `followers`
- **Legend:** `partner`
- **Chart Type:** Clustered Bar Chart

## Chart 8: Competitor Analysis
**File:** `powerbi_chart8_competitor_analysis_dashboard.csv`
- **X-Axis:** `competitor_name`
- **Y-Values:** `market_share`
- **Chart Type:** Bar Chart

## Chart 9: Revenue Trends
**File:** `powerbi_chart9_revenue_trends_analysis.csv`
- **X-Axis:** `date`
- **Y-Values:** `revenue`
- **Legend:** `traffic_source`
- **Chart Type:** Line Chart

## Chart 10: Mojo Impact
**File:** `powerbi_chart10_mojo_acquisition_impact_dashboard.csv`
- **Cards:** `acquisition_impact_score`, `market_share_expansion`
- **Gauges:** `roas_improvement`, `ctr_improvement`
- **Chart Type:** Cards & Gauges

## Key Data Types to Set:
- `date` → Date/DateTime
- `country_code` → Text
- `revenue`, `sessions`, `clicks` → Whole Number
- `ctr`, `conversion_rate`, `roas` → Decimal Number
- `partner`, `country`, `platform` → Text

## Essential Slicers:
- Date Range
- Country
- Partner (EVAGO/Mojo)
- Location Type (Primary/Expansion)

## Additional Notes:
- **Country Field:** All campaign, funnel, and device charts now include a `country` field for filtering and analysis.
- **Device Metrics:** Device performance is now split realistically by device type (Mobile, Desktop, Tablet). 