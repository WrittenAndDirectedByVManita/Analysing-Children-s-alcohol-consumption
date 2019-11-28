#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 10:36:49 2018

@author: Manita
"""
#******************************************************************************
# Library
#******************************************************************************

import pandas as pd
import numpy as np

#******************************************************************************
# Import default tables
#******************************************************************************


path = 'C:\\Users\\vitor\\OneDrive - NOVAIMS\\machine learning\\Project_02\\data\\'


colnames = ["country","gender","daily","weekly","less_weekly","dont","total","n"]
smoking = pd.read_excel(path+'smoking.xls',names=colnames, skiprows=5)

colnames = ["country","gender","never","11y_orless","12y","13y","14y","15y","16y_ormore","total","n"]
first_drunk = pd.read_excel(path+'age_first_drunk.xls',names=colnames, skiprows=5)

colnames = ["country","gender","daily","weekly","monthly","rarely","never","total","n"]
alcopops = pd.read_excel(path+'alcopops.xls',names=colnames, skiprows=5)

colnames = ["country","gender","never","once","2_3times","4_10times","10_more","total","n"]
been_drunk = pd.read_excel(path+'been_drunk.xls',names=colnames, skiprows=5)

colnames = ["country","gender","never","11y_orless","12y","13y","14y","15y","16y_ormore","total","n"]
canabis = pd.read_excel(path+'canabis.xls',names=colnames, skiprows=5)

colnames = ["country","gender","rarely","less_weekly","weekly","daily","total","n"]
evening_friends = pd.read_excel(path+'evening_friends.xls',names=colnames, skiprows=5)

colnames = ["country","gender","none","30min","1h","2_3h","4_6h","7h_ormore","total","n"]
exercise = pd.read_excel(path+'exercise.xls',names=colnames, skiprows=5)

colnames = ["country","gender","1","2","3","4","5","6","7","total"]
family_help = pd.read_excel(path+'family_help.xls',names=colnames, skiprows=5)

colnames = ["country","gender","1","2","3","4","5","6","7","total"]
friends_help = pd.read_excel(path+'friends_help.xls',names=colnames, skiprows=5)

colnames = ["country","gender","5","4","3","2","1","total","n"]
family_well = pd.read_excel(path+'family_well_off.xls',names=colnames, skiprows=5)

colnames = ["country","gender","0","1","2","3","4","5","6","7","8","9","10","total","n"]
life_sas = pd.read_excel(path+'life_satisf.xls',names=colnames, skiprows=5)

colnames = ["country","gender","very_good","good","avg","below_avg","total","n"]
school_achieve = pd.read_excel(path+'school_achievement.xls',names=colnames, skiprows=5)

colnames = ["country","gender","yes","no","total","n"]
sex = pd.read_excel(path+'sex.xls',names=colnames, skiprows=5)

colnames = ["country","gender","never","less_1","1d","2d","3d","4d","5d_ormore","total","n"]
drink_day = pd.read_excel(path+'typical_drink_day.xls',names=colnames, skiprows=5)

# datasource in the end
smoking = smoking.loc[smoking.gender.notna()]
first_drunk = first_drunk.loc[first_drunk.gender.notna()]
alcopops = alcopops.loc[alcopops.gender.notna()]
been_drunk = been_drunk.loc[been_drunk.gender.notna()]
canabis = canabis.loc[canabis.gender.notna()]
evening_friends = evening_friends.loc[evening_friends.gender.notna()]
exercise = exercise.loc[exercise.gender.notna()]
friends_help = friends_help.loc[friends_help.gender.notna()]
family_help = family_help.loc[family_help.gender.notna()]
family_well = family_well.loc[family_well.gender.notna()]
life_sas = life_sas.loc[life_sas.gender.notna()]
school_achieve = school_achieve.loc[school_achieve.gender.notna()]
sex = sex.loc[sex.gender.notna()]
drink_day = drink_day.loc[drink_day.gender.notna()]


#******************************************************************************
# Import extra variables
#******************************************************************************

wb = pd.read_excel(path+'Worldbank.xlsx')
wb = wb[:304]

rawdata = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')

























