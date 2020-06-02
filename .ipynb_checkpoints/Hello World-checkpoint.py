# Importing necessary libaries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
print('Pandas, NumPy, Seaborn and MatplotLib have been sucessfully loaded')

# Loading data csv dataset into the dataframe
df = pd.read_csv('Data_clean.csv')
print('The dataset has successfully been loaded into the data frame')

# Dropping irrelevant column Unnamed
df.drop('Unnamed: 0', axis=1, inplace=True)
print('Column Unnamed: 0 Successfully removed from the dataframe')

# Creating different age groups by Filtering the categorical variable Age 
age1 = df['Age'] == '16-25 Years'
age2 = df['Age'] == '26-35 Years'
age3 = df['Age'] == '36-45 Years'
age4 = df['Age'] == '46 Years above'
print('Filtering complete and four age groups created')

# Summing up numerical variables (Efficiency, Innovativeness and Sustainability) for each age group into separate dataframes
df1 = pd.DataFrame(df[age1][['Efficiency', 'Innovativeness', 'Sustainability']].sum(axis=0).map(int)).transpose()
df2 = pd.DataFrame(df[age2][['Efficiency', 'Innovativeness', 'Sustainability']].sum(axis=0).map(int)).transpose()
df3 = pd.DataFrame(df[age3][['Efficiency', 'Innovativeness', 'Sustainability']].sum(axis=0).map(int)).transpose()
df4 = pd.DataFrame(df[age4][['Efficiency', 'Innovativeness', 'Sustainability']].sum(axis=0).map(int)).transpose()
print('Variables have been successfully summed up for the four age groups separately.\nFour separate dataframes have been created for the four age groups containing sums of the variables.')

# Joining the four dataframes into one
df_age = df1.append([df2, df3, df4], ignore_index=True)
print('The four dataframes have been successfully joined into one.')

# Placing the categorical variable age group as the first column
df_age['Age Group'] = df['Age'].unique()
df_age.set_index('Age Group', inplace=True)
df_age.reset_index(inplace=True)
print('Age Group successfully set as the first column.')

# Defining variable x and y needed for further analysis
x = df_age['Age Group']
y = [df_age['Efficiency'], df_age['Innovativeness'], df_age['Sustainability']]
print('Variables successfully defined for visualization.')

# Creating a figure with specific size on which stackplot will be plotted
plt.figure(figsize=(10,8))
# Creating a stackplot of the Age groups and (Efficiency, Innovativeness and Sustainability)
plt.stackplot(x,y, labels=['Efficiency', 'Innovativeness', 'Sustainability'], baseline='zero')
# Setting plot title the location of the legend
plt.title('Stackplot showing three layers')
plt.legend(loc='upper right')
# Showing plot
plt.show()

# Creating a figure with specific size on which stacked barplot will be plotted
plt.figure(figsize=(10,8))
# Creating the three different layers of bars to be plotted, a variant of stackplot
plt.bar(x, y[0], edgecolor='white', width=1)
plt.bar(x, y[1], bottom = y[0], edgecolor='white', width=1)
plt.bar(x, y[2], bottom = np.add(y[0],y[1]), edgecolor='white', width=1)
# Setting the plot title, location and labels of the legend
plt.title('Barplot, a variant of Stackplot')
plt.legend(labels=['Efficiency', 'Innovativeness', 'Sustainability'], loc='upper right')
# Showing plot
plt.show()