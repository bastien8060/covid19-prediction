import pandas
from sklearn import linear_model
from scipy import stats


df = pandas.read_csv("data.csv")

X = df['Dates']
y = df['Cases']

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

speed = myfunc(10)

print(speed)
