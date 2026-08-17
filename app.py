from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)
app.json.ensure_ascii = False  
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/kural/<int:number>')
def get_kural(number):
    if number < 1 or number > 1330:
        return jsonify({"error": "Please enter a number between 1 and 1330."}), 400

    try:
        response = requests.get(f"https://tamil-kural-api.vercel.app/api/kural/{number}")
        data = response.json()
        
        return jsonify({
            "kural": data["kural"],
            "tamil_meaning": data["meaning"]["ta_mu_va"],
            "english_meaning": data["meaning"]["en"]
        })
    except Exception as e:
        return jsonify({"error": "Failed to fetch Thirukkural details."}), 500

if __name__ == '__main__':
    app.run(debug=True)