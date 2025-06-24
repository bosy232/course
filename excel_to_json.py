<<<<<<< HEAD
import pandas as pd
import hashlib
import json
import numpy as np

excel_file = 'courses.xlsx'
df = pd.read_excel(excel_file, header=None)
df.columns = df.iloc[2]
df = df[3:]
df = df.reset_index(drop=True)

# حذف الأعمدة التي اسمها NaN
df = df.loc[:, ~df.columns.isna()]

# حذف الأعمدة التي كل قيمها NaN
df = df.dropna(axis=1, how='all')

# استبدال أي قيمة NaN في الخلايا بقيمة فارغة
df = df.replace({np.nan: ""})

print("أسماء الأعمدة بعد التعديل:", df.columns)

def generate_code(name, idx):
    base = f"{name}-{idx}"
    return hashlib.sha256(base.encode()).hexdigest()[:8]

# لاحظ هنا اسم العمود بالضبط مع المسافة في النهاية
df['code'] = [generate_code(row['Participant Name '], idx) for idx, row in df.iterrows()]

data = df.to_dict(orient='records')

with open('employees.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

=======
import pandas as pd
import hashlib
import json
import numpy as np

excel_file = 'courses.xlsx'
df = pd.read_excel(excel_file, header=None)
df.columns = df.iloc[2]
df = df[3:]
df = df.reset_index(drop=True)

# حذف الأعمدة التي اسمها NaN
df = df.loc[:, ~df.columns.isna()]

# حذف الأعمدة التي كل قيمها NaN
df = df.dropna(axis=1, how='all')

# استبدال أي قيمة NaN في الخلايا بقيمة فارغة
df = df.replace({np.nan: ""})

print("أسماء الأعمدة بعد التعديل:", df.columns)

def generate_code(name, idx):
    base = f"{name}-{idx}"
    return hashlib.sha256(base.encode()).hexdigest()[:8]

# لاحظ هنا اسم العمود بالضبط مع المسافة في النهاية
df['code'] = [generate_code(row['Participant Name '], idx) for idx, row in df.iterrows()]

data = df.to_dict(orient='records')

with open('employees.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

>>>>>>> 5736c5ba0be12afe508f50f6fda9bf4c6c2fd184
print("تم التحويل بنجاح! ملف employees.json جاهز وخالي من NaN.")