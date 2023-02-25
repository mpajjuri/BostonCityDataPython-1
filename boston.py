# read json from url and print the data
import json
import urllib.request
import urllib.parse
import urllib.error
import pandas as pd

url = "https://pollysnips.s3.amazonaws.com/bostonEmployeeSalaries.json"
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

url = "https://pollysnips.s3.amazonaws.com/bostonEmployeeSalaries.json"
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
print(type(data))
print(data[:2])
# print the structure of the data

# load the data into a dictionary
info = json.loads(data)
myData = info["data"]

print(myData[0:5])
print(myData[0][8])
print("Total Salary:"+ myData[0][18])
print("Total Salary:"+ myData[1][18])
print(type(myData[0][18]))

#store the data in a pandas dataframe
df = pd.DataFrame(myData)

#convert the salary column to a float
salary = df[18].astype(float)
# plot salaries in a histogram
salary.plot.hist(bins=20)
# print total of all salaries
print("Total Salary:"+ str(salary.sum()))

#print out job categories and the number of employees in each category
#convert job category column to a string
jobCat = df[9].astype(str)
print(jobCat.value_counts())

#create a pie chart of the number of employees in each job category: [teacher, police, paraprofessional, other]
#create a list of the job categories
jobCatList = jobCat.value_counts().index.tolist()
#pick out the first 4 job categories
jobCatList = jobCatList[0:4]
#create a list of the number of employees the first 4 job categories
jobCatCount = jobCat.value_counts().tolist()
#plot the pie chart
pd.Series(jobCatCount, index=jobCatList).plot.pie()

# print out the ranked list of the top 10 highest mean salaries by job category
print(salary.groupby(jobCat).mean().sort_values(ascending=False).head(10))

# plot the ranked list of the top 10 highest mean salaries by job category on a bar chart
salary.groupby(jobCat).mean().sort_values(ascending=False).head(10).plot.bar()