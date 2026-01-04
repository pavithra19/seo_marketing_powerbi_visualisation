import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json

class PowerBIDataPreparation:
    def __init__(self):
        self.datasets = {}
        
    def load_all_datasets(self):
        """Load all generated datasets"""
        print("Loading all datasets...")
        
        dataset_files = [
            'evago_google_analytics_data.csv',
            'evago_google_ads_data.csv', 
            'evago_seo_keywords_data.csv',
            'evago_social_media_data.csv',
            'evago_competitor_analysis_data.csv',
            'evago_conversion_funnel_data.csv',
            'evago_device_performance_data.csv',
            'evago_campaign_performance_data.csv',
            'evago_geographic_performance_data.csv',
            'evago_time_series_data.csv'
        ]
        
        for file in dataset_files:
            try:
                name = file.replace('evago_', '').replace('_data.csv', '')
                self.datasets[name] = pd.read_csv(file)
                print(f"Loaded {file} - {len(self.datasets[name])} rows")
            except FileNotFoundError:
                print(f"Warning: {file} not found")
        
        return self.datasets
    
    def prepare_chart_1_traffic_overview(self):
        """Chart 1: Website Traffic Overview (Line Chart)"""
        print("Preparing Chart 1: Website Traffic Overview...")
        
        # Aggregate daily traffic by country
        traffic_data = self.datasets['google_analytics'].copy()
        traffic_data['date'] = pd.to_datetime(traffic_data['date'])
        
        # Daily totals
        daily_traffic = traffic_data.groupby('date').agg({
            'sessions': 'sum',
            'users': 'sum', 
            'pageviews': 'sum',
            'revenue': 'sum'
        }).reset_index()
        
        # Add moving averages
        daily_traffic['sessions_ma_7d'] = daily_traffic['sessions'].rolling(7).mean()
        daily_traffic['sessions_ma_30d'] = daily_traffic['sessions'].rolling(30).mean()
        
        # Save for Power BI
        daily_traffic.to_csv('powerbi_chart1_traffic_overview.csv', index=False)
        print(f"Saved powerbi_chart1_traffic_overview.csv with {len(daily_traffic)} rows")
        
        return daily_traffic
    
    def prepare_chart_2_geographic_performance(self):
        """Chart 2: Geographic Performance (Map/Bar Chart)"""
        print("Preparing Chart 2: Geographic Performance...")
        
        geo_data = self.datasets['geographic_performance'].copy()
        geo_data['date'] = pd.to_datetime(geo_data['date'])
        
        # Monthly performance by country
        geo_monthly = geo_data.groupby(['country', pd.Grouper(key='date', freq='M')]).agg({
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
            'Germany': 'DEU', 'Netherlands': 'NLD', 'Belgium': 'BEL',
            'France': 'FRA', 'UK': 'GBR', 'Austria': 'AUT', 'Switzerland': 'CHE'
        }
        geo_monthly['country_code'] = geo_monthly['country'].map(country_codes)
        
        geo_monthly.to_csv('powerbi_chart2_geographic_performance.csv', index=False)
        print(f"Saved powerbi_chart2_geographic_performance.csv with {len(geo_monthly)} rows")
        
        return geo_monthly
    
    def prepare_chart_3_campaign_performance(self):
        """Chart 3: Campaign Performance (Bar Chart)"""
        print("Preparing Chart 3: Campaign Performance...")
        
        campaign_data = self.datasets['campaign_performance'].copy()
        campaign_data['date'] = pd.to_datetime(campaign_data['date'])
        
        # Monthly campaign performance
        campaign_monthly = campaign_data.groupby(['campaign', pd.Grouper(key='date', freq='M')]).agg({
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
        
        campaign_monthly.to_csv('powerbi_chart3_campaign_performance.csv', index=False)
        print(f"Saved powerbi_chart3_campaign_performance.csv with {len(campaign_monthly)} rows")
        
        return campaign_monthly
    
    def prepare_chart_4_conversion_funnel(self):
        """Chart 4: Conversion Funnel (Funnel Chart)"""
        print("Preparing Chart 4: Conversion Funnel...")
        
        funnel_data = self.datasets['conversion_funnel'].copy()
        funnel_data['date'] = pd.to_datetime(funnel_data['date'])
        
        # Monthly funnel data
        funnel_monthly = funnel_data.groupby(pd.Grouper(key='date', freq='M')).agg({
            'visitors': 'sum',
            'page_views': 'sum',
            'add_to_cart': 'sum',
            'checkout_started': 'sum',
            'purchases': 'sum'
        }).reset_index()
        
        # Calculate conversion rates between stages
        funnel_monthly['visitor_to_pageview_rate'] = funnel_monthly['page_views'] / funnel_monthly['visitors']
        funnel_monthly['pageview_to_cart_rate'] = funnel_monthly['add_to_cart'] / funnel_monthly['page_views']
        funnel_monthly['cart_to_checkout_rate'] = funnel_monthly['checkout_started'] / funnel_monthly['add_to_cart']
        funnel_monthly['checkout_to_purchase_rate'] = funnel_monthly['purchases'] / funnel_monthly['checkout_started']
        funnel_monthly['overall_conversion_rate'] = funnel_monthly['purchases'] / funnel_monthly['visitors']
        
        funnel_monthly.to_csv('powerbi_chart4_conversion_funnel.csv', index=False)
        print(f"Saved powerbi_chart4_conversion_funnel.csv with {len(funnel_monthly)} rows")
        
        return funnel_monthly
    
    def prepare_chart_5_device_performance(self):
        """Chart 5: Device Performance (Pie/Bar Chart)"""
        print("Preparing Chart 5: Device Performance...")
        
        device_data = self.datasets['device_performance'].copy()
        device_data['date'] = pd.to_datetime(device_data['date'])
        
        # Monthly device performance
        device_monthly = device_data.groupby(['device', pd.Grouper(key='date', freq='M')]).agg({
            'sessions': 'sum',
            'conversions': 'sum',
            'revenue': 'sum',
            'bounce_rate': 'mean',
            'avg_session_duration': 'mean'
        }).reset_index()
        
        # Calculate conversion rates
        device_monthly['conversion_rate'] = device_monthly['conversions'] / device_monthly['sessions']
        device_monthly['revenue_per_session'] = device_monthly['revenue'] / device_monthly['sessions']
        
        device_monthly.to_csv('powerbi_chart5_device_performance.csv', index=False)
        print(f"Saved powerbi_chart5_device_performance.csv with {len(device_monthly)} rows")
        
        return device_monthly
    
    def prepare_chart_6_seo_keyword_rankings(self):
        """Chart 6: SEO Keyword Rankings (Line Chart)"""
        print("Preparing Chart 6: SEO Keyword Rankings...")
        
        seo_data = self.datasets['seo_keywords'].copy()
        seo_data['date'] = pd.to_datetime(seo_data['date'])
        
        # Weekly keyword performance
        seo_weekly = seo_data.groupby(['keyword', pd.Grouper(key='date', freq='W')]).agg({
            'ranking': 'mean',
            'search_volume': 'mean',
            'clicks': 'sum',
            'impressions': 'sum',
            'ctr': 'mean',
            'avg_position': 'mean'
        }).reset_index()
        
        # Calculate organic traffic potential
        seo_weekly['organic_traffic_potential'] = seo_weekly['search_volume'] * (1 / seo_weekly['ranking'])
        
        seo_weekly.to_csv('powerbi_chart6_seo_keywords.csv', index=False)
        print(f"Saved powerbi_chart6_seo_keywords.csv with {len(seo_weekly)} rows")
        
        return seo_weekly
    
    def prepare_chart_7_social_media_performance(self):
        """Chart 7: Social Media Performance (Bar Chart)"""
        print("Preparing Chart 7: Social Media Performance...")
        
        social_data = self.datasets['social_media'].copy()
        social_data['date'] = pd.to_datetime(social_data['date'])
        
        # Monthly social media performance
        social_monthly = social_data.groupby(['platform', pd.Grouper(key='date', freq='M')]).agg({
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
        
        social_monthly.to_csv('powerbi_chart7_social_media.csv', index=False)
        print(f"Saved powerbi_chart7_social_media.csv with {len(social_monthly)} rows")
        
        return social_monthly
    
    def prepare_chart_8_competitor_analysis(self):
        """Chart 8: Competitor Analysis (Bar Chart)"""
        print("Preparing Chart 8: Competitor Analysis...")
        
        competitor_data = self.datasets['competitor_analysis'].copy()
        competitor_data['date'] = pd.to_datetime(competitor_data['date'])
        
        # Monthly competitor performance
        competitor_monthly = competitor_data.groupby(['competitor', pd.Grouper(key='date', freq='M')]).agg({
            'ranking': 'mean',
            'search_volume': 'sum',
            'estimated_traffic': 'sum',
            'market_share': 'mean'
        }).reset_index()
        
        # Calculate average ranking
        competitor_monthly['avg_ranking'] = competitor_monthly['ranking']
        
        competitor_monthly.to_csv('powerbi_chart8_competitor_analysis.csv', index=False)
        print(f"Saved powerbi_chart8_competitor_analysis.csv with {len(competitor_monthly)} rows")
        
        return competitor_monthly
    
    def prepare_chart_9_revenue_trends(self):
        """Chart 9: Revenue Trends (Line Chart)"""
        print("Preparing Chart 9: Revenue Trends...")
        
        time_data = self.datasets['time_series'].copy()
        time_data['date'] = pd.to_datetime(time_data['date'])
        
        # Weekly revenue trends
        revenue_weekly = time_data.groupby(pd.Grouper(key='date', freq='W')).agg({
            'total_traffic': 'sum',
            'total_conversions': 'sum',
            'total_revenue': 'sum',
            'avg_order_value': 'mean',
            'conversion_rate': 'mean',
            'revenue_per_visitor': 'mean'
        }).reset_index()
        
        # Add growth rates
        revenue_weekly['revenue_growth'] = revenue_weekly['total_revenue'].pct_change()
        revenue_weekly['traffic_growth'] = revenue_weekly['total_traffic'].pct_change()
        
        revenue_weekly.to_csv('powerbi_chart9_revenue_trends.csv', index=False)
        print(f"Saved powerbi_chart9_revenue_trends.csv with {len(revenue_weekly)} rows")
        
        return revenue_weekly
    
    def prepare_chart_10_kpi_dashboard(self):
        """Chart 10: KPI Dashboard (Cards/Gauges)"""
        print("Preparing Chart 10: KPI Dashboard...")
        
        # Create KPI summary data
        kpi_data = []
        
        # Current month KPIs
        current_date = datetime.now()
        current_month = current_date.replace(day=1)
        
        # Traffic KPIs
        traffic_data = self.datasets['google_analytics'].copy()
        traffic_data['date'] = pd.to_datetime(traffic_data['date'])
        current_month_traffic = traffic_data[traffic_data['date'] >= current_month]
        
        # Revenue KPIs
        revenue_data = self.datasets['time_series'].copy()
        revenue_data['date'] = pd.to_datetime(revenue_data['date'])
        current_month_revenue = revenue_data[revenue_data['date'] >= current_month]
        
        # Campaign KPIs
        campaign_data = self.datasets['campaign_performance'].copy()
        campaign_data['date'] = pd.to_datetime(campaign_data['date'])
        current_month_campaigns = campaign_data[campaign_data['date'] >= current_month]
        
        kpi_data.append({
            'metric': 'Total Sessions',
            'value': current_month_traffic['sessions'].sum(),
            'category': 'Traffic'
        })
        
        kpi_data.append({
            'metric': 'Total Revenue',
            'value': current_month_revenue['total_revenue'].sum(),
            'category': 'Revenue'
        })
        
        kpi_data.append({
            'metric': 'Conversion Rate',
            'value': (current_month_traffic['sessions'].sum() * 0.03),  # 3% conversion rate
            'category': 'Performance'
        })
        
        kpi_data.append({
            'metric': 'ROAS',
            'value': current_month_campaigns['roas'].mean(),
            'category': 'ROI'
        })
        
        kpi_data.append({
            'metric': 'Avg Order Value',
            'value': current_month_revenue['avg_order_value'].mean(),
            'category': 'Revenue'
        })
        
        kpi_data.append({
            'metric': 'Total Campaigns',
            'value': len(current_month_campaigns['campaign'].unique()),
            'category': 'Campaigns'
        })
        
        kpi_df = pd.DataFrame(kpi_data)
        kpi_df.to_csv('powerbi_chart10_kpi_dashboard.csv', index=False)
        print(f"Saved powerbi_chart10_kpi_dashboard.csv with {len(kpi_df)} rows")
        
        return kpi_df
    
    def create_powerbi_data_model(self):
        """Create a comprehensive data model for Power BI"""
        print("Creating Power BI data model...")
        
        # Load all datasets
        self.load_all_datasets()
        
        # Prepare all charts
        charts = {
            'chart1_traffic_overview': self.prepare_chart_1_traffic_overview(),
            'chart2_geographic_performance': self.prepare_chart_2_geographic_performance(),
            'chart3_campaign_performance': self.prepare_chart_3_campaign_performance(),
            'chart4_conversion_funnel': self.prepare_chart_4_conversion_funnel(),
            'chart5_device_performance': self.prepare_chart_5_device_performance(),
            'chart6_seo_keywords': self.prepare_chart_6_seo_keyword_rankings(),
            'chart7_social_media': self.prepare_chart_7_social_media_performance(),
            'chart8_competitor_analysis': self.prepare_chart_8_competitor_analysis(),
            'chart9_revenue_trends': self.prepare_chart_9_revenue_trends(),
            'chart10_kpi_dashboard': self.prepare_chart_10_kpi_dashboard()
        }
        
        # Create summary
        summary = {
            'charts_prepared': len(charts),
            'total_files': len(charts),
            'files_created': [f'powerbi_{name}.csv' for name in charts.keys()],
            'chart_descriptions': {
                'chart1_traffic_overview': 'Website Traffic Overview - Line Chart',
                'chart2_geographic_performance': 'Geographic Performance - Map/Bar Chart',
                'chart3_campaign_performance': 'Campaign Performance - Bar Chart',
                'chart4_conversion_funnel': 'Conversion Funnel - Funnel Chart',
                'chart5_device_performance': 'Device Performance - Pie/Bar Chart',
                'chart6_seo_keywords': 'SEO Keyword Rankings - Line Chart',
                'chart7_social_media': 'Social Media Performance - Bar Chart',
                'chart8_competitor_analysis': 'Competitor Analysis - Bar Chart',
                'chart9_revenue_trends': 'Revenue Trends - Line Chart',
                'chart10_kpi_dashboard': 'KPI Dashboard - Cards/Gauges'
            }
        }
        
        with open('powerbi_data_summary.json', 'w') as f:
            json.dump(summary, f, indent=2, default=str)
        
        print("\nPower BI data preparation complete!")
        print("Files created for Power BI:")
        for name, desc in summary['chart_descriptions'].items():
            print(f"  - powerbi_{name}.csv: {desc}")
        print("  - powerbi_data_summary.json")
        
        return charts

if __name__ == "__main__":
    preparer = PowerBIDataPreparation()
    charts = preparer.create_powerbi_data_model() 