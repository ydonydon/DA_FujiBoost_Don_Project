#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse.......
#Name: <Don>
#Group Name: <FujiBoost>
#Class: <PNJ>
#Date: <Feb 2021>
#Version: <->
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd
#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################

#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
  def __init__(self):

    #load excel data (CSV format) to dataframe - 'df'
    dataframe = pd.read_csv('MonthyVisitors.csv')
    #show specific country dataframe
    sortCountry(dataframe)
#########################################################################
#CLASS Branch: End of Code
#########################################################################

#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
def sortCountry(df):

  #display sorted dataframe for Europe Region 1996-2006
  print("\n\n" + "Europe region was selected.")

  #display sorted dataframe based on given year range of region (1996 - 2006)
  print("The countries in the region are shown below.")
  print(" Year range: 1996 - 2006" + "\n")
  eur_region = df.iloc[216:348, 20:31]
  df1 = df.iloc[216:348,0:2]
  result = df1.join(eur_region)
  print("Total number of countries:", str(len(result.columns) - 2) + "\n")
  print(result)

  #display the top 3 countries that visited Singapore over the span of 10 years
  print("\n" + "The Top 3 countries of visitors to Singapore from the selected region over the span of 10 years:")
  eur_finalresult = df.iloc[216:348, 20:31].sum(axis=0).sort_values(ascending=False).nlargest(3)

  print(eur_finalresult.to_string())


  return
#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':
  
  #Project Title
  print('######################################')
  print('# Data Analysis App - PYTHON Project #')
  print('######################################')

  #perform data analysis on specific excel (CSV) file
  DataAnalysis()

#########################################################################
#Main Branch: End of Code
#########################################################################