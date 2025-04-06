import pandas as pd
import numpy as np

#understandin the series data type 
# data=[10,20,30,40,124351435,21356,1263217,136]
# series=pd.Series(data) #give the data in the series with the labelled data 
# print(series)

#data with custom labeles
# data=[12,23,34,4,56]
# label=['a','b','c','d','e']
# series=pd.Series(data,index=label)# give teh data with the custom labeles
# print(series)

#dataframe data types
# data={'name':['pratik','saiesh','abhijit'],
#       'age':[19,23,43],
#       'city':['mumbai','Delhi','Banglore']}
# result=pd.DataFrame(data)
# print(result)

#accsessing the column from tha data 
# data={'name':['pratik','saiesh','abhijit'],
#       'age':[19,23,43],
#       'city':['mumbai','Delhi','Banglore']}
# result=pd.DataFrame(data)
# print(result['name']) # acsessing the name column

# data={'name':['pratik','saiesh','abhijit'],
#       'age':[19,23,43],
#       'city':['mumbai','Delhi','Banglore']}
# result=pd.DataFrame(data)
# print(result['age']) #accsesing the age data 

# data={'name':['pratik','saiesh','abhijit'],
#       'age':[19,23,43],
#       'city':['mumbai','Delhi','Banglore']}
# result=pd.DataFrame(data)
# print(result.loc[2]) #accsesing the data  row wise of abhijit

# reading tha data in pandas from file
# df = pd.read_csv("student_data_100.csv")  # Replace "data.csv" with your file path
# print(df)  # Display first 5 rows

# df = pd.read_csv("student_data_100.csv") 
# print(df.info())  #give the information of the all file data


# df = pd.read_csv("student_data_100.csv") 
# print(df.describe())  #give the information of the all file data

# df = pd.read_csv("student_data_100.csv") 
# print(df.isnull().sum())  #give the information of the all file data

#remove the duplicate from th data
# df = pd.read_csv("student_data_100.csv") 
# print(df["Student_ID"].duplicated().sum()) #kiti duplicate aahet te kadate aahe 

#deleting the null values
# df = pd.read_csv("student_data_100.csv") 
# print(df.dropna())
# print("deleted null values")

#replace the null values from the data set
# df = pd.read_csv("student_data_100.csv") 
# df.replace(np.nan, "pratik")  here the null values are repalced by the pratik name 
# print(df)

#Replcing the null values from th particular row or column
# df = pd.read_csv("student_data_100.csv") 
# df['Age'].replace(np.nan,0,inplace=True)  here the null value from the age column is replace by the 0 value
# print(df)

#fill null values by the bacword values
# df = pd.read_csv("student_data_100.csv") 
# result=pd.DataFrame(df)
# result.bfill(inplace=True)
# print(result)

#fill null values by the forward values
# df = pd.read_csv("student_data_100.csv") 
# result=pd.DataFrame(df)
# result.ffill(inplace=True)
# print(result)


#cloumn transformation and its opration
# df = pd.read_csv("student_data_100.csv") 
# df['Student_name_AND_AGE']=df['Age']+ 10  #add 10 and ceate the new column
# print(df)

#capitalize(using the string function)
# df = pd.read_csv("student_data_100.csv") 
# df['Name_upper']=df['Name'].str.upper()
# print(df)

#merge function
# df1=pd.DataFrame({'Id':[1,2,3],
#                   'name':['pratik','saiesh','shardul'],
#                   'mobile No':[9843,23213,13131]})
# df2=pd.DataFrame({'Id':[2,3,1],
#                   'marks':[23,45,65],
#                   'salary':[1200,3400,4000]})
# merged_df=pd.merge(df1,df2,on='Id') #here we can use the merge function we consider id which is unique so we can choose the use parameter 
# print(merged_df)

#left merge function
# df1=pd.DataFrame({'Id':[1,2,3],
#                   'name':['pratik','saiesh','shardul'],
#                   'mobile No':[9843,23213,13131]})
# df2=pd.DataFrame({'Id':[2,3,4],
#                   'marks':[23,45,65],
#                   'salary':[1200,3400,4000]})

# merged_df=pd.merge(df1,df2,on="Id",how='left') #it means that the left like df1 values are include but from df2 only common elemnets are getting 
# print(merged_df)

#right merge
# df1=pd.DataFrame({'Id':[1,2,3],
#                   'name':['pratik','saiesh','shardul'],
#                   'mobile No':[9843,23213,13131]})
# df2=pd.DataFrame({'Id':[2,3,4],
#                   'marks':[23,45,65],
#                   'salary':[1200,3400,4000]})

# merged_df=pd.merge(df1,df2,on="Id",how='right') #it means that the left like df2 values are include but from df13 only common elemnets are getting 
# print(merged_df)

#join function
#by Default join left join(here the index ia important acooerding to the index the joining is perform)
# df1=pd.DataFrame({'name':['pratik','saiesh','shardul']},index=[1,2,3])
# df2=pd.DataFrame({'marks':[90,98,90]},index=[2,3,4])
# joined_df=df1.join(df2)
# print(joined_df)

#right join 
# df1=pd.DataFrame({'name':['pratik','saiesh','shardul']},index=[1,2,3])
# df2=pd.DataFrame({'marks':[90,98,90]},index=[2,3,4])
# joined_df=df1.join(df2,how='right')
# print(joined_df)

#inner join function
# df1=pd.DataFrame({'name':['pratik','saiesh','shardul']},index=[1,2,3])
# df2=pd.DataFrame({'marks':[90,98,90]},index=[2,3,4])
# joined_df=df1.join(df2,how='inner') #it will give only common elements
# print(joined_df)

#outer join function
# df1=pd.DataFrame({'name':['pratik','saiesh','shardul']},index=[1,2,3])
# df2=pd.DataFrame({'marks':[90,98,90]},index=[2,3,4])
# joined_df=df1.join(df2,how='outer') #it will give all the  elements so it will not common or not all the id are included
# print(joined_df)














