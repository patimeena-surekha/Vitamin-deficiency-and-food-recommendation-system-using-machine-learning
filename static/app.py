import os
import MySQLdb
from flask import Flask, session, url_for, redirect, render_template, request, abort, flash
from database import db_connect,admin_loginact,user_reg,user_loginact,admin_viewusers,uviewact,uviewdeact,add_categoryact,add_productact,admin_viewproducts,admin_adelete,admin_cate,add_addacountdetailsact,add_moneyact
from database import db_connect,user_viewaccuont,user_search,admin_viewpurchaseproducts,admin_viewrecommedns,user_productsact,user_recommend,add_cartact,user_viewrecommend,user_viewcart
from database import db_connect,purchase1,user_viewcatp,remove1,analyst_loginact,user_viewpurchase,user_rateact
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route("/")
def FUN_root():
    return render_template("index.html")


@app.route("/admin.html")
def admin():
    return render_template("admin.html")  

@app.route("/user.html")
def user():
    return render_template("user.html") 

@app.route("/analyst.html")
def analyst():
    return render_template("analyst.html")

@app.route("/register.html")
def register():
    return render_template("register.html") 

@app.route("/addcategory.html")
def addcategory():
    return render_template("addcategory.html")
    
@app.route("/addproducts.html")
def addproducts():
    a = admin_cate()
    return render_template("addproducts.html",a=a)

@app.route("/managebankacount.html")
def managebankacount():
    return render_template("managebankacount.html")

@app.route("/addacountdetails.html")
def addacountdetails():
    return render_template("addacountdetails.html")

@app.route("/addmoney.html")
def addmoney():
    return render_template("addmoney.html")

@app.route("/searchproducts.html")
def searchproducts():
    return render_template("searchproducts.html")


#--------------------------------------------------Login----------------------------------------------------
@app.route("/adminlogact", methods=['GET', 'POST'])
def adminlogact():
    if request.method == 'POST':
        status = admin_loginact(request.form['username'], request.form['password'])
        print(status)
        if status == 1:
            session['username'] = request.form['username']
            return render_template("adminhome.html", m1="sucess")
        else:
            return render_template("admin.html", m1="Login Failed")

@app.route("/useract", methods=['GET', 'POST'])
def useract():
    if request.method == 'POST':
        status = user_loginact(request.form['username'], request.form['password'])
        print(status)
        if status == 1:
            session['username'] = request.form['username']
            return render_template("userhome.html", m1="sucess")
        else:
            return render_template("user.html", m1="Login Failed")

@app.route("/analystact", methods=['GET', 'POST'])
def analystlogact():
    if request.method == 'POST':
        status = analyst_loginact(request.form['username'], request.form['password'])
        print(status)
        if status == 1:
            session['username'] = request.form['username']
            return render_template("analysthome.html", m1="sucess")
        else:
            return render_template("analyst.html", m1="Login Failed")
#-----------------------------------------------Register------------------------------------------------
@app.route("/registeract", methods = ['GET','POST'])
def registeract():
   if request.method == 'POST':    
      id="0"
      status = user_reg(id,request.form['username'],request.form['password'],request.form['email'],request.form['dob'],request.form['gender'],request.form['address'],request.form['mobile'])
      if status == 1:
       return render_template("user.html",m1="sucess")
      else:
       return render_template("register.html",m1="failed")


#-------------------------------------------View-------------------------------------------------------
@app.route("/viewusers.html")
def viewusers():
    data = admin_viewusers()
    print(data)
    return render_template("viewusers.html",users = data)    

@app.route("/viewproducts.html")
def viewproducts():
    data = admin_viewproducts()
    print(data)
    return render_template("viewproducts.html",products = data)

@app.route("/adminviewpurchasedproducts.html")
def admin_view_products():
    data = admin_viewpurchaseproducts()
    print(data)
    return render_template("adminviewpurchasedproducts.html",apurchase = data)

@app.route("/adminviewrecommends.html")
def admin_view_recommends():
    data = admin_viewrecommedns()
    print(data)
    return render_template("adminviewrecommends.html",arecommend = data)

@app.route("/viewaccount.html")
def viewaccount():
    data = user_viewaccuont()
    print(data)
    return render_template("viewaccount.html",accounts = data)

@app.route("/searchproductsact", methods = ['GET','POST'])
def user_searchproductsact():
     if request.method == 'POST': 
      category=request.form['category']
      data = user_search(category)
    
      print(data)
     return render_template("searchproductsact.html",search = data)

@app.route("/viewrecommends.html")
def viewrecommends():
    data = user_viewrecommend()
    print(data)
    return render_template("viewrecommends.html",rec = data)

@app.route("/viewcartproducts.html")
def viewcartproducts():
    data = user_viewcart()
    print(data)
    return render_template("viewcartproducts.html",purchase = data)

@app.route("/viewpurchasedproducts.html")
def viewpurchaseproducts():
    data = user_viewpurchase()
    print(data)
    return render_template("viewpurchasedproducts.html",purchasepro = data)

@app.route("/giverating.html")
def giverating():
    data = user_viewpurchase()
    print(data)
    return render_template("giverating.html",purchasep = data)
#-------------------------------------------activate---------------------------------------------------
@app.route("/uactivate")
def uactivate():
    status = uviewact(request.args.get('username'),request.args.get('email'),request.args.get('gender'))
    data = admin_viewusers()
    if status == 1:
       return render_template("viewusers.html",m1="sucess",users=data)
    else:
       return render_template("viewusers.html",m1="failed",users=data)   

@app.route("/udeactivate")
def udeactivate():
    status = uviewdeact(request.args.get('username'),request.args.get('email'),request.args.get('gender'))
    data = admin_viewusers()
    if status == 1:
       return render_template("viewusers.html",m2="sucess",users=data)
    else:
       return render_template("viewusers.html",m2="failed",users=data)

@app.route("/productdetails")
def productdetails():
    productname =request.args.get('productname')
    data= user_productsact(productname)
    return render_template("productdetails.html",m1="sucess",products1=data)

@app.route("/recommend")
def recommend():
    productname =request.args.get('productname')
    
    data,data1 = user_recommend(productname)
    return render_template("recommend.html",m1="sucess",product=data,user=data1)

@app.route("/purchase")
def purchase():
    status = purchase1(request.args.get('productname'),request.args.get('category'),request.args.get('price'),request.args.get('image'))
    data = user_viewcatp()
    if status == 1:
       return render_template("viewcartproducts.html",m2="sucess",purchase=data)
    else:
       return render_template("viewcartproducts.html",m2="failed",)

@app.route("/remove")
def remove():
    status = remove1(request.args.get('productname'),request.args.get('category'),request.args.get('price'),request.args.get('image'))
    data = user_viewcatp()
    if status == 1:
       return render_template("viewcartproducts.html",m1="sucess",purchase=data)
    else:
       return render_template("viewcartproducts.html",m2="failed",)

@app.route("/giveratingact",methods = ['GET','POST'])
def rateact():
    if request.method == 'POST':
     status =user_rateact(request.form['productname'],request.form['category'],request.form['review'],request.form['rating'])
    
    if status == 1:
       return render_template("giverating.html",m1="sucess")
    else:
       return render_template("giverating.html",m2="failed")
#-------------------------------------------delete-----------------------------------------------------
@app.route("/adelete")
def adelete():
    status = admin_adelete(request.args.get('category'),request.args.get('productname'),request.args.get('price'))
    data = admin-adelete()
    if status == 1:
       return render_template("viewproducts.html",m2="sucess",products=data)
    else:
       return render_template("viewproducts.html",m2="failed",products=data)
#---------------------------------------------Add-------------------------------------------------------
@app.route("/addcategoryact", methods = ['GET','POST'])
def addcategoryact():
   if request.method == 'POST':
      id="0"   
      status = add_categoryact(id,request.form['category'])
   if status == 1:
       return render_template("addcategory.html",m1="sucess")
   else:
       return render_template("addcategory.html",m1="failed")

@app.route("/addproductsact", methods = ['GET','POST'])
def addproductsact():
   if request.method == 'POST':
      id="0"   
      status = add_productact(id,request.form['category_select'],request.form['productname'],request.form['description'],request.form['price'],request.form['brand'],request.form['image'])
   if status == 1:
       return render_template("addcategory.html",m1="sucess")
   else:
       return render_template("addcategory.html",m2="failed")

@app.route("/addacountdetailsact", methods = ['GET','POST'])
def addacountdetailsact():
   if request.method == 'POST':
      status = add_addacountdetailsact(request.form['username'],request.form['branch'],request.form['email'],request.form['address'],request.form['mobile'],request.form['amount'])
   if status == 1:
       return render_template("addacountdetails.html",m1="sucess")
   else:
       return render_template("addacountdetails.html",m2="failed")

@app.route("/addmoneyact", methods = ['GET','POST'])
def addmoneyact():
   if request.method == 'POST':
      status = add_moneyact(request.form['username'],request.form['amount'])
   if status == 1:
       return render_template("addmoney.html",m1="sucess")
   else:
       return render_template("addmoney.html",m2="failed")

@app.route("/addtocart", methods = ['GET','POST'])
def addtocart():
   if request.method == 'POST':
      status = add_cartact(request.form['category'],request.form['productname'],request.form['price'],request.args.get('image'))
     
   if status == 1:
       return render_template("productdetails.html",m1="sucess")
   else:
       return render_template("productdetails.html",m2="failed" )
# ----------------------------------------------Update Item------------------------------------------
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
