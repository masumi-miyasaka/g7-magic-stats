import pandas as pd
import wbgapi as wb

countries = ['US', 'GB', 'FR', 'DE', 'IT', 'CA', 'JP']
indicators = {
    'FP.CPI.TOTL.ZG': 'Inflation',
    'NY.GDP.MKTP.CD': 'Nominal_GDP',
    'GC.TAX.TOTL.GD.ZS': 'Tax_Revenue'
}

start_year = 2015
end_year = 2025

print("データを取得中...")

try:
    df = wd.data.DataFrame(indicators.keys(), countries, mr=10)
    df = df.reset_index()
    df['series'] = df['series'].map(indicators)
    df.to_csv('g7_economic_data.csv', index=False)
    print("成功！ 'g7_economic_data.csv' に保存されました。")
    print(df.head()) 

except Exception as e:
    print(f"エラーが出たよ: {e}")