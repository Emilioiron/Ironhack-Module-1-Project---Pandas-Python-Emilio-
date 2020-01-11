


def visualize(df, title):
    barchart = df.plot.bar(x="lastName", y="Earning_in BUSD", rot=70, title=title)
    return barchart


def save_barchart(barchart, title):
    fig = barchart.get_figure()
    fig.savefig('./data/results/'+ title + '.pdf')
    fig.savefig('./data/results/' + title + '.png')


