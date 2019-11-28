#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 10:38:27 2018

@author: Manita
"""

#################
# Average responses
t = np.arange(1, 8)

family_help['family_help'] = family_help[['1','2','3','4','5','6','7']].mul(t, axis=1).sum(axis=1)/family_help.total

friends_help['friends_help'] = friends_help[['1','2','3','4','5','6','7']].mul(t, axis=1).sum(axis=1)/friends_help.total

t = np.arange(1, 6)
t=sorted(t,reverse=True)

family_well['family_well'] = family_well[['5','4','3','2','1']].mul(t, axis=1).sum(axis=1)/100

t = np.arange(0,11)
life_sas['life_sas'] = life_sas[["0","1","2","3","4","5","6","7","8","9","10"]].mul(t, axis=1).sum(axis=1)/100

#################
# delete total and N

table_names = [smoking,
               first_drunk,
               alcopops,
               been_drunk,
               canabis,
               evening_friends,
               exercise,
               friends_help,
               family_help,
               family_well,
               life_sas,
               school_achieve,
               sex,
               drink_day]

for table in table_names:
    table.drop(columns=["total","n"],errors='ignore',inplace=True)

#################
# Fill country na

for table in table_names:
    for index, row in table.iterrows():
        if(pd.isnull(row['country'])):
            table.loc[table.index == index, 'country'] = table['country'].loc[table.index.isin([index-1])].values
        

#################
# Reduce dimensionality

alcopops['alcopops'] = alcopops.daily + alcopops.weekly

been_drunk['been_drunk'] = 100 - (been_drunk.never + been_drunk.once)

first_drunk['first_drunk'] = first_drunk['11y_orless'] + first_drunk['12y'] + first_drunk['13y']

canabis['canabis'] = 100 - (canabis.never)

drink_day['drink_day'] = 100 - (drink_day.never + drink_day.less_1 + drink_day['1d'] + drink_day['2d'])

evening_friends['evening_friends'] = evening_friends.daily + evening_friends.weekly

exercise['exercise'] = exercise['2_3h'] + exercise['4_6h'] + exercise['7h_ormore']

school_achieve['school_achieve'] = school_achieve.very_good + school_achieve.good

smoking['smoking'] = smoking.daily + smoking.weekly

sex['sex'] = sex.yes


#################
# merge tables

from functools import reduce

dfs =[smoking[['country', 'gender', 'smoking']],
      first_drunk[['country', 'gender', 'first_drunk']],
      alcopops[['country', 'gender', 'alcopops']],
      been_drunk[['country', 'gender', 'been_drunk']],
      canabis[['country', 'gender', 'canabis']],
      evening_friends[['country', 'gender','evening_friends']],
      exercise[['country', 'gender','exercise']],
      friends_help[['country', 'gender','friends_help']],
      family_help[['country', 'gender','family_help']],
      family_well[['country', 'gender','family_well']],
      life_sas[['country', 'gender','life_sas']],
      school_achieve[['country', 'gender','school_achieve']],
      sex[['country', 'gender','sex']],
      drink_day[['country', 'gender','drink_day']]]
       
df = reduce(lambda left,right: pd.merge(left,right,on=['country','gender'],how='outer'), dfs)

df.loc[df.gender == 'Boy','gender'] = 1
df.loc[df.gender == 'Girl','gender'] = 0

#################
# Nulls

df.isnull().sum()

df[df.isnull().any(axis=1)]

# Fill missing with mean

boy = df.loc[df.gender==1]
girl = df.loc[df.gender==0]

missing_columns = ['first_drunk','canabis','evening_friends','friends_help','family_help','sex','drink_day','alcopops']

for column_name in missing_columns:
    boy[column_name].fillna((boy[column_name].mean()), inplace=True)
    girl[column_name].fillna((girl[column_name].mean()), inplace=True)
    

# reset indexes
boy.reset_index(drop=True,inplace=True)
girl.reset_index(drop=True,inplace=True)



#******************************************************************************
# Aggregated dataframe: Boys + Girls
#******************************************************************************

total = pd.concat([boy,girl])
agg = total.groupby(by = "country").mean()
agg.drop(columns = "gender",inplace=True)
agg.reset_index(inplace=True)

agg = agg.merge(rawdata, how = "left", left_on = "country", right_on = "COUNTRY")
agg.drop(columns= ["COUNTRY", "GDP (BILLIONS)"], inplace = True)

# fill country codes
# BEL
agg.loc[agg['country'].str.contains('Bel'),'CODE'] = 'BEL'
# GBR

agg.loc[agg['country'].str.contains('Eng'),'CODE'] = 'GBR'
agg.loc[agg['country'].str.contains('Scot'),'CODE'] = 'GBR'
agg.loc[agg['country'].str.contains('Wal'),'CODE'] = 'GBR'

# MDA
agg.loc[agg['country'].str.contains('Mold'),'CODE'] = 'MDA'















