from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import Tk, Canvas, NW,Tk, Text, Entry, Button, messagebox, ttk
import psycopg2.extras
from database_connection import DatabaseCon

#We make window settings here.
root = Tk()
root.title("Tez App")
root.configure(bg="black")

pencere_genisligi = 1300  
pencere_yuksekligi = 700  
root.geometry(f"{pencere_genisligi}x{pencere_yuksekligi}")

canvas = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
canvas.pack()

#The background image is here.
resimbg = ImageTk.PhotoImage(Image.open('img//bos.png'))
canvas.create_image(0, 0, anchor=NW, image=resimbg)


#We defined the search function here.
def find():

    db_connection = DatabaseCon()
    try:

        search = entry_search.get()

        search_query = search
        if search_query is not None:
            query = f'(SELECT * FROM public."Thesis" WHERE "TITLE" LIKE %s)'
            db_connection.cur.execute(query, ('%' + search_query + '%',))

        else:
            print(error)

        for record in db_connection.cur.fetchall():

            thesisno_text = record['THESIS_NO']
            authorid_text = record['AUTHOR_ID']
            year_text = record['YEAR']
            title_text = record['TITLE']
            typeid_text = record['TYPE_ID']
            subject_text = record['SUBJECT']            
            
            
            
            text_thesis_no2.insert("end", f"   {thesisno_text}\n\n\n")
            text_author2.insert("end", f"{authorid_text}\n\n\n")
            text_year2.insert("end", f"{year_text}\n\n\n")
            text_title2.insert("end", f"{title_text}\n\n\n")
            text_type2.insert("end", f"{typeid_text}\n\n\n")
            text_subject2.insert("end", f"{subject_text}\n\n\n")


        db_connection.conn.commit()

        db_connection.conn.close()


    except Exception as error:
        print(error)
    finally:
        db_connection.close_connection()

    
    
    picture_searchpage.place(width=303, height=48, x=508, y=75)
    
    buttonfind.place_forget()
    buttonlogin.place_forget()
    
    picture_date.place_forget()
    picture_mainpage.place_forget()
    
    entry_date.place_forget()

    picture_search_thesis.place_forget()

    entry_search.place_forget()

    buttonthesis.place(width=135, height=110, x=1137, y=47)
    
    
    text_thesis_no.place(width=94, height=46, x=0, y=204)
    text_author.place(width=176, height=46, x=94, y=204)
    text_year.place(width=94, height=46, x=270, y=204)
    text_title.place(width=661, height=46, x=639, y=204)
    text_type.place(width=115, height=46, x=524, y=204)
    text_subject.place(width=160, height=46, x=364, y=204)
    
    
    text_thesis_no2.place(width=97, height=450, x=0, y=250)
    text_author2.place(width=176, height=450, x=94, y=250)
    text_year2.place(width=94, height=450, x=270, y=250)
    text_title2.place(width=661, height=450, x=639, y=250)
    text_type2.place(width=115, height=450, x=524, y=250)
    text_subject2.place(width=160, height=450, x=364, y=250)
    
    checkbox.place(width=20, height=20, x=5, y=252)
    checkbox2.place(width=20, height=20, x=5, y=297)
    
    
#We defined the function of the return button here.
def home():
    buttonhome.place_forget()
    buttonlogin2.place_forget()
    buttonaddthesis.place_forget()
    buttonupdate.place_forget()
    
    picture_date.place_forget()
    picture_thesispage.place_forget()
    entry_date.place_forget()
    

    picture_username.place_forget()
    picture_password.place_forget()
    picture_thesisadd.place_forget()

    entry_username.place_forget()
    entry_password.place_forget()
    
    text_thesis_no.place_forget()
    text_author.place_forget()
    text_year.place_forget()
    text_title.place_forget()
    text_type.place_forget()
    text_subject.place_forget()
    
    text_thesis_no2.place_forget()
    text_author2.place_forget()
    text_year2.place_forget()
    text_title2.place_forget()
    text_type2.place_forget()
    text_subject2.place_forget()
    text_thesis.place_forget()
    text_thesis.place_forget()
    text_thesis_no3.place_forget()
    
    
    

    buttonlogin.place(width=291, height=161, x=976, y=22)
    buttonfind.place(width=343, height=130, x=492, y=554)

    picture_search_thesis.place(width=345, height=44, x=495, y=286)

    entry_search.place(width=649, height=94, x=325, y=402)
 
#The function we use to read the theses after searching for them.
def readthesis():
        
    buttonhome.place(width=135, height=110, x=1137, y=47)
    
    picture_thesispage.place(width=166, height=40, x=555, y=86)
    
    picture_searchpage.place_forget()
    
    buttonthesis.place_forget()
    
    checkbox.place_forget()
    checkbox2.place_forget()
    
    text_thesis.place(width=1203, height=496, x=97, y=204)
    text_thesis_no3.place(width=97, height=496, x=0, y=204)
    
    db_connection = DatabaseCon()
    try:

        search = entry_search.get()

        search_query = search
        if search_query is not None:
            query = f'(SELECT * FROM public."Thesis" WHERE "TITLE" LIKE %s)'
            db_connection.cur.execute(query, ('%' + search_query + '%',))

        else:
            print(error)

        for record in db_connection.cur.fetchall():

            thesisno_text = record['THESIS_NO']
            thesis_text = record['ABSTRACT']



            text_thesis_no3.insert("end", f"ID:{thesisno_text}\n\n\n\n\n\n")
            text_thesis.insert("end", f"{thesis_text}\n\n\n\n")


        db_connection.conn.commit()

        db_connection.conn.close()


    except Exception as error:
        print(error)
    finally:
        db_connection.close_connection()
    

    
#We defined the function of the login button here.  
def login():
    buttonfind.place_forget()
    buttonlogin.place_forget()
    
    picture_date.place_forget()
    entry_date.place_forget()
    
    picture_search_thesis.place_forget()
    picture_mainpage.place_forget()

    entry_search.place_forget()

    buttonhome.place(width=135, height=110, x=1137, y=47)
    buttonlogin2.place(width=350, height=123, x=500, y=566)
    
    picture_username.place(width=303, height=41, x=515, y=220)
    picture_password.place(width=317, height=41, x=508, y=404)

    entry_username.place(width=649, height=94, x=342, y=267)
    entry_password.place(width=649, height=94, x=342, y=456)

    
#We defined the function of the login button 2 here.  
def login2():
    
    kullanici_adi = entry_username.get()
    sifre = entry_password.get()

    if kullanici_adi == "volkan" and sifre == "tunali":
        buttonlogin2.place_forget()
        buttongeri.place_forget()
        buttonnext.place_forget()
        buttonadd.place_forget()
        buttonupdate2.place_forget()
    
        picture_username.place_forget()
        picture_password.place_forget()
        picture_language.place_forget()
        picture_thesisname.place_forget()
        picture_subject.place_forget()
        picture_university.place_forget()
        picture_ınstitute.place_forget()
        picture_type.place_forget()
        picture_year.place_forget()
        picture_pages.place_forget()
        picture_supervisor.place_forget()
        picture_co.place_forget()
        picture_keyword.place_forget()
        picture_abstract.place_forget()
        picture_thesis2.place_forget()
        picture_name.place_forget()
        picture_surname.place_forget()
        picture_mail.place_forget()
        picture_university2.place_forget()
        picture_ınstitute2.place_forget()
        picture_rank.place_forget()
        picture_thesisadd.place_forget()
        picture_up.place_forget()

        entry_username.place_forget()
        entry_password.place_forget()
        combo_language.place_forget()
        entry_thesis_name.place_forget()
        entry_subject.place_forget()
        combo_university.place_forget()
        combo_institute.place_forget()
        combo_type.place_forget()
        entry_year.place_forget()
        entry_pages.place_forget()
        combo_supervisor.place_forget()
        combo_co.place_forget()
        combo_keyword.place_forget()
        entry_abstract.place_forget()
        entry_thesis.place_forget()
        entry_name.place_forget()
        entry_surname.place_forget()
        entry_mail.place_forget()
        combo_university2.place_forget()
        combo_institute2.place_forget()
        combo_rank.place_forget()
        
        picture_date.place_forget()
        entry_date.place_forget()

        buttonaddthesis.place(width=582, height=143, x=38, y=350)
        buttonupdate.place(width=582, height=143, x=669, y=350)
        buttonhome.place(width=135, height=110, x=1137, y=47)
    else:
        messagebox.showerror("Error", "Username or password is incorrect!")
    
    

#We defined the function of the add thesis button here.
def add_thesis():
    buttonaddthesis.place_forget()
    buttonupdate.place_forget()
    buttonhome.place_forget()
    
    picture_date.place_forget()
    entry_date.place_forget()
    

    buttonnext.place(width=287, height=132, x=982, y=41)

    picture_language.place(width=241, height=48, x=70, y=234)
    picture_thesisname.place(width=316, height=48, x=70, y=376)
    picture_subject.place(width=193, height=48, x=793, y=243)
    picture_university.place(width=246, height=48, x=70, y=528)
    picture_ınstitute.place(width=203, height=60, x=792, y=388)
    picture_type.place(width=128, height=60, x=792, y=528)
    picture_thesisadd.place(width=272, height=43, x=502, y=76)

    combo_language.place(width=371, height=54, x=71, y=296)
    entry_thesis_name.place(width=371, height=54, x=71, y=454)
    entry_subject.place(width=371, height=54, x=793, y=296)
    combo_university.place(width=371, height=54, x=71, y=598)
    combo_institute.place(width=371, height=54, x=793, y=454)
    combo_type.place(width=371, height=54, x=792, y=598)


#We defined the function of the next page1 button here.   
def nextpage1():
    buttonnext.place_forget()

    picture_username.place_forget()
    picture_password.place_forget()
    picture_language.place_forget()
    picture_thesisname.place_forget()
    picture_subject.place_forget()
    picture_university.place_forget()
    picture_ınstitute.place_forget()
    picture_type.place_forget()
    
    picture_date.place_forget()
    entry_date.place_forget()

    entry_username.place_forget()
    entry_password.place_forget()
    combo_language.place_forget()
    entry_thesis_name.place_forget()
    entry_subject.place_forget()
    combo_university.place_forget()
    combo_institute.place_forget()
    combo_type.place_forget()

    buttonnext2.place(width=287, height=132, x=982, y=41)

    picture_year.place(width=134, height=40, x=47, y=249)
    picture_pages.place(width=425, height=48, x=60, y=366)
    picture_supervisor.place(width=264, height=47, x=711, y=252)
    picture_co.place(width=361, height=47, x=708, y=369)
    picture_keyword.place(width=218, height=40, x=57, y=482)
    picture_abstract.place(width=218, height=40, x=711, y=485)

    entry_year.place(width=371, height=54, x=60, y=296)
    entry_pages.place(width=371, height=54, x=60, y=413)
    combo_supervisor.place(width=371, height=54, x=711, y=299)
    combo_co.place(width=371, height=54, x=711, y=416)
    combo_keyword.place(width=371, height=142, x=60, y=529)
    entry_abstract.place(width=371, height=142, x=711, y=529)

#We defined the function of the next page2 button here.
def nextpage2():
    buttonnext2.place_forget()
    
    picture_year.place_forget()
    picture_pages.place_forget()
    picture_supervisor.place_forget()
    picture_co.place_forget()
    picture_keyword.place_forget()
    picture_abstract.place_forget()

    entry_year.place_forget()
    entry_pages.place_forget()
    combo_supervisor.place_forget()
    combo_co.place_forget()
    combo_keyword.place_forget()
    entry_abstract.place_forget()
    
    picture_date.place_forget()
    entry_date.place_forget()

    buttonadd.place(width=292, height=102, x=960, y=417)
    buttongeri.place(width=150, height=150, x=1115, y=27)


    picture_thesis2.place(width=216, height=40, x=67, y=370)
    picture_date.place(width=413, height=45, x=91, y=230)

    entry_thesis.place(width=840, height=211, x=94, y=436)
    entry_date.place(width=410, height=64, x=94, y=286)
    
    
#We defined the function of the add thesis page button here.
def add():

    db_connection = DatabaseCon()
    try:
        language1 = combo_language.get()
        language1_id = int(language1.split('-')[0].strip())
        
        thesisname = entry_thesis_name.get()
        
        university2 = combo_university.get()
        university2_id = int(university2.split('-')[0].strip())
        
        subject = entry_subject.get()
        
        institute2 = combo_institute.get()
        institute2_id = int(institute2.split('-')[0].strip())
        
        type = combo_type.get()
        type_id = int(type.split('-')[0].strip())
        
        year = entry_year.get()
        pages = entry_pages.get()
        
        keyword = combo_keyword.get()
        keyword_id = int(keyword.split('-')[0].strip())
    
        supervisor = combo_supervisor.get()
        supervisor_id = int(supervisor.split('-')[0].strip())
        
        co = combo_co.get()
        co_id = int(co.split('-')[0].strip())
        
        abstract = entry_abstract.get()
        submissiondate = entry_date.get()
        kullanici_adi = 100
        

        insert_script = '''INSERT INTO public."Thesis" 
        ("AUTHOR_ID", "SUPERVISOR_ID", "UNIVERSITY_ID", "LANGUAGE_ID", "TYPE_ID", "TITLE", "INSTITUTES_ID", "NUMBER_OF_PAGES", "SUBJECT", "ABSTRACT", "YEAR", "COSUPERVISOR_ID", "SUBMISSION_DATE", "KEYWORD_ID") VALUES 
        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''

        insert_values = [(kullanici_adi, supervisor_id, university2_id, language1_id, type_id, thesisname, institute2_id, pages, subject, abstract, year, co_id, submissiondate, keyword_id)]

        for record in insert_values:
            db_connection.cur.execute(insert_script, record)

        db_connection.conn.commit()
    except Exception as error:
        print(error)
    finally:
        db_connection.close_connection()
        
    
    buttonlogin2.place_forget()
    buttongeri.place_forget()
    buttonnext.place_forget()
    buttonadd.place_forget()
    
    picture_username.place_forget()
    picture_password.place_forget()
    picture_language.place_forget()
    picture_thesisname.place_forget()
    picture_subject.place_forget()
    picture_university.place_forget()
    picture_ınstitute.place_forget()
    picture_type.place_forget()
    picture_year.place_forget()
    picture_pages.place_forget()
    picture_supervisor.place_forget()
    picture_co.place_forget()
    picture_keyword.place_forget()
    picture_abstract.place_forget()
    picture_thesis2.place_forget()
    picture_date.place_forget()
    picture_thesisadd.place_forget()

    entry_username.place_forget()
    entry_password.place_forget()
    combo_language.place_forget()
    entry_thesis_name.place_forget()
    entry_subject.place_forget()
    combo_university.place_forget()
    combo_institute.place_forget()
    combo_type.place_forget()
    entry_year.place_forget()
    entry_pages.place_forget()
    combo_supervisor.place_forget()
    combo_co.place_forget()
    combo_keyword.place_forget()
    entry_abstract.place_forget()
    entry_thesis.place_forget()
    entry_date.place_forget()

    buttonaddthesis.place(width=582, height=143, x=38, y=350)
    buttonupdate.place(width=582, height=143, x=669, y=350)
    buttonhome.place(width=135, height=110, x=1137, y=47)




#We defined the function of the update thesis page button here.
def update_thesis():
      
    
    buttonaddthesis.place_forget()
    buttonupdate.place_forget()
    buttonhome.place_forget()

    buttonupdate2.place(width=552, height=125, x=638, y=477)

    buttongeri.place(width=150, height=150, x=1119, y=27)

    picture_name.place(width=144, height=35, x=60, y=225)
    picture_surname.place(width=222, height=35, x=57, y=334)
    picture_mail.place(width=159, height=35, x=57, y=442)
    picture_university2.place(width=247, height=39, x=60, y=559)
    picture_ınstitute2.place(width=205, height=35, x=648, y=228)
    picture_rank.place(width=144, height=35, x=638, y=334)
    picture_up.place(width=332, height=105, x=503, y=45)

    entry_name.place(width=371, height=54, x=60, y=267)
    entry_surname.place(width=371, height=54, x=60, y=371)
    entry_mail.place(width=371, height=54, x=60, y=482)
    combo_university2.place(width=371, height=54, x=60, y=602)
    combo_institute2.place(width=371, height=54, x=648, y=267)
    combo_rank.place(width=371, height=54, x=648, y=371)

#We defined the function of the update thesis button here.
def update():

    db_connection = DatabaseCon()

    try:
        name = entry_name.get()
        surname = entry_surname.get()   
        mail1 = entry_mail.get()
        
        university = combo_university2.get()
        university_id = int(university.split('-')[0].strip())
        
        institute = combo_institute2.get()
        institute_id = int(institute.split('-')[0].strip())
        
        rank = combo_rank.get()
        rank_id = int(rank.split('-')[0].strip())
        
    

        insert_script = '''INSERT INTO public."Person" ("PERSON_FNAME", "PERSON_LNAME", "PERSON_EMAIL", "UNIVERSITY_ID", "PERSON_RANK")  VALUES (%s,%s,%s,%s,%s)'''
        insert_values = [(name, surname, mail1, university_id, rank_id)]
        for record in insert_values:
            db_connection.cur.execute(insert_script, record)

        db_connection.conn.commit()
    except Exception as error:
        print(error)
    finally:

        db_connection.close_connection()
    
    buttonlogin2.place_forget()
    buttongeri.place_forget()
    buttonnext.place_forget()
    buttonadd.place_forget()
    buttonupdate2.place_forget()
    
    picture_username.place_forget()
    picture_password.place_forget()
    picture_language.place_forget()
    picture_thesisname.place_forget()
    picture_subject.place_forget()
    picture_university.place_forget()
    picture_ınstitute.place_forget()
    picture_type.place_forget()
    picture_year.place_forget()
    picture_pages.place_forget()
    picture_supervisor.place_forget()
    picture_co.place_forget()
    picture_keyword.place_forget()
    picture_abstract.place_forget()
    picture_thesis2.place_forget()
    picture_name.place_forget()
    picture_surname.place_forget()
    picture_mail.place_forget()
    picture_university2.place_forget()
    picture_ınstitute2.place_forget()
    picture_rank.place_forget()
    picture_up.place_forget()

    entry_username.place_forget()
    entry_password.place_forget()
    combo_language.place_forget()
    entry_thesis_name.place_forget()
    entry_subject.place_forget()
    combo_university.place_forget()
    combo_institute.place_forget()
    combo_type.place_forget()
    entry_year.place_forget()
    entry_pages.place_forget()
    combo_supervisor.place_forget()
    combo_co.place_forget()
    combo_keyword.place_forget()
    entry_abstract.place_forget()
    entry_thesis.place_forget()
    entry_name.place_forget()
    entry_surname.place_forget()
    entry_mail.place_forget()
    combo_university2.place_forget()
    combo_institute2.place_forget()
    combo_rank.place_forget()

    buttonaddthesis.place(width=582, height=143, x=38, y=350)
    buttonupdate.place(width=582, height=143, x=669, y=350)
    buttonhome.place(width=135, height=110, x=1137, y=47)



#We defined the function of the some database connection here.
def fetch_rank_options():
    db_connection = DatabaseCon()

    try:
        
        query = 'SELECT "RANK_ID", "RANK_NAME" FROM public."Rank"'
        db_connection.cur.execute(query)
        ranks = db_connection.cur.fetchall()

        rank_options = [f"{rank[0]} - {rank[1]}" for rank in ranks]

        combo_rank['values'] = rank_options
    except Exception as error:
        print(error)
    finally:
        db_connection.close_connection()
        
        
        
        
 
def fetch_university_options():
    db_connection = DatabaseCon()

    try:
        query = 'SELECT "UNIVERSITY_ID", "UNIVERSITY_NAME" FROM public."University"'
        db_connection.cur.execute(query)
        options = [f"{option[0]} - {option[1]}" for option in db_connection.cur.fetchall()]

        combo_university['values'] = options
    except Exception as error:
        print(error)
    finally:
        db_connection.close_connection()


def fetch_university2_options():
    db_connection = DatabaseCon()

    try:
        query = 'SELECT "UNIVERSITY_ID", "UNIVERSITY_NAME" FROM public."University"'
        db_connection.cur.execute(query)
        options = [f"{option[0]} - {option[1]}" for option in db_connection.cur.fetchall()]

        combo_university2['values'] = options
    except Exception as error:
        print(error)
    finally:
        db_connection.close_connection()


def fetch_language_options():
    db_connection = DatabaseCon()

    try:
        query = 'SELECT "LANGUAGE_ID", "LANGUAGE_NAME" FROM public."Languages"'
        db_connection.cur.execute(query)
        options = [f"{option[0]} - {option[1]}" for option in db_connection.cur.fetchall()]

        combo_language['values'] = options
    except Exception as error:
        print(error)
    finally:
        db_connection.close_connection()     


def fetch_institute_options():
    db_connection = DatabaseCon()

    try:
        query = 'SELECT "INSTITUTES_ID", "INSTITUTES_NAME" FROM public."Institutes"'
        db_connection.cur.execute(query)
        options = [f"{option[0]} - {option[1]}" for option in db_connection.cur.fetchall()]

        combo_institute['values'] = options
    except Exception as error:
        print(error)
    finally:
        db_connection.close_connection()

def fetch_type_options():
    db_connection = DatabaseCon()

    try:
        query = 'SELECT "TYPE_ID", "TYPE_NAME" FROM public."Type"'
        db_connection.cur.execute(query)
        options = [f"{option[0]} - {option[1]}" for option in db_connection.cur.fetchall()]

        combo_type['values'] = options
    except Exception as error:
        print(error)
    finally:
        db_connection.close_connection()

def fetch_keyword_options():
    db_connection = DatabaseCon()

    try:
        query = 'SELECT "KEYWORD_ID", "KEYWORD_NAME" FROM public."Keyword"'
        db_connection.cur.execute(query)
        options = [f"{option[0]} - {option[1]}" for option in db_connection.cur.fetchall()]

        combo_keyword['values'] = options
    except Exception as error:
        print(error)
    finally:
        db_connection.close_connection()

def fetch_supervisor_options():
    db_connection = DatabaseCon()

    try:
        query = 'SELECT "SUPERVISOR_ID", "PERSON_ID" FROM public."Supervisor"'
        db_connection.cur.execute(query)
        options = [f"{option[0]} - {option[1]}" for option in db_connection.cur.fetchall()]

        combo_supervisor['values'] = options
    except Exception as error:
        print(error)
    finally:
        db_connection.close_connection()

def fetch_co_options():
    db_connection = DatabaseCon()

    try:
        query = 'SELECT "COSUPERVISOR_ID", "PERSON_ID" FROM public."Cosupervisor"'
        db_connection.cur.execute(query)
        options = [f"{option[0]} - {option[1]}" for option in db_connection.cur.fetchall()]

        combo_co['values'] = options
    except Exception as error:
        print(error)
    finally:
        db_connection.close_connection()

def fetch_institute2_options():
    db_connection = DatabaseCon()

    try:
        query = 'SELECT "INSTITUTES_ID", "INSTITUTES_NAME" FROM public."Institutes"'
        db_connection.cur.execute(query)
        options = [f"{option[0]} - {option[1]}" for option in db_connection.cur.fetchall()]

        combo_institute2['values'] = options
    except Exception as error:
        print(error)
    finally:
        db_connection.close_connection()




#We defined the buttons here.
loginbutton = ImageTk.PhotoImage(Image.open('img//Login.png'))
buttonlogin = Button(root, image=loginbutton,command=login,highlightthickness=0, borderwidth=0, background= '#90B1DB', activebackground= '#90B1DB')
buttonlogin.place(width=291, height=161, x=976, y=22)

findbutton = ImageTk.PhotoImage(Image.open('img//Find.png'))
buttonfind = Button(root, image=findbutton,command=find,highlightthickness=0, borderwidth=0)
buttonfind.place(width=343, height=130, x=492, y=554)

homebutton = ImageTk.PhotoImage(Image.open('img//geri.png'))
buttonhome = Button(root, image=homebutton,command=home,highlightthickness=0, borderwidth=0, background= '#90B1DB', activebackground= '#90B1DB')
buttonhome.place_forget()

login2button = ImageTk.PhotoImage(Image.open('img//Login2.png'))
buttonlogin2 = Button(root, image=login2button,command=login2,highlightthickness=0, borderwidth=0)
buttonlogin2.place_forget()

addthesisbutton = ImageTk.PhotoImage(Image.open('img//Addthesis.png'))
buttonaddthesis = Button(root, image=addthesisbutton,command=add_thesis,highlightthickness=0, borderwidth=0)
buttonaddthesis.place_forget()

updatebutton = ImageTk.PhotoImage(Image.open('img//Update2.png'))
buttonupdate = Button(root, image=updatebutton,command=update_thesis,highlightthickness=0, borderwidth=0)
buttonupdate.place_forget()

geributton = ImageTk.PhotoImage(Image.open('img//geri2.png'))
buttongeri = Button(root, image=geributton,command=login2,highlightthickness=0, borderwidth=0, background= '#90B1DB', activebackground= '#90B1DB')
buttongeri.place_forget()

nextbutton = ImageTk.PhotoImage(Image.open('img//Nextpage.png'))
buttonnext = Button(root, image=nextbutton,command=nextpage1,highlightthickness=0, borderwidth=0, background= '#90B1DB', activebackground= '#90B1DB')
buttonnext.place_forget()

nextbutton2 = ImageTk.PhotoImage(Image.open('img//Nextpage.png'))
buttonnext2 = Button(root, image=nextbutton2,command=nextpage2,highlightthickness=0, borderwidth=0, background= '#90B1DB', activebackground= '#90B1DB')
buttonnext2.place_forget()

addbutton = ImageTk.PhotoImage(Image.open('img//Add.png'))
buttonadd = Button(root, image=addbutton,command=add,highlightthickness=0, borderwidth=0)
buttonadd.place_forget()

updatebutton2 = ImageTk.PhotoImage(Image.open('img//Update.png'))
buttonupdate2 = Button(root, image=updatebutton2,command=update,highlightthickness=0, borderwidth=0)
buttonupdate2.place_forget()

thesisbutton = ImageTk.PhotoImage(Image.open('img//tez.png'))
buttonthesis = Button(root, image=thesisbutton,command=readthesis,highlightthickness=0, borderwidth=0, background= '#90B1DB', activebackground= '#90B1DB')
buttonthesis.place_forget()


#We defined the pictures here.
picturelogo = PhotoImage(file="img//logo.png")
picture_logo = tk.Label(root, image=picturelogo, background= '#90B1DB')
picture_logo.place(width=70, height=67, x=60, y=36)

picturethesis = PhotoImage(file="img//Thesisapp.png")
picture_thesis = tk.Label(root, image=picturethesis, background= '#90B1DB')
picture_thesis.place(width=174, height=93, x=155, y=36)

picturesearch_thesis = PhotoImage(file="img//SearchThesis.png")
picture_search_thesis = tk.Label(root, image=picturesearch_thesis)
picture_search_thesis.place(width=345, height=44, x=495, y=286)

picturemainpage = PhotoImage(file="img//MainPage.png")
picture_mainpage = tk.Label(root, image=picturemainpage, background= '#90B1DB')
picture_mainpage.place(width=337, height=51, x=481, y=79)

pictureusername = PhotoImage(file="img//UserName.png")
picture_username = tk.Label(root, image=pictureusername)
picture_username.place_forget()

picturepassword = PhotoImage(file="img//Password.png")
picture_password = tk.Label(root, image=picturepassword)
picture_password.place_forget()

picturelanguage = PhotoImage(file="img//Language.png")
picture_language = tk.Label(root, image=picturelanguage)
picture_language.place_forget()

picturethesisname = PhotoImage(file="img//ThesisName.png")
picture_thesisname = tk.Label(root, image=picturethesisname)
picture_thesisname.place_forget()

picturesubject = PhotoImage(file="img//Subject.png")
picture_subject = tk.Label(root, image=picturesubject)
picture_subject.place_forget()

pictureuniversity = PhotoImage(file="img//University.png")
picture_university = tk.Label(root, image=pictureuniversity)
picture_university.place_forget()

pictureınstitute = PhotoImage(file="img//Institute.png")
picture_ınstitute = tk.Label(root, image=pictureınstitute)
picture_ınstitute.place_forget()

picturetype = PhotoImage(file="img//Type.png")
picture_type = tk.Label(root, image=picturetype)
picture_type.place_forget()

pictureyear = PhotoImage(file="img//Year.png")
picture_year = tk.Label(root, image=pictureyear)
picture_year.place_forget()

picturepages = PhotoImage(file="img//pages.png")
picture_pages = tk.Label(root, image=picturepages)
picture_pages.place_forget()

picturesupervisor = PhotoImage(file="img//Supervisor.png")
picture_supervisor = tk.Label(root, image=picturesupervisor)
picture_supervisor.place_forget()

pictureco = PhotoImage(file="img//co.png")
picture_co = tk.Label(root, image=pictureco)
picture_co.place_forget()

picturekeyword = PhotoImage(file="img//Keyword.png")
picture_keyword = tk.Label(root, image=picturekeyword)
picture_keyword.place_forget()

pictureabstract = PhotoImage(file="img//Abstract.png")
picture_abstract = tk.Label(root, image=pictureabstract)
picture_abstract.place_forget()

picturethesis2 = PhotoImage(file="img//Thesis.png")
picture_thesis2 = tk.Label(root, image=picturethesis2)
picture_thesis2.place_forget()

picturename = PhotoImage(file="img//Name.png")
picture_name = tk.Label(root, image=picturename)
picture_name.place_forget()

picturesurname = PhotoImage(file="img//Surname.png")
picture_surname = tk.Label(root, image=picturesurname)
picture_surname.place_forget()

picturemail = PhotoImage(file="img//mail.png")
picture_mail = tk.Label(root, image=picturemail)
picture_mail.place_forget()

pictureuniversity2 = PhotoImage(file="img//University.png")
picture_university2 = tk.Label(root, image=pictureuniversity2)
picture_university2.place_forget()

pictureınstitute2 = PhotoImage(file="img//Institute.png")
picture_ınstitute2 = tk.Label(root, image=pictureınstitute2)
picture_ınstitute2.place_forget()

picturerank = PhotoImage(file="img//Rank.png")
picture_rank = tk.Label(root, image=picturerank)
picture_rank.place_forget()

picturedate = PhotoImage(file="img//Date.png")
picture_date = tk.Label(root, image=picturedate)
picture_date.place_forget()

picturesearchpage = PhotoImage(file="img//SearchPage.png")
picture_searchpage = tk.Label(root, image=picturesearchpage, background= '#90B1DB')
picture_searchpage.place_forget()

picturethesispage = PhotoImage(file="img//Thesis.png")
picture_thesispage = tk.Label(root, image=picturethesispage, background= '#90B1DB')
picture_thesispage.place_forget()

picturethesisadd = PhotoImage(file="img//Add.Thesis.png")
picture_thesisadd = tk.Label(root, image=picturethesisadd, background= '#90B1DB')
picture_thesisadd.place_forget()

pictureup = PhotoImage(file="img//Up.png")
picture_up = tk.Label(root, image=pictureup, background= '#90B1DB')
picture_up.place_forget()


#We defined the entrys here.
entry_search = Entry(root, font=('Arial', 30), bd=2, relief="groove")
entry_search.place(width=649, height=94, x=325, y=402)

entry_username = Entry(root, font=('Arial', 30), bd=2, relief="groove")
entry_username.place_forget()

entry_password = Entry(root, show="*", font=('Arial', 30), bd=2, relief="groove")
entry_password.place_forget()

entry_thesis_name = Entry(root, font=('Arial', 30), bd=2, relief="groove")
entry_thesis_name.place_forget()

entry_subject = Entry(root, font=('Arial', 30), bd=2, relief="groove")
entry_subject.place_forget()

entry_year = Entry(root, font=('Arial', 30), bd=2, relief="groove")
entry_year.place_forget()

entry_pages = Entry(root, font=('Arial', 30), bd=2, relief="groove")
entry_pages.place_forget()

entry_abstract = Entry(root, font=('Arial', 30), bd=2, relief="groove")
entry_abstract.place_forget()

entry_thesis = Entry(root, font=('Arial', 30), bd=2, relief="groove")
entry_thesis.place_forget()

entry_name = Entry(root, font=('Arial', 30), bd=2, relief="groove")
entry_name.place_forget()

entry_surname = Entry(root, font=('Arial', 30), bd=2, relief="groove")
entry_surname.place_forget()

entry_mail = Entry(root, font=('Arial', 30), bd=2, relief="groove")
entry_mail.place_forget()

entry_title = Entry(root, font=('Arial', 30), bd=2, relief="groove")
entry_title.place_forget()

entry_date = Entry(root, font=('Arial', 30), bd=2, relief="groove")
entry_date.place_forget()


#We defined the comboboxs here.
combo_rank = ttk.Combobox(root)
combo_rank.place_forget()

combo_institute = ttk.Combobox(root)
combo_institute.place_forget()

combo_type = ttk.Combobox(root)
combo_type.place_forget()

combo_keyword = ttk.Combobox(root)
combo_keyword.place_forget()

combo_supervisor = ttk.Combobox(root)
combo_supervisor.place_forget()

combo_co = ttk.Combobox(root)
combo_co.place_forget()

combo_institute2 = ttk.Combobox(root)
combo_institute2.place_forget()

combo_university = ttk.Combobox(root)
combo_university.place_forget()

combo_university2 = ttk.Combobox(root)
combo_university2.place_forget()

combo_language = ttk.Combobox(root)
combo_language.place_forget()


#We defined the texts here.
text_thesis_no = Text(root, wrap="word", width=150, height=40)
text_thesis_no.place_forget()
text_thesis_no.insert("1.0","THESIS NO", "bold")
text_thesis_no.tag_configure("bold", font=("TkDefaultFont", 12, "bold"))

text_author = Text(root, wrap="word", width=160, height=40)
text_author.place_forget()
text_author.insert("1.0","AUTHOR:","bold")
text_author.tag_configure("bold", font=("TkDefaultFont", 12, "bold"))

text_year = Text(root, wrap="word", width=160, height=40)
text_year.place_forget()
text_year.insert("1.0","YEAR:","bold")
text_year.tag_configure("bold", font=("TkDefaultFont", 12, "bold"))

text_title = Text(root, wrap="word", width=160, height=40)
text_title.place_forget()
text_title.insert("1.0","TITLE:","bold")
text_title.tag_configure("bold", font=("TkDefaultFont", 12, "bold"))

text_type = Text(root, wrap="word", width=160, height=40)
text_type.place_forget()
text_type.insert("1.0","TYPE:","bold")
text_type.tag_configure("bold", font=("TkDefaultFont", 12, "bold"))

text_subject = Text(root, wrap="word", width=160, height=40)
text_subject.place_forget()
text_subject.insert("1.0","SUBJECT:","bold")
text_subject.tag_configure("bold", font=("TkDefaultFont", 12, "bold"))

text_thesis_no2 = Text(root, wrap="word", width=150, height=40)
text_thesis_no2.place_forget()

text_author2 = Text(root, wrap="word", width=160, height=40)
text_author2.place_forget()

text_year2 = Text(root, wrap="word", width=160, height=40)
text_year2.place_forget()

text_title2 = Text(root, wrap="word", width=160, height=40)
text_title2.place_forget()

text_type2 = Text(root, wrap="word", width=160, height=40)
text_type2.place_forget()

text_subject2 = Text(root, wrap="word", width=160, height=40)
text_subject2.place_forget()

text_thesis = Text(root, wrap="word", width=160, height=40)
text_thesis.place_forget()

text_thesis_no3 = Text(root, wrap="word", width=160, height=40)
text_thesis_no3.place_forget()

#We defined the checkboxes here.
checkbox = tk.Checkbutton(root)
checkbox.place_forget()

checkbox2 = tk.Checkbutton(root)
checkbox2.place_forget()


fetch_rank_options()
fetch_university_options()
fetch_university2_options()
fetch_language_options()
fetch_institute_options()
fetch_type_options()
fetch_keyword_options()
fetch_supervisor_options()
fetch_co_options()
fetch_institute2_options()


#Start window.
root.mainloop()
