def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    nodeCount = int(lines[0])

    points = []
    for i in range(1, nodeCount+1):
        line = lines[i]
        parts = line.split()
        points.append(Point(float(parts[0]), float(parts[1]),i-1))

    # build a trivial solution
    # visit the nodes in the order they appear in the file
    solution = range(0, nodeCount)
    if nodeCount == 33810: # greedy solution for larger node count
     solution  = greedy.greedy_sol(points, nodeCount) 
    elif nodeCount == 574: # 2-opt solution
     edge_list = []
     for i in range(0,nodeCount-1):
        edge_list.append([i,i+1])
     edge_list.append([nodeCount-1,0])
     solution = two__opt.improve(points,nodeCount,edge_list)
    else:  # shortest length first initial feasible solution 
     edgelist = slf.sol(points,nodeCount) 
     solution  =  two__opt.improve(points,nodeCount,edgelist)
     
#  to read the output file and create the submission file in excel format with the visit order and location name
    output_cols = ['visit_order','location_name']
    output_data = []
    for index, val in enumerate(solution, start=1):
        output_data.append([index,val])
    output_df = pd.DataFrame(output_data,columns=output_cols)
    if not output_df.empty:
     output_df.to_excel('outputs\output1.xlsx', index=False)
     print("File created successfully.")
    else:
     print("The DataFrame is empty. No file created.")
    output_df.to_excel('outputs/output.xlsx',index=False)
     
     
       
       

    # calculate the length of the tour
    obj = length(points[solution[-1]], points[solution[0]])
    for index in range(0, nodeCount-1):
        obj += length(points[solution[index]], points[solution[index+1]])

    # prepare the solution in the specified output format
    output_data = '%.2f' % obj + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, solution))

    return output_data