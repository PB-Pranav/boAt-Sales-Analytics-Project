"""
Boat Sales Project - Data Loader

Purpose: 
This script loads raw and cleaned CSV datasets for the Boat Sales analysis project.

Usage:
    from data_loader import load_raw, load_cleaned
    
    # Load raw data
    sales, channels, products, customers, delivery = load_raw()
    
    # Load cleaned data
    sales, channels, products, customers, delivery = load_cleaned()
"""
import pandas as pd

RAW   = r"C:\Users\Hello\Downloads\project\BoatSalesProject\data\raw"
CLEAN = r"C:\Users\Hello\Downloads\project\BoatSalesProject\data\cleaned"

def load_raw():
    sales     = pd.read_csv(f"{RAW}\\Sales_data.csv")           
    channels  = pd.read_csv(f"{RAW}\\Sales_Channel.csv")    
    products  = pd.read_csv(f"{RAW}\\Product_Details.csv")     
    customers = pd.read_csv(f"{RAW}\\Customer_Details.csv")    
    delivery  = pd.read_csv(f"{RAW}\\Delivery_Partner_Data.csv") 
    return sales, channels, products, customers, delivery

def load_cleaned():
    sales     = pd.read_csv(f"{CLEAN}\\Sales_Data.csv")        
    customers = pd.read_csv(f"{CLEAN}\\Customer_Details.csv")   
    channels  = pd.read_csv(f"{RAW}\\Sales_Channel.csv")        
    products  = pd.read_csv(f"{RAW}\\Product_Details.csv")     
    delivery  = pd.read_csv(f"{RAW}\\Delivery_Partner_Data.csv") 
    return sales, channels, products, customers, delivery
