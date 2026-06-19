import pandas as pd

RAW   = r"C:\Users\Hello\Downloads\project\BoatSalesProject\data\raw"
CLEAN = r"C:\Users\Hello\Downloads\project\BoatSalesProject\data\cleaned"

def load_raw():
    sales     = pd.read_csv(f"{RAW}\\Sales_data.csv")           # exact name
    channels  = pd.read_csv(f"{RAW}\\Sales_Channel.csv")        # exact name
    products  = pd.read_csv(f"{RAW}\\Product_Details.csv")      # exact name
    customers = pd.read_csv(f"{RAW}\\Customer_Details.csv")     # exact name
    delivery  = pd.read_csv(f"{RAW}\\Delivery_Partner_Data.csv") # exact name
    return sales, channels, products, customers, delivery

def load_cleaned():
    sales     = pd.read_csv(f"{CLEAN}\\Sales_Data.csv")         # exact name
    customers = pd.read_csv(f"{CLEAN}\\Customer_Details.csv")   # exact name
    channels  = pd.read_csv(f"{RAW}\\Sales_Channel.csv")        # exact name
    products  = pd.read_csv(f"{RAW}\\Product_Details.csv")      # exact name
    delivery  = pd.read_csv(f"{RAW}\\Delivery_Partner_Data.csv") # exact name
    return sales, channels, products, customers, delivery