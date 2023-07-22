import json
from flask import Flask, render_template,request, jsonify 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/menu")
def menu():
    return render_template('menu.html')

@app.route("/submitJSON", methods=["POST"])
def processJSON(): 
    global items,quantity,price,total,cost
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    A = int(jsonObj['a'])
    B = int(jsonObj['b'])
    C = int(jsonObj['c'])
    D = int(jsonObj['d'])
    E = int(jsonObj['e'])
    F = int(jsonObj['f'])
    G = int(jsonObj['g'])
    H = int(jsonObj['h'])
    I = int(jsonObj['i'])
    J = int(jsonObj['j'])
    K = int(jsonObj['k'])

   

    items=['Chicken Biryani   ','Prawns Biryani   ','Egg Biryani      ','Mutton Biryani   ','Chicken Lollipops','Chicken Manchurian','Chicken Kabab      ','Fish Fry          ','Maltesers Tiramisu','Coke              ','Chocolate Milkshake']
    price=[250,300,150,450,300,200,400,200,400,100,150]
    print(items)
    quantity=[A,B,C,D,E,F,G,H,I,J,K]
    total=[]
    for i in range(11):
        total.append(price[i]*quantity[i])

    cost=0
    for j in total:
        cost=cost+j
    

    return " "

@app.route("/bill")
def bill():

    return render_template('bill.html',quantity=quantity,items=items,price=price,total=total,cost=cost)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')


if __name__=='__main__':
	app.run(debug=True)
