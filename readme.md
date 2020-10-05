## Create VEnv
At the root of a folder : 
 - python -m venv YourEnvName
 - Activate : cd ... YourEnvName\Scripts\  cmd = activate
 - python -m pip install --upgrade pip
 - pip install -r requirements.txt
 - desactivate : cd ... \Scripts\ cmd = deactivate

## Split the dataframe 
python split.py

## Batch prediction
python predict.py

## Return Auc value and graph as APP
streamlit run api_ui.py

## Return Auc value as Api REST
Windows : set FLASK_APP=app.py
Mac : export FLASK_APP=app.py
flask run
Request Windows : curl --request POST \   --url "http://localhost:5000/submit" \   --header "accept: multipart/form-data" \   -F "file=@test2-predictions.csv"
Request Mac : curl --request POST \   --url 'http://localhost:5000/submit' \   --header 'accept: multipart/form-data' \   -F 'file=@test2-predictions.csv'