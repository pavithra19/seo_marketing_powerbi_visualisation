import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import json
import os

class EvagoFlexiblePartnerSimulator:
    def __init__(self):
        self.start_date = datetime(2023, 1, 1)
        self.end_date = datetime(2024, 12, 31)
        self.date_range = pd.date_range(start=self.start_date, end=self.end_date, freq='D')
        
        # EVAGO's actual global presence
        self.locations = {
            'Germany': {
                'cities': ['Berlin', 'Hamburg', 'Munich', 'Frankfurt', 'Cologne'],
                'type': 'Primary Market',
                'partners': ['Local Partner A', 'Local Partner B'],
                'keywords_lang': 'de'
            },
            'Netherlands': {
                'cities': ['Amsterdam', 'Rotterdam', 'The Hague'],
                'type': 'Primary Market',
                'partners': ['Dutch Partner X', 'Dutch Partner Y'],
                'keywords_lang': 'nl'
            },
            'England': {
                'cities': ['London', 'Manchester'],
                'type': 'Primary Market',
                'partners': ['UK Partner 1', 'UK Partner 2'],
                'keywords_lang': 'en'
            },
            'North America': {
                'cities': ['New York', 'Los Angeles', 'Toronto', 'Vancouver'],
                'type': 'Expansion Market',
                'partners': ['NA Partner Alpha', 'NA Partner Beta'],
                'keywords_lang': 'en'
            },
            'Australia': {
                'cities': ['Sydney', 'Melbourne', 'Brisbane'],
                'type': 'Expansion Market',
                'partners': ['AUS Partner One', 'AUS Partner Two'],
                'keywords_lang': 'en'
            }
        }
        
        # Distribution offices worldwide
        self.distribution_offices = [
            'Singapore', 'Dubai', 'Hong Kong', 'Tokyo', 'Mumbai',
            'São Paulo', 'Mexico City', 'Cape Town', 'Stockholm', 'Warsaw',
            'Prague', 'Vienna'
        ]
        
        # Flexible campaign structure
        self.campaigns = [
            # Core EVAGO Campaigns
            'EVAGO Event Infrastructure', 'EVAGO Crowd Control', 'EVAGO Construction Safety',
            'EVAGO Festival Equipment', 'EVAGO Corporate Events', 'EVAGO Sports Events',
            
            # Partner Integration Campaigns (flexible)
            'Partner Joint Events', 'Partner Equipment Integration', 'EVAGO-Partner Partnership',
            'Unified Rental Solutions', 'Partner Support', 'EVAGO-Partner Brand Transition'
        ]
        
        # Multi-language keywords
        self.keywords = {
            'de': [  # German
                'Absperrgitter mieten', 'Veranstaltungsbarrieren', 'Crowd Control Barrieren',
                'Festival Absperrungen', 'Bauabsperrungen', 'Sicherheitsbarrieren',
                'Event Infrastruktur', 'Temporäre Zäune', 'Barrieren Vermietung',
                'Menschenmengen Management', 'Event Sicherheit', 'Temporäre Barrieren'
            ],
            'nl': [  # Dutch
                'afzettingen huren', 'evenement barrières', 'crowd control barrières',
                'festival afzettingen', 'bouwafzettingen', 'veiligheidsbarrières',
                'evenement infrastructuur', 'tijdelijke hekken', 'barrières verhuur',
                'menigte beheer', 'evenement beveiliging', 'tijdelijke barrières'
            ],
            'en': [  # English
                'event barrier hire', 'crowd control barriers', 'festival fencing',
                'construction barriers', 'safety barriers', 'event infrastructure',
                'temporary fencing', 'barrier rental', 'crowd management',
                'event security', 'temporary barriers', 'event equipment hire'
            ]
        }
        
        # Ad groups for comprehensive coverage
        self.ad_groups = [
            'EVAGO Barrier Rental', 'EVAGO Event Safety', 'EVAGO Crowd Control',
            'EVAGO Construction Barriers', 'EVAGO Festival Equipment',
            'Partner Equipment', 'Partner Event Rental', 'Partner Crowd Control',
            'EVAGO-Partner Partnership', 'Unified Rental Solutions'
        ]
        
        # Flexible partner integration date (can be customized)
        self.partner_integration_date = datetime(2023, 6, 1)
        
    def get_keywords_for_country(self, country):
        """Get appropriate keywords for each country"""
        lang = self.locations[country]['keywords_lang']
        return self.keywords[lang]
    
    def generate_google_analytics_data(self):
        """Generate Google Analytics data with flexible partner integration"""
        data = []
        
        for date in self.date_range:
            for country, info in self.locations.items():
                for city in info['cities']:
                    # Simulate realistic traffic patterns
                    base_traffic = random.randint(50, 800)
                    weekend_boost = 1.4 if date.weekday() >= 5 else 1.0
                    seasonal_boost = 1.6 if date.month in [6, 7, 8] else 1.0  # Summer boost
                    
                    # Partner integration boost after integration date
                    partner_boost = 1.3 if date >= self.partner_integration_date else 1.0
                    
                    sessions = int(base_traffic * weekend_boost * seasonal_boost * partner_boost * random.uniform(0.8, 1.2))
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
                        'partners': ', '.join(info['partners']),
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
    
    def generate_seo_keyword_data(self):
        """Generate SEO keyword data with proper language support"""
        data = []
        
        for date in self.date_range:
            for country, info in self.locations.items():
                keywords = self.get_keywords_for_country(country)
                for keyword in keywords:
                    # Simulate keyword rankings and performance
                    base_ranking = random.randint(1, 50)
                    ranking = max(1, base_ranking + random.randint(-3, 3))
                    search_volume = random.randint(100, 8000)
                    clicks = int(search_volume * (1 / ranking) * random.uniform(0.1, 0.4))
                    impressions = int(search_volume * random.uniform(0.5, 1.5))
                    ctr = clicks / impressions if impressions > 0 else 0
                    
                    # Organic traffic calculation
                    organic_traffic = int(clicks * random.uniform(0.8, 1.2))
                    
                    data.append({
                        'date': date,
                        'keyword': keyword,
                        'country': country,
                        'language': info['keywords_lang'],
                        'ranking': ranking,
                        'search_volume': search_volume,
                        'clicks': clicks,
                        'impressions': impressions,
                        'ctr': ctr,
                        'avg_position': ranking + random.uniform(-2, 2),
                        'organic_traffic': organic_traffic,
                        'keyword_type': 'localized'
                    })
        
        return pd.DataFrame(data)
    
    def generate_partner_performance_data(self):
        """Generate partner performance data (optional)"""
        data = []
        
        for date in self.date_range:
            for country, info in self.locations.items():
                for partner in info['partners']:
                    # Simulate partner performance
                    referrals = random.randint(10, 100)
                    conversions = int(referrals * random.uniform(0.1, 0.3))
                    revenue = conversions * random.uniform(50, 200)
                    commission_rate = random.uniform(0.05, 0.15)
                    
                    data.append({
                        'date': date,
                        'country': country,
                        'partner': partner,
                        'referrals': referrals,
                        'conversions': conversions,
                        'revenue': revenue,
                        'commission_rate': commission_rate,
                        'commission_amount': revenue * commission_rate
                    })
        
        return pd.DataFrame(data)
    
    def generate_all_data(self):
        """Generate all datasets with flexible partner approach"""
        print("Generating comprehensive EVAGO data with flexible partner integration...")
        
        # Generate core datasets
        datasets = {
            'google_analytics': self.generate_google_analytics_data(),
            'seo_keywords': self.generate_seo_keyword_data(),
            'partner_performance': self.generate_partner_performance_data()
        }
        
        # Create data directory if it doesn't exist
        os.makedirs('data/', exist_ok=True)
        
        # Save each dataset
        for name, df in datasets.items():
            filename = f'data/evago_{name}_data.csv'
            df.to_csv(filename, index=False)
            print(f"Saved {filename} with {len(df)} rows")
        
        # Create summary
        summary = {
            'datasets_generated': len(datasets),
            'date_range': f"{self.start_date.date()} to {self.end_date.date()}",
            'total_records': sum(len(df) for df in datasets.values()),
            'files_created': list(datasets.keys()),
            'evago_locations': self.locations,
            'distribution_offices': self.distribution_offices,
            'partner_integration_date': self.partner_integration_date.isoformat(),
            'campaigns': self.campaigns,
            'keywords_by_language': {lang: len(keywords) for lang, keywords in self.keywords.items()},
            'note': 'Flexible partner integration - can be customized for any partner type'
        }
        
        with open('data/evago_flexible_data_summary.json', 'w') as f:
            json.dump(summary, f, indent=2, default=str)
        
        print(f"\nData generation complete! Generated {summary['total_records']} total records.")
        print("Files created in data/ directory:")
        for name in datasets.keys():
            print(f"  - evago_{name}_data.csv")
        print("  - evago_flexible_data_summary.json")
        
        return datasets

if __name__ == "__main__":
    simulator = EvagoFlexiblePartnerSimulator()
    datasets = simulator.generate_all_data() 