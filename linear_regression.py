import pandas as pd
import matplotlib.pyplot as plt

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

ficoScores = loansData['FICO.Range'].map(lambda scores: scores.split("-"))
ficoScores = ficoScores.map(lambda scores: [int(score) for score in scores])
ficoScores = ficoScores.map(lambda scores: scores[0])
loansData['FICO.Score'] = ficoScores
print loansData['FICO.Score'][0:5]

loanLength = loansData['Loan.Length']
loanLength = loanLength.map(lambda length: length.rstrip(" months"))
loanLength = loanLength.map(lambda length: int(length))
loansData['Loan.Length'] = loanLength

interestRates = loansData['Interest.Rate']
interestRates = interestRates.map(lambda rate: rate.rstrip("%"))
interestRates = interestRates.map(lambda rate: float(rate) / 100)
loansData['Interest.Rate'] = interestRates

# plt.figure()
# p = loansData['FICO.Score'].hist()
# plt.show()

a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10))
a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
