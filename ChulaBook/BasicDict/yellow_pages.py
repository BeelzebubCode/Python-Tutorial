def reverse(d):
    """สลับค่าใน dict ให้ key=value, value=key"""
    reverse_dict = {}
    for key, value in d.items():
        reverse_dict[value] = key
    return reverse_dict

n = int(input())
notebook_data = {}
for _ in range(n):
    data = input().split()
    # name = f"{entry[0]} {entry[1]}"
    # phone = entry[2]
    # name_to_phone[name] = phone
    # phone_to_name[phone] = name

    # สร้าง dict ที่ key = full_name, value = phone
    notebook_data[data[0]+" "+data[1]] = data[2]

m = int(input())
# นำข้อมูลมา reverse
reverse_notebool_data = reverse(notebook_data)
information = []
for _ in range(m):
    data = input()
    # รับข้อมูลที่จะตรวจสอบ
    information.append(data)

for data in information:
    if data in notebook_data:
        print(f"{data} --> {notebook_data[data]}")
    elif data in reverse_notebool_data:
        print(f"{data} --> {reverse_notebool_data[data]}")
    else:
        print(f"{data} --> Not found")