import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pdf_contract import pdf_contractor

sns.set(style='ticks', color_codes=True)

report_path = r'C:\Yukang\Study\python\PycharmProjects\pdf_report_analysis\report\M254_PT1'
#report_path = r'C:\Yukang\Study\python\PycharmProjects\pdf_report_analysis\temp\report'
# fig_path = r'C:\Yukang\Study\python\PycharmProjects\pdf_report_analysis\figs\comparsion'
csv_path = r'C:\Yukang\Study\python\PycharmProjects\pdf_report_analysis\csv\M254_PT1_csv'


def read_file(path):
    file_dir = os.listdir(path)
    data_report = np.zeros((len(file_dir), 12, 3), dtype=np.float)

    for i, file in enumerate(file_dir):
        if 'A264' in file:
            df = pd.read_csv(os.path.join(path, file), header=None, skiprows=[0, 12], encoding='gbk')
        else:
            # df = pd.read_csv(os.path.join(path, file), header=None, skiprows=1, encoding='gbk')
            '''from M254 ET, BEFF added so delete MITOEL'''
            df = pd.read_csv(os.path.join(path, file), header=None, skiprows=[0, 7], encoding='gbk')
        for column in df.columns.tolist():
            for index in df.index.tolist():
                df[column][index] = df[column][index].split(' ')[1]

        data_report[i] = df.values
    return data_report


def data_channels(data):
    """
    :param data: numpy [file_num, 12, 3]
    :return:
    """
    df = pd.DataFrame([data[:, 0, 0], data[:, 0, 1], data[:, 0, 2]]).transpose()  # N

    for i in np.arange(1, 12):
        df = pd.concat([df, pd.DataFrame([data[:, i, 0], data[:, i, 1], data[:, i, 2]]).transpose()], axis=1)

    df.columns = range(df.shape[1])
    df[0] = 'HT1'
    df[1] = 'HT2'
    df[2] = 'HT3'

    return df


def flatten_df(df, column_name, path):
    """
    set the same channel in one column
    :return:
    """
    flatt_df = pd.DataFrame(np.array([df[0].values,
                                      df[1].values, df[2].values]).flatten(), columns=[column_name[0]])
    for i in np.arange(1, len(column_name)):
        flatt_df[column_name[i]] = np.array([df[3 * i].values,
                                             df[3 * i + 1].values, df[3 * i + 2].values]).flatten()

    ### add date and engine number info
    date = []
    engine_no = []
    file_dir = os.listdir(path)
    for file in file_dir:
        date_file = file.split('_')[0]
        engine_no_file = file.split('_')[-1].split('.')[0]
        date.append(date_file)
        engine_no.append(engine_no_file)

    flatt_df['Date'] = np.array([date, date, date]).flatten()
    flatt_df['Engine_No'] = np.array([engine_no, engine_no, engine_no]).flatten()
    return flatt_df

#class drawing(data_set):
def draw_md(data_set):
    ax = sns.boxplot(x="N", y="MD", data=data_set, whis=np.inf)
    ax = sns.stripplot(x="N", y="MD", jitter=0.2, data=data_set, color=".3")
    plt.ylim(200, 340)
    plt.grid(axis="y")
    # plt.savefig(os.path.join(fig_path, 'MD.png'))
    plt.show()


def draw_p(data_set):
    ax = sns.boxplot(x="N", y="P", data=data_set, whis=np.inf)
    ax = sns.stripplot(x="N", y="P", jitter=0.2, data=data_set, color=".3")
    plt.ylim(100, 180)
    plt.grid(axis="y")
    # plt.savefig(os.path.join(fig_path, 'P.png'))
    plt.show()


def draw_mip2i(data_set):
    ax = sns.boxplot(x="N", y="MIP2I", data=data_set, whis=np.inf)
    ax = sns.stripplot(x="N", y="MIP2I", jitter=0.2, data=data_set, color=".3")
    plt.ylim(2000, 2700)
    # plt.grid(axis="y")
    # plt.savefig(os.path.join(fig_path, 'MIP2I.png'))
    plt.show()


def draw_poeln(data_set, fig_path):
    ax = sns.boxplot(x="N", y="POELN", data=data_set, whis=np.inf)
    ax = sns.stripplot(x="N", y="POELN", jitter=0.2, data=data_set, color=".3")
    plt.ylim(1, 7)
    # plt.grid(axis="y")
    plt.savefig(os.path.join(fig_path, 'POELN.png'))


def draw_mipcri(data_set, fig_path):
    ax = sns.boxplot(x="N", y="MIPCRI", data=data_set, whis=np.inf)
    ax = sns.stripplot(x="N", y="MIPCRI", jitter=0.2, data=data_set, color=".3")
    plt.ylim(34, 36)
    # plt.grid(axis="y")
    plt.savefig(os.path.join(fig_path, 'MIPCRI.png'))


def draw_pkgh(data_set, fig_path):
    ax = sns.boxplot(x="N", y="PKGH", data=data_set, whis=np.inf)
    ax = sns.stripplot(x="N", y="PKGH", jitter=0.2, data=data_set, color=".3")
    plt.ylim(-100, 50)
    plt.grid(axis="y")
    plt.savefig(os.path.join(fig_path, 'PKGH.png'))


def draw_tabg1r(data_set):
    ax = sns.boxplot(x="N", y="TABG1R", data=data_set, whis=np.inf)
    ax = sns.stripplot(x="N", y="TABG1R", jitter=0.2, data=data_set, color=".3")
    plt.ylim(400, 1000)
    plt.grid(axis="y")
    # plt.savefig(os.path.join(fig_path, 'TABG1R.png'))
    plt.show()


def draw_beff(data_set):
    ax = sns.boxplot(x="N", y="BEFF", data=data_set, whis=np.inf)
    ax = sns.stripplot(x="N", y="BEFF", jitter=0.2, data=data_set, color=".3")
    plt.ylim(200, 280)
    plt.grid(axis="y")
    # plt.savefig(os.path.join(fig_path, 'TABG1R.png'))
    plt.show()


eng_type = 'M254_E15_150'  # you can change it by yourself
test_type = 'HT'
pdf_contractor(report_path, csv_path, eng_type, test_type)
data = read_file(csv_path)
df = data_channels(data)


if 'M254' in eng_type:
    column_name = ['N', 'MD', 'P', 'MIP2I', 'MITL', 'MITW',
                   'POELN', 'OELSTS', 'MIPCRI', 'PKGH', 'TABG1R', 'BEFF']  # add BEFF from M254 ET, and delete MITOEL
    flatt_df = flatten_df(df, column_name, csv_path)
    flatt_df['BEFF'][flatt_df['N'] == 'HT3'] = 0  # normalize BEFF at idle step
else:
    column_name = ['N', 'MD', 'P', 'MIP2I', 'MITL', 'MITW', 'MITOEL',
                   'POELN', 'OELSTS', 'MIPCRI', 'PKGH', 'TABG1R']
    flatt_df = flatten_df(df, column_name, csv_path)



# flatt_df.to_csv(r'C:\Yukang\Study\python\PycharmProjects\pdf_report_analysis\temp\flatt_df.csv')
"""### draw graph ###"""
# draw_md(flatt_df)
# draw_p(flatt_df)

# draw_mip2i(flatt_df)
# draw_poeln(flatt_df)
# draw_mipcri(flatt_df)

# draw_pkgh(flatt_df)

# draw_tabg1r(flatt_df)
# draw_mitl(flatt_df)
draw_beff(flatt_df)


# print(flatt_df[['Date', 'Engine_No', 'TABG1R']][(flatt_df['TABG1R'] < 600) & (flatt_df['N'] == 'HT3')])

"""
limit change: percentile
"""
low_per = 10
high_per = 90
res = np.zeros((len(column_name) - 1, 6), dtype=np.float)

for i, col in enumerate(column_name[1:]):
    for step in range(3):
        arr = np.array(flatt_df[col][flatt_df['N'] == 'HT' + str(step + 1)])
        low = np.percentile(arr, low_per)
        high = np.percentile(arr, high_per).round(2)
        res[i, 2 * step:2 * step + 2] = [low, high]
        #print(col + ', HT' + step + ":", low, high)


limit = pd.DataFrame(res, index=column_name[1:], columns=['HT1', 'HT1', 'HT2', 'HT2', 'HT3', 'HT3'])

#print(limit)
