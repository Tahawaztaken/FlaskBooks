from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    example_embed='Enter an index: '
    return render_template('index.html', embed=example_embed)

@app.route('/test', methods=['GET', 'POST'])
def testfn():
    # GET request
    if request.method == 'GET':
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers
    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200

data = list(range(1,300,3))
print (data)

@app.route('/getdata/<index_no>', methods=['GET','POST'])
def data_get(index_no):
    
    if request.method == 'POST': # POST request
        print(request.get_text())  # parse as text
        return 'OK', 200
    
    else: # GET request
        return 'result: %s ;'%(data[int(index_no)])
    
app.run(debug=True)