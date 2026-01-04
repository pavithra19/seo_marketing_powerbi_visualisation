import pandas as pd
import json

def preview_data():
    """Preview all generated datasets"""
    print("=" * 60)
    print("EVAGO MARKETING DATA PREVIEW")
    print("=" * 60)
    
    # Power BI optimized files
    powerbi_files = [
        'powerbi_chart1_traffic_overview.csv',
        'powerbi_chart2_geographic_performance.csv', 
        'powerbi_chart3_campaign_performance.csv',
        'powerbi_chart4_conversion_funnel.csv',
        'powerbi_chart5_device_performance.csv',
        'powerbi_chart6_seo_keywords.csv',
        'powerbi_chart7_social_media.csv',
        'powerbi_chart8_competitor_analysis.csv',
        'powerbi_chart9_revenue_trends.csv',
        'powerbi_chart10_kpi_dashboard.csv'
    ]
    
    print("\n📊 POWER BI OPTIMIZED DATASETS:")
    print("-" * 40)
    
    for i, file in enumerate(powerbi_files, 1):
        try:
            df = pd.read_csv(file)
            print(f"\n{i}. {file}")
            print(f"   Rows: {len(df)} | Columns: {len(df.columns)}")
            print(f"   Date Range: {df['date'].min()} to {df['date'].max()}")
            print(f"   Sample columns: {list(df.columns[:5])}")
            
            # Show first few rows
            print("   Sample data:")
            print(df.head(2).to_string(index=False))
            print()
            
        except Exception as e:
            print(f"Error reading {file}: {e}")
    
    # Show summary files
    print("\n📋 SUMMARY FILES:")
    print("-" * 20)
    
    try:
        with open('powerbi_data_summary.json', 'r') as f:
            summary = json.load(f)
        
        print(f"Charts prepared: {summary['charts_prepared']}")
        print(f"Total files: {summary['total_files']}")
        print("\nChart descriptions:")
        for name, desc in summary['chart_descriptions'].items():
            print(f"  - {name}: {desc}")
            
    except Exception as e:
        print(f"Error reading summary: {e}")
    
    print("\n" + "=" * 60)
    print("🎯 NEXT STEPS FOR POWER BI:")
    print("=" * 60)
    print("1. Open Power BI Desktop")
    print("2. Import each 'powerbi_chart*.csv' file")
    print("3. Create relationships between datasets")
    print("4. Build the 10 charts as described in README.md")
    print("5. Arrange charts in a dashboard layout")
    print("6. Add filters and slicers for interactivity")
    print("\n📁 All files are ready for Power BI import!")

if __name__ == "__main__":
    preview_data() 