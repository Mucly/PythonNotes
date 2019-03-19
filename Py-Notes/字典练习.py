# 生成字母A-Z的ASCII码对照表
number_generate = [v for v in range(65, 65 + 26)]
alpha_dict = map(chr, number_generate)
alpha_dict = dict(zip(alpha_dict, number_generate))
print(alpha_dict)  # {'A': 65, 'B': 66, ... , 'Y': 89, 'Z': 90}


# 计数字典
from collections import defaultdict
count_dict = defaultdict(int)
count_dict['a'] += 1
