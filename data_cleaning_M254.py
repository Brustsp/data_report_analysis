"""
extract data channels from csv and do cleaning,
preparation for plotting

channel: MD, P
"""

import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style='ticks', color_codes=True)

csv_path = r'C:\Yukang\Study\python\PycharmProjects\pdf_report_analysis\csv\M254_csv'
fig_path = r'C:\Yukang\Study\python\PycharmProjects\pdf_report_analysis\figs'


def read_file(path):
    """
    :param path: converted csv report
    :return: numpy [file_num, 12, 3]
    """
    file_dir = os.listdir(path)
    data_report = np.zeros((len(file_dir), 12, 3), dtype=np.float)

    for i, file in enumerate(file_dir):
        df = pd.read_csv(os.path.join(path, file), header=None, skiprows=1, encoding='gbk')

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
    df = pd.DataFrame([data[:, 0, 0], data[:, 0, 1], data[:, 0, 2]]).transpose() # N

    for i in np.arange(1, 12):
        df = pd.concat([df, pd.DataFrame([data[:, i, 0], data[:, i, 1], data[:, i, 2]]).transpose()], axis=1)

    column_name = ['N_4000', 'N_61000', 'N_idle',
                   'MD_4000', 'MD_6100', 'MD_idle',
                   'P_4000', 'P_6100', 'P_idle',
                   'MIP2I_4000', 'MIP2I_6100', 'MIP2I_idle',
                   'MITL_4000', 'MITL_6100', 'MITL_idle',
                   'MITW_4000', 'MITW_6100', 'MITW_idle',
                   'MITOEL_4000', 'MITOEL_6100', 'MITOEL_idle',
                   'POELN_4000', 'POELN_6100', 'POELN_idle',
                   'OELSTS_4000', 'OELSTS_6100', 'OELSTS_idle',
                   'MIPCRI_4000', 'MIPCRI_6100', 'MIPCRI_idle',
                   'PKGH_4000', 'PKGH_6100', 'PKGH_idle',
                   'TABG1R_4000', 'TABG1R_6100', 'TABG1R_idle']

    df.columns = column_name
    # df.to_csv('cleaned_data.csv')

    """
    MD = [data[:, 1, 0], data[:, 1, 1], data[:, 1, 2]]
    P = [data[:, 2, 0], data[:, 2, 1], data[:, 2, 2]]
    MIP2I = [data[: 3, 0], data[: 3, 1], data[: 3, 2]]
    MITL = [data[:, 4, 0], data[: 3, 1], data[: 3, 2]]
    MITW = [data[:, 5, 0], data[:, 5, 1], data[:, 5, 2]]
    MITOEL = [data[:, 6, 0], data[:, 6, 1], data[:, 6, 2]]
    POELN = [data[:, 7, 0], data[:, 7, 1], data[:, 7, 2]]
    OELSTS = [data[:, 8, 0], data[:, 8, 1], data[:, 8, 2]]
    PKGH = [data[:, 10, 0], data[:, 10, 1], data[:, 10, 2]]
    TABG1R = [data[:, 11, 0], data[:, 11, 1], data[:, 11, 2]]
    """
    return df


def draw_md(data_set, fig_path):
    ax = sns.boxplot(x="N", y="MD", data=data_set, whis=np.inf)
    ax = sns.stripplot(x="N", y="MD", jitter=0.2, data=data_set, color=".3")
    plt.ylim(200, 340)
    plt.grid(axis="y")
    plt.savefig(os.path.join(fig_path, 'MD.png'))
    #plt.show()


def draw_p(data_set, fig_path):
    ax = sns.boxplot(x="N", y="P", data=data_set, whis=np.inf)
    ax = sns.stripplot(x="N", y="P", jitter=0.2, data=data_set, color=".3")
    plt.ylim(100, 180)
    #plt.grid(axis="y")
    plt.savefig(os.path.join(fig_path, 'P.png'))
    #plt.show()


def draw_mip2i(data_set, fig_path):
    ax = sns.boxplot(x="N", y="MIP2I", data=data_set, whis=np.inf)
    ax = sns.stripplot(x="N", y="MIP2I", jitter=0.2, data=data_set, color=".3")
    plt.ylim(2000, 2600)
    #plt.grid(axis="y")
    plt.savefig(os.path.join(fig_path, 'MIP2I.png'))


def draw_poeln(data_set, fig_path):
    ax = sns.boxplot(x="N", y="POELN", data=data_set, whis=np.inf)
    ax = sns.stripplot(x="N", y="POELN", jitter=0.2, data=data_set, color=".3")
    plt.ylim(1, 7)
    #plt.grid(axis="y")
    plt.savefig(os.path.join(fig_path, 'POELN.png'))


def draw_mipcri(data_set, fig_path):
    ax = sns.boxplot(x="N", y="MIPCRI", data=data_set, whis=np.inf)
    ax = sns.stripplot(x="N", y="MIPCRI", jitter=0.2, data=data_set, color=".3")
    plt.ylim(34, 36)
    #plt.grid(axis="y")
    plt.savefig(os.path.join(fig_path, 'MIPCRI.png'))


def draw_pkgh(data_set, fig_path):
    ax = sns.boxplot(x="N", y="PKGH", data=data_set, whis=np.inf)
    ax = sns.stripplot(x="N", y="PKGH", jitter=0.2, data=data_set, color=".3")
    plt.ylim(-100, 50)
    plt.grid(axis="y")
    plt.savefig(os.path.join(fig_path, 'PKGH.png'))


def draw_tabg1r(data_set, fig_path):
    ax = sns.boxplot(x="N", y="TABG1R", data=data_set, whis=np.inf)
    ax = sns.stripplot(x="N", y="TABG1R", jitter=0.2, data=data_set, color=".3")
    # plt.ylim(500, 1000)
    #plt.grid(axis="y")
    plt.savefig(os.path.join(fig_path, 'TABG1R.png'))


data = read_file(csv_path)
df = data_channels(data)
df['N_4000'] = '4000'
df['N_6100'] = '6100'
df['N_idle'] = '800'


flatt_df = pd.DataFrame(np.array([df['N_4000'].values, df['N_6100'].values, df['N_idle'].values]).flatten(), columns=['N'])
flatt_df['MD'] = np.array([df['MD_4000'].values, df['MD_6100'].values, df['MD_idle'].values]).flatten()
flatt_df['P'] = np.array([df['P_4000'].values, df['P_6100'].values, df['P_idle'].values]).flatten()
flatt_df['MITW'] = np.array([df['MITW_4000'].values, df['MITW_6100'].values, df['MITW_idle'].values]).flatten()
flatt_df['MIP2I'] = np.array([df['MIP2I_4000'].values, df['MIP2I_6100'].values, df['MIP2I_idle'].values]).flatten()
flatt_df['MITL'] = np.array([df['MITL_4000'].values, df['MITL_6100'].values, df['MITL_idle'].values]).flatten()
flatt_df['MITOEL'] = np.array([df['MITOEL_4000'].values, df['MITOEL_6100'].values, df['MITOEL_idle'].values]).flatten()
flatt_df['MIPCRI'] = np.array([df['MIPCRI_4000'].values, df['MIPCRI_6100'].values, df['MIPCRI_idle'].values]).flatten()
flatt_df['POELN'] = np.array([df['POELN_4000'].values, df['POELN_6100'].values, df['POELN_idle'].values]).flatten()
flatt_df['OELSTS'] = np.array([df['OELSTS_4000'].values, df['OELSTS_6100'].values, df['OELSTS_idle'].values]).flatten()
flatt_df['PKGH'] = np.array([df['PKGH_4000'].values, df['PKGH_6100'].values, df['PKGH_idle'].values]).flatten()
flatt_df['TABG1R'] = np.array([df['TABG1R_4000'].values, df['TABG1R_6100'].values, df['TABG1R_idle'].values]).flatten()


# draw_md(flatt_df, fig_path)
# draw_p(flatt_df, fig_path)
#
# draw_mip2i(flatt_df, fig_path)
# draw_poeln(flatt_df, fig_path)
# draw_mipcri(flatt_df, fig_path)

# draw_pkgh(flatt_df, fig_path)

# draw_tabg1r(flatt_df, fig_path)

# print(flatt_df['PKGH'])

# """plot trend for boost air pressure"""
# plt.scatter(x=np.arange(1, len(df['MIP2I_4000'])+1), y=df['MIP2I_4000'], marker='o')
# plt.scatter(x=np.arange(1, len(df['MIP2I_6100'])+1), y=df['MIP2I_6100'], marker='v')
# plt.grid()
# plt.legend(['N=4000', 'N=6100'])
# plt.show()
