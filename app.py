
from flask import Flask
app = Flask(__name__)
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from process import process_data
@app.route('/process_data')
def predict ():
    data=process_data()
    
    #output to firebase
    for record in data:
        # convert any list values to strings
        for key, value in record.items():
            if isinstance(value, list):
                record[key] = ', '.join(value)

        # set the document in Firestore
        doc_ref = db.collection(u'Out').document(record['output'])
        doc_ref.set(record)
    return my_dict        
        
#/////////////////////////////////////////////////////////////
if __name__ == '__main__':
    app.run(host="0.0.0", port=9000)
