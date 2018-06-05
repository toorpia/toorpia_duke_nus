
## Data preparation: Analyze Human and Bat Data ##  

### Requirement
- Python3



### 2 steps before you run this code

1: Please put your data-file in the same folder.

2: Insert your data-file name in the line 8.

Step1:
In order to read your data-file, you have to put it in the same folder or you can add your file path in the line 8 by yourself.

Step2:
Please insert your data-file name like below in Line8.

```sh
df = pd.read_csv("YOUR_FILENAME.csv")
```


After these 2 steps, you can run the code with the command line below in your directory.
```sh
$ Python data_modify.py
```
#### Don't forget to go to your file directory!
ex: If you put this code in download directory, you need to change directory like below.
```sh
$ cd downloads
$ cd toorpia_duke_nus
$ python data_modify.py
```

### Option
If you want to change name of fixed-data file, you can change it in line 71:
```sh
df1 = df1.to_csv("NEW_FIXED-DATA_NAME.csv", index=False, header=None)
```

### Now you are all set to use toorPIA!
