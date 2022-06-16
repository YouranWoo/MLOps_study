# 참고
# https://keraskorea.github.io/posts/2018-10-27-Keras%20%EB%AA%A8%EB%8D%B8%EC%9D%84%20REST%20API%EB%A1%9C%20%EB%B0%B0%ED%8F%AC%ED%95%B4%EB%B3%B4%EA%B8%B0/
# https://blog.naver.com/PostView.nhn?blogId=wideeyed&logNo=221350966399
# 강의 [Fastcampus] 머신러닝 서비스 구축을 위한 실전 MLOps 올인원 패키지 Online.

from flask import Flask, jsonify, request
import tensorflow as tf
import numpy as np
import os

from preprocess import preprocess_drugdata, restore_target

app = Flask('My 1st Flask App')

def load_model():
    global model
    model = None
    model_dir = "./model/drug_model_0422.h5"
    model = tf.keras.models.load_model(model_dir)

@app.route('/predict', methods=['POST'])
def predict_drug():
    success_val = False
    try:
        # parser = reqparse.RequestParser()
        # parser.add_argument('age', required=True, type=int, help='age is required (10 <= age < 80)')
        # parser.add_argument('sex', required=True, type=str, help='sex is required (F/M)')
        # parser.add_argument('bp', required=True, type=str, help='bp is required (option: HIGH/NORMAL/LOW)')
        # parser.add_argument('cholesterol', required=True, type=str, help='cholesterol is required (option: HIGH/NORMAL)')
        # parser.add_argument('na_to_k', required=True, type=float, help='na_to_k is required')
        # args = parser.parse_args()
        
        request_body = request.get_json(force=True)
        data = [request_body['sex'], request_body['age'], request_body['bp'], 
        request_body['cholesterol'], request_body['na_to_k']]

        pp = preprocess_drugdata(data)
        pp_input = pp.preprocess()

        prediction = model.predict(pp_input)
        success_val = True
        return jsonify({"success": success_val, "drug" : restore_target(prediction)})

    except Exception as e:
        return jsonify({"success": success_val, "error": str(e)})

if __name__ == '__main__':
    load_model()
    app.run(host='0.0.0.0', port=8000, debug=True) # 8000포트로 실행