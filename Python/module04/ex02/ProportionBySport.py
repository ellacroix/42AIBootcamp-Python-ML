from FileLoader import FileLoader


def proportionBySport(df, year, sport, gender):
    prop = 0.
    yeardf = df[df["Year"] == year]
    genderdf = yeardf[yeardf["Sex"] == gender]
    genderdf = genderdf.drop_duplicates(subset = "Name")
    sportdf = genderdf[genderdf["Sport"] == sport]
    prop = sportdf.shape[0] / genderdf.shape[0]
    return prop


loader = FileLoader()
data = loader.load('../data/athlete_events.csv')
print(proportionBySport(data, 2004, 'Tennis', 'M'))