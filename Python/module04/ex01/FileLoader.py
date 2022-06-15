import pandas as pd


class FileLoader:

    def load(self, path):
        data = pd.read_csv(path)
        df = pd.DataFrame(data)
        print("Loading data set of dimension {} x {} ".format(df.shape[0], df.shape[1]))
        return df

    def display(self, df, n):
       if n >= 0:
           print(df.head(n))
       else:
           print(df.tail(-n))