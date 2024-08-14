from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def hello():
    return render_template('Operations.html')

@app.route('/form',methods=['GET'])
def form():
    Num1=int(request.args.get("Num1"))
    Num2=int(request.args.get("Num2"))
    Add=Num1+Num2
    Sub=Num1-Num2
    Mul=Num1*Num2
    Div=Num1/Num2
    return "Addition="+str(Add)+"<br>Subtraction="+str(Sub)+"<br>Multiplication="+str(Mul)+"<br>Division="+str(Div)

if __name__=="__main__":
    app.run(debug=True)
