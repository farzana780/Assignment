import pandas as pd
import pylab

df = pd.read_csv("pressure.csv", skiprows=1)

df["Pressure (Pa)"] = df["Pressure (Pa)"]/1000000
df.rename(columns={"Pressure (Pa)": "Pressure (MPa)"}, inplace=True)
print(df)

df.plot.scatter(x="Pressure (MPa)", y="KP (m)")
pylab.show()
