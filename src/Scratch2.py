# from collections import Counter
#
# doc = ["i am a fellow student",
#        "we both are the good student",
#        "a student works hard"]
#
# count = dict(Counter(word for sentence in doc for word in sentence.split()))
# print(count)

# import pandas as pd
#
# data = {'String': ['foo bar hello world this day', 'foo bar', 'hello bar world'],
#         'Value': [10, 2, 5]}
# df = pd.DataFrame(data, columns=['String', 'Value'])
# df['Unique Word'] = df['String'].str.split()
# res = df.drop('String', 1).explode('Unique Word').groupby(['Unique Word']).agg(['count']).reset_index()
# print(res)

import sys
import pprint

is_pypy = '__pypy__' in sys.builtin_module_names


pp = pprint.PrettyPrinter(indent=4)
pp.pprint(is_pypy)

pp.pprint(sys.builtin_module_names)

#pp.pprint(sys.modules)