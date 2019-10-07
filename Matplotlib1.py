import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
x=np.linspace(0,2,50)
plt.scatter(x,x,label="linear")
plt.scatter(x,x**2,label="quadratic")
plt.scatter(x,x**3,label="cubic")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend()
plt.title("Practice Graph")
plt.show()
ds=pd.read_csv(r"C:\Users\student\Desktop\New folder (4)\1.csv",encoding='cp1252')
plt.bar(ds["genre"],ds["quantity"],color="red",edgecolor="orange")
plt.show()
d=pd.read_csv(r"C:\Users\student\Desktop\New folder (4)\2.csv",encoding='cp1252')
score_England = d['score_England']
score_Bangladesh = d['score_Bangladesh']
legend = ['England', 'Bangladesh']
plt.hist([score_England, score_Bangladesh], color=['red', 'blue'])
plt.xlabel("Runs/Delivery")
plt.ylabel("Frequency")
plt.legend(legend)
plt.xticks(range(0, 7))
plt.yticks(range(1, 20))
plt.title(' Trophy 2018 Final\n Runs scored in 4 overs')
plt.show()