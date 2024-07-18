import math
from collections import namedtuple
# import greedy
# import two__opt
# import shortest_length_first as slf
# import pdb
import pandas as pd


solution = [1,3,4,10,5,9,2,8,6,7]
output_cols = ['visit_order','location_name']
output_data = []
for index, val in enumerate(solution, start=1):
    output_data.append([index,val])
output_df = pd.DataFrame(output_data,columns=output_cols)
output_df.to_excel('output.xlsx',index=False)