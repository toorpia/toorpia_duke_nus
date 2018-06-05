import pandas as pd
import numpy as np

class Data_Prepare():

#Insert file name here like: "YOUR_FILE.csv" so that the program can read your file.

    df = pd.read_csv("YOUR_FILE.csv")

# """
#   Thank you for adding it! You are all set!
#   Type commandline:::  Python data.modify1.py
#   so you can get the fixed data-file!
#
# """

###### Program start here #######
    df = df.sort_values(by= [list(df)[0], list(df)[1]])
    num = df._get_numeric_data()
    num[num < 10] = 0
    data = []

    ##hedader preparation
    header = []
    family_protein = list(df)[0] +  "-" + list(df)[1]
    header.append(family_protein)
    for each in list(df)[5:len(list(df))]:
        header.append(each)
    data.append(header)

    # ##data preparation
    for each in df.values:
        row_set = []
        protein = each[0] + "-" + each[1]
        row_set.append(protein)
        for value in each[5:len(each)]:
            if (value == '0' or value == "" or value == None):
                row_set.append(0)
            else:
                row_set.append(float(value))
        data.append(row_set)

    def protein(self):
        protein_data = []
        for value in self.data:
            ##beginning
            if(len(protein_data) <= 1):
                protein_data.append(value)
              #from next
            else:
                last = protein_data[len(protein_data)-1]
                if(value[0] == last[0]):
                    value_column = 1
                    while(value_column < len(protein_data[0])):
                        last[value_column] += value[value_column]
                        value_column += 1
                else:
                    if value == 0:
                        protein_data(None)
                    protein_data.append(value)
        df1 = pd.DataFrame(protein_data)
        df1 = df1.replace(0, np.nan)
        df1 = df1.dropna(axis=0, thresh=2)



        ##Here is the part where you create csv file
        #If you want to change name of the fix-data file, you can!
        #You can do: df1= df1.to_csv("NEW_FILE_NAME.csv", index=False, header=None)
        ###########
        df1 = df1.to_csv("result.csv", index=False, header=None)
        ############


        print("Ta-da! fixed data csv file is created in the file! You are done!")

data_prepare = Data_Prepare()
data_prepare.protein()
