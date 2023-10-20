import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error, r2_score

data=pd.read_csv('ML\HR_comma_sep.csv')
# print(data.shape)

# find missing data
# print(data.isnull().values.any())
# print(data.dtypes)
# print(data.salary.unique(), data.sales.unique())
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

final_data=merged.drop(['sales'],axis='columns')
# print(final_data.columns)


# plot 
# plt.scatter(x= final_data.salary , y=final_data.left)
# plt.show()


# create model 
X=final_data.drop('left',axis='columns')
y=final_data.left
X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.2)

# fit the model to the training data
model=LinearRegression()
model.fit(X_train,Y_train)

# make predictions
# predictions=model.predict(X_test)
# evaluate the model
# print(predictions)

accuracy=model.score(X_test,Y_test)
print(accuracy)

