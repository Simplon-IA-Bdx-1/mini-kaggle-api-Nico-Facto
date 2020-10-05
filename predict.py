from pycaret.classification import load_model, predict_model
import pandas as pd

class IaProd():

    def __init__(self,dataframe):
        self.df_inc = dataframe

    def iaJob(self):
        saved_model = load_model('Prod_model') 
        predictions = predict_model(saved_model, data = self.df_inc)
        return predictions

if __name__ == "__main__":

    df = pd.read_csv("test2.csv",index_col=0)
    this_job = IaProd(df)
    pred = this_job.iaJob()
    pred.to_csv("test2-predictions.csv")