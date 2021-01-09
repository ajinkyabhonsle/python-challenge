#!/usr/bin/env python
# coding: utf-8

# In[10]:



import csv 
import os


csvbudget = os.path.join('budget_data.csv')
exportbudget2 = os.path.join('budget_data_latest.txt')
# # create monthList
monthList = []
with open(csvbudget) as csvfile:    
    csvReader = csv.reader(csvfile)    
    for row in csvReader:        
        monthList.append(row[0]) 
# print("-----monthList----- ",monthList)  
 
 # find total number of months   
numOfMonths =0
for i in monthList[1:]:
    numOfMonths = numOfMonths+1
# print("-----numOfMonths----- ",numOfMonths)  

# create profitLossList
profitLossList = []
with open(csvbudget) as csvfile:    
    csvReader = csv.reader(csvfile)    
    for idx, row in enumerate(csvReader):
            if idx==0 :
                continue
            profitLossList.append(row[1])  
# print("-----profitLossList----- ",profitLossList)  

# find total net profit loss
netSum=0
for row in profitLossList:
    netSum = netSum+int(row)
# print("-----netSum----- ",netSum)  

# # create ChangeList
changeList = []
n = len(profitLossList) 
for i in range(n - 1) : 
# difference between consecutive numbers 
    diff = int(profitLossList[i+1]) - int(profitLossList[i]) 
    changeList.append(diff)
# print("-----changeList----- ",changeList)
# print("-----max of changeList----- ",max(changeList))
indexForMaxMonthList = changeList.index(max(changeList))+2
# print("-----max of month----- ",monthList[indexForMaxMonthList])

# print("-----min of changeList----- ",min(changeList))
indexForMinMonthList = changeList.index(min(changeList))+2
# print("-----min of month----- ",monthList[indexForMinMonthList])

# find total changeList sum and avg
netSumOfChangeList=0
for row in changeList:
    netSumOfChangeList = netSumOfChangeList+int(row)
    netmonthlyavg = netSumOfChangeList/(numOfMonths-1)
# print("-----netSum of changeList----- ",netSumOfChangeList)
# print("-----avg of netSum of changeList----- ",netmonthlyavg)


     
summary = (
    f"\nFinancial Analysis\n"
    f"-----------------------\n"
    f"Total Months: {numOfMonths}\n"
    f"Total Net Sum: ${netSum}\n"
    f"Avg Change:${netmonthlyavg:.2f}\n"
    f"Greatest increase in profits{monthList[indexForMaxMonthList]},(${max(changeList)})\n"
    f"Greatest decrease in profits{monthList[indexForMinMonthList]},(${min(changeList)})\n"
    )
print(summary)
            
        
with open(exportbudget2,"w") as txt_file:
    txt_file.write(summary)





    



# In[ ]:





# In[ ]:




