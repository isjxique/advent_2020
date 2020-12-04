
input_data_handle = open("input.txt", "r") 

input_data = input_data_handle.readlines()
input_data = [ int( in_num.replace('\n','') )  for in_num in input_data  ] 

#expense_product = [ val_1*val_2 if val_1+val_2==2020 else 0 for val_1 in input_data for val_2 in input_data
#expense_product = [ val_1*val_2 if val_1+val_2+val_3==2020 else 0 for val_1 in input_data for val_2 in input_data for val_3 in input_data]

expense_product_final = sum(set(  [ val_1*val_2*val_3 if val_1+val_2+val_3==2020 else 0 for val_1 in input_data for val_2 in input_data for val_3 in input_data]   ))

print(expense_product_final)

