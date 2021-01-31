from flask import Flask, request, jsonify
import pandas as pd
import sklearn.metrics as metrics

app = Flask(__name__)

batch_df = pd.read_csv('test2.csv', index_col=0)

@app.route('/submit', methods=["POST"])
def submit():

    # Load requested file
    predictions = request.files['file']
    df_pred = pd.read_csv(predictions)

    # Prediction / True values
    y_true = batch_df["SeriousDlqin2yrs"]
    y_scores = df_pred["Score"]

    # Compute score
    output = round(metrics.roc_auc_score(y_true, y_scores),4)

    return 'Score {}'.format(output)

if __name__ == "__main__":
    app.run(debug=True)