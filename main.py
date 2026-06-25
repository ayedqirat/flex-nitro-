from flask import Flask
import threading
import os

app = Flask('')

@app.route('/')
def home():
    return "السكربت يعمل بنجاح 24/7!"

def run():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

threading.Thread(target=run).start()
os.system("python flex_nitro_tool.py")
