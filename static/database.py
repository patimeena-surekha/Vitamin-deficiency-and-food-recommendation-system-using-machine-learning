import sqlite3
import hashlib
import datetime
import MySQLdb
from flask import session
from datetime import datetime


def db_connect():
    _conn = MySQLdb.connect(host="localhost", user="root",
                            passwd="", db="userbehaviour")
    c = _conn.cursor()

    return c, _conn

# -------------------------------Loginact-----------------------------------------------------------------
def admin_loginact(username, password):
    try:
        c, conn = db_connect()
        j = c.execute("select * from admin where username='" +
                      username+"' and password='"+password+"'")
        c.fetchall()
        conn.close()
        return j
    except Exception as e:
        return(str(e))

def user_loginact(username, password):
    try:
        c, conn = db_connect()
        j = c.execute("select * from user where username='" +
                      username+"' and password='"+password+"'")
        data = c.fetchall()
        # for a in data:
        #   session['uname'] = a[0]
       
        c.fetchall()
        conn.close()
        return j
    except Exception as e:
        return(str(e))

def analyst_loginact(username, password):
    try:
        c, conn = db_connect()
        j = c.execute("select * from analyst where username='" +
                      username+"' and password='"+password+"'")
        c.fetchall()
        conn.close()
        return j
    except Exception as e:
        return(str(e))
#-------------------------------------register---------------------------------------------------
def user_reg(id,username, password, email, dob, gender, address, mobile):
    try:
        c, conn = db_connect()
        print(id,username, password, email, dob,
              gender, address, mobile)
        j = c.execute("insert into user (id,username,password,email,dob,gender,address,mobile) values ('"+id+"','"+username +
                      "','"+password+"','"+email+"','"+dob+"','"+gender+"','"+address+"','"+mobile+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))
#--------------------------------------------view----------------------------------------------
def admin_viewusers():
    c, conn = db_connect()
    c.execute("select username,email,gender,address,status from user")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

def admin_viewproducts():
    c, conn = db_connect()
    c.execute("select * from products")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

def admin_viewpurchaseproducts():
    c, conn = db_connect()
    c.execute("select * from purchasedproducts")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

def admin_viewrecommedns():
    c, conn = db_connect()
    c.execute("select * from recommends")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

def admin_cate():
    c, conn = db_connect()
    c.execute("select * from category")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

def user_viewaccuont():
    c, conn = db_connect()
    username=  session['username']
    c.execute("select * from accountdetails where username='"+username+"'")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

def user_search(category):
    c, conn = db_connect()
    
    c.execute("select * from products where category='"+category+"'")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

def user_productsact(productname):
    c, conn = db_connect()
    
    c.execute("select * from products where productname='"+productname+"'")
    result = c.fetchall()
   
    conn.close()
    print("result")
    return result

def user_recommend(productname):
    c, conn = db_connect()
    
    c.execute("select * from products where productname='"+productname+"'")
    result = c.fetchall()
    c.execute("select username from user ")
    result1 = c.fetchall()
    conn.close()
    print("result")
    return result,result1

def user_viewrecommend():
    c, conn = db_connect()
    username=  session['username']
    c.execute("select * from recommends where username='"+username+"'")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

def user_viewcart():
    c, conn = db_connect()
    username=  session['username']
    c.execute("select category,productname,price,image from cart where username='"+username+"'")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

def user_viewcatp():
    c, conn = db_connect()
    username=  session['username']
    c.execute("select productname,category,price,image from cart where username='"+username+"'")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

def user_viewpurchase():
    c, conn = db_connect()
    username=  session['username']
    c.execute("select * from purchasedproducts where username='"+username+"'")
    result = c.fetchall()
    conn.close()
    print("result")
    return result
#-------------------------------------accept and reject-------------------------------------------------
def uviewact(username, email,gender):
    c, conn = db_connect()
    j = c.execute("update user set status='Accepted' where username='"+username+"'")
    conn.commit()
    conn.close()
    return j

def uviewdeact(username, email,gender):
    c, conn = db_connect()
    j = c.execute("update user set status='Rejected' where username='"+username+"'")
    conn.commit()
    conn.close()
    return j

def admin_adelete(category,productname,price):
    c, conn = db_connect()
    j = c.execute("delete from products where category='"+category+"' and productname='"+productname+"' and price='"+price+"'")
    conn.commit()
    conn.close()
    return j


#----------------------------------------Add-----------------------------------------------------------
def add_categoryact(id, category):
    c, conn = db_connect()
    print(id, category)
    j = c.execute("insert into category (id,category) values ('" + id + "','" +
                  category + "')")
    conn.commit()
    conn.close()
    return j

def add_productact(id, category,productname,description,price,brand,image):
    c, conn = db_connect()
    print(id, category)
    j = c.execute("insert into category (id,category,productname,description,price,brand,image) values ('" + id + "','" +
                  category + "','" + productname + "','" + description + "','" + brand + "','" + image + "')")
    conn.commit()
    conn.close()
    return j

def add_addacountdetailsact(username, branch,email,address,mobile,amount):
    c, conn = db_connect()
   
    j = c.execute("insert into accountdetails (username,branch,email,address,mobile,amount) values ('" +
                  username + "','" + branch + "','" + email + "','" + address + "','" + mobile + "','" + amount + "')")
    
    conn.commit()
    conn.close()
    return j

def add_moneyact(username,amount):
    c, conn = db_connect()
    print(amount)
    c.execute("select amount from  accountdetails where username='"+username+"'")
    data=c.fetchall()
    print(data)

    b=int(amount)
    
    d=int(data[0][0])
    t=int(b+d)
   
    print(amount)
    print(t)
    j = c.execute("update accountdetails set amount="+str(t)+" where username='"+username+"'")
    conn.commit()
    conn.close()
    return j

def add_cartact(category,productname,price,image):
    c, conn = db_connect()
    username=  session['username']
    j = c.execute("insert into cart (username,category,productname,price,image) values ('" +
                  username + "','" + category + "','" + productname + "','" + price + "','" + image + "')")
    
    conn.commit()
    conn.close()
    return j

def purchase1(productname,category,price,image):
    c, conn = db_connect()
    username=  session['username']
    c.execute("select amount from  accountdetails where username='"+username+"'")
    data = c.fetchall()
    x=int(price)
    
    y=int(data[0][0])
    z=int(y-x)
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    j = c.execute("insert into purchasedproducts (username,category,productname,price,dt,image) values ('" +
                  username + "','" + category + "','" + productname + "','" + price + "','" + dt_string + "','" + image + "')")

    j = c.execute("update accountdetails set amount="+str(z)+" where username='"+username+"'")
    
    conn.commit()
    conn.close()
    return j

def remove1(productname,category,price,image):
    c, conn = db_connect()
    username=  session['username']
    j = c.execute("delete from cart where username='"+username+"' and productname='"+productname+"' ")
    
    conn.commit()
    conn.close()
    return j

def user_rateact(productname,category,review,rating):
    c, conn = db_connect()
    username=  session['username']
    j = c.execute("insert into reviews(username,productname,category,review,rating) values ('" +
                  username + "','" + productname + "','" + category + "','" + review + "','" + rating + "')")
    
    conn.commit()
    conn.close()
    return j
# ----------------------------------------------Update Items------------------------------------------


if __name__ == "__main__":
    print(db_connect())
