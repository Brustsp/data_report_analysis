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
