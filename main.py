import datetime
import firebase_admin
from firebase_admin import firestore
from flask import Flask, render_template


app = Flask(__name__)

firebase_app = firebase_admin.initialize_app()
db = firestore.client()
occurrences_collection = db.collection("occurrences")
occurrences_query = occurrences_collection.order_by("timestamp", direction=firestore.Query.DESCENDING).limit(1)


@app.route("/")
def index():
    baddadan_document = next(occurrences_query.stream(), None).to_dict()

    if baddadan_document is None:
        render_template("error.html", error="Database error: forgot Baddadan!"), 500
    
    last_baddadan_time = baddadan_document["timestamp"]
    days_since_last_baddadan = (datetime.datetime.now().timestamp() - last_baddadan_time.timestamp()) / 86400
    return render_template("index.html", days=f"{days_since_last_baddadan:.1f}")


if __name__ == "__main__":
    app.run()