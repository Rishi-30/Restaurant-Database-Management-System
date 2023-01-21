from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import tkinter.messagebox as tm
from tkhtmlview import *
import mysql.connector as mc


win=Tk()
win.geometry('900x600')
win.title('The Big Barbeque')
win.config(bg='pink')


#Creating Labels
l1=Label(win,text='The Big Barbeque',bg='pink',fg='green',font=('forte',25,'bold'))
l1.place(x=25,y=35)

l2=Label(win,text='Biryani, North Indian, Mughlai, BBQ, Fast Food, Italian, Desserts',bg='pink',fg='purple',font=('eras demi itc',28))
l2.place(x=250,y=300)

l3=Label(win,text='ROYAPURAM, Chennai',fg='black',bg='pink',font=('forte',20,'bold'))
l3.place(x=600,y=400)

l4=Label(win, text = '**Timing**', bg = 'pink', fg = 'blue', font = ('calibri', 15, 'bold'))
l4.place(x =120,y=600)

l5=Label(win, text = '[Afternoon--12:00 pm to 3:30 pm]', bg = 'pink', fg = 'green', font =('calibri', 15, 'bold'))
l5.place(x=40,y =630)

l6=Label(win,text='[ Evening--06:30 pm to 10:30pm ]', bg='pink', fg='green', font=('calibri',15,'bold'))
l6.place(x=40,y=660)


#Creating Buttons:
def About():
    p=Toplevel(win)
    p.geometry('900x600')
    p.config(bg='white')
    p.title('About')
    a=Button(p,text='back',width=20,pady=7,command=p.destroy,bg='red')
    a.pack(side=BOTTOM)
    
    l7=Label(p,text='# Barbecue or barbeque (informally BBQ in the UK, US, and Canada, barbie in Australia and braai in South Africa)' ,fg='black',font=('calibri',15))
    l7.place(x=70,y=200)

    l8=Label(p,text='# Is a term used with significant regional and national variations to describe various cooking methods that use live fire and smoke to cook the food',fg='black',font=('calibri',15))
    l8.place(x=70,y=250)

    l9=Label(p,text='# The English word barbecue and its cognates in other languages come from the Native-American Taino word barbacoa.',fg='black',font=('calibri',15))
    l9.place(x=70,y=300)

    l10=Label(p,text='# Etymologists believe this to be derived from barabicu found in the language of the Arawak people of the Caribbean and the Timucua people of Florida',fg='black',font=('calibri',15))
    l10.place(x=70,y=350)
    
    l11=Label(p,text='# In American English usage in the Southern U.S, grilling refers to a fast process over high heat while barbecuing refers to a slow process using indirect heat or hot smoke',fg='black',font=('calibri',15))
    l11.place(x=70,y=400)

    l12=Label(p,text='# The term barbecue also refers to the meat being roasted.',fg='black',font=('calibri',15))
    l12.place(x=70,y=450)

    l13=Label(p,text='# In the modern barbecue smaller cuts of meat are dipped in or basted with a highly seasoned sauce. The type of meat and style of sauces reflect regional tastes.',fg='black',font=('calibri',15))
    l13.place(x=70,y=500)

    l14=Label(p,text='# BARBEQUE STYLES ARE AS DIVERSE AS THE LOYAL CROWDS that enjoy this popular American style of cooking, which originated in the southern and border states.',fg='black',font=('calibri',15))
    l14.place(x=70,y=550)

    l15=Label(p,text='WELCOME TO OUR GRAND RESTAURANT',fg='green',bg='pink',font=('algerian',20,'bold'))
    l15.place(x=70,y=50)

b1=Button(win,text='About', bg='skyblue',fg='black',width=5, padx=10, command=About, relief=RIDGE, font=('calibri',16,'bold'))
b1.place(x=350,y=55)


def Menu():
    q=Toplevel(win)
    q.geometry('900x600')
    q.config(bg='grey')
    q.title('Menu')
    b=Button(q,text='Back',width=20, pady=7, command=q.destroy, bg='red')
    b.pack(side=BOTTOM)

    l16=Label(q,text='🍗LUNCH🍗 & 🍽 DINNER 🍽',fg='white',bg='grey',font=('magneta',17,'bold'))
    l16.place(x=600,y=0)

    l17=Label(q,text='Mutton Biryani\t\t\t\tRs.340',fg='white',bg='grey',font=('lucida calligraphy',13,'bold'))
    l17.place(x=0,y=30)

    l18=Label(q,text='Chicken Biryani\t\t\t\tRs.240',fg='white',bg='grey',font=('lucida calligraphy',13,'bold'))
    l18.place(x=0,y=60)

    l19=Label(q,text='Spl Chicken Biryani\t\t\tRs.420',fg='white',bg='grey',font=('lucida calligraphy',13,'bold'))
    l19.place(x=0,y=90)

    l20=Label(q,text='Spl Mutton Biryani\t\t\tRs.560',fg='white',bg='grey',font=('lucida calligraphy',13,'bold'))
    l20.place(x=0,y=120)

    l21=Label(q,text='Extra Mutton\t\t\t\tRs.220',fg='white',bg='grey',font=('lucida calligraphy',13,'bold'))
    l21.place(x=0,y=150)

    l22=Label(q,text='Extra Chicken\t\t\t\tRs.145',fg='white',bg='grey',font=('lucida calligraphy',13,'bold'))
    l22.place(x=0,y=180)

    l23=Label(q,text='🐓Tandoori Non-Veg Starters🐓',fg='white', bg='grey', font=('lucida calligraphy',17,'bold'))
    l23.place(x=120,y=210)

    l24=Label(q,text='Tandoori Chicken Half(2 pcs)\t\tRs.200',fg='white',bg='grey',font=('lucida calligraphy',13,'bold'))
    l24.place(x=0,y=240)

    l25=Label(q,text='Shikari Murg Full(4 pcs)\t\t\tRs.360',fg='white',bg='grey',font=('lucida calligraphy',13,'bold'))
    l25.place(x=0,y=270)

    l26=Label(q,text='Shikari Murg Half(2 pcs)\t\t\tRs.200',fg='white',bg='grey',font=('lucida calligraphy',13,'bold'))
    l26.place(x=0,y=300)

    l27=Label(q,text='Chicken Multani Kabab(6 pcs)\t\tRs.260',fg='white',bg='grey',font=('lucida calligraphy',13,'bold'))
    l27.place(x=0,y=330)

    l28=Label(q,text='Chicken Reshmi Kabab(6 pcs)\t\tRs.230',fg='white',bg='grey',font=('lucida calligraphy',13,'bold'))
    l28.place(x=0,y=360)

    l22=Label(q,text='Chicken Tikka Kabab(6 pcs)\t\t\tRs.230',fg='white',bg='grey',font=('lucida calligraphy',13,'bold'))
    l22.place(x=0,y=390)

    l29=Label(q,text='Chicken Hariwali Kabab(6 pcs)\t\tRs.230',fg='white',bg='grey',font=('lucida calligraphy',13,'bold'))
    l29.place(x=0,y=420)

    l30=Label(q,text='Chicken Malai Kabab(6 pcs)\t\t\tRs.230',fg='white',bg='grey',font=('lucida calligraphy',13,'bold'))
    l30.place(x=0,y=450)

    l31=Label(q,text='Chicken Vatialy Kabab(6 pcs.)\t\tRs.260',fg='white',bg='grey',font=('lucida calligraphy',13,'bold'))
    l31.place(x=0,y=480)

    l32=Label(q,text='Chicken Banjara Kabab(6 pcs.)\t\tRs.230',fg='white',bg='grey',font=('lucida calligraphy',13,'bold'))
    l32.place(x=0,y=510)

    l33=Label(q,text='Tandoori Chicken Full(4 pcs)\t\t\tRs.360',fg='white',bg='grey',font=('lucida calligraphy',13,'bold'))
    l33.place(x=0,y=540)

    l34=Label(q,text='🥣 SOUPS 🥣', fg='white', bg='grey', font=('lucida calligraphy',17,'bold'))
    l34.place(x=120,y=570)

    l35=Label(q,text='Mutton soup \t\t\t\tRs.150', fg='white', bg='grey', font=('lucida calligraphy',13,'bold'))
    l35.place(x=0,y=600)

    l36=Label(q,text='Chicken soup \t\t\t\tRs.120', fg='white', bg='grey', font=('lucida calligraphy',13,'bold'))
    l36.place(x=0,y=630)

    l37=Label(q,text='Veg soup \t\t\t\tRs.100', fg='white', bg='grey', font=('lucida calligraphy',13,'bold'))
    l37.place(x=0,y=660)

    l38=Label(q,text='Mushroom soup \t\t\t\tRs.130', fg='white', bg='grey', font=('lucida calligraphy',13,'bold'))
    l38.place(x=0,y=690)

    l39=Label(q,text='🍦ICE CREAMS🍦', fg='white', bg='grey', font=('lucida calligraphy',17,'bold'))
    l39.place(x=850,y=30)

    l40=Label(q,text='Vanilla ice creams\t\t\tRs.30',fg='white',bg='grey',font=('lucida calligraphy',13,'bold'))
    l40.place(x=750,y=60)

    l41=Label(q,text='Black Berry ice creams\t\tRs.50',fg='white',bg='grey',font=('lucida calligraphy',13,'bold'))
    l41.place(x=750,y=90)

    l42=Label(q,text='ChocoBar ice creams\t\tRs.40',fg='white',bg='grey',font=('lucida calligraphy',13,'bold'))
    l42.place(x=750,y=120)

    l43=Label(q,text='Nutty Bar ice creams\t\tRs.90',fg='white',bg='grey',font=('lucida calligraphy',13,'bold'))
    l43.place(x=750,y=150)

    l44=Label(q,text='Strawberry ice creams\t\tRs.30',fg='white',bg='grey',font=('lucida calligraphy',13,'bold'))
    l44.place(x=750,y=180)

    l45=Label(q,text='ButterScotch ice creams\t\tRs.30',fg='white',bg='grey',font=('lucida calligraphy',13,'bold'))
    l45.place(x=750,y=210)

    l47=Label(q,text='🥤SOFT DRINKS🥤',fg='white',bg='grey',font=('lucida calligraphy',17,'bold'))
    l47.place(x=850,y=240)

    l48=Label(q,text='PEPSI\t\t\t\tRs.40',fg='white',bg='grey',font=('lucida calligraphy',13,'bold'))
    l48.place(x=750,y=270)

    l49=Label(q,text='COCA COLA\t\t\tRs.40',fg='white',bg='grey',font=('lucida calligraphy',13,'bold'))
    l49.place(x=750,y=300)

    l50=Label(q,text='FANTA\t\t\t\tRs.40',fg='white',bg='grey',font=('lucida calligraphy',13,'bold'))
    l50.place(x=750,y=330)

    l51=Label(q,text='MIRINDA\t\t\tRs.40',fg='white',bg='grey',font=('lucida calligraphy',13,'bold'))
    l51.place(x=750,y=360)

    l52=Label(q,text='BOVONTO\t\t\tRs.40',fg='white',bg='grey',font=('lucida calligraphy',13,'bold'))
    l52.place(x=750,y=390)

b2=Button(win,text='Menu', bg='skyblue', fg='black', width=5, padx=10, command=Menu, relief=RIDGE, font=('calibri',16,'bold'))
b2.place(x=500,y=55)


def Gallery():
    r=Toplevel(win)
    r.geometry('900x600')
    r.config(bg='royal blue')
    r.title('Gallery')
    c=Button(r,text='Back', width=20, pady=7, command=r.destroy, bg='red')
    c.pack(side=BOTTOM)

    l53=HTMLLabel(r,html='<img src="C:/Users/Sakthish Kumar/Downloads/res.jpeg">')
    l53.place(x=100,y=80,width=300,height=200)

    l54=HTMLLabel(r,html='<img src="C:/Users/Sakthish Kumar/Downloads/res1.jpeg">')
    l54.place(x=1000,y=80,width=300,height=200)

    l55=HTMLLabel(r,html='<img src="C:/Users/Sakthish Kumar/Downloads/res2.jpeg">')
    l55.place(x=100,y=400,width=300,height=200)

    l56=HTMLLabel(r,html='<img src="C:/Users/Sakthish Kumar/Downloads/res3.jpg">')
    l56.place(x=1000,y=400,width=300,height=200)

b3=Button(win,text='Gallery', bg='skyblue',fg='black',width=5,padx=10,command=Gallery,relief=RIDGE,font=('calibri',14,'bold'))
b3.place(x=750,y=55)


def Offers():
    s=Toplevel(win)
    s.geometry('900x600')
    s.config(bg='white')
    s.title('Offers')
    d=Button(s,text='Back', width=20, pady=7, command=s.destroy, bg='red')
    d.pack(side=BOTTOM)

    
    l57=Label(s,text='Coupon Details',fg='white',bg='royal blue',font=('calibri',20,'bold'))
    l57.place(x=50,y=0)

    l58=Label(s,text='Get Upto 10% OFF on paying via PAYtm',fg='red',bg='lavender',font=('magneta',16,'bold'))
    l58.place(x=0,y=50)

    l59=Label(s,text='* Special Combo will be provided for barbecue card holders',fg='black',bg='lavender',font=('magneta',16,'bold'))
    l59.place(x=0,y=100)

    l60=Label(s,text='* FLAT 10% OFF for more than Rs.1500 Foods',fg='black',bg='lavender',font=('magneta',16,'bold'))
    l60.place(x=0,y=130)

    l61=Label(s,text='* Other Terms & Conditions applied',fg='black',bg='lavender',font=('magneta',16,'bold'))
    l61.place(x=0,y=160)

    l62=Label(s,text='Get 12% OFF for credit card holders cashback',fg='red',bg='lavender',font=('magneta',16,'bold'))
    l62.place(x=0,y=200)

    l63=Label(s,text='* Offer applicable for credit card holders',fg='black',bg='lavender',font=('magneta',16,'bold'))
    l63.place(x=0,y=230)

    l64=Label(s,text='* Assured Cashback : Rs. 200',fg='black',bg='lavender',font=('magneta',16,'bold'))
    l64.place(x=0,y=260)

    l65=Label(s,text='* Other Terms & Conditions applied',fg='black',bg='lavender',font=('magneta',16,'bold'))
    l65.place(x=0,y=290)

    l66=Label(s,text='Free complimentary sweets for customers',fg='red',bg='lavender',font=('magneta',16,'bold'))
    l66.place(x=0,y=340)

    l67=Label(s,text='(1 unit of sweets is free on orders above Rs.500)',fg='black',bg='lavender',font=('magneta',16,'bold'))
    l67.place(x=0,y=370)

    l68=Label(s,text='* Offer will be provided automatically',fg='black',bg='lavender',font=('magneta',16,'bold'))
    l68.place(x=0,y=400)

    l69=Label(s,text='* Other Terms & Conditons are applied',fg='black',bg='lavender',font=('magneta',16,'bold'))
    l69.place(x=0,y=460)

    l70=Label(s,text='* If you have added the free item already, its price will be reduced from the bill.',fg='black',bg='lavender',font=('magneta',16,'bold'))
    l70.place(x=0,y=430)
    


b4=Button(win,text='Offers', bg='skyblue',fg='black',width=5,padx=10,command=Offers,relief=RIDGE,font=('calibri',14,'bold'))
b4.place(x=900,y=55)

def BookAtable():
    t=Toplevel(win)
    t.geometry('900x600')
    t.config(bg='sky blue')
    t.title('BookAtable')
    
    def Submit(*args):
        e=i_Name.get()
        e1=i_MobileNo.get()
        e2=i_MailID.get()
        e3=i_TableNumber.get()
        e4=i_TableType.get()
        e5=i_Date_Time.get()
        conn = mc.connect(host="localhost",user="root", password="",database="rk")
        cur = conn.cursor()
        cur.execute("insert into booking(Name, MobileNo, MailID, TableNumber, TableType,Date_Time) values('"+e+"','"+e1+"', '"+e2+"', '"+e3+"','"+e4+"','"+e5+"')")   
        conn.close()   
    
    i_Name = StringVar()   
    i_MobileNo = StringVar()
    i_MailID = StringVar()
    i_TableNumber = StringVar()
    i_TableType = StringVar()
    i_Date_Time = StringVar()
    

    l71=Label(t,text='Name', fg='black', bg='sky blue', font=('Times',16,'bold')).place(x=10,y=50)
    e1=Entry(t,width=25,textvar=i_Name,fg='black',font=('Times',16,'bold')).place(x=150,y=50)

    l72=Label(t,text='MobileNo', fg='black', bg='sky blue', font=('Times',16,'bold')).place(x=10,y=100)
    e2=Entry(t,width=25,textvar=i_MobileNo, fg='black', font=('Times',16,'bold')).place(x=150,y=100)

    l73=Label(t,text='MailID', fg='black', bg='sky blue', font=('Times',16,'bold')).place(x=10,y=150)
    e3=Entry(t,width=25, textvar=i_MailID, fg='black', font=('Times',16,'bold')).place(x=150,y=150)

    l74=Label(t,text='TableNumber', fg='black', bg='sky blue', font=('Times',16,'bold')).place(x=10,y=200)

    c1=ttk.Combobox(t,textvar=i_TableNumber,width=25, font=('Times',16,'bold'))
    c1['values']=('01','02','03','04','05','06','07','08','09','10','11','12')
    c1.place(x=150,y=200)
    
    l75=Label(t,text='TableType', fg='black', bg='sky blue', font=('Times',16,'bold'))
    l75.place(x=10,y=250)

    combo= ttk.Combobox(t,textvar=i_TableType, width=25, font=('Times',16,'bold'))
    combo['values']=('Family Table','Couples Table','Kidz Table')
    combo.place(x=150,y=250)

    l76=Label(t,text='Date_Time', fg='black', bg='sky blue', font=('Times',16,'bold')).place(x=10,y=300)
    e5=Entry(t,width=25, textvar=i_Date_Time, fg='black', font=('Times',16,'bold')).place(x=150,y=300)

    e1=Button(t,text='Submit',width=20,pady=7,command = Submit,bg='green').place(x=700,y=650)
    
    def Back():
        t.destroy()
    e=Button(t,text='Back', width=20, pady=7, command=t.destroy, bg='red')
    e.place(x=500,y=650)
    
b5=Button(win,text='BookAtable', bg='skyblue', fg='black', width=15, padx=10, command=BookAtable, relief=RIDGE, font=('calibri',14,'bold'))
b5.place(x=1100,y=55)   


def Exit():
    win.destroy()
    
b7=Button(win,text='Exit',bg='red',fg='white',width=5,padx=10, command=Exit, relief=RIDGE, bd=5, font=('times',10,'bold'))
b7.place(x=1350,y=55)

win.mainloop()
        


 
