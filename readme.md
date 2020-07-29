## Create Env
at the root of a folder : python -m venv EnvName
pip install -r requirements.txt
 -Activate : cd ... EnvName\Scripts\  cmd = activate
 -desactivate : cd ... \Scripts\ cmd = deactivate

## Split the dataframe 
python split.py

## Batch prediction
python predict.py

## Return Auc value and graph
streamlit run api.py  