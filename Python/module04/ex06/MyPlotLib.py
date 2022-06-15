from FileLoader import FileLoader
import matplotlib.pyplot as plt


class MyPlotLib:

    @staticmethod
    def histogram(data, features):
        data.hist(column=features, grid=True, bins=10, rwidth=0.9, color='green')
        plt.grid(axis='y', alpha=0.75)
        plt.show()
        return None

    @staticmethod
    def density(data, features):
        return None

    @staticmethod
    def pair_plot(data, features):
        return None

    @staticmethod
    def box_plot(data, features):
        return None

loader = FileLoader()
data = loader.load('../data/athlete_events.csv')
MyPlotLib.histogram(data, ["Height", "Weight"])
