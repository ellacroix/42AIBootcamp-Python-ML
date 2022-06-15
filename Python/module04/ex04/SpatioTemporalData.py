from FileLoader import FileLoader

class SpatioTemporalData():

    def __init__(self, data):
        self.data = data

    def where(self, year):
        yeardf = self.data[self.data["Year"] == year]
        #yeardf = yeardf.drop_duplicates(subset = "Year")
        return yeardf["City"].unique().tolist()

    def when(self, city):
        citydf = self.data[self.data["City"] == city]
        #yeardf = yeardf.drop_duplicates(subset = "Year")
        return citydf["Year"].unique().tolist()


loader = FileLoader()
data = loader.load('../data/athlete_events.csv')
sp = SpatioTemporalData(data)
print(sp.where(1896))
print(sp.when('Athina'))
