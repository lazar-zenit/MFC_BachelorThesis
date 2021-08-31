import pandas as pd
import numpy as np


#import .csv
data=pd.read_excel("radno.xls")
#print(data)

#Anode surface (m^2)
Aan=0.00825
#open circuit voltage (mV)
OCV_mV=8.5
OCV=OCV_mV/1000

#make Numpy arrays from a DataFrame
Rex_array_kOhm=data[["Rex"]].to_numpy()
UL_array_mV=data[["UL"]].to_numpy()
Rex_array=Rex_array_kOhm*1000
UL_array=UL_array_mV/1000

#calculate current and internal resistance by Ohm's law
Current_array=UL_array/Rex_array
Ri_array=((OCV/UL_array)-1)*Rex_array

#calculate power, power density and current density for each resistance
Power_array=UL_array*Current_array
Power_density=Power_array/Aan
Current_density=Current_array/Aan

#put calculated data in Dataframe and print out the values for some of the parameters
data["Ri"]=Ri_array
data["I"]=Current_array
data["P"]=Power_array
data["Pan"]=Power_density
data["Ian"]=Current_density
data["OCV"]=OCV
data["Aan"]=Aan #in m^2

print("Površina anode: ", Aan, " m^2")


print(data.to_markdown())

#format data to make it easier for copy/pasting back to excel
print("I:")
print(data.I.to_string(index=False))
print("P")
print(data.P.to_string(index=False))
print("Pan")
print(data.Pan.to_string(index=False))
print("Ian")
print(data.Ian.to_string(index=False))
print("Ri")
print(data.Ri.to_string(index=False))


