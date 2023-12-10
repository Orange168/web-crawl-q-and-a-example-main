# import pandas as pd

# # 模拟Excel数据
# data = {'text': ['Hello', 'World', 'Python', 'Programming', 'Data', 'Science'],
#         'n_tokens': [1, 2, 4, 6, 21, 33]}
# df = pd.DataFrame(data)

# # 遍历DataFrame中的每一行
# for row in df.iterrows():
#     # 取出每一行的'text'列的值
#     text_value = row[1]['text']
#     print(text_value)
#     n_tokens = row[1]['n_tokens']
#     print(n_tokens)



import pandas as pd
from ast import literal_eval
import numpy as np

# 假设的CSV数据
csv_data = """
text,embeddings
"Hello world","[0.1, 0.2, 0.3]"
"I love machine learning","[0.4, 0.5, 0.6]"
"""

# 将假设的CSV数据写入文件
with open('processed/embeddings.csv', 'w') as file:
    file.write(csv_data.strip())

# 读取CSV文件
df = pd.read_csv('processed/embeddings.csv', index_col=0)

# 将字符串形式的列表转换为NumPy数组
df['embeddings'] = df['embeddings'].apply(literal_eval).apply(np.array)
print('========================================')
# 打印DataFrame的前几行
print(df.head())
