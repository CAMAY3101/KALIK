"""
Author: Gilberto Ramos Salinas 
Project: Sentiment Analisys For CryptoCurrency Forecasting 
app: Data Transformation
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


"""
The main porpuse of this program is to transform the data into only one csv file by using the data from the carpet /BinanceData 
each csv file in here is inside of a zip folder called in the next way:
XRPETH-1d-2019-09.zip 
XRPETH-1d-2019-10.zip
XRPETH-1d-2019-11.zip
XRPETH-1d-2019-12.zip
XRPETH-1d-2020-01.zip
XRPETH-1d-2020-02.zip
XRPETH-1d-2020-03.zip
XRPETH-1d-2020-04.zip
XRPETH-1d-2020-05.zip
and so on...

inside of each zip folder there is a csv file called in the next way:
XRPETH-1d-2019-09.csv
XRPETH-1d-2019-10.csv
XRPETH-1d-2019-11.csv
XRPETH-1d-2019-12.csv
XRPETH-1d-2020-01.csv
XRPETH-1d-2020-02.csv
XRPETH-1d-2020-03.csv
XRPETH-1d-2020-04.csv
XRPETH-1d-2020-05.csv
and so on...

so the program will read each csv file and will transform it into a pandas dataframe and then will concatenate all the dataframes into one dataframe
"""

#The first step is to get the csv from the zip folder
#The second step is to transform the csv into a pandas dataframe
#The third step is to concatenate all the dataframes into one dataframe

#import the necessary libraries to extract the csv from the zip folder
import zipfile
import os

#get the csv from the zip folder that is inside of the carpet /BinanceData
def get_data_from_zip(zip_file):
    #get the current working directory
    cwd = os.getcwd()
    #get the path of the zip folder
    zip_path = os.path.join(cwd, 'BinanceData', zip_file)
    #get the path of the csv file
    csv_path = os.path.join(cwd, 'BinanceData', zip_file[:-4] + '.csv')
    #extract the csv file from the zip folder
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(cwd + '/BinanceData')
    #return the path of the csv file
    return csv_path

#concatenate the dataframes into one dataframe
#In order to get de date fromo the csv file we must open the csv file to get the date
#For example: XRPETH-1d-2019-09.csv the date is 2019-09 and the rows are the data from the month of september
# The row 0 is the first day of the month and the row 30 is the last day of the month
#The date is the same for all the rows in the csv file
#The date must be in Timestamp format
#The date must be the index of the dataframe
#The date must be the first column of the dataframe
#The date must be in the format YYYY-MM-DD

def concatenate_dataframe(csv_path, names):
    #define the date of the csv file
    date = csv_path[-11:-4]
    # print(date)
    #dependinf of the month the number of days is different so lets create a dictionary with the number of days of each month
    days = {'01':31, '02':28, '03':31, '04':30, '05':31, '06':30, '07':31, '08':31, '09':30, '10':31, '11':30, '12':31}
    #for other years the number of days of february is 29
    if date[0:4] == '2020':
        days['02'] = 29

    #put the csv data into a pandas dataframe
    df = pd.read_csv(csv_path, names=names)
    #add the col at the beginning of the dataframe called date
    #The values of the col date are the days of the month
    #For example as we know date is 2019-09 we can write 2019-09-01, 2019-09-02, 2019-09-03, 
    # 2019-09-04, 2019-09-05, 2019-09-06, 2019-09-07, 2019-09-08, 2019-09-09, 2019-09-10, 2019-09-11, 2019-09-12, 2019-09-13,
    #  2019-09-14, 2019-09-15, 2019-09-16, 2019-09-17, 2019-09-18, 2019-09-19, 2019-09-20, 2019-09-21, 2019-09-22, 2019-09-23, 
    # 2019-09-24, 2019-09-25, 2019-09-26, 2019-09-27, 2019-09-28, 2019-09-29, 2019-09-30 depending on the number of days of the month 

    #create a list with the days of the month
    days_list = []
    for i in range(1, days[date[5:7]] + 1):
        if i < 10:
            days_list.append(date + '-0' + str(i))
        else:
            days_list.append(date + '-' + str(i))

    #add the col date to the dataframe
    df['date'] = days_list
    #set the date as the index of the dataframe
    df.set_index('date', inplace=True)
    #return the dataframe
    return df


def add_dataframe(df,csv_path,names):
    df2 = concatenate_dataframe(csv_path, names)
    df = pd.concat([df, df2])
    return df


def convert_to_csv(df):
    df.to_csv('Binance.csv')

def file_Iterator(): # return a list of all the files in the directory with the extension .zip and .csv
    #get the current working directory
    cwd = os.getcwd()
    #get the path of the carpet /BinanceData
    path = os.path.join(cwd, 'BinanceData')
    #get the list of the files in the carpet /BinanceData
    files = os.listdir(path)
    #create a list of the zip files
    zip_files = []
    #create a list of the csv files
    csv_files = []
    #iterate over the files to get the zip files and the csv files
    for file in files:
        if file[-3:] == 'zip':
            zip_files.append(file)
        elif file[-3:] == 'csv':
            csv_files.append(file)
    #return the lists of the zip files and the csv files
    return zip_files, csv_files 

def decompress_zip():#decompress the zip files
    #get the current working directory
    cwd = os.getcwd()
    #get the path of the carpet /BinanceData
    path = os.path.join(cwd, 'BinanceData')
    #get the list of the files in the carpet /BinanceData
    files = os.listdir(path)
    #create a list of the zip files
    for file in files:
        if file[-3:] == 'zip':
            get_data_from_zip(file)
        
def main():
    csv = get_data_from_zip('XRPETH-1d-2019-10.zip')
    zip_names, csv_names = file_Iterator()
    #define the names of the columns of the dataframe
    names = ['open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'num_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore']
    #create an empty dataframe with the names of the columns
    df = concatenate_dataframe(csv, names)
    #iterate over the zip files to get the csv files
    for zip_file in zip_names:
        csv_path = get_data_from_zip(zip_file)
        df = add_dataframe(df, csv_path, names)
    #convert the dataframe to csv
    convert_to_csv(df)
main()