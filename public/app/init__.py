from flask import Flask

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    return {"status": "OK", "version": "1.0"}

if __name__ == '__main__':
    app.run()
