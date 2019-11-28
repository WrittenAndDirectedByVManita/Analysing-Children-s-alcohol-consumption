#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 10:17:49 2018

@author: Manita
"""

# extra variables
# Data: http://databank.worldbank.org/data/download/WDI_csv.zip
# http://databank.worldbank.org/data/reports.aspx?source=2&series=NY.GDP.PCAP.CD&country=

# PIB
# Religion
# Political parties

# data -> wb

wb_countries = set(wb['Country Name'])

wb.drop(columns = ["Series Code"],inplace=True)

indicators = wb['Series Name'].unique()

#  create a DataFrame with indicators as columns

df = pd.DataFrame(wb['Country Code'].unique())
for i in indicators:
    data = wb.groupby(["Series Name"])[2014].get_group(i).reset_index(drop=True)
    
    df = pd.concat([df,data], axis = 1)
    
# rename columns

ind = ['CountryCode','GDPpc','Ruralpop',
       'Teenmom','OutschoolM',
       'OutschoolF','OutschoolT',
       'Expeduc','Urbanpop']
    

df.columns = ind

# replace ".." with na

for i in ind:
    df.loc[df[i] == "..", i] = np.nan

df.isna().sum()

# drop variables with too many nulls

df.drop(columns=['OutschoolF','OutschoolM'], inplace=True)

# fill nulls with mean

values = {'Teenmom':np.mean(df.Teenmom),
            'OutschoolT':np.mean(df.OutschoolT),
            'Expeduc':np.mean(df.Expeduc)}

df.fillna(value=values, inplace=True) 

# Merge with extra variables

total_extra = agg.merge(df, how = "outer", left_on= "CODE", right_on = "CountryCode")

total_extra.drop(columns = ['CountryCode'], inplace = True)

total_extra['GDPpc']=total_extra['GDPpc'].convert_objects(convert_numeric=True)
total_extra['Ruralpop']=total_extra['Ruralpop'].convert_objects(convert_numeric=True)
total_extra['Urbanpop']=total_extra['Urbanpop'].convert_objects(convert_numeric=True)
total_extra.dtypes

#******************************************************************************
# CORRELATIONS
#******************************************************************************
#******************************************************************************
# Total
#******************************************************************************


extra_corr = np.round(total_extra.corr(),decimals=2)

mask = np.zeros_like(extra_corr)
mask[np.triu_indices_from(mask)] = True
with sns.axes_style("white"):
    plt.figure(figsize = (15,10))
    sns.heatmap(extra_corr, 
            xticklabels=extra_corr.columns.values,
            yticklabels=extra_corr.columns.values,
            linewidths=0, annot= True, mask=mask,square=False, cmap = cmap)
plt.title("Correlations for extra variables", loc = "left", fontweight = "bold")
plt.show()



















