######################################################
#  Your info here
######################################################
# Dr. Ignaz Semmelweis was a Hungarian physician born in 1818 and active at the Vienna General Hospital.
# in the early 1840s at the Vienna General Hospital as many as 10% of the women giving birth were dying.
# An overwhelming number of women were dying from childbed fever, a deadly disease affecting women that
# just have given birth. Semmelweis suspected the cause was the contaminated hands of the doctors
# delivering the babies. An examination of data from clinics in Vienna helped him to prove his hypothesis
# and save lives. Let’s look at the data ourselves.

# Import pandas, numpy, matplotlib.pyplot, and seaborn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


###### Variables ######
# yearly data filename
yearly_dataset: str = "yearly_deaths_by_clinic.csv"

# monthly data filename (Clinic 1 Data Only)
monthly_dataset: str = "monthly_deaths.csv"


# Use pandas read_csv() to read the yearly dataset
yearly_df = pd.read_csv(yearly_dataset)

# Use pandas read_csv() to read the monthly dataset (Clinic 1 Data Only)
monthly_df = pd.read_csv(monthly_dataset)


###### Initial look at the yearly dataset ######
# Print the dataset
print(yearly_df)


###### Visualizations of the yearly dataset ######
# Plot the deaths by year and by clinic
# Create a dodged bar graph of the number of deaths by year by clinic using Seaborn barplot()
sns.barplot(data=yearly_df, x="year", y="deaths", hue="clinic")
plt.title("Deaths by Year and Clinic")
plt.xlabel("Year")
plt.ylabel("Number of Deaths")
plt.show()


# Add a new feature, "Percentage of Deaths" to the dataframe which is the 
# number of deaths divided by the sum of the births and deaths
yearly_df["Percentage of Deaths"] = yearly_df["deaths"] / (yearly_df["births"] + yearly_df["deaths"])

print(yearly_df)


# Create a dodged bar graph of the percentage of deaths by year by clinic using Seaborn barplot()
sns.barplot(data=yearly_df, x="year", y="Percentage of Deaths", hue="clinic")
plt.title("Percentage of Deaths by Year and Clinic")
plt.xlabel("Year")
plt.ylabel("Percentage of Deaths")
plt.show()


###### Initial look at the monthly dataset from Clinic 1 ######
# Print the dataset
print(monthly_df)


###### Visualizations of the monthly dataset ######
# Add a new feature, "Percentage of Deaths" to the dataframe which is the 
# number of deaths divided by the sum of the births and deaths
monthly_df["Percentage of Deaths"] = monthly_df["deaths"] / (monthly_df["births"] + monthly_df["deaths"])


# Change the data type of "date" column from string to datetime
monthly_df["date"] = pd.to_datetime(monthly_df["date"])


# Print the dataset again to make sure looks OK
print(monthly_df)


# Create a line graph of the percentage of deaths for Clinic 1 using Seaborn lineplot()
sns.lineplot(data=monthly_df, x="date", y="Percentage of Deaths")
plt.title("Monthly Percentage of Deaths in Clinic 1")
plt.xlabel("Date")
plt.ylabel("Percentage of Deaths")
plt.show()


# Split monthly into two dataframes, i.e., create one dataframe with data before handwashing,
# and another dataframe with data from after handwashing
before_washing = monthly_df[monthly_df["date"] < "1847-06-01"]
after_washing = monthly_df[monthly_df["date"] >= "1847-06-01"]


# Create a line graph of the two datasets just created to highlight the decrease in deaths
sns.lineplot(data=before_washing, x="date", y="Percentage of Deaths", label="Before Handwashing")
sns.lineplot(data=after_washing, x="date", y="Percentage of Deaths", label="After Handwashing")
plt.title("Percentage of Deaths Before and After Handwashing")
plt.xlabel("Date")
plt.ylabel("Percentage of Deaths")
plt.show()


# Calculate the decrease in the deaths of women in childbirth due to handwashing as a percentage,
# i.e., 100*(afterHW - beforeHW)/beforeHW
percentage_decrease = 100 * (
    after_washing["Percentage of Deaths"].mean() - before_washing["Percentage of Deaths"].mean()
) / before_washing["Percentage of Deaths"].mean()

print("Percentage decrease after handwashing:", percentage_decrease)
