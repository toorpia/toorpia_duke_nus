class Bat_Summed():
## insert the file name here
  df = pd.read_csv("row_data/VirScan_zscores-Table 1.csv")
  

  # data = []
  # ##hedader preparation
  # header = []
  # family_protein = list(df)[0] +  "-" + list(df)[1]
  # header.append(family_protein)
  # for each in list(df)[5:len(list(df))]:
  #     header.append(each)
  # data.append(header)
  #
  # # ##data preparation
  # for each in df.values:
  #     row_set = []
  #     protein = each[0] + "-" + each[1]
  #     row_set.append(protein)
  #     for value in each[5:len(each)]:
  #         if (value == '0' or value == "" or value == None):
  #             row_set.append(0)
  #         else:
  #             row_set.append(float(value))
  #     data.append(row_set)
  #
  # # print(df.values[0][0])
  # def protein(self):
  #     protein_data = []
  #     for value in self.data:
  #         ##beginning
  #         if(len(protein_data) <= 1):
  #           protein_data.append(value)
  #         #from next
  #         else:
  #           last = protein_data[len(protein_data)-1]
  #           if(value[0] == last[0]):
  #               value_column = 1
  #               while(value_column < len(protein_data[0])):
  #                   last[value_column] += value[value_column]
  #                   value_column += 1
  #           else:
  #               protein_data.append(value)
  #
  #     df1 = pd.DataFrame(protein_data)
  #     df1.to_csv("bat_data/bat_protein_summed.csv", index=False, header=None)
  #     # df1.to_csv("bat_data/test.csv", index=False, header=None)
  #
  #
  #

summed = Bat_Summed()
summed.protein()
