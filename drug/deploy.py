# 참고
# https://keraskorea.github.io/posts/2018-10-27-Keras%20%EB%AA%A8%EB%8D%B8%EC%9D%84%20REST%20API%EB%A1%9C%20%EB%B0%B0%ED%8F%AC%ED%95%B4%EB%B3%B4%EA%B8%B0/
# https://blog.naver.com/PostView.nhn?blogId=wideeyed&logNo=221350966399

from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import tensorflow as tf
import numpy as np
import os

from preprocess import preprocess_drugdata, restore_target

def load_model():
    global model
    model = None
    model_dir = "./model/drug_model_0422.h5"
    model = tf.keras.models.load_model(model_dir)

class predict_drug(Resource):

    def get(self):
        success_val = False
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('age', required=True, type=int, help='age is required (10 <= age < 80)')
            parser.add_argument('sex', required=True, type=str, help='sex is required (F/M)')
            parser.add_argument('bp', required=True, type=str, help='bp is required (option: HIGH/NORMAL/LOW)')
            parser.add_argument('cholesterol', required=True, type=str, help='cholesterol is required (option: HIGH/NORMAL)')
            parser.add_argument('na_to_k', required=True, type=float, help='na_to_k is required')
            args = parser.parse_args()
            pp = preprocess_drugdata(args)
            input = pp.preprocess()

            prediction = model.predict(input)
            return {"success": success_val, "drug" : restore_target(prediction)}

        except Exception as e:
            return {"success": success_val, "error": str(e)}

app = Flask('My 1st Flask App')
api = Api(app)
api.add_resource(predict_drug, '/predict')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True) # 8000포트로 실행