import pandas as pd 
from read_processed_data import length
def modify_output(solution,points,nodeCount):
    # calculate the length of the tour
    obj = length(points[solution[-1]], points[solution[0]])
    for index in range(0, nodeCount-1):
        obj += length(points[solution[index]], points[solution[index+1]])

    # prepare the solution in the specified output format
    output_data = '%.2f' % obj + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, solution))
    return output_data
def visualize_output(solution):
    output_cols = ['visit_order','location_name']
    output_data = []
    for index, val in enumerate(solution, start=1):
        output_data.append([index,val])
    output_df = pd.DataFrame(output_data,columns=output_cols)
    if not output_df.empty:
     output_df.to_excel('outputs\output2.xlsx', index=False)
     print("File created successfully.")
    else:
     print("The DataFrame is empty. No file created.")
    output_df.to_excel('outputs/output.xlsx',index=False)