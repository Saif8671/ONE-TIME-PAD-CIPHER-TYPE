from flask import Flask, render_template, request
from one import generate_key, encode, decode
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        choice = request.form['choice']
        text = request.form['text'].strip().upper()
        key_input = request.form['key']
        try:
            key = list(map(int, key_input.split(',')))
            if len(text) != len(key):
                result = "ERROR: Key length must match text length."
            else:
                if choice == 'encode':
                    result = encode(text, key)
                elif choice == 'decode':
                    result = decode(text, key)
                else:
                    result = "Invalid choice"
        except ValueError:
            result = "Invalid key format. Use comma-separated numbers."
    return render_template('index.html', result=result)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)