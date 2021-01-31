import streamlit as st
import sklearn.metrics as metrics
import pandas as pd   
import matplotlib.pyplot as plt 

class ApiProd():

    def __init__(self,dataframe):
        self.batch_df = dataframe

    def ui_Manager(self):
        
        y_true = self.batch_df["SeriousDlqin2yrs"]
        y_scores = self.batch_df["Score"] ## ---> a chercher dans le fichier test2.csv 

        rac = round(metrics.roc_auc_score(y_true, y_scores),4)
        disp_res = f"Auc for this session : {rac}"
        print("-----------")
        st.text(disp_res)
        print(disp_res)

        lr_fpr, lr_tpr, _ = metrics.roc_curve(y_true, y_scores)
        plt.plot(lr_fpr, lr_tpr, marker='.')
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        st.pyplot(figsize=(8,8))


if __name__ == "__main__":
    
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.title("Auc Api for kaggle GMSC challenge")
    df = pd.read_csv("test2-predictions.csv")
    this_job = ApiProd(df)
    this_job.ui_Manager()




