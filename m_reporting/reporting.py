


title = input('Write a title: ')

​def visualize(df, title):
    barchart = df.plot.bar(x="lastName", y="difference_19_10",
                           rot=70, title=title)
    return barchart
barchart = visualize(df_final, title)

​def save_barchart(barchart):
    fig = barchart.get_figure()
    fig.savefig('../data/results/' + title + '.pdf')
    return

​save_barchart(barchart)
