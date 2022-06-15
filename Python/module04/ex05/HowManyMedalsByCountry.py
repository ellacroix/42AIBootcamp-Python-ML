from FileLoader import FileLoader


def howManyMedalsByCountry(df, country):
    dict = {}
    countrydf = df[df["Team"] == country].sort_values(by="Year")
    for year in countrydf["Year"].unique():
        medals = {}
        yeardf = countrydf[countrydf["Year"] == year]
        medals["G"] = yeardf[yeardf["Medal"] == 'Gold'].drop_duplicates(subset = "Event").shape[0]
        medals["S"] = yeardf[yeardf["Medal"] == 'Silver'].drop_duplicates(subset = "Event").shape[0]
        medals["B"] = yeardf[yeardf["Medal"] == 'Bronze'].drop_duplicates(subset = "Event").shape[0]
        dict[year] = medals
    return dict


loader = FileLoader()
data = loader.load('../data/athlete_events.csv')
print(howManyMedalsByCountry(data, 'France'))
