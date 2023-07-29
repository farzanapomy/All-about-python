import pandas as pd
import matplotlib.pyplot as plt


download_url="E://New_folder//python//Digital Image Processing//alphabet_stock_data.csv"
df = pd.read_csv(download_url)
type(df)
pd.set_option("display.max.columns", None)
df.head()