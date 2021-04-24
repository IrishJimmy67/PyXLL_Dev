import pandas

list_RHeader_Cells = [
    {"rangeStart": "J1", "rangeEnd": "N1"},
    {"rangeStart": "J2", "rangeEnd": "N2"},
    {"rangeStart": "J3", "rangeEnd": "N3"},
    {"rangeStart": "J4", "rangeEnd": "N4"}
]

# for dic in list_RHeader_Cells:
#     for val in dic.values():
#         print(val)

# for dic in list_RHeader_Cells:
#     print(dic)
#     for key in dic:
#         print(dic[key])

for dic in list_RHeader_Cells:
    tmpRange = "'" + dic['rangeStart'] + ":" + dic['rangeEnd'] + "'"
    print(tmpRange)

    # for key in dic:
    #     print(key)
    #     print(dic[key])

    # print(dic)
    # print([(k, dic[k]) for k in dic])

