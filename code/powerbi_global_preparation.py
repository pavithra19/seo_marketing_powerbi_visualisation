import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json
import os

class PowerBIGlobalDataPreparation:
    def __init__(self):
        self.datasets = {}
        
    def load_all_datasets(self):
        """Load all generated datasets"""
        print("Loading all global datasets...")
        
        dataset_files = [
            'data/evago_google_analytics_data.csv',
            'data/evago_google_ads_data.csv', 
            'data/evago_seo_keywords_data.csv',
            'data/evago_social_media_data.csv',
            'data/evago_competitor_analysis_data.csv',
            'data/evago_conversion_funnel_data.csv',
            'data/evago_device_performance_data.csv',
            'data/evago_campaign_performance_data.csv',
            'data/evago_geographic_performance_data.csv',
            'data/evago_time_series_data.csv',
            'data/evago_mojo_acquisition_impact_data.csv'
        ]
        
        for file in dataset_files:
            try:
                name = file.replace('data/evago_', '').replace('_data.csv', '')
                self.datasets[name] = pd.read_csv(file)
                print(f"Loaded {file} - {len(self.datasets[name])} rows")
            except FileNotFoundError:
                print(f"Warning: {file} not found")
        
        return self.datasets
    
    def prepare_chart_1_global_traffic_overview(self):
        """Chart 1: Global Website Traffic Overview (Line Chart)"""
        print("Preparing Chart 1: Global Website Traffic Overview...")
        
        # Aggregate daily traffic by country and city
        traffic_data = self.datasets['google_analytics'].copy()
        traffic_data['date'] = pd.to_datetime(traffic_data['date'])
        
        # Daily totals with location breakdown
        daily_traffic = traffic_data.groupby(['date', 'country', 'location_type']).agg({
            'sessions': 'sum',
            'users': 'sum', 
            'pageviews': 'sum',
            'revenue': 'sum',
            'organic_traffic': 'sum',
            'paid_traffic': 'sum'
        }).reset_index()
        
        # Add moving averages
        daily_traffic['sessions_ma_7d'] = daily_traffic.groupby('country')['sessions'].rolling(7).mean().reset_index(0, drop=True)
        daily_traffic['sessions_ma_30d'] = daily_traffic.groupby('country')['sessions'].rolling(30).mean().reset_index(0, drop=True)
        
        # Save for Power BI
        daily_traffic.to_csv('powerbi_dashboards/powerbi_chart1_global_traffic_overview.csv', index=False)
        print(f"Saved powerbi_chart1_global_traffic_overview.csv with {len(daily_traffic)} rows")
        
        return daily_traffic
    
    def prepare_chart_2_geographic_performance_map(self):
        """Chart 2: Geographic Performance Map (Map Chart)"""
        print("Preparing Chart 2: Geographic Performance Map...")
        
        geo_data = self.datasets['geographic_performance'].copy()
        geo_data['date'] = pd.to_datetime(geo_data['date'])
        
        # Monthly performance by country
        geo_monthly = geo_data.groupby(['country', 'location_type', pd.Grouper(key='date', freq='ME')]).agg({
            'impressions': 'sum',
            'clicks': 'sum',
            'conversions': 'sum',
            'revenue': 'sum',
            'cost': 'sum'
        }).reset_index()
        
        # Calculate KPIs
        geo_monthly['ctr'] = geo_monthly['clicks'] / geo_monthly['impressions']
        geo_monthly['conversion_rate'] = geo_monthly['conversions'] / geo_monthly['clicks']
        geo_monthly['roas'] = geo_monthly['revenue'] / geo_monthly['cost']
        
        # Add country codes for mapping
        country_codes = {
            'Germany': 'DEU', 'Netherlands': 'NLD', 'England': 'GBR',
            'North America': 'USA', 'Australia': 'AUS'
        }
        geo_monthly['country_code'] = geo_monthly['country'].map(country_codes)
        
        geo_monthly.to_csv('powerbi_dashboards/powerbi_chart2_geographic_performance_map.csv', index=False)
        print(f"Saved powerbi_chart2_geographic_performance_map.csv with {len(geo_monthly)} rows")
        
        return geo_monthly
    
    def prepare_chart_3_campaign_performance_comparison(self):
        """Chart 3: Campaign Performance Comparison (Bar Chart) with country breakdown"""
        print("Preparing Chart 3: Campaign Performance Comparison...")
        
        campaign_data = self.datasets['campaign_performance'].copy()
        campaign_data['date'] = pd.to_datetime(campaign_data['date'])
        
        # Monthly campaign performance by country
        campaign_monthly = campaign_data.groupby(['country', 'campaign', 'is_mojo_campaign', pd.Grouper(key='date', freq='ME')]).agg({
            'budget': 'sum',
            'spend': 'sum',
            'impressions': 'sum',
            'clicks': 'sum',
            'conversions': 'sum',
            'revenue': 'sum'
        }).reset_index()
        
        # Calculate KPIs
        campaign_monthly['ctr'] = campaign_monthly['clicks'] / campaign_monthly['impressions']
        campaign_monthly['cpc'] = campaign_monthly['spend'] / campaign_monthly['clicks']
        campaign_monthly['roas'] = campaign_monthly['revenue'] / campaign_monthly['spend']
        campaign_monthly['budget_utilization'] = campaign_monthly['spend'] / campaign_monthly['budget']
        
        campaign_monthly.to_csv('powerbi_dashboards/powerbi_chart3_campaign_performance_comparison.csv', index=False)
        print(f"Saved powerbi_chart3_campaign_performance_comparison.csv with {len(campaign_monthly)} rows")
        return campaign_monthly
    
    def prepare_chart_4_conversion_funnel_analysis(self):
        """Chart 4: Conversion Funnel Analysis (Funnel Chart) with country breakdown"""
        print("Preparing Chart 4: Conversion Funnel Analysis...")
        
        funnel_data = self.datasets['conversion_funnel'].copy()
        funnel_data['date'] = pd.to_datetime(funnel_data['date'])
        
        # Monthly funnel data by country
        funnel_monthly = funnel_data.groupby(['country', 'location_type', 'mojo_integration', pd.Grouper(key='date', freq='ME')]).agg({
            'website_visitors': 'sum',
            'service_page_views': 'sum',
            'contact_form_views': 'sum',
            'contact_form_submits': 'sum',
            'qualified_leads': 'sum',
            'project_discussions': 'sum',
            'contracts_signed': 'sum'
        }).reset_index()
        
        # Calculate conversion rates between stages
        funnel_monthly['visitor_to_pageview_rate'] = funnel_monthly['service_page_views'] / funnel_monthly['website_visitors']
        funnel_monthly['pageview_to_formview_rate'] = funnel_monthly['contact_form_views'] / funnel_monthly['service_page_views']
        funnel_monthly['formview_to_submit_rate'] = funnel_monthly['contact_form_submits'] / funnel_monthly['contact_form_views']
        funnel_monthly['submit_to_lead_rate'] = funnel_monthly['qualified_leads'] / funnel_monthly['contact_form_submits']
        funnel_monthly['lead_to_discussion_rate'] = funnel_monthly['project_discussions'] / funnel_monthly['qualified_leads']
        funnel_monthly['discussion_to_contract_rate'] = funnel_monthly['contracts_signed'] / funnel_monthly['project_discussions']
        funnel_monthly['overall_conversion_rate'] = funnel_monthly['contracts_signed'] / funnel_monthly['website_visitors']
        
        funnel_monthly.to_csv('powerbi_dashboards/powerbi_chart4_conversion_funnel_analysis.csv', index=False)
        print(f"Saved powerbi_chart4_conversion_funnel_analysis.csv with {len(funnel_monthly)} rows")
        return funnel_monthly
    
    def prepare_chart_5_device_performance_breakdown(self):
        """Chart 5: Device Performance Breakdown (Pie Chart) with country breakdown"""
        print("Preparing Chart 5: Device Performance Breakdown...")
        
        device_data = self.datasets['device_performance'].copy()
        device_data['date'] = pd.to_datetime(device_data['date'])
        
        # Monthly device performance by country
        device_monthly = device_data.groupby(['country', 'device', 'location_type', 'mojo_integration', pd.Grouper(key='date', freq='ME')]).agg({
            'sessions': 'sum',
            'conversions': 'sum',
            'revenue': 'sum',
            'bounce_rate': 'mean',
            'avg_session_duration': 'mean'
        }).reset_index()
        
        device_monthly.to_csv('powerbi_dashboards/powerbi_chart5_device_performance_breakdown.csv', index=False)
        print(f"Saved powerbi_chart5_device_performance_breakdown.csv with {len(device_monthly)} rows")
        return device_monthly
    
    def prepare_chart_6_seo_keyword_rankings_trends(self):
        """Chart 6: SEO Keyword Rankings Trends (Line Chart) with country breakdown"""
        print("Preparing Chart 6: SEO Keyword Rankings Trends...")
        
        seo_data = self.datasets['seo_keywords'].copy()
        seo_data['date'] = pd.to_datetime(seo_data['date'])
        
        # Weekly keyword performance by type and country
        seo_weekly = seo_data.groupby(['keyword', 'country', 'keyword_type', 'is_mojo_keyword', pd.Grouper(key='date', freq='W')]).agg({
            'ranking': 'mean',
            'search_volume': 'mean',
            'clicks': 'sum',
            'impressions': 'sum',
            'ctr': 'mean',
            'avg_position': 'mean',
            'organic_traffic': 'sum'
        }).reset_index()
        
        # Calculate organic traffic potential
        seo_weekly['organic_traffic_potential'] = seo_weekly['search_volume'] * (1 / seo_weekly['ranking'])
        
        seo_weekly.to_csv('powerbi_dashboards/powerbi_chart6_seo_keyword_rankings_trends.csv', index=False)
        print(f"Saved powerbi_chart6_seo_keyword_rankings_trends.csv with {len(seo_weekly)} rows")
        
        return seo_weekly
    
    def prepare_chart_7_social_media_performance_comparison(self):
        """Chart 7: Social Media Performance Comparison (Bar Chart)"""
        print("Preparing Chart 7: Social Media Performance Comparison...")
        
        social_data = self.datasets['social_media'].copy()
        social_data['date'] = pd.to_datetime(social_data['date'])
        
        # Monthly social media performance by platform
        social_monthly = social_data.groupby(['platform', 'is_mojo_campaign', pd.Grouper(key='date', freq='ME')]).agg({
            'reach': 'sum',
            'impressions': 'sum',
            'engagement': 'sum',
            'clicks': 'sum',
            'conversions': 'sum',
            'cost': 'sum'
        }).reset_index()
        
        # Calculate KPIs
        social_monthly['engagement_rate'] = social_monthly['engagement'] / social_monthly['reach']
        social_monthly['click_through_rate'] = social_monthly['clicks'] / social_monthly['impressions']
        social_monthly['conversion_rate'] = social_monthly['conversions'] / social_monthly['clicks']
        social_monthly['cost_per_engagement'] = social_monthly['cost'] / social_monthly['engagement']
        
        social_monthly.to_csv('powerbi_dashboards/powerbi_chart7_social_media_performance_comparison.csv', index=False)
        print(f"Saved powerbi_chart7_social_media_performance_comparison.csv with {len(social_monthly)} rows")
        
        return social_monthly
    
    def prepare_chart_8_competitor_analysis_dashboard(self):
        """Chart 8: Competitor Analysis Dashboard (Bar Chart) with country and keyword breakdown"""
        print("Preparing Chart 8: Competitor Analysis Dashboard...")
        
        competitor_data = self.datasets['competitor_analysis'].copy()
        competitor_data['date'] = pd.to_datetime(competitor_data['date'])
        
        # Monthly competitor performance by country and keyword
        competitor_monthly = competitor_data.groupby([
            'country', 'competitor', 'is_mojo_competitor', 'keyword', pd.Grouper(key='date', freq='ME')
        ]).agg({
            'ranking': 'mean',
            'search_volume': 'sum',
            'estimated_traffic': 'sum',
            'market_share': 'mean'
        }).reset_index()
        
        # Calculate average ranking
        competitor_monthly['avg_ranking'] = competitor_monthly['ranking']
        
        competitor_monthly.to_csv('powerbi_dashboards/powerbi_chart8_competitor_analysis_dashboard.csv', index=False)
        print(f"Saved powerbi_chart8_competitor_analysis_dashboard.csv with {len(competitor_monthly)} rows")
        
        return competitor_monthly
    
    def prepare_chart_9_revenue_trends_analysis(self):
        """Chart 9: Revenue Trends Analysis (Line Chart) with all relevant fields"""
        print("Preparing Chart 9: Revenue Trends Analysis...")
        
        time_data = self.datasets['time_series'].copy()
        time_data['date'] = pd.to_datetime(time_data['date'])
        
        # Weekly revenue trends
        revenue_weekly = time_data.groupby(pd.Grouper(key='date', freq='W')).agg({
            'total_traffic': 'sum',
            'organic_traffic': 'sum',
            'paid_traffic': 'sum',
            'total_conversions': 'sum',
            'total_revenue': 'sum',
            'avg_order_value': 'mean',
            'conversion_rate': 'mean',
            'revenue_per_visitor': 'mean',
            'mojo_integration_active': 'max'
        }).reset_index()
        
        # Add growth rates
        revenue_weekly['revenue_growth'] = revenue_weekly['total_revenue'].pct_change()
        revenue_weekly['traffic_growth'] = revenue_weekly['total_traffic'].pct_change()
        revenue_weekly['organic_growth'] = revenue_weekly['organic_traffic'].pct_change()
        
        revenue_weekly.to_csv('powerbi_dashboards/powerbi_chart9_revenue_trends_analysis.csv', index=False)
        print(f"Saved powerbi_chart9_revenue_trends_analysis.csv with {len(revenue_weekly)} rows")
        
        return revenue_weekly
    
    def prepare_chart_10_mojo_acquisition_impact_dashboard(self):
        """Chart 10: Mojo Acquisition Impact Dashboard (Cards/Gauges) with all relevant fields"""
        print("Preparing Chart 10: Mojo Acquisition Impact Dashboard...")
        
        # Create KPI summary data
        kpi_data = []
        
        # Use the most recent 3 months with data
        def get_recent_months(df, date_col):
            df[date_col] = pd.to_datetime(df[date_col])
            if df.empty:
                return df
            last_date = df[date_col].max()
            first_date = last_date - pd.DateOffset(months=3)
            return df[df[date_col] > first_date]
        
        # Traffic KPIs
        traffic_data = get_recent_months(self.datasets['google_analytics'].copy(), 'date')
        # Revenue KPIs
        revenue_data = get_recent_months(self.datasets['time_series'].copy(), 'date')
        # Campaign KPIs
        campaign_data = get_recent_months(self.datasets['campaign_performance'].copy(), 'date')
        # Mojo Acquisition Impact KPIs
        mojo_data = get_recent_months(self.datasets['mojo_acquisition_impact'].copy(), 'date')
        
        kpi_data.append({
            'metric': 'Total Sessions',
            'value': traffic_data['sessions'].sum(),
            'category': 'Traffic',
            'mojo_impact': 'Global'
        })
        
        kpi_data.append({
            'metric': 'Total Revenue',
            'value': revenue_data['total_revenue'].sum(),
            'category': 'Revenue',
            'mojo_impact': 'Global'
        })
        
        kpi_data.append({
            'metric': 'Organic Traffic',
            'value': traffic_data['organic_traffic'].sum(),
            'category': 'SEO',
            'mojo_impact': 'Enhanced'
        })
        
        kpi_data.append({
            'metric': 'ROAS',
            'value': campaign_data['roas'].mean(),
            'category': 'ROI',
            'mojo_impact': 'Improved'
        })
        
        kpi_data.append({
            'metric': 'Market Share',
            'value': mojo_data['market_share'].mean(),
            'category': 'Market',
            'mojo_impact': 'Expanded'
        })
        
        kpi_data.append({
            'metric': 'Brand Awareness',
            'value': mojo_data['brand_awareness'].mean(),
            'category': 'Brand',
            'mojo_impact': 'Strengthened'
        })
        
        kpi_data.append({
            'metric': 'Mojo Campaigns',
            'value': len(campaign_data[campaign_data['is_mojo_campaign'] == True]),
            'category': 'Campaigns',
            'mojo_impact': 'New'
        })
        
        kpi_data.append({
            'metric': 'Acquisition Impact Score',
            'value': mojo_data['acquisition_impact_score'].mean(),
            'category': 'Performance',
            'mojo_impact': 'Positive'
        })
        
        kpi_df = pd.DataFrame(kpi_data)
        kpi_df.to_csv('powerbi_dashboards/powerbi_chart10_mojo_acquisition_impact_dashboard.csv', index=False)
        print(f"Saved powerbi_chart10_mojo_acquisition_impact_dashboard.csv with {len(kpi_df)} rows")
        
        return kpi_df
    
    def create_powerbi_data_model(self):
        """Create a comprehensive data model for Power BI"""
        print("Creating Power BI global data model...")
        
        # Create powerbi_dashboards directory if it doesn't exist
        os.makedirs('powerbi_dashboards', exist_ok=True)
        
        # Load all datasets
        self.load_all_datasets()
        
        # Prepare all charts
        charts = {
            'chart1_global_traffic_overview': self.prepare_chart_1_global_traffic_overview(),
            'chart2_geographic_performance_map': self.prepare_chart_2_geographic_performance_map(),
            'chart3_campaign_performance_comparison': self.prepare_chart_3_campaign_performance_comparison(),
            'chart4_conversion_funnel_analysis': self.prepare_chart_4_conversion_funnel_analysis(),
            'chart5_device_performance_breakdown': self.prepare_chart_5_device_performance_breakdown(),
            'chart6_seo_keyword_rankings_trends': self.prepare_chart_6_seo_keyword_rankings_trends(),
            'chart7_social_media_performance_comparison': self.prepare_chart_7_social_media_performance_comparison(),
            'chart8_competitor_analysis_dashboard': self.prepare_chart_8_competitor_analysis_dashboard(),
            'chart9_revenue_trends_analysis': self.prepare_chart_9_revenue_trends_analysis(),
            'chart10_mojo_acquisition_impact_dashboard': self.prepare_chart_10_mojo_acquisition_impact_dashboard()
        }
        
        # Create summary
        summary = {
            'charts_prepared': len(charts),
            'total_files': len(charts),
            'files_created': [f'powerbi_{name}.csv' for name in charts.keys()],
            'chart_descriptions': {
                'chart1_global_traffic_overview': 'Global Website Traffic Overview - Line Chart with Location Breakdown',
                'chart2_geographic_performance_map': 'Geographic Performance Map - Map Chart with Country Codes',
                'chart3_campaign_performance_comparison': 'Campaign Performance Comparison - Bar Chart (EVAGO vs Mojo)',
                'chart4_conversion_funnel_analysis': 'Conversion Funnel Analysis - Funnel Chart by Location Type',
                'chart5_device_performance_breakdown': 'Device Performance Breakdown - Pie/Bar Chart by Location',
                'chart6_seo_keyword_rankings_trends': 'SEO Keyword Rankings Trends - Line Chart (EVAGO vs Mojo Keywords)',
                'chart7_social_media_performance_comparison': 'Social Media Performance Comparison - Bar Chart by Platform',
                'chart8_competitor_analysis_dashboard': 'Competitor Analysis Dashboard - Bar Chart including Mojo Legacy',
                'chart9_revenue_trends_analysis': 'Revenue Trends Analysis - Line Chart with Organic vs Paid Traffic',
                'chart10_mojo_acquisition_impact_dashboard': 'Mojo Acquisition Impact Dashboard - Cards/Gauges with Impact Metrics'
            },
            'seo_sea_metrics_included': [
                'CTR (Click-Through Rate)',
                'CPC (Cost Per Click)',
                'ROAS (Return on Ad Spend)',
                'Organic Traffic',
                'Paid Traffic',
                'Keyword Performance',
                'Conversion Rates',
                'Bounce Rate',
                'Session Duration',
                'Market Share',
                'Brand Awareness',
                'Engagement Rate',
                'Click-through Rate',
                'Cost per Engagement'
            ],
            'global_locations_covered': [
                'Germany (5 locations)',
                'Netherlands',
                'England (2 locations)',
                'North America',
                'Australia',
                '12 Distribution Offices Worldwide'
            ],
            'mojo_acquisition_features': [
                'Pre/Post Acquisition Comparison',
                'Mojo Campaign Performance',
                'Mojo Keyword Rankings',
                'Acquisition Impact Score',
                'Market Share Expansion',
                'Brand Awareness Growth'
            ]
        }
        
        with open('powerbi_dashboards/powerbi_global_data_summary.json', 'w') as f:
            json.dump(summary, f, indent=2, default=str)
        
        print("\nPower BI global data preparation complete!")
        print("Files created for Power BI:")
        for name, desc in summary['chart_descriptions'].items():
            print(f"  - powerbi_{name}.csv: {desc}")
        print("  - powerbi_global_data_summary.json")
        print(f"\nSEO/SEA Metrics Covered: {len(summary['seo_sea_metrics_included'])}")
        print(f"Global Locations: {len(summary['global_locations_covered'])}")
        print(f"Mojo Acquisition Features: {len(summary['mojo_acquisition_features'])}")
        
        return charts

if __name__ == "__main__":
    preparer = PowerBIGlobalDataPreparation()
    charts = preparer.create_powerbi_data_model() 