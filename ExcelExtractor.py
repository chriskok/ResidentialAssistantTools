from docx import Document
from docx.shared import Inches
import pandas as pd

# READ FROM EXCEL
file_name =  "ignore/4E.xlsx"
sheet = 0
df = pd.read_excel(io=file_name, sheet_name=sheet)
cols = [3, 6, 8]
df.drop(df.columns[cols],axis=1,inplace=True)
print(df.head(5))  # print first 5 rows of the dataframe
