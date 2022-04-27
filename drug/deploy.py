# https://keraskorea.github.io/posts/2018-10-27-Keras%20%EB%AA%A8%EB%8D%B8%EC%9D%84%20REST%20API%EB%A1%9C%20%EB%B0%B0%ED%8F%AC%ED%95%B4%EB%B3%B4%EA%B8%B0/
# https://blog.naver.com/PostView.nhn?blogId=wideeyed&logNo=221350966399

from flask import Flask
from flask_restful import Api, Resource, reqparse
import tensorflow as tf
import numpy as np
import os

from preprocess import preprocess_drugdata

def load_model():
    global model
    model_dir = "/Users/youranwoo/workspace/model_api/drug/model/drug_model_0422.h5"
    model = tf.keras.models.load_model(model_dir)


def parse_input():
    parser = reqparse.RequestParser()
    parser.add_argument('age', required=True, type=int, help='age is required (10 <= age < 80)')
    parser.add_argument('sex',  required=True, type=str, help='sex is required (F/M)')
    parser.add_argument('bp', required=True, type=str, help='bp is required (option: HIGH/NORMAL/LOW)')
    parser.add_argument('cholesterol',  required=True, type=str, help='cholesterol is required (option: HIGH/NORMAL)')
    parser.add_argument('na_to_k',  required=True, type=float, help='na_to_k is required')
    args = parser.parse_args()
    processed_input = preprocess_drugdata(args)

    return processed_input