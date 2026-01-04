import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import json

class EvagoMarketingDataSimulator:
    def __init__(self):
        self.start_date = datetime(2023, 1, 1)
        self.end_date = datetime(2024, 12, 31)
        self.date_range = pd.date_range(start=self.start_date, end=self.end_date, freq='D')
        
        # EVAGO-specific data
        self.countries = ['Germany', 'Netherlands', 'Belgium', 'France', 'UK', 'Austria', 'Switzerland']
        self.campaigns = [
            'Summer Festival Campaign', 'Corporate Events Q1', 'Sports Events', 
            'Music Festivals', 'Trade Shows', 'Wedding Season', 'Holiday Events',
            'Construction Safety', 'Crowd Control', 'VIP Events'
        ]
        self.keywords = [
            'Absperrgitter mieten', 'event barrier hire', 'crowd control barriers',
            'festival fencing', 'construction barriers', 'safety barriers',
            'event infrastructure', 'temporary fencing', 'barrier rental',
            'crowd management', 'event security', 'temporary barriers'
        ]
        self.ad_groups = [
            'Barrier Rental', 'Event Safety', 'Crowd Control', 'Construction Barriers',
            'Festival Equipment', 'Corporate Events', 'Sports Events', 'Music Events'
        ]
        
    def generate_google_analytics_data(self):
        """Generate Google Analytics data for website performance"""
        data = []
        
        for date in self.date_range:
            for country in self.countries:
                # Simulate realistic traffic patterns
                base_traffic = random.randint(100, 1000)
                weekend_boost = 1.3 if date.weekday() >= 5 else 1.0
                seasonal_boost = 1.5 if date.month in [6, 7, 8] else 1.0  # Summer boost
                
                sessions = int(base_traffic * weekend_boost * seasonal_boost * random.uniform(0.8, 1.2))
                users = int(sessions * random.uniform(0.7, 0.9))
                pageviews = int(sessions * random.uniform(1.5, 3.0))
                bounce_rate = random.uniform(0.3, 0.7)
                avg_session_duration = random.uniform(60, 300)
                
                data.append({
                    'date': date,
                    'country': country,
                    'sessions': sessions,
                    'users': users,
                    'pageviews': pageviews,
                    'bounce_rate': bounce_rate,
                    'avg_session_duration': avg_session_duration,
                    'conversion_rate': random.uniform(0.01, 0.05),
                    'revenue': sessions * random.uniform(10, 50)
                })
        
        return pd.DataFrame(data)
    
    def generate_google_ads_data(self):
        """Generate Google Ads performance data"""
        data = []
        
        for date in self.date_range:
            for campaign in self.campaigns:
                for ad_group in self.ad_groups:
                    # Simulate realistic ad performance
                    impressions = random.randint(1000, 10000)
                    clicks = int(impressions * random.uniform(0.01, 0.05))
                    cost = clicks * random.uniform(1.5, 4.0)
                    conversions = int(clicks * random.uniform(0.02, 0.08))
                    revenue = conversions * random.uniform(50, 200)
                    
                    data.append({
                        'date': date,
                        'campaign': campaign,
                        'ad_group': ad_group,
                        'impressions': impressions,
                        'clicks': clicks,
                        'cost': cost,
                        'conversions': conversions,
                        'revenue': revenue,
                        'ctr': clicks / impressions if impressions > 0 else 0,
                        'cpc': cost / clicks if clicks > 0 else 0,
                        'conversion_rate': conversions / clicks if clicks > 0 else 0,
                        'roas': revenue / cost if cost > 0 else 0
                    })
        
        return pd.DataFrame(data)
    
    def generate_seo_keyword_data(self):
        """Generate SEO keyword ranking and performance data"""
        data = []
        
        for date in self.date_range:
            for keyword in self.keywords:
                for country in self.countries:
                    # Simulate keyword rankings and performance
                    ranking = random.randint(1, 50)
                    search_volume = random.randint(100, 5000)
                    clicks = int(search_volume * (1 / ranking) * random.uniform(0.1, 0.3))
                    impressions = int(search_volume * random.uniform(0.5, 1.5))
                    ctr = clicks / impressions if impressions > 0 else 0
                    
                    data.append({
                        'date': date,
                        'keyword': keyword,
                        'country': country,
                        'ranking': ranking,
                        'search_volume': search_volume,
                        'clicks': clicks,
                        'impressions': impressions,
                        'ctr': ctr,
                        'avg_position': ranking + random.uniform(-2, 2)
                    })
        
        return pd.DataFrame(data)
    
    def generate_social_media_data(self):
        """Generate social media performance data"""
        platforms = ['Facebook', 'Instagram', 'LinkedIn', 'Twitter']
        data = []
        
        for date in self.date_range:
            for platform in platforms:
                for campaign in self.campaigns:
                    # Simulate social media metrics
                    reach = random.randint(5000, 50000)
                    impressions = int(reach * random.uniform(1.2, 2.0))
                    engagement = int(reach * random.uniform(0.01, 0.05))
                    clicks = int(engagement * random.uniform(0.3, 0.7))
                    conversions = int(clicks * random.uniform(0.02, 0.06))
                    
                    data.append({
                        'date': date,
                        'platform': platform,
                        'campaign': campaign,
                        'reach': reach,
                        'impressions': impressions,
                        'engagement': engagement,
                        'clicks': clicks,
                        'conversions': conversions,
                        'engagement_rate': engagement / reach if reach > 0 else 0,
                        'cost': reach * random.uniform(0.01, 0.05)
                    })
        
        return pd.DataFrame(data)
    
    def generate_competitor_analysis_data(self):
        """Generate competitor analysis data"""
        competitors = ['Competitor A', 'Competitor B', 'Competitor C', 'Competitor D']
        data = []
        
        for date in self.date_range:
            for competitor in competitors:
                for keyword in self.keywords[:5]:  # Top 5 keywords
                    # Simulate competitor performance
                    ranking = random.randint(1, 30)
                    search_volume = random.randint(200, 3000)
                    estimated_traffic = int(search_volume * (1 / ranking) * random.uniform(0.1, 0.4))
                    
                    data.append({
                        'date': date,
                        'competitor': competitor,
                        'keyword': keyword,
                        'ranking': ranking,
                        'search_volume': search_volume,
                        'estimated_traffic': estimated_traffic,
                        'market_share': random.uniform(0.05, 0.25)
                    })
        
        return pd.DataFrame(data)
    
    def generate_conversion_funnel_data(self):
        """Generate conversion funnel data"""
        data = []
        
        for date in self.date_range:
            for country in self.countries:
                # Simulate funnel stages
                visitors = random.randint(500, 3000)
                page_views = int(visitors * random.uniform(1.5, 3.0))
                add_to_cart = int(visitors * random.uniform(0.05, 0.15))
                checkout_started = int(add_to_cart * random.uniform(0.6, 0.9))
                purchases = int(checkout_started * random.uniform(0.7, 0.95))
                
                data.append({
                    'date': date,
                    'country': country,
                    'visitors': visitors,
                    'page_views': page_views,
                    'add_to_cart': add_to_cart,
                    'checkout_started': checkout_started,
                    'purchases': purchases,
                    'conversion_rate': purchases / visitors if visitors > 0 else 0
                })
        
        return pd.DataFrame(data)
    
    def generate_device_performance_data(self):
        """Generate device performance data"""
        devices = ['Desktop', 'Mobile', 'Tablet']
        data = []
        
        for date in self.date_range:
            for device in devices:
                for country in self.countries:
                    # Simulate device-specific performance
                    sessions = random.randint(200, 2000)
                    conversions = int(sessions * random.uniform(0.01, 0.05))
                    revenue = conversions * random.uniform(30, 150)
                    bounce_rate = random.uniform(0.3, 0.7)
                    
                    data.append({
                        'date': date,
                        'device': device,
                        'country': country,
                        'sessions': sessions,
                        'conversions': conversions,
                        'revenue': revenue,
                        'bounce_rate': bounce_rate,
                        'avg_session_duration': random.uniform(60, 300)
                    })
        
        return pd.DataFrame(data)
    
    def generate_campaign_performance_data(self):
        """Generate detailed campaign performance data"""
        data = []
        
        for date in self.date_range:
            for campaign in self.campaigns:
                # Simulate campaign metrics
                budget = random.uniform(100, 1000)
                spend = budget * random.uniform(0.7, 1.1)
                impressions = random.randint(5000, 50000)
                clicks = int(impressions * random.uniform(0.01, 0.04))
                conversions = int(clicks * random.uniform(0.02, 0.08))
                revenue = conversions * random.uniform(50, 200)
                
                data.append({
                    'date': date,
                    'campaign': campaign,
                    'budget': budget,
                    'spend': spend,
                    'impressions': impressions,
                    'clicks': clicks,
                    'conversions': conversions,
                    'revenue': revenue,
                    'ctr': clicks / impressions if impressions > 0 else 0,
                    'cpc': spend / clicks if clicks > 0 else 0,
                    'roas': revenue / spend if spend > 0 else 0,
                    'budget_utilization': spend / budget if budget > 0 else 0
                })
        
        return pd.DataFrame(data)
    
    def generate_geographic_performance_data(self):
        """Generate geographic performance data"""
        data = []
        
        for date in self.date_range:
            for country in self.countries:
                # Simulate geographic performance
                impressions = random.randint(2000, 20000)
                clicks = int(impressions * random.uniform(0.01, 0.05))
                conversions = int(clicks * random.uniform(0.02, 0.08))
                revenue = conversions * random.uniform(40, 180)
                cost = clicks * random.uniform(1.5, 4.0)
                
                data.append({
                    'date': date,
                    'country': country,
                    'impressions': impressions,
                    'clicks': clicks,
                    'conversions': conversions,
                    'revenue': revenue,
                    'cost': cost,
                    'ctr': clicks / impressions if impressions > 0 else 0,
                    'conversion_rate': conversions / clicks if clicks > 0 else 0,
                    'roas': revenue / cost if cost > 0 else 0
                })
        
        return pd.DataFrame(data)
    
    def generate_time_series_data(self):
        """Generate time series data for trend analysis"""
        data = []
        
        for date in self.date_range:
            # Simulate overall business metrics over time
            base_traffic = 1000 + (date - self.start_date).days * 2  # Growing trend
            seasonal_factor = 1 + 0.3 * np.sin(2 * np.pi * date.timetuple().tm_yday / 365)
            
            total_traffic = int(base_traffic * seasonal_factor * random.uniform(0.8, 1.2))
            total_conversions = int(total_traffic * random.uniform(0.02, 0.06))
            total_revenue = total_conversions * random.uniform(80, 150)
            avg_order_value = total_revenue / total_conversions if total_conversions > 0 else 0
            
            data.append({
                'date': date,
                'total_traffic': total_traffic,
                'total_conversions': total_conversions,
                'total_revenue': total_revenue,
                'avg_order_value': avg_order_value,
                'conversion_rate': total_conversions / total_traffic if total_traffic > 0 else 0,
                'revenue_per_visitor': total_revenue / total_traffic if total_traffic > 0 else 0
            })
        
        return pd.DataFrame(data)
    
    def generate_all_data(self):
        """Generate all datasets and save them"""
        print("Generating comprehensive EVAGO marketing data...")
        
        # Generate all datasets
        datasets = {
            'google_analytics': self.generate_google_analytics_data(),
            'google_ads': self.generate_google_ads_data(),
            'seo_keywords': self.generate_seo_keyword_data(),
            'social_media': self.generate_social_media_data(),
            'competitor_analysis': self.generate_competitor_analysis_data(),
            'conversion_funnel': self.generate_conversion_funnel_data(),
            'device_performance': self.generate_device_performance_data(),
            'campaign_performance': self.generate_campaign_performance_data(),
            'geographic_performance': self.generate_geographic_performance_data(),
            'time_series': self.generate_time_series_data()
        }
        
        # Save each dataset
        for name, df in datasets.items():
            filename = f'evago_{name}_data.csv'
            df.to_csv(filename, index=False)
            print(f"Saved {filename} with {len(df)} rows")
        
        # Create a summary file
        summary = {
            'datasets_generated': len(datasets),
            'date_range': f"{self.start_date.date()} to {self.end_date.date()}",
            'total_records': sum(len(df) for df in datasets.values()),
            'files_created': list(datasets.keys())
        }
        
        with open('evago_data_summary.json', 'w') as f:
            json.dump(summary, f, indent=2, default=str)
        
        print(f"\nData generation complete! Generated {summary['total_records']} total records.")
        print("Files created:")
        for name in datasets.keys():
            print(f"  - evago_{name}_data.csv")
        print("  - evago_data_summary.json")
        
        return datasets

if __name__ == "__main__":
    simulator = EvagoMarketingDataSimulator()
    datasets = simulator.generate_all_data() 