import pandas as pd
from read_processed_data import length

def modify_output(vehicle_tours,customers,customer_count,vehicle_count,depot):
    obj = 0
    for v in range(0, vehicle_count):
        vehicle_tour = vehicle_tours[v]
        if len(vehicle_tour) > 0:
            obj += length(depot,customers[vehicle_tour[0]])
            for i in range(0, len(vehicle_tour)-1):
                obj += length(customers[vehicle_tour[i]],customers[vehicle_tour[i+1]])
            obj += length(customers[vehicle_tour[-1]],depot)

    # prepare the solution in the specified output format
    outputData = '%.2f' % obj + ' ' + str(0) + '\n'
    obj = '%.2f' % obj
    output_lst = []
    
    for v in range(0, vehicle_count):
        outputData += str(depot.index) + ' ' + ' '.join([str(customers[customer].index) for customer in vehicle_tours[v]]) + ' ' + str(depot.index) + '\n'
        output_lst.append([str(depot.index)]+[str(customers[customer].index) for customer in vehicle_tours[v]]+[str(depot.index)])
    
    return outputData,output_lst

def visualize_output(output_lst,c,v):
    #forming the dataframe
    
     df  =  pd.DataFrame(output_lst,index = [f'vehicle {i+1}' for i in range(len(output_lst))]
                        ,columns = ['' for i in range(max(len(output_lst[j]) for j in range(len(output_lst))))])
    
     print(df)
     df.to_excel(f'output_{c}_{v}.xlsx')