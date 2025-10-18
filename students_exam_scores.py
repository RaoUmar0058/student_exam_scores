import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/Users/mac/Downloads/student_exam_scores.csv")
print(df.head())
df.describe() 
df.info()
df.isnull().sum()
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
# Convert columns to numeric, setting errors to NaN
df['hours_studie'] = pd.to_numeric(df['hours_studied'], errors='coerce')
df['exam_score'] = pd.to_numeric(df['exam_score'], errors='coerce')
# %matplotlib inline
# Drop any rows where either 'hours_studie' or 'exam_score' is NaN
df.dropna(subset=['hours_studie', 'exam_score'], inplace=True)
print(df.drop("student_id",axis=1).corr())
#change sleep hours()
# hours studied vs exam score 
sns.scatterplot(x="hours_studie" , y="exam_score", data=df)
plt.title("hours studied vs exam Score")
plt.savefig("hours_vs_score.png",dpi=300,bbox_inches='tight') 
plt.show()
# Sleep hours vs Exam score
sns.scatterplot(x="sleep_hours", y="exam_score", data=df)
plt.title("Sleep Hours vs Exam Score")
plt.savefig("sleep_vs_score.png",dpi=300,bbox_inches='tight')
plt.show()
# Attendance vs Exam score
sns.scatterplot(x="attendance_percent", y="exam_score", data=df)
plt.title("Attendance vs Exam Score")
plt.savefig("attendence_vs_score.png",dpi=300,bbox_inches='tight')
plt.show()
plt.tight_layout()
plt.savefig("all_three_graphs.png",dpi=300,bbox_inches='tight')
plt.show()
plt.savefig(r"C:\Users\YourName\Downloads\graph1.png")
