import os
import pdfplumber
import pandas as pd

path_report = r'C:\Yukang\Study\python\PycharmProjects\pdf_report_analysis\report'
path_csv = r'C:\Yukang\Study\python\PycharmProjects\pdf_report_analysis\csv'

path_report_M254 = os.path.join(path_report, 'M254_OT')
path_report_M264 = os.path.join(path_report, 'M264_E15_140')

path_csv_M254 = os.path.join(path_csv, 'M254_csv')
path_csv_M264 = os.path.join(path_csv, 'M264_csv')

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


"""### M264 ###"""
for i, file in enumerate(os.listdir(path_report_M264)):
    label = file[-10:-4]

    with pdfplumber.open(os.path.join(path_report_M264, file)) as pdf:
        page = pdf.pages[0]
        table = page.extract_table()

        df = pd.DataFrame(table)

        df.to_csv(os.path.join(path_csv_M264, label + '.csv'), index=False, header=False, columns=[1, 2, 3], encoding='gbk')

