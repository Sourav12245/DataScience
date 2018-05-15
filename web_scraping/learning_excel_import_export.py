import pandas as pd
df = pd.read_excel("C:\\Users\Sourav\Desktop\countries.xls", sheet_name=0,header=None
                   ,names=["Country","Marks","Date"],encode ="uft-8")

print(df["Country"])
