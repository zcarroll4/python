import requests

base_url = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service"
endpoint = "/v1/accounting/od/tcir_annual_table_1?fields=record_date,fiscal_year,fiscal_year_rate&filter=record_date:gte:2024-01-01"
response = requests.get(f"{base_url}{endpoint}")

data = response.json()

print(data)