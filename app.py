from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def get_song():
    
    return render_template(
        'index.html'
    )
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)

