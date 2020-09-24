import os
import pdfplumber
import pandas as pd

path_report = r'C:\Yukang\Study\python\PycharmProjects\pdf_report_analysis\temp\report'
path_csv = r'C:\Yukang\Study\python\PycharmProjects\pdf_report_analysis\temp\csv'

### creat a dict for ZB number ###
zb_num = {'M254_E15_150': ['A2540100006', 'A2540101502', 'A2540102504', 'A2540102704'],

          'M264_E15_115': ['A2640100906'],
          'M264_E15_140': ['A2640103306', 'A2640103506', 'A2640101106', 'A2640101306'],
          'M264_E20_145': ['A2640100007'],
          'A264_E20_190': ['A2640103406', 'A2640101206', 'A2640101406', 'A2640101506'],
          'A264_E20_225': ['A2640101606'],

          'A274_E20_155': ['A2740101314', 'A2740101816'],

          'A282_E14_100': ['A2820101503', 'A2820106700', 'A2820103103', 'A2820103203'],
          'A282_E14_120': ['A2820101603', 'A2820101703', 'A2820106800', 'A2820103303', 'A2820103403', 'A2820103503', 'A2820103603']}

eng_type = 'M254_E15_150' # you can change it by yourself
test_type = 'HT'

for i, file in enumerate(os.listdir(path_report)):
    for zb in zb_num[eng_type]:
        flag = test_type + '_' + eng_type
        if flag in file:
            label = file[:-4]

            with pdfplumber.open(os.path.join(path_report, file)) as pdf:
                page = pdf.pages[0]
                table = page.extract_table()

                df = pd.DataFrame(table)

                df.to_csv(os.path.join(path_csv, label + '.csv'), index=False, header=False, columns=[1, 2, 3],
                  encoding='gbk')
        else:
            continue


"""
path_report_M254 = os.path.join(path_report, 'M254_OT')
path_report_M264 = os.path.join(path_report, 'M264_E15_140')

path_csv_M254 = os.path.join(path_csv, 'M254_csv')
path_csv_M264 = os.path.join(path_csv, 'M264_csv')
"""


# """### M254 ###"""
# for i, file in enumerate(os.listdir(path_report_M254)):
#     label = file[-6:-4]
#
#     with pdfplumber.open(os.path.join(path_report_M254, file)) as pdf:
#         page = pdf.pages[0]
#         table = page.extract_table()
#
#         df = pd.DataFrame(table)
#
#         df.to_csv(os.path.join(path_csv_M254, label + '.csv'), index=False, header=False, columns=[1, 2, 3],
#                   encoding='gbk')


# """### M264 ###"""
# for i, file in enumerate(os.listdir(path_report_M264)):
#     label = file[-10:-4]
#
#     with pdfplumber.open(os.path.join(path_report_M264, file)) as pdf:
#         page = pdf.pages[0]
#         table = page.extract_table()
#
#         df = pd.DataFrame(table)
#
#         df.to_csv(os.path.join(path_csv_M264, label + '.csv'), index=False, header=False, columns=[1, 2, 3], encoding='gbk')

