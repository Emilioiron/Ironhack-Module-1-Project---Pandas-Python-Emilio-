


title = 'Diference_BUSD'

def visualize(df, title):
    barchart = df.plot.bar(x="lastName", y="difference_19_10", rot=70, title=title)
    return barchart


def save_barchart(barchart):
    fig = barchart.get_figure()
    fig.savefig('./data/results/'+ title + '.pdf')


