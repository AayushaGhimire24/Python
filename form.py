from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def hello():
    return render_template('form.html')
@app.route('/form',methods=['GET'])
def form():
    name=request.args.get("name")
    return "<h1>Hello"+name+"</h1>"
if __name__=="__main__":
    app.run(debug=True)
