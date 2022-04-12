from datetime import datetime
import csv

with open('2017.csv', 'r', encoding='utf-8') as fi:
    data = list(csv.DictReader(fi))   #Lista de dict


counting_exchange = {}
for row in data:
    if row['exchange'] in counting_exchange:
        counting_exchange[row['exchange']] += 1
    
    else:
        counting_exchange[row['exchange']] = 1

count_order = sorted(counting_exchange.items(), key=lambda x: x[1])   
text, total = count_order[-1]

maximum = [count_order[-2] if i[0] != 'off exchange' else count_order[-1] for i in count_order]
second, value = maximum[0]

print(f'The Exchange that has had the most transactions in the file: {text}: {total}, seguido de: {second}: {value}')

##-------------------second----------------

agust_2017 = {}
for row in data:
    if '201708' in row['inputdate']:
        if row['companyName'] in agust_2017:
            agust_2017[row['companyName']] += row['valueEUR']
        else:
            agust_2017[row['companyName']] = row['valueEUR']

results_2017 = sorted(agust_2017.items(), key=lambda x: x[1]) 
company, valorEur = results_2017[-1]
print(company)

##-------------------third----------------
contador = 0   #22006 --> 100%
month_1 = []
month_2 = []
month_3 = []
month_4 = []
month_5 = []
month_6 = []
month_7 = []
month_8 = []
month_9 = []
month_10 = []
month_11 = []
month_12 = []
 
for row in data:
       
    if row['tradeSignificance'] == '3' and '2017' in row['inputdate']:
       
        if '201701' in row['inputdate']:
            month_1.append(row['tradeSignificance'])
        
        elif '201702' in row['inputdate']:
            month_2.append(row['tradeSignificance'])  

        elif '201703' in row['inputdate']:
            month_3.append(row['tradeSignificance'])

        elif '201704' in row['inputdate']:
            month_4.append(row['tradeSignificance'])  
        
        elif '201705' in row['inputdate']:
            month_5.append(row['tradeSignificance'])

        elif '201706' in row['inputdate']:
            month_6.append(row['tradeSignificance'])
        
        elif '201707' in row['inputdate']:
            month_7.append(row['tradeSignificance'])

        elif '201708' in row['inputdate']:
            month_8.append(row['tradeSignificance'])
        
        elif '201709' in row['inputdate']:
            month_9.append(row['tradeSignificance'])

        elif '201710' in row['inputdate']:
            month_10.append(row['tradeSignificance'])
        
        elif '201711' in row['inputdate']:
            month_11.append(row['tradeSignificance'])
        
        elif '201712' in row['inputdate']:
            month_12.append(row['tradeSignificance'])    

        contador += 1

def porcentaje(mes):
    return (100 * len(mes)) / contador

print(f'Jan, {round(porcentaje(month_1))}%')
print(f'Feb, {round(porcentaje(month_2))}%')
print(f'Mar, {round(porcentaje(month_3))}%')
print(f'Apr, {round(porcentaje(month_4))}%')
print(f'May, {round(porcentaje(month_5))}%')
print(f'Jun, {round(porcentaje(month_6))}%')
print(f'Jul, {round(porcentaje(month_7))}%')
print(f'Aug, {round(porcentaje(month_8))}%')
print(f'Sep, {round(porcentaje(month_9))}%')
print(f'Oct, {round(porcentaje(month_10))}%')
print(f'Nov, {round(porcentaje(month_11))}%')
print(f'Dic, {round(porcentaje(month_12))}%')

 




     

    


        
