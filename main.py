from caesar import rotate_string
from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form="""<!DOCTYPE html><html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      
      <form name="form" method="post">
        Rotate by: <input text="rotate" name="rotate" ></input>
        <textarea name ="textarea1">{0}</textarea>
        <input type="submit"></input>
      </form>


    </body>
</html>"""


@app.route("/", methods=['POST'])
def encrypt():
    rotate=int(request.form['rotate'])
    display=rotate_string(request.form['textarea1'],rotate)
    
    return form.format(display)

@app.route("/")
def index():
    return form.format("")



app.run()