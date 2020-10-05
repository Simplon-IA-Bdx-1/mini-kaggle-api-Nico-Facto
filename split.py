import pandas as pd

class split_csv():

    def __init__(self,dataframe):
        self.df = dataframe

    def split_data(self):

        midel_value = int(len(self.df)/2)
        train_df = df.iloc[:midel_value, :]
        test2_df = df.iloc[midel_value+1:, :]
        return train_df, test2_df

    def export_data(self,train_df, test2_df):
        train_df.to_csv("train2.csv")
        test2_df.to_csv("test2.csv")

if __name__ == "__main__":

    df = pd.read_csv("data/cs-training.csv", index_col=0)
    this_job = split_csv(df)
    train_df, test2_df = this_job.split_data()
    this_job.export_data(train_df, test2_df)

