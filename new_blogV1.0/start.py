# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__, template_folder='./templates')

@app.route('/')
def fake_index():
    return render_template('fake_index.html')

@app.route('/index')
def index():
    conn = mysql.connector.connect(host='***',user='***', password='***', database='blog')
    cursor = conn.cursor()
    cursor.execute('select blog_title,info,au01,au02,website from special')
    str2 = cursor.fetchone()
    cursor.close()
    conn.close()
    blog_title = str2[0]
    info = str2[1]
    au01 = str2[2]
    au02 = str2[3]
    website = str2[4]
    return render_template('index.html',blog_title=blog_title,info=info,au01=au01,au02=au02,website=website)

@app.route('/cppcode/<num>')
def cppcode(num):
    str1='C++'
    conn = mysql.connector.connect(host='***',user='***', password='***',  database='blog')
    cursor = conn.cursor()
    cursor.execute('select news_title,au01,au02,tag, news_about,news_infos from cppcode where id = %s',(num,))
    str3 = cursor.fetchone()
    title = str3[0]
    au01 = str3[1]
    au02 = str3[2]
    tag = str3[3]
    about = str3[4]
    infos = str3[5]
    cursor.close()
    conn.close()
    return render_template('code.html',str1=str1,title=title,au01=au01,au02=au02,tag=tag,about=about,infos=infos)

@app.route('/pythoncode/<num>')
def pythoncode(num):
    str1='Python'
    conn = mysql.connector.connect(host='***',user='***', password='***',  database='blog')
    cursor = conn.cursor()
    cursor.execute('select news_title,au01,au02,tag, news_about,news_infos from pythoncode where id = %s',(num,))
    str3 = cursor.fetchone()
    title = str3[0]
    au01 = str3[1]
    au02 = str3[2]
    tag = str3[3]
    about = str3[4]
    infos = str3[5]
    cursor.close()
    conn.close()
    return render_template('code.html',str1=str1,title=title,au01=au01,au02=au02,tag=tag,about=about,infos=infos)

@app.route('/projectcode/<num>')
def projectcode(num):
    str1='Project'
    conn = mysql.connector.connect(host='***',user='***', password='***',  database='blog')
    cursor = conn.cursor()
    cursor.execute('select news_title,au01,au02,tag, news_about,news_infos from projectcode where id = %s',(num,))
    str3 = cursor.fetchone()
    title = str3[0]
    au01 = str3[1]
    au02 = str3[2]
    tag = str3[3]
    about = str3[4]
    infos = str3[5]
    cursor.close()
    conn.close()
    return render_template('code.html',str1=str1,title=title,au01=au01,au02=au02,tag=tag,about=about,infos=infos)

@app.route('/patcode/<num>')
def patcode(num):
    str1='PAT'
    conn = mysql.connector.connect(host='***',user='***', password='***',  database='blog')
    cursor = conn.cursor()
    cursor.execute('select news_title,au01,au02,tag, news_about,news_infos from patcode where id = %s',(num,))
    str3 = cursor.fetchone()
    title = str3[0]
    au01 = str3[1]
    au02 = str3[2]
    tag = str3[3]
    about = str3[4]
    infos = str3[5]
    cursor.close()
    conn.close()
    return render_template('code.html',str1=str1,title=title,au01=au01,au02=au02,tag=tag,about=about,infos=infos)

@app.route('/cppshare/<num>')
def cppshare(num):
    str1='C++'
    conn = mysql.connector.connect(host='***',user='***', password='***',  database='blog')
    cursor = conn.cursor()
    cursor.execute('select id from cppcode')
    idcontent = cursor.fetchall()
    idlen = len(idcontent)
    page_count = idlen/9
    inum = (int)(num)
    counts1 = 1
    counts2 = 0
    cursor.execute('select news_title,id from cppcode')
    str4 = cursor.fetchall()
    str2 = []
    for (i,j,) in str4:
        if counts1 != (inum-1)*9+1 :
            counts1 = counts1 + 1
        else:
            str2.append((i,j))
            counts2 = counts2 + 1
            if counts2 == 9:
                break
    cursor.close()
    conn.close()
    type = 'cppcode'
    previous_page = inum-1
    next_page = inum+1
    if page_count < 1:
        page_count = 1
    if inum-1 == 0:
        previous_page = 1
    if inum == page_count:
        next_page = page_count
    type2 = 'cppshare'
    if page_count-(int)(page_count) > 0:
        page_count = (int)(page_count)+1
    return render_template('share.html',type2=type2,type=type,str1=str1,str2=str2,previous_page=inum-1,next_page=inum+1,last_page=page_count,total=page_count)

@app.route('/pythonshare/<num>')
def pythonshare(num):
    str1='Python'
    conn = mysql.connector.connect(host='***',user='***', password='***',  database='blog')
    cursor = conn.cursor()
    cursor.execute('select id from pythoncode')
    idcontent = cursor.fetchall()
    idlen = len(idcontent)
    page_count = idlen/9
    inum = (int)(num)
    counts1 = 1
    counts2 = 0
    cursor.execute('select news_title,id from pythoncode')
    str4 = cursor.fetchall()
    str2 = []
    for (i,j,) in str4:
        if counts1 != (inum-1)*9+1 :
            counts1 = counts1 + 1
        else:
            str2.append((i,j))
            counts2 = counts2 + 1
            if counts2 == 9:
                break
    cursor.close()
    conn.close()
    type = 'pythoncode'
    previous_page = inum-1
    next_page = inum+1
    if page_count < 1:
        page_count = 1
    if inum-1 == 0:
        previous_page = 1
    if inum == page_count:
        next_page = page_count
    type2 = 'pythonshare'
    if page_count-(int)(page_count) > 0:
        page_count = (int)(page_count)+1
    return render_template('share.html',type2=type2,type=type,str1=str1,str2=str2,previous_page=previous_page,next_page=next_page,last_page=page_count,total=page_count)

@app.route('/projectshare/<num>')
def projectshare(num):
    str1='Project'
    conn = mysql.connector.connect(host='***',user='***', password='***',  database='blog')
    cursor = conn.cursor()
    cursor.execute('select id from projectcode')
    idcontent = cursor.fetchall()
    idlen = len(idcontent)
    page_count = idlen/9
    inum = (int)(num)
    counts1 = 1
    counts2 = 0
    cursor.execute('select news_title,id from projectcode')
    str4 = cursor.fetchall()
    str2 = []
    for (i,j,) in str4:
        if counts1 != (inum-1)*9+1 :
            counts1 = counts1 + 1
        else:
            str2.append((i,j))
            counts2 = counts2 + 1
            if counts2 == 9:
                break
    cursor.close()
    conn.close()
    type = 'projectcode'
    previous_page = inum-1
    next_page = inum+1
    if page_count < 1:
        page_count = 1
    if inum-1 == 0:
        previous_page = 1
    if inum == page_count:
        next_page = page_count
    type2 = 'projectshare'
    if page_count-(int)(page_count) > 0:
        page_count = (int)(page_count)+1
    return render_template('share.html',type2=type2,type=type,str1=str1,str2=str2,previous_page=previous_page,next_page=next_page,last_page=page_count,total=page_count)

@app.route('/patshare/<num>')
def patshare(num):
    str1='PAT'
    conn = mysql.connector.connect(host='***',user='***', password='***',  database='blog')
    cursor = conn.cursor()
    cursor.execute('select id from patcode')
    idcontent = cursor.fetchall()
    idlen = len(idcontent)
    page_count = idlen/9
    inum = (int)(num)
    counts1 = 1
    counts2 = 0
    cursor.execute('select news_title,id from patcode')
    str4 = cursor.fetchall()
    str2 = []
    for (i,j,) in str4:
        if counts1 != (inum-1)*9+1 :
            counts1 = counts1 + 1
        else:
            str2.append((i,j))
            counts2 = counts2 + 1
            if counts2 == 9:
                break
    cursor.close()
    conn.close()
    type = 'patcode'
    previous_page = inum-1
    next_page = inum+1
    if page_count < 1:
        page_count = 1
    if inum-1 == 0:
        previous_page = 1
    if inum == page_count:
        next_page = page_count
    type2 = 'patshare'
    if page_count-(int)(page_count) > 0:
        page_count = (int)(page_count)+1
    return render_template('share.html',type2=type2,type=type,str1=str1,str2=str2,previous_page=previous_page,next_page=next_page,last_page=page_count,total=page_count)

@app.route('/login', methods = ['POST', 'GET'])
def editoradd():
...


@app.route('/add', methods=['POST'])
def add():
...

@app.route('/delete', methods=['POST'])
def receive():
...

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5001)
