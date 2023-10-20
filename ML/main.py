import pandas as pd
data=pd.read_csv('ML\HR_comma_sep.csv')
# print(data.shape)

# find missing data
# print(data.isnull().values.any())
# print(data.dtypes)
print(data.salary.unique(), data.sales.unique())
# data.replace(to_replace='sales',value='1')

clean_up_values={
    "salary": {
        'low':1,
        'medium':2,
        'high':3
    },
}

data=data.replace(clean_up_values)
# print(data)

# get dummies for the departments
dummies=pd.get_dummies(data.sales)
# print(dummies)

# merge dummies into original data

merged=pd.concat([data,dummies],axis='columns')
# print(merged)

final_data=merged.drop(['sales'],axis=1)
print(final_data)