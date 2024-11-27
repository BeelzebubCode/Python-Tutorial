import csv
import pandas as pd

data = []
group_a = []
group_b = []

with open("data.csv", encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

data = sorted(data, key=lambda data : data["โรงเรียน"])

i = 1
for item in data:
    if i % 2 == 0:
        group_a.append(item)
    else:
        group_b.append(item)
    i+=1
# print(len(group_a), len(group_b))

# สร้าง DataFrame 
df_group_a = pd.DataFrame(group_a, columns=["โรงเรียน", "จังหวัด", "ทีม"])
df_group_b = pd.DataFrame(group_b, columns=["โรงเรียน", "จังหวัด", "ทีม"])
# print(len(df_group_a), len(df_group_b))
with pd.ExcelWriter('rov_group.xlsx', engine='openpyxl') as writer:
    df_group_a.to_excel(writer, sheet_name='Groups', startrow=2, index=False, header=False)
    df_group_b.to_excel(writer, sheet_name='Groups', startrow=len(df_group_a)+4, index=False, header=False)
    worksheet = writer.sheets['Groups']

    # เขียนหัวข้อ Group A
    worksheet.cell(row=1, column=1, value='Group A')
    worksheet.cell(row=2, column=1, value='โรงเรียน')
    worksheet.cell(row=2, column=2, value='จังหวัด')
    worksheet.cell(row=2, column=3, value='ทีม')

    # เขียนหัวข้อ Group B
    start_row_group_b = len(df_group_a) + 5
    worksheet.cell(row=start_row_group_b-2, column=1, value='Group B')
    worksheet.cell(row=start_row_group_b-1, column=1, value='โรงเรียน')
    worksheet.cell(row=start_row_group_b-1, column=2, value='จังหวัด')
    worksheet.cell(row=start_row_group_b-1, column=3, value='ทีม')

    for col in worksheet.columns:
        max_length = 0
        column = col[0].column_letter
        for cell in col:
            try:
               if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = (max_length + 2)
        worksheet.column_dimensions[column].width = adjusted_width