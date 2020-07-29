## Create VEnv
At the root of a folder : 
 - python -m venv YourEnvName
 - python -m pip install --upgrade pip
 - pip install -r requirements.txt
 - Activate : cd ... YourEnvName\Scripts\  cmd = activate
 - desactivate : cd ... \Scripts\ cmd = deactivate

## Split the dataframe 
python split.py

## Batch prediction
python predict.py

## Return Auc value and graph
streamlit run api.py  