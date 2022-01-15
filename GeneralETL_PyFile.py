import requests
import pandas as pd
import matplotlib.pyplot as plt
import config


api_key = config.api_key

fullurl = 'https://api.census.gov/data/2018/abstcb?get=GEO_ID,NAME,NAICS2017,NAICS2017_LABEL,SEX,SEX_LABEL,ETH_GROUP,ETH_GROUP_LABEL,RACE_GROUP,RACE_GROUP_LABEL,VET_GROUP,VET_GROUP_LABEL,NSFSZFI,NSFSZFI_LABEL,FACTORS_P,FACTORS_P_LABEL,YEAR,FIRMPDEMP,FIRMPDEMP_F,FIRMPDEMP_PCT,FIRMPDEMP_PCT_F,RCPPDEMP,RCPPDEMP_F,RCPPDEMP_PCT,RCPPDEMP_PCT_F,EMP,EMP_F,EMP_PCT,EMP_PCT_F,PAYANN,PAYANN_F,PAYANN_PCT,PAYANN_PCT_F,FIRMPDEMP_S,FIRMPDEMP_S_F,FIRMPDEMP_PCT_S,FIRMPDEMP_PCT_S_F,RCPPDEMP_S,RCPPDEMP_S_F,RCPPDEMP_PCT_S,RCPPDEMP_PCT_S_F,EMP_S,EMP_S_F,EMP_PCT_S,EMP_PCT_S_F,PAYANN_S,PAYANN_S_F,PAYANN_PCT_S,PAYANN_PCT_S_F&for=us:*&key='
data = requests.get(fullurl+api_key)
#print(data)
#print(type(data))

tech_df = pd.DataFrame(data.json())

# promote headers
header_row = 0
tech_df.columns = tech_df.iloc[header_row]
tech_df.drop(labels=0,axis=0,inplace=True)

# do some cleaning
tech_df.drop(['GEO_ID',"NAME","YEAR","NAICS2017","SEX","ETH_GROUP"],inplace=True,axis=1)
tech_df.drop(["RACE_GROUP","VET_GROUP","NSFSZFI","FIRMPDEMP_F","FIRMPDEMP_PCT_F"],inplace=True,axis=1)
tech_df.drop(["RCPPDEMP_F","RCPPDEMP_PCT_F","EMP_F","EMP_PCT_F","PAYANN_F"],inplace=True,axis=1)
tech_df.drop(["PAYANN_PCT_F","FIRMPDEMP_S","FIRMPDEMP_S_F","FIRMPDEMP_PCT_S"],inplace=True,axis=1)
tech_df = tech_df.drop(tech_df.columns[16:],axis = 1)
print(tech_df)

# inspect
tech_df.shape
tech_df.info(verbose=True)