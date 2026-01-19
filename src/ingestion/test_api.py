import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_alpha_vantage():
    """Test connection to Alpha Vantage API"""
    api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
    symbol = 'AAPL'
    
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
    
    print(f"Testing API connection for {symbol}...")
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print("✓ API Connection Successful!")
        print(f"\nSample Data for {symbol}:")
        print(data)
        return data
    else:
        print(f"✗ API Connection Failed: {response.status_code}")
        return None

if __name__ == "__main__":
    test_alpha_vantage()