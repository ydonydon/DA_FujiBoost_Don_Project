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
import matplotlib.pyplot as pit
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

  # load excel data (CSV format) to dataframe - 'df'
  df = pd.read_csv('MonthyVisitors.csv')

  #Prompt Region and Year range
  regions = ['S.E.A', 'Asia-Pacific', 'South-Asia-Pacific', 'Middle East', 'Europe', 'North America', 'Australia', 'Africa']

  #Available Regions
  print(regions)
  
  #User input regions
  region = str(input('Enter a Region:'))
  print("\n\n" , regions)
  
  #Error checking for region
  while True:
    region = str(region)
    if not region in regions:
      print ("Region is invalid try again")
      break
    elif region == "S.E.A":
      sea_region = df.iloc[: ,2:9]
      df1 = df.iloc[0:479,0:2]
      result = df1.join(sea_region)
      print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
      print(result)
      break
    elif region == "Asia-Pacific":
      ap_region = df.iloc[: ,9:14]
      df1 = df.iloc[0:479,0:2]
      result = df1.join(ap_region)
      print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
      print(result)
      break
    elif region == "South-Asia-Pacific":
      sap_region = df.iloc[: ,14:17]
      df1 = df.iloc[0:479,0:2]
      result = df1.join(sap_region)
      print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
      print(result)
      break
    elif region == "Middle East":
      me_region = df.iloc[: ,17:20]
      df1 = df.iloc[0:479,0:2]
      result = df1.join(me_region)
      print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
      print(result)
      break
    elif region == "Europe":
      eur_region = df.iloc[: ,20:31]
      df1 = df.iloc[0:479,0:2]
      result = df1.join(eur_region)
      print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
      print(result)
      break
    elif region == "North America":
      na_region = df.iloc[: ,31:33]
      df1 = df.iloc[0:479,0:2]
      result = df1.join(na_region)
      print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
      print(result)
      break
    elif region == "Australia":
      aus_region = df.iloc[: ,33:35]
      df1 = df.iloc[0:479,0:2]
      result = df1.join(aus_region)
      print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
      print(result)
      break
    elif region == "Africa":
      afr_region = df.iloc[: ,35:36]
      df1 = df.iloc[0:479,0:2]
      result = df1.join(afr_region)
      print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
      print(result)
      break
    else:
      print("There is an ERROR! Please check for spelling error")
      break
      
 #Prompt Year range
  year = ['1978-1988', '1988-1998', '1999-2008', '2009-2017']
  print(year)
  
  #User input Year
  year = int(input('Enter a Year:'))
  print("\n\n" , year)
  
  #Error checking for year
  while True:
    year = int(year)
    if year == 1978 and region == "S.E.A":
     sea_region = df.iloc[:120 ,:9]
     print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
     print(sea_region)
     break
    elif year == 1978 and region == "Asia-Pacific":
     ap_region = df.iloc[:120 ,9:14]
     df1 = df.iloc[:120,:2]
     results = df1.join(ap_region)
     print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
     print(results)
     break
    elif year == 1978 and region == "South-Asia-Pacific":
     sap_region = df.iloc[:120 ,14:17]
     df1 = df.iloc[:120,:2]
     results = df1.join(sap_region)
     print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
     print(results)
     break
    elif year == 1978 and region == "Middle-East":
     me_region = df.iloc[:120 ,17:20]
     df1 = df.iloc[:120,:2]
     results = df1.join(me_region)
     print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
     print(results)
     break
    elif year == 1978 and region == "Europe":
     eur_region = df.iloc[:120 ,20:31]
     df1 = df.iloc[:120,:2]
     results = df1.join(eur_region)
     print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
     print(results)
     break
    elif year == 1978 and region == "North-America":
     na_region = df.iloc[:120 ,31:33]
     df1 = df.iloc[:120,:2]
     results = df1.join(na_region)
     print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
     print(results)
     break
    elif year == 1978 and region == "Australia":
     aus_region = df.iloc[:120 ,33:35]
     df1 = df.iloc[:120,:2]
     results = df1.join(aus_region)
     print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
     print(results)
     break
    elif year == 1978 and region == "Africa":
     afr_region = df.iloc[:120 ,35:36]
     df1 = df.iloc[:120,:2]
     results = df1.join(afr_region)
     print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
     print(results)
     break
    elif year == 1988 and region == "S.E.A":
     sea_region = df.iloc[120:252 ,:9]
     print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
     print(sea_region)
     break
    elif year == 1988 and region == "Asia-Pacific":
     ap_region = df.iloc[120:252 ,9:14]
     df1 = df.iloc[120:252,:2]
     results = df1.join(ap_region)
     print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
     print(results)
     break
    elif year == 1988 and region == "South-Asia-Pacific":
     sap_region = df.iloc[120:252 ,14:17]
     df1 = df.iloc[120:252,:2]
     results = df1.join(sap_region)
     print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
     print(results)
     break
    elif year == 1988 and region == "Middle-East":
     me_region = df.iloc[120:252 ,17:20]
     df1 = df.iloc[120:252,:2]
     results = df1.join(me_region)
     print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
     print(results)
     break
    elif year == 1988 and region == "Europe":
     eur_region = df.iloc[120:252 ,20:31]
     df1 = df.iloc[120:252,:2]
     results = df1.join(eur_region)
     print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
     print(results)
     break
    elif year == 1988 and region == "North-America":
     na_region = df.iloc[120:252 ,31:33]
     df1 = df.iloc[120:252,:2]
     results = df1.join(na_region)
     print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
     print(results)
     break
    elif year == 1988 and region == "Australia":
     aus_region = df.iloc[120:252 ,33:35]
     df1 = df.iloc[120:252,:2]
     results = df1.join(aus_region)
     print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
     print(results)
     break
    elif year == 1988 and region == "Africa":
     afr_region = df.iloc[120:252 ,35:36]
     df1 = df.iloc[120:252,:2]
     results = df1.join(afr_region)
     print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
     print(results)
     break
    elif year == 1999 and region == "S.E.A":
     sea_region = df.iloc[252:372 ,:9]
     print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
     print(sea_region)
     break
    elif year == 1999 and region == "Asia-Pacific":
     ap_region = df.iloc[252:372 ,9:14]
     df1 = df.iloc[252:372,:2]
     results = df1.join(ap_region)
     print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
     print(results)
     break
    elif year == 1999 and region == "South-Asia-Pacific":
     sap_region = df.iloc[252:372 ,14:17]
     df1 = df.iloc[252:372,:2]
     results = df1.join(sap_region)
     print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
     print(results)
     break
    elif year == 1999 and region == "Middle-East":
     me_region = df.iloc[252:372 ,17:20]
     df1 = df.iloc[252:372,:2]
     results = df1.join(me_region)
     print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
     print(results)
     break
    elif year == 1999 and region == "Europe":
     eur_region = df.iloc[252:372 ,20:31]
     df1 = df.iloc[252:372,:2]
     results = df1.join(eur_region)
     print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
     print(results)
     break
    elif year == 1999 and region == "North-America":
     na_region = df.iloc[252:372 ,31:33]
     df1 = df.iloc[252:372,:2]
     results = df1.join(na_region)
     print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
     print(results)
     break
    elif year == 1999 and region == "Australia":
     aus_region = df.iloc[252:372 ,33:35]
     df1 = df.iloc[252:372,:2]
     results = df1.join(aus_region)
     print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
     print(results)
     break
    elif year == 1999 and region == "Africa":
     afr_region = df.iloc[252:372 ,35:36]
     df1 = df.iloc[252:372,:2]
     results = df1.join(afr_region)
     print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
     print(results)
     break
    elif year == 2009 and region == "S.E.A":
     sea_region = df.iloc[372:479 ,:9]
     print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
     print(sea_region)
     break
    elif year == 2009 and region == "Asia-Pacific":
     ap_region = df.iloc[372:479 ,9:14]
     df1 = df.iloc[372:479,:2]
     results = df1.join(ap_region)
     print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
     print(results)
     break
    elif year == 2009 and region == "South-Asia-Pacific":
     sap_region = df.iloc[372:479 ,14:17]
     df1 = df.iloc[372:479,:2]
     results = df1.join(sap_region)
     print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
     print(results)
     break
    elif year == 2009 and region == "Middle-East":
     me_region = df.iloc[372:479 ,17:20]
     df1 = df.iloc[372:479,:2]
     results = df1.join(me_region)
     print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
     print(results)
     break
    elif year == 2009 and region == "Europe":
     eur_region = df.iloc[372:479 ,20:31]
     df1 = df.iloc[372:479,:2]
     results = df1.join(eur_region)
     print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
     print(results)
     break
    elif year == 2009 and region == "North-America":
     na_region = df.iloc[372:479 ,31:33]
     df1 = df.iloc[372:479,:2]
     results = df1.join(na_region)
     print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
     print(results)
     break
    elif year == 2009 and region == "Australia":
     aus_region = df.iloc[372:479 ,33:35]
     df1 = df.iloc[372:479,:2]
     results = df1.join(aus_region)
     print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
     print(results)
     break
    elif year == 2009 and region == "Africa":
     afr_region = df.iloc[372:479 ,35:36]
     df1 = df.iloc[372:479,:2]
     results = df1.join(afr_region)
     print("Total number of countries:", str(len(result.columns) - 2) + "\n") 
     print(results)
     break
    else:  
     print ("Year is invalid try again")
     break

#Europe Region Pie Chart
activities = ['United Kingdom', 'Germany', 'France', 'Italy', 'Netherlands', 'Greece', 'Belgium & Luxembourg', 'Switzerland', 'Austria', 'Scandinavia', 'CIS & Eastern Europe']
slices = [4569048, 1760776, 823145, 396964, 729330, 130491, 217463, 526466, 172926, 934676, 590486]
colours = ['FF3333', 'FF7733', 'FFF933','58FF33','33FFB8','33FFDA','33FFFF','0031BD','6009B8','F262EC','84034F']

pit.pie(slices,
        labels=activities,
        startangle=90,
        shadow=True,
        explode=(0.2, 0, 0,0,0,0,0,0,0,0,0), #explode the first pie as largest
        autopct='%1.2f%%')

pit.legend()

pit.show()

#########################################################################
#Main Branch: End of Code
######################################################################### 