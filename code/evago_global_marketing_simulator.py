import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import json
import os

class EvagoGlobalMarketingSimulator:
    def __init__(self):
        self.start_date = datetime(2023, 1, 1)
        self.end_date = datetime(2024, 12, 31)
        self.date_range = pd.date_range(start=self.start_date, end=self.end_date, freq='D')
        
        # EVAGO's actual global presence
        self.locations = {
            'Germany': {
                'cities': ['Berlin', 'Hamburg', 'Munich', 'Frankfurt', 'Cologne'],
                'type': 'Primary Market',
                'mojo_integration': True
            },
            'Netherlands': {
                'cities': ['Amsterdam', 'Rotterdam', 'The Hague'],
                'type': 'Primary Market',
                'mojo_integration': True
            },
            'England': {
                'cities': ['London', 'Manchester'],
                'type': 'Primary Market',
                'mojo_integration': True
            },
            'North America': {
                'cities': ['New York', 'Los Angeles', 'Toronto', 'Vancouver'],
                'type': 'Expansion Market',
                'mojo_integration': False
            },
            'Australia': {
                'cities': ['Sydney', 'Melbourne', 'Brisbane'],
                'type': 'Expansion Market',
                'mojo_integration': False
            },
            'Croatia': {
                'cities': ['Zagreb', 'Split', 'Rijeka'],
                'type': 'Primary Market',
                'mojo_integration': True
            }
        }
        
        # Distribution offices worldwide
        self.distribution_offices = [
            'Singapore', 'Dubai', 'Hong Kong', 'Tokyo', 'Mumbai',
            'São Paulo', 'Mexico City', 'Cape Town', 'Stockholm', 'Warsaw',
            'Prague', 'Vienna'
        ]
        
        # EVAGO + Mojo Rental campaigns
        self.campaigns = [
            # EVAGO Original Campaigns
            'EVAGO Event Infrastructure', 'EVAGO Crowd Control', 'EVAGO Construction Safety',
            'EVAGO Festival Equipment', 'EVAGO Corporate Events', 'EVAGO Sports Events',
            
            # Mojo Rental Integration Campaigns
            'Mojo-EVAGO Joint Events', 'Mojo Equipment Integration', 'EVAGO-Mojo Partnership',
            'Unified Rental Solutions', 'Mojo Legacy Support', 'EVAGO-Mojo Brand Transition'
        ]
        
        # Comprehensive keywords including Mojo terms
        self.keywords = [
            # EVAGO Keywords
            'Absperrgitter mieten', 'event barrier hire', 'crowd control barriers',
            'festival fencing', 'construction barriers', 'safety barriers',
            'event infrastructure', 'temporary fencing', 'barrier rental',
            'crowd management', 'event security', 'temporary barriers',
            
            # Mojo Rental Keywords
            'mojo rental', 'mojo event equipment', 'mojo barrier hire',
            'mojo crowd control', 'mojo festival equipment', 'mojo construction barriers',
            
            # Combined Keywords
            'evago mojo rental', 'evago mojo barriers', 'evago mojo events',
            'unified event rental', 'evago mojo partnership', 'mojo evago integration'
        ]
        
        # Ad groups for comprehensive coverage
        self.ad_groups = [
            'EVAGO Barrier Rental', 'EVAGO Event Safety', 'EVAGO Crowd Control',
            'EVAGO Construction Barriers', 'EVAGO Festival Equipment',
            'Mojo Equipment', 'Mojo Event Rental', 'Mojo Crowd Control',
            'EVAGO-Mojo Partnership', 'Unified Rental Solutions'
        ]
        
        # Mojo acquisition date (simulated)
        self.mojo_acquisition_date = datetime(2023, 6, 1)
        
    def generate_google_analytics_data(self):
        """Generate Google Analytics data with global presence"""
        data = []
        
        for date in self.date_range:
            for country, info in self.locations.items():
                for city in info['cities']:
                    # Simulate realistic traffic patterns
                    base_traffic = random.randint(50, 800)
                    weekend_boost = 1.4 if date.weekday() >= 5 else 1.0
                    seasonal_boost = 1.6 if date.month in [6, 7, 8] else 1.0  # Summer boost
                    
                    # Mojo integration boost after acquisition
                    mojo_boost = 1.3 if date >= self.mojo_acquisition_date and info['mojo_integration'] else 1.0
                    
                    sessions = int(base_traffic * weekend_boost * seasonal_boost * mojo_boost * random.uniform(0.8, 1.2))
                    users = int(sessions * random.uniform(0.7, 0.9))
                    pageviews = int(sessions * random.uniform(1.5, 3.0))
                    bounce_rate = random.uniform(0.3, 0.7)
                    avg_session_duration = random.uniform(60, 300)
                    
                    # Organic traffic simulation
                    organic_traffic = int(sessions * random.uniform(0.4, 0.6))
                    paid_traffic = sessions - organic_traffic
                    
                    data.append({
                        'date': date,
                        'country': country,
                        'city': city,
                        'location_type': info['type'],
                        'mojo_integration': info['mojo_integration'],
                        'sessions': sessions,
                        'users': users,
                        'pageviews': pageviews,
                        'bounce_rate': bounce_rate,
                        'avg_session_duration': avg_session_duration,
                        'organic_traffic': organic_traffic,
                        'paid_traffic': paid_traffic,
                        'conversion_rate': random.uniform(0.01, 0.05),
                        'revenue': sessions * random.uniform(10, 50)
                    })
        
        return pd.DataFrame(data)
    
    def generate_google_ads_data(self):
        """Generate Google Ads performance data with Mojo integration"""
        data = []
        
        for date in self.date_range:
            for campaign in self.campaigns:
                for ad_group in self.ad_groups:
                    for country, info in self.locations.items():
                        # Simulate realistic ad performance
                        impressions = random.randint(1000, 15000)
                        clicks = int(impressions * random.uniform(0.01, 0.05))
                        cost = clicks * random.uniform(1.5, 4.0)
                        conversions = int(clicks * random.uniform(0.02, 0.08))
                        revenue = conversions * random.uniform(50, 200)
                        
                        # Mojo campaigns performance boost
                        if 'mojo' in campaign.lower() and date >= self.mojo_acquisition_date:
                            revenue *= 1.2
                            conversions = int(conversions * 1.15)
                        
                        data.append({
                            'date': date,
                            'campaign': campaign,
                            'ad_group': ad_group,
                            'country': country,
                            'impressions': impressions,
                            'clicks': clicks,
                            'cost': cost,
                            'conversions': conversions,
                            'revenue': revenue,
                            'ctr': clicks / impressions if impressions > 0 else 0,
                            'cpc': cost / clicks if clicks > 0 else 0,
                            'conversion_rate': conversions / clicks if clicks > 0 else 0,
                            'roas': revenue / cost if cost > 0 else 0,
                            'is_mojo_campaign': 'mojo' in campaign.lower()
                        })
        
        return pd.DataFrame(data)
    
    def generate_seo_keyword_data(self):
        """Generate comprehensive SEO keyword data with country breakdown (relevant and common keywords)"""
        data = []
        # Define keyword-country mapping
        german_keywords = [
            'absperrgitter mieten', 'veranstaltungsinfrastruktur', 'bühnenbarrikaden',
            'eventausstattung', 'sicherheitszäune', 'temporäre zäune', 'gitterzaun verleih',
            'crowd management', 'festivalzaun', 'bodenschutzsysteme'
        ]
        dutch_keywords = [
            'dranghek huren', 'evenementen infrastructuur', 'podium barrières',
            'tijdelijke afrastering', 'festival hekwerk', 'verhuur evenementenmateriaal',
            'menigtebeheer', 'grondbescherming'
        ]
        english_keywords = [
            'event barrier hire', 'crowd control barriers', 'stage barricades',
            'temporary fencing', 'event infrastructure', 'ground protection',
            'barrier rental', 'crowd management', 'festival fencing', 'safety barriers'
        ]
        croatian_keywords = [
            'najam barijera', 'infrastruktura događanja', 'pozornica barijere',
            'privremene ograde', 'najam opreme za događanja', 'upravljanje publikom',
            'zaštitne ograde', 'podna zaštita'
        ]
        # Mojo/brand keywords (appear in all markets)
        brand_keywords = [
            'mojo rental', 'mojo barriers', 'terraplas rental', 'entertee hire',
            'no fuss event hire', 'talos infrastructure', 'evago group', 'unified event rental'
        ]
        # Common universal keywords for all markets
        common_keywords = [
            'event infrastructure', 'event equipment rental', 'crowd management',
            'temporary fencing', 'event safety', 'event logistics', 'event solutions',
            'event supplier', 'event support', 'event planning'
        ]
        for date in self.date_range:
            for country, info in self.locations.items():
                # Assign keywords by country
                if country == 'Germany':
                    keywords = german_keywords + brand_keywords + common_keywords
                elif country == 'Netherlands':
                    keywords = dutch_keywords + brand_keywords + common_keywords
                elif country in ['England', 'North America', 'Australia']:
                    keywords = english_keywords + brand_keywords + common_keywords
                elif country == 'Croatia':
                    keywords = croatian_keywords + brand_keywords + common_keywords
                else:
                    keywords = brand_keywords + common_keywords
                for keyword in set(keywords):
                    # Simulate keyword rankings and performance
                    base_ranking = random.randint(1, 50)
                    # Mojo/brand keywords get boost after acquisition
                    if any(brand in keyword.lower() for brand in ['mojo', 'terraplas', 'entertee', 'no fuss', 'talos', 'evago']):
                        if date >= self.mojo_acquisition_date:
                            base_ranking = max(1, base_ranking - 5)
                    ranking = max(1, base_ranking + random.randint(-3, 3))
                    search_volume = random.randint(100, 8000)
                    clicks = int(search_volume * (1 / ranking) * random.uniform(0.1, 0.4))
                    impressions = int(search_volume * random.uniform(0.5, 1.5))
                    ctr = clicks / impressions if impressions > 0 else 0
                    organic_traffic = int(clicks * random.uniform(0.8, 1.2))
                    data.append({
                        'date': date,
                        'keyword': keyword,
                        'country': country,
                        'ranking': ranking,
                        'search_volume': search_volume,
                        'clicks': clicks,
                        'impressions': impressions,
                        'ctr': ctr,
                        'avg_position': ranking + random.uniform(-2, 2),
                        'organic_traffic': organic_traffic,
                        'is_mojo_keyword': 'mojo' in keyword.lower(),
                        'keyword_type': 'brand' if any(brand in keyword.lower() for brand in ['mojo', 'terraplas', 'entertee', 'no fuss', 'talos', 'evago']) else 'market'
                    })
        return pd.DataFrame(data)
    
    def generate_social_media_data(self):
        """Generate social media performance data with realistic platform differences"""
        platforms = ['Facebook', 'Instagram', 'LinkedIn', 'Twitter', 'TikTok']
        # Assign different base metrics for each platform
        platform_bases = {
            'Facebook':    {'reach': (6000, 90000), 'engagement': 0.025, 'conversion': 0.035},
            'Instagram':   {'reach': (4000, 70000), 'engagement': 0.045, 'conversion': 0.030},
            'LinkedIn':    {'reach': (2000, 30000), 'engagement': 0.020, 'conversion': 0.025},
            'Twitter':     {'reach': (3000, 40000), 'engagement': 0.015, 'conversion': 0.020},
            'TikTok':      {'reach': (5000, 80000), 'engagement': 0.060, 'conversion': 0.040},
        }
        data = []
        for date in self.date_range:
            for platform in platforms:
                for campaign in self.campaigns:
                    for country, info in self.locations.items():
                        # Use platform-specific base metrics
                        base = platform_bases[platform]
                        reach = random.randint(*base['reach'])
                        impressions = int(reach * random.uniform(1.2, 2.0))
                        engagement = int(reach * random.uniform(base['engagement'] * 0.8, base['engagement'] * 1.2))
                        clicks = int(engagement * random.uniform(0.3, 0.7))
                        conversions = int(clicks * random.uniform(base['conversion'] * 0.8, base['conversion'] * 1.2))
                        # Mojo campaigns get more engagement
                        if 'mojo' in campaign.lower() and date >= self.mojo_acquisition_date:
                            engagement = int(engagement * 1.25)
                            clicks = int(clicks * 1.2)
                        data.append({
                            'date': date,
                            'platform': platform,
                            'campaign': campaign,
                            'country': country,
                            'reach': reach,
                            'impressions': impressions,
                            'engagement': engagement,
                            'clicks': clicks,
                            'conversions': conversions,
                            'engagement_rate': engagement / reach if reach > 0 else 0,
                            'click_through_rate': clicks / impressions if impressions > 0 else 0,
                            'cost': reach * random.uniform(0.01, 0.05),
                            'is_mojo_campaign': 'mojo' in campaign.lower()
                        })
        return pd.DataFrame(data)
    
    def generate_competitor_analysis_data(self):
        """Generate country-specific competitor analysis including Mojo competitors"""
        # Define country-specific competitors
        country_competitors = {
            'Germany':      ['StagePro DE', 'EventBarriers GmbH', 'FestZaun', 'Mojo Legacy'],
            'Netherlands':  ['DutchEvents', 'BarrierRent NL', 'Mojo Legacy', 'EventMasters NL'],
            'England':      ['UK Event Hire', 'BarrierCo UK', 'Mojo Legacy', 'EventSafe UK'],
            'North America':['US Event Solutions', 'BarrierPro USA', 'Mojo Legacy', 'EventGuard NA'],
            'Australia':    ['AussieEvents', 'BarrierHire AU', 'Mojo Legacy', 'EventWorks AU'],
            'Croatia':      ['CroEvent', 'Barijere HR', 'Mojo Legacy', 'EventPlus HR'],
        }
        data = []
        for date in self.date_range:
            for country, info in self.locations.items():
                competitors = country_competitors.get(country, ['Mojo Legacy'])
                for competitor in competitors:
                    for keyword in self.keywords:
                        # Simulate competitor performance
                        base_ranking = random.randint(1, 30)
                        # Mojo Legacy performance changes after acquisition
                        if competitor == 'Mojo Legacy' and date >= self.mojo_acquisition_date:
                            base_ranking = min(base_ranking + 5, 30)  # Worse ranking
                        ranking = max(1, base_ranking + random.randint(-2, 2))
                        search_volume = random.randint(200, 4000)
                        estimated_traffic = int(search_volume * (1 / ranking) * random.uniform(0.1, 0.4))
                        data.append({
                            'date': date,
                            'competitor': competitor,
                            'keyword': keyword,
                            'country': country,
                            'ranking': ranking,
                            'search_volume': search_volume,
                            'estimated_traffic': estimated_traffic,
                            'market_share': random.uniform(0.05, 0.25),
                            'is_mojo_competitor': competitor == 'Mojo Legacy'
                        })
        return pd.DataFrame(data)
    
    def generate_campaign_performance_data(self):
        """Generate detailed campaign performance data with country field"""
        data = []
        
        for date in self.date_range:
            for campaign in self.campaigns:
                for country, info in self.locations.items():
                    # Simulate campaign metrics
                    budget = random.uniform(100, 1500)
                    spend = budget * random.uniform(0.7, 1.1)
                    impressions = random.randint(5000, 60000)
                    clicks = int(impressions * random.uniform(0.01, 0.04))
                    conversions = int(clicks * random.uniform(0.02, 0.08))
                    revenue = conversions * random.uniform(50, 250)
                    
                    # Mojo campaigns get budget boost after acquisition
                    if 'mojo' in campaign.lower() and date >= self.mojo_acquisition_date:
                        budget *= 1.3
                        spend *= 1.25
                    
                    data.append({
                        'date': date,
                        'campaign': campaign,
                        'country': country,
                        'location_type': info['type'],
                        'mojo_integration': info['mojo_integration'],
                        'budget': budget,
                        'spend': spend,
                        'impressions': impressions,
                        'clicks': clicks,
                        'conversions': conversions,
                        'revenue': revenue,
                        'ctr': clicks / impressions if impressions > 0 else 0,
                        'cpc': spend / clicks if clicks > 0 else 0,
                        'roas': revenue / spend if spend > 0 else 0,
                        'budget_utilization': spend / budget if budget > 0 else 0,
                        'is_mojo_campaign': 'mojo' in campaign.lower()
                    })
        
        return pd.DataFrame(data)
    
    def generate_conversion_funnel_data(self):
        """Generate conversion funnel data (EVAGO-appropriate stages) with country field"""
        data = []
        
        for date in self.date_range:
            for country, info in self.locations.items():
                website_visitors = random.randint(500, 4000)
                service_page_views = int(website_visitors * random.uniform(0.4, 0.7))
                contact_form_views = int(service_page_views * random.uniform(0.2, 0.5))
                contact_form_submits = int(contact_form_views * random.uniform(0.2, 0.5))
                qualified_leads = int(contact_form_submits * random.uniform(0.3, 0.7))
                project_discussions = int(qualified_leads * random.uniform(0.3, 0.7))
                contracts_signed = int(project_discussions * random.uniform(0.2, 0.5))
                
                data.append({
                    'date': date,
                    'country': country,
                    'location_type': info['type'],
                    'mojo_integration': info['mojo_integration'],
                    'website_visitors': website_visitors,
                    'service_page_views': service_page_views,
                    'contact_form_views': contact_form_views,
                    'contact_form_submits': contact_form_submits,
                    'qualified_leads': qualified_leads,
                    'project_discussions': project_discussions,
                    'contracts_signed': contracts_signed
                })
        
        return pd.DataFrame(data)
    
    def generate_device_performance_data(self):
        """Generate device performance data with country field and realistic device splits"""
        devices = ['Desktop', 'Mobile', 'Tablet']
        device_shares = {'Desktop': 0.35, 'Mobile': 0.55, 'Tablet': 0.10}
        conversion_rates = {'Desktop': 0.045, 'Mobile': 0.025, 'Tablet': 0.015}
        avg_revenue = {'Desktop': 120, 'Mobile': 80, 'Tablet': 60}
        data = []
        
        for date in self.date_range:
            for country, info in self.locations.items():
                total_sessions = random.randint(1000, 6000)
                for device in devices:
                    sessions = int(total_sessions * device_shares[device] * random.uniform(0.9, 1.1))
                    conversions = int(sessions * conversion_rates[device] * random.uniform(0.8, 1.2))
                    revenue = conversions * avg_revenue[device] * random.uniform(0.8, 1.2)
                    bounce_rate = random.uniform(0.3, 0.7)
                    data.append({
                        'date': date,
                        'device': device,
                        'country': country,
                        'location_type': info['type'],
                        'sessions': sessions,
                        'conversions': conversions,
                        'revenue': revenue,
                        'bounce_rate': bounce_rate,
                        'avg_session_duration': random.uniform(60, 300),
                        'mojo_integration': info['mojo_integration']
                    })
        
        return pd.DataFrame(data)
    
    def generate_geographic_performance_data(self):
        """Generate geographic performance data"""
        data = []
        
        for date in self.date_range:
            for country, info in self.locations.items():
                # Simulate geographic performance
                impressions = random.randint(2000, 25000)
                clicks = int(impressions * random.uniform(0.01, 0.05))
                conversions = int(clicks * random.uniform(0.02, 0.08))
                revenue = conversions * random.uniform(40, 200)
                cost = clicks * random.uniform(1.5, 4.0)
                
                # Mojo integration boost
                if info['mojo_integration'] and date >= self.mojo_acquisition_date:
                    revenue *= 1.15
                    conversions = int(conversions * 1.1)
                
                data.append({
                    'date': date,
                    'country': country,
                    'location_type': info['type'],
                    'impressions': impressions,
                    'clicks': clicks,
                    'conversions': conversions,
                    'revenue': revenue,
                    'cost': cost,
                    'ctr': clicks / impressions if impressions > 0 else 0,
                    'conversion_rate': conversions / clicks if clicks > 0 else 0,
                    'roas': revenue / cost if cost > 0 else 0,
                    'mojo_integration': info['mojo_integration']
                })
        
        return pd.DataFrame(data)
    
    def generate_time_series_data(self):
        """Generate time series data for trend analysis"""
        data = []
        
        for date in self.date_range:
            # Simulate overall business metrics over time
            base_traffic = 1000 + (date - self.start_date).days * 3  # Growing trend
            seasonal_factor = 1 + 0.3 * np.sin(2 * np.pi * date.timetuple().tm_yday / 365)
            
            # Mojo acquisition boost
            mojo_boost = 1.2 if date >= self.mojo_acquisition_date else 1.0
            
            total_traffic = int(base_traffic * seasonal_factor * mojo_boost * random.uniform(0.8, 1.2))
            total_conversions = int(total_traffic * random.uniform(0.02, 0.06))
            total_revenue = total_conversions * random.uniform(80, 180)
            avg_order_value = total_revenue / total_conversions if total_conversions > 0 else 0
            
            # Organic vs Paid traffic
            organic_traffic = int(total_traffic * random.uniform(0.4, 0.6))
            paid_traffic = total_traffic - organic_traffic
            
            data.append({
                'date': date,
                'total_traffic': total_traffic,
                'organic_traffic': organic_traffic,
                'paid_traffic': paid_traffic,
                'total_conversions': total_conversions,
                'total_revenue': total_revenue,
                'avg_order_value': avg_order_value,
                'conversion_rate': total_conversions / total_traffic if total_traffic > 0 else 0,
                'revenue_per_visitor': total_revenue / total_traffic if total_traffic > 0 else 0,
                'mojo_integration_active': date >= self.mojo_acquisition_date
            })
        
        return pd.DataFrame(data)
    
    def generate_mojo_acquisition_impact_data(self):
        """Generate specific data showing Mojo acquisition impact"""
        data = []
        
        for date in self.date_range:
            # Pre and post acquisition metrics
            is_post_acquisition = date >= self.mojo_acquisition_date
            
            # Simulate acquisition impact
            base_metrics = {
                'total_revenue': random.uniform(50000, 150000),
                'total_customers': random.randint(200, 800),
                'market_share': random.uniform(0.15, 0.35),
                'brand_awareness': random.uniform(0.25, 0.55),
                'customer_satisfaction': random.uniform(0.7, 0.95)
            }
            
            if is_post_acquisition:
                # Post-acquisition improvements
                for key in base_metrics:
                    if key in ['total_revenue', 'total_customers', 'market_share']:
                        base_metrics[key] *= random.uniform(1.2, 1.5)
                    else:
                        base_metrics[key] *= random.uniform(1.05, 1.15)
            
            data.append({
                'date': date,
                'is_post_acquisition': is_post_acquisition,
                'total_revenue': base_metrics['total_revenue'],
                'total_customers': base_metrics['total_customers'],
                'market_share': base_metrics['market_share'],
                'brand_awareness': base_metrics['brand_awareness'],
                'customer_satisfaction': base_metrics['customer_satisfaction'],
                'acquisition_impact_score': random.uniform(0.8, 1.6) if is_post_acquisition else 1.0
            })
        
        return pd.DataFrame(data)
    
    def generate_all_data(self):
        """Generate all datasets and save them"""
        print("Generating comprehensive EVAGO global marketing data...")
        print(f"Including Mojo Rental acquisition impact from {self.mojo_acquisition_date.date()}")
        
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
            'time_series': self.generate_time_series_data(),
            'mojo_acquisition_impact': self.generate_mojo_acquisition_impact_data()
        }
        
        # Create data directory if it doesn't exist
        os.makedirs('data', exist_ok=True)
        
        # Save each dataset
        for name, df in datasets.items():
            filename = f'data/evago_{name}_data.csv'
            df.to_csv(filename, index=False)
            print(f"Saved {filename} with {len(df)} rows")
        
        # Create a comprehensive summary file
        summary = {
            'datasets_generated': len(datasets),
            'date_range': f"{self.start_date.date()} to {self.end_date.date()}",
            'total_records': sum(len(df) for df in datasets.values()),
            'files_created': list(datasets.keys()),
            'evago_locations': self.locations,
            'distribution_offices': self.distribution_offices,
            'mojo_acquisition_date': self.mojo_acquisition_date.isoformat(),
            'campaigns': self.campaigns,
            'keywords': self.keywords,
            'seo_sea_metrics_covered': [
                'CTR (Click-Through Rate)',
                'KPIs (Key Performance Indicators)',
                'Organic Traffic',
                'Click-through Rates',
                'Keyword Performance',
                'ROAS (Return on Ad Spend)',
                'CPC (Cost Per Click)',
                'Conversion Rates',
                'Bounce Rate',
                'Session Duration',
                'Market Share',
                'Brand Awareness'
            ]
        }
        
        with open('data/evago_global_data_summary.json', 'w') as f:
            json.dump(summary, f, indent=2, default=str)
        
        print(f"\nData generation complete! Generated {summary['total_records']} total records.")
        print("Files created in data/ directory:")
        for name in datasets.keys():
            print(f"  - evago_{name}_data.csv")
        print("  - evago_global_data_summary.json")
        
        return datasets

if __name__ == "__main__":
    simulator = EvagoGlobalMarketingSimulator()
    datasets = simulator.generate_all_data() 