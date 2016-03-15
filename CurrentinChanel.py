#!/bin/python
import matplotlib.pyplot as plt
import numpy as np

Conductivity_Galinstan = 3.15*10**6
Resistiviy_Galinstan = 1/Conductivity_Galinstan
Area = 16*10**(-4) #m^2
Lenght = 0.8 #m
Resistance = (Resistiviy_Galinstan/Area)*Lenght

#PotentialDifference = 1 #V

#PotentialDifference = input("Potential Difference (V): ")

PotentialDifference = np.arange(0.0,1,0.01)


Current = PotentialDifference/Resistance

data_Diagonal = np.loadtxt("Diagonal.txt",float)
Diagonal_Voltage = data_Diagonal[:,0]
Diagonal_Current = data_Diagonal[:,1]

data_Straight = np.loadtxt("Straight.txt",float)
Straight_Voltage = data_Straight[:,0]
Straight_Current = data_Straight[:,1]

data_Adjacent = np.loadtxt("Adjacent.txt",float)
Adjacent_Voltage = data_Adjacent[:,0]
Adjacent_Current = data_Adjacent[:,1]

data_Diagonal_880 = np.loadtxt("Diagonal_880RPM.txt",float)
Diagonal_Voltage_880 = data_Diagonal_880[:,0]
Diagonal_Current_880 = data_Diagonal_880[:,1]

data_Straight_880 = np.loadtxt("Straight_880RPM.txt",float)
Straight_Voltage_880 = data_Straight_880[:,0]
Straight_Current_880 = data_Straight_880[:,1]

data_Adjacent_880 = np.loadtxt("Adjacent_880RPM.txt",float)
Adjacent_Voltage_880 = data_Adjacent_880[:,0]
Adjacent_Current_880 = data_Adjacent_880[:,1]

data_Diagonal_967 = np.loadtxt("Diagonal_967RPM.txt",float)
Diagonal_Voltage_967 = data_Diagonal_967[:,0]
Diagonal_Current_967 = data_Diagonal_967[:,1]

data_Straight_970 = np.loadtxt("Straight_970RPM.txt",float)
Straight_Voltage_970 = data_Straight_970[:,0]
Straight_Current_970 = data_Straight_970[:,1]

data_Adjacent_962 = np.loadtxt("Adjacent_962RPM.txt",float)
Adjacent_Voltage_962 = data_Adjacent_962[:,0]
Adjacent_Current_962 = data_Adjacent_962[:,1]



#print('Resistance = %s') %Resistance
#print('Potential Difference = %s') %PotentialDifference
#print('Current = %s') %Current

plt.figure(1)
plt.plot(Diagonal_Voltage,Diagonal_Current, linestyle ='--',marker='x',label='Diagonal')
plt.plot(Straight_Voltage,Straight_Current, linestyle ='--',marker='x',label='Straight')
plt.plot(Adjacent_Voltage,Adjacent_Current, linestyle ='--',marker='x',label='Adjacent')
plt.plot(PotentialDifference,Current,label='Theoretical')
plt.xlabel('Potential Difference (V)')
plt.ylabel('Current (A)')
plt.legend(loc='best')
plt.title('Channel Standstill')
plt.savefig('CurrentinChannel_theory.png')

plt.figure(2)
plt.plot(Diagonal_Voltage,Diagonal_Current, linestyle ='--',marker='x',label='0RPM')
plt.plot(Diagonal_Voltage_880,Diagonal_Current_880, linestyle ='--',marker='x',label='880RPM')
plt.plot(Diagonal_Voltage_967,Diagonal_Current_967, linestyle ='--',marker='x',label='967RPM')
plt.xlabel('Potential Difference (V)')
plt.ylabel('Current (A)')
plt.legend(loc='best')
plt.title('Diagonal Current Alignment')
plt.savefig('CurrentinChannel_Diagonal.png')


plt.figure(3)
plt.plot(Straight_Voltage,Straight_Current, linestyle ='--',marker='x',label='0RPM')
plt.plot(Straight_Voltage_880,Straight_Current_880, linestyle ='--',marker='x',label='880RPM')
plt.plot(Straight_Voltage_970,Straight_Current_970, linestyle ='--',marker='x',label='970RPM')
plt.xlabel('Potential Difference (V)')
plt.ylabel('Current (A)')
plt.legend(loc='best')
plt.title('Straight Current Alignment')
plt.savefig('CurrentinChannel_Straight.png')

plt.figure(4)
plt.plot(Adjacent_Voltage,Adjacent_Current, linestyle ='--',marker='x',label='0RPM')
plt.plot(Adjacent_Voltage_880,Adjacent_Current_880, linestyle ='--',marker='x',label='880RPM')
plt.plot(Adjacent_Voltage_962,Adjacent_Current_962, linestyle ='--',marker='x',label='962RPM')
plt.xlabel('Potential Difference (V)')
plt.ylabel('Current (A)')
plt.legend(loc='best')
plt.title('Across Current Alignment')
plt.savefig('CurrentinChannel_Across.png')

plt.figure(5)
plt.plot(Diagonal_Voltage_880,Diagonal_Current_880, linestyle ='--',marker='x',label='Diagonal')
plt.plot(Straight_Voltage_880,Straight_Current_880, linestyle ='--',marker='x',label='Straight')
plt.plot(Adjacent_Voltage_880,Adjacent_Current_880, linestyle ='--',marker='x',label='Adjacent')
#plt.plot(PotentialDifference,Current,label='Theoretical')
plt.xlabel('Potential Difference (V)')
plt.ylabel('Current (A)')
plt.legend(loc='best')
plt.title('Channel 880RPM')
plt.savefig('CurrentinChannel_880RPM.png')

plt.figure(6)
plt.plot(Diagonal_Voltage_967,Diagonal_Current_967, linestyle ='--',marker='x',label='Diagonal')
plt.plot(Straight_Voltage_970,Straight_Current_970, linestyle ='--',marker='x',label='Straight')
plt.plot(Adjacent_Voltage_962,Adjacent_Current_962, linestyle ='--',marker='x',label='Adjacent')
#plt.plot(PotentialDifference,Current,label='Theoretical')
plt.xlabel('Potential Difference (V)')
plt.ylabel('Current (A)')
plt.legend(loc='best')
plt.title('Channel 970RPM')
plt.savefig('CurrentinChannel_970RPM.png')


plt.show()












































