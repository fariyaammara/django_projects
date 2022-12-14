
import subprocess
from subprocess import call
import os
import sqlite3
import json
import shutil


def package_name_extract(packagename):
    cmd=["adb","shell"]
    cmd_root=["adb","root"]
    sp=subprocess.Popen(cmd_root,shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out,err=sp.communicate()
    if len(err)==0:
        cmd_db="adb pull data/data/"+packagename+"/databases"
        call=subprocess.Popen(cmd_db,shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        exit_code=call.wait()
        out,err=call.communicate()
        print(out)
        if exit_code==0:
            get_resp=read_db_files()
            return get_resp
        else:     
            return("No Database file found in the application")

def read_db_files():
    extension=['.db','.sqlite']
    get_dir=os.getcwd()+"/databases/"
    for file_name in os.listdir(get_dir):
        f=os.path.join(get_dir,file_name)
        for get_ext in extension:
            if f.endswith(get_ext):
                try:
                    #importdb(f)
                    list_tablenames=[]
                    try:
                        conn = sqlite3.connect(f)
                        cursor = conn.cursor()
                        sql_query = """SELECT name FROM sqlite_master WHERE type='table';"""
                        cursor.execute(sql_query)
                        list_tablenames=cursor.fetchall()
                        test = extract_table_info(list_tablenames,cursor)
                    except:
                        print("exeption found")
                except:
                    print("Database folder is empty")
    try:
        shutil.rmtree(get_dir, ignore_errors=True)
    except OSError as error:
        print("cannot remove")
    
    return test


'''def importdb(db):
    list_tablenames=[]
    try:
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        sql_query = """SELECT name FROM sqlite_master WHERE type='table';"""
        cursor.execute(sql_query)
        list_tablenames=cursor.fetchall()
        extract_table_info(list_tablenames,cursor)
    except:
        print("exeption found")
'''
def extract_table_info(list_tablenames,cursor):

    store={}
    list_db=[]
    try:
        for tab in list_tablenames:
            store[tab[0]]={}
            print("\n\n<<]------"+ tab[0] +"------>>\n\n")
            for row in cursor.execute('SELECT * FROM '+tab[0]+';'):
                list_db.append(row)
            store[tab[0]]=list_db
    finally:
        cursor.close()
        print(store)
    return(store)
    
     


#get_connected_devices()
