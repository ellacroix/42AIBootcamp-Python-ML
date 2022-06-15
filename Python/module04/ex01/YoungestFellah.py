from FileLoader import FileLoader


def youngestfellah(df, year):
    yeardf = df[df["Year"] == year]
    male = yeardf[yeardf["Sex"] == 'M']
    female = yeardf[yeardf["Sex"] == 'F']
    youngestmale = male['Age'].min()
    youngestfemale = female['Age'].min()
    dict = {"f":youngestfemale, "m":youngestmale}
    return dict

loader = FileLoader()
data = loader.load('../data/athlete_events.csv')
print(youngestfellah(data, 1991))