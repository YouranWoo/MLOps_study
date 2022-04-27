from re import A
import numpy as np

class preprocess_drugdata():
    """
    preprocess의 기준은 drug_train.ipynb에서 학습/테스트 데이터 전처리에 근거함
    """

    def __init__(self, args):
        self.args = args
        self.sex = self.args['sex']
        self.age = self.args['age']
        self.bp = self.args['bp']
        self.chol = self.args['cholesterol']
        self.na2k = self.args['na_to_k']
        self.na2k_min = 6.269
        self.na2k_max = 38.247

    def preprocess(self):
        age_array = self.vectorize_age()
        sex_array = self.vectorize_sex()
        bp_array = self.vectorize_bp()
        chol_array = self.vectorize_cholesterol()
        na2k_array = self.vectorize_na2k()
        return np.concatenate((age_array, sex_array, bp_array, chol_array, na2k_array), axis=0).reshape(1, -1)

    def vectorize_sex(self):
        return np.array([1]) if self.sex == "M" else np.array([0])

    def vectorize_age(self):
        default_array = np.zeros(shape=(7,))
        group_num = int(self.age / 10)
        default_array[group_num - 1] = 1
        return default_array

    def vectorize_bp(self):
        default_array = np.zeros(shape=(3,))
        if self.bp == 'BP_HIGH':
            default_array[0] = 1
        elif self.bp == 'BP_LOW':
            default_array[1] = 1
        else:  #'BP_NORMAL' 
            default_array[2] = 1
        return default_array

    def vectorize_cholesterol(self):
        return np.array([1]) if self.chol == 'Cholesterol_NORMAL' else np.array([0])

    def vectorize_na2k(self):
        return np.array([(self.na2k - self.na2k_min) / (self.na2k_max - self.na2k_min)])

    def restore_target(self, target_vector):
        target = np.reshape(target_vector, (1,))[0]
        if target == 0:
            return 'DrugY'
        elif target == 1:
            return 'DrugA'
        elif target == 2:
            return 'DrugB'
        elif target == 3:
            return 'DrugC'
        else: #target == 4
            return 'DrugX'


def test_preprocess():
    args = {'age': 20, 'sex' : 'F', 'bp': 'BP_HIGH', 'cholesterol':'Cholesterol_NORMAL', 'na_to_k':10}
    pp = preprocess_drugdata(args)
    result = pp.preprocess()
    print(result)
    print(result.shape)

    target = np.array([1])
    print(pp.restore_target(target))

test_preprocess()