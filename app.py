# from flask import Flask, render_template, request
import numpy as np
import pickle

# app = Flask(__name__)
# model = pickle.load(open('model.pkl', 'rb'))
#
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# @app.route('/predict', methods=['GET', 'POST'])
# def predict():
#     val1 = request.form['bedrooms']
#     val2 = request.form['bathrooms']
#     val3 = request.form['floors']
#     val4 = request.form['yr_built']
#     arr = np.array([val1, val2, val3, val4])
#     arr = arr.astype(np.float64)
#     pred = model.predict([arr])
#
#     return render_template('index.html', data=int(pred))
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import numpy as np
import pickle

app = FastAPI()
templates = Jinja2Templates(directory="templates")
model = pickle.load(open('model.pkl', 'rb'))

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
async def predict(request: Request, bedrooms: float = Form(...), bathrooms: float = Form(...), floors: float = Form(...), yr_built: float = Form(...)):
    arr = np.array([bedrooms, bathrooms, floors, yr_built])
    pred = model.predict([arr.reshape(1, -1)])
    return templates.TemplateResponse("index.html", {"request": request, "data": int(pred[0])})
