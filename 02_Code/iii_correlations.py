#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 09:38:21 2018

@author: Manita
"""
# cmap
cmap = sns.diverging_palette(20, 220, sep = 20, as_cmap=True)

#******************************************************************************
# BOY
#******************************************************************************
cmap = sns.diverging_palette(20, 220, sep = 20, as_cmap=True)


boy_corr = np.round(boy.drop(columns=["gender"]).corr(),decimals=2)

mask = np.zeros_like(boy_corr)
mask[np.triu_indices_from(mask)] = True
with sns.axes_style("white"):
    plt.figure(figsize = (15,10))
    sns.heatmap(boy_corr, 
            xticklabels=boy_corr.columns.values,
            yticklabels=boy_corr.columns.values,
            linewidths=0, annot= True,mask=mask,square=False, cmap = cmap)
plt.title("Correlations for Boys", loc = "left", fontweight = "bold")
plt.show()


#******************************************************************************
# Girl
#******************************************************************************


girl_corr = np.round(girl.drop(columns=["gender"]).corr(),decimals=2)

mask = np.zeros_like(girl_corr)
mask[np.triu_indices_from(mask)] = True
with sns.axes_style("white"):
    plt.figure(figsize = (15,10))
    sns.heatmap(girl_corr, 
            xticklabels=girl_corr.columns.values,
            yticklabels=girl_corr.columns.values,
            linewidths=0, annot= True, mask=mask,square=False, cmap = cmap)
plt.title("Correlations for Girls", loc = "left", fontweight = "bold")
plt.show()



'''
-> Same correlation
In both tables, first_drunk is postively correlated with been_drunk, the same way
friends help is with family help
-> Different correlation
-> Boys
evening with friends is slightly positevly correlated with sex
-> Girls
been drunk is slightly positevly correlated with sex
'''

