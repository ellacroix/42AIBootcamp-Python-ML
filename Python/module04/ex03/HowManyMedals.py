from FileLoader import FileLoader


def howManyMedals(df, name):
    dict = {}
    namedf = df[df["Name"] == name]
    for year in namedf["Year"].unique():
        medals = {}
        yeardf = namedf[namedf["Year"] == year]
        medals['G'] = yeardf[yeardf["Medal"] == 'Gold'].shape[0]
        medals['S'] = yeardf[yeardf["Medal"] == 'Silver'].shape[0]
        medals['B'] = yeardf[yeardf["Medal"] == 'Bronze'].shape[0]
        dict[year] = medals
    return dict


loader = FileLoader()
data = loader.load('../data/athlete_events.csv')
print(howManyMedals(data, 'Kjetil Andr Aamodt'))
