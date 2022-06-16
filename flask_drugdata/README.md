# HOW TO EXECUTE

## 1. Run Flask server.
#### code
```
python deploy.py
```
#### result
2022-06-16 14:23:48.667298: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
 * Serving Flask app 'My 1st Flask App' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on all addresses (0.0.0.0)
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:8000
 * Running on http://10.122.150.125:8000 (Press CTRL+C to quit)
 * Restarting with stat
2022-06-16 14:23:51.448678: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
 * Debugger is active!
 * Debugger PIN: 719-260-491 
  
  

## 2. Make an API call with cURL and wait the response.
### < Example >
#### call
```
curl -X POST http://localhost:8000/predict -d '{"age":58, "sex":"M", "bp":"BP_HIGH", "cholesterol":"Cholesterol_HIGH", "na_to_k":10}'
```
#### -> response
{
  "drug": "DrugB", 
  "success": true
}
