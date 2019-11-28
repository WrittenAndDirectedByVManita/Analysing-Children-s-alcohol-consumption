#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 14:36:02 2018

@author: Manita
"""

# variable with all - > total_extra
# remove correlated variables
to_regress = total_extra.drop(columns = ['country', 'CODE', 'Ruralpop', 
                                         'first_drunk', 'exercise', 
                                         'family_help'])

# Loop for simple regressions

target = 'been_drunk'
rest = to_regress.drop(columns = [target]).columns
r_squared = []
coef = []
y = to_regress[target]
for var in rest: 
    x = to_regress[var]
    mod = sm.OLS(y, sm.add_constant(x)).fit()
    r_squared.append(np.round(mod.rsquared, decimals = 3))
    coef.append(np.round(mod.params[1], decimals = 3))
    


# DataFrame
params_df = pd.DataFrame({"variable":rest, "R2": r_squared, "coef": coef})
params_df.sort_values(by="R2", ascending = False,inplace=True)
params_df.set_index("variable", inplace=True)
params_df['signal'] = 0
params_df.loc[params_df.coef > 0, "signal"] = 1

# Plot    
clrs = ['skyblue' if (x > 0) else 'salmon' for x in params_df['signal'] ]
red_patch = mpatches.Patch(color='salmon', label='Negative coef')
blue_patch = mpatches.Patch(color='skyblue', label='Positive coef')

plt.subplots(figsize=(7,12))
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
sns.barplot(y = params_df.index, x = 'R2', data = params_df,
            orient = "h", palette=clrs, edgecolor = "black")
plt.legend(handles=[blue_patch, red_patch], loc = "lower right")
plt.title("Dependent Variable: "+target, loc='left',fontweight = "bold")
plt.xlabel('R Squared')
plt.ylabel('Dependent Variables')
plt.show()

# Choose top k variables to regress

k = 7
# regression details
x = to_regress[params_df[:k].index]
mod = sm.OLS(y, sm.add_constant(x)).fit()
print(mod.summary())

























