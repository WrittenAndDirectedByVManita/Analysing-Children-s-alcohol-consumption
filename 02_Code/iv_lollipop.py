#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 10:42:47 2018

@author: Manita
"""

#******************************************************************************
# alcopops
#******************************************************************************
# Create a dataframe
value1=boy.alcopops
value2=girl.alcopops
df = pd.DataFrame({'group': boy.country,'boys':value1 , 'girls':value2 })
 
# Reorder it following the values of the first value:
ordered_df = df.sort_values(by='boys')
my_range=range(1,len(df.index)+1)

# The vertical plot is made using the hline function
# I load the seaborn library only to benefit the nice looking feature

plt.figure(figsize = (7,10))
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.hlines(y=my_range, xmin=ordered_df['boys'], xmax=ordered_df['girls'], color='grey', alpha=0.4)
plt.scatter(ordered_df['boys'], my_range, color='skyblue', alpha=1, label='boys')
plt.scatter(ordered_df['girls'], my_range, color='red', alpha=0.4 , label='girls')
plt.legend(loc = "lower right")
plt.yticks(my_range, ordered_df['group'])
plt.gca().get_yticklabels()[25].set_color("red")
plt.title("Percentage of adolescents that drink daily or weekly", loc='left',fontweight = "bold")
plt.xlim(0,10,1.5)
plt.xlabel('%')
plt.show()


#******************************************************************************
# drink_day
#******************************************************************************
# Create a dataframe
value1=boy.drink_day
value2=girl.drink_day
df = pd.DataFrame({'group': boy.country,'boys':value1 , 'girls':value2 })
 
# Reorder it following the values of the first value:
ordered_df = df.sort_values(by='boys')
my_range=range(1,len(df.index)+1)
 
# The vertical plot is made using the hline function
# I load the seaborn library only to benefit the nice looking feature

plt.figure(figsize = (7,10))
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.hlines(y=my_range, xmin=ordered_df['boys'], xmax=ordered_df['girls'], color='grey', alpha=0.4)
plt.scatter(ordered_df['boys'], my_range, color='skyblue', alpha=1, label='boys')
plt.scatter(ordered_df['girls'], my_range, color='red', alpha=0.4 , label='girls')
plt.legend(loc = "lower right")
plt.yticks(my_range, ordered_df['group'])
plt.gca().get_yticklabels()[7].set_color("red")
plt.title("Percentage of adolescents that drink 3 or more drinks", loc='left',fontweight = "bold")
plt.xlim(0,50,10)
plt.xlabel('%')
plt.show()


