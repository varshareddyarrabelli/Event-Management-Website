import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect,session
from flask_session import Session
from werkzeug.exceptions import abort
from datetime import date 

dates=date.today().strftime('%Y-%m-%d')

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn
def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post
app = Flask(__name__)
app.config['SECRET_KEY']='your secret key'
app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
Session(app)

@app.route('/cse')
def cse_index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts order by date1').fetchall()
    conn.close()
    return render_template('cse.html', posts=posts,dates=dates)

@app.route('/cse/<int:post_id>')
def cse_post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/department_login.html/login_cs/create', methods=('GET', 'POST'))
def cse_create():
    if session["login"] != "login_cs" or session["login"]=="" :
        return redirect (url_for("dep_login")) 
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        date1=request.form['date1']
        #dept_name=request.form['dept_name']
        dept_name='cse'
        time=request.form['time']
        venue=request.form['venue']
        url=request.form['url']
        conn = get_db_connection()
        conn.execute('INSERT INTO posts (title, content,venue,dept_name,url,time,date1) VALUES (?, ?,?,?,?,?,?)',
                     (title, content,venue,dept_name,url,time,date1))
        conn.commit()
        conn.close()
        return redirect(url_for('login_cs'))
    return render_template('create.html')

@app.route('/department_login.html/login_cs/<int:id>/edit', methods=('GET', 'POST'))
def cse_edit(id):
    if session["login"] != "login_cs" or session["login"]=="" :
        return redirect (url_for("dep_login")) 
    post = get_post(id)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        date1=request.form['date1']
        venue=request.form['venue']
        url=request.form['url']
        time=request.form['time']
        #dept_name=request.form['dept_name']
        dept_name='cse'

        conn = get_db_connection()
        conn.execute('UPDATE posts SET title = ?, content = ?, date1=?,venue=?,url=?,time=?'
                         ' WHERE id = ?',
                         (title, content,date1,venue,url,time, id))
        conn.commit()
        conn.close()
        return redirect(url_for('login_cs'))

    return render_template('cse_edit.html', post=post)


@app.route('/department_login.html/login_cs/<int:id>/delete', methods=('POST',))
def cse_delete(id):
    if session["login"] != "login_cs" or session["login"]=="" :
        return redirect (url_for("dep_login") ) 
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('login_cs'))

@app.route('/ece')
def ece_index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts order by date1').fetchall()
    conn.close()
    return render_template('ece.html', posts=posts,dates=dates)

@app.route('/ece/<int:post_id>')
def ece_post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/department_login.html/login_ec/create', methods=('GET', 'POST'))
def ece_create():
    if session["login"] != "login_ec" or session["login"]=="" :
        return redirect (url_for("dep_login"))  
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        date1=request.form['date1']
        #dept_name=request.form['dept_name']
        dept_name='ece'
        time1=request.form['time']
        venue=request.form['venue']
        url=request.form['url']
        conn = get_db_connection()
        conn.execute('INSERT INTO posts (title, content,venue,dept_name,url,time,date1) VALUES (?, ?,?,?,?,?,?)',
                     (title, content,venue,dept_name,url,time1,date1))
        conn.commit()
        conn.close()
        return redirect(url_for('login_ec'))
    return render_template('ece_create.html')
    
@app.route('/department_login.html/login_ec/<int:id>/edit', methods=('GET', 'POST'))
def ece_edit(id):
    if session["login"] != "login_ec" or session["login"]=="" :
        return redirect (url_for("dep_login") )
    post = get_post(id)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        date1=request.form['date1']
        venue=request.form['venue']
        url=request.form['url']
        time=request.form['time']
        #dept_name=request.form['dept_name']
        dept_name='ece'

        conn = get_db_connection()
        conn.execute('UPDATE posts SET title = ?, content = ?, date1=?,venue=?,url=?,time=?'
                         ' WHERE id = ?',
                         (title, content,date1,venue,url,time, id))
        conn.commit()
        conn.close()
        return redirect(url_for('login_ec'))

    return render_template('ece_edit.html', post=post)

@app.route('/department_login.html/login_ec/<int:id>/delete', methods=('POST',))
def ece_delete(id):
    if session["login"] != "login_ec" or session["login"]=="" :
        return redirect (url_for("dep_login") )
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('login_ec'))
    
@app.route('/eee')
def eee_index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts order by date1').fetchall()
    conn.close()
    return render_template('eee.html', posts=posts,dates=dates)

@app.route('/eee/<int:post_id>')
def eee_post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/department_login.html/login_ee/create', methods=('GET', 'POST'))
def eee_create():
    if session["login"] != "login_ee" or session["login"]=="" :
        return redirect (url_for("dep_login") )
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        date1=request.form['date1']
        #dept_name=request.form['dept_name']
        dept_name='eee'
        time=request.form['time']
        venue=request.form['venue']
        url=request.form['url']
        conn = get_db_connection()
        conn.execute('INSERT INTO posts (title, content,venue,dept_name,url,time,date1) VALUES (?, ?,?,?,?,?,?)',
                     (title, content,venue,dept_name,url,time,date1))
        conn.commit()
        conn.close()
        return redirect(url_for('login_ee'))
    return render_template('eee_create.html')

@app.route('/department_login.html/login_ee/<int:id>/edit', methods=('GET', 'POST'))
def eee_edit(id):
    if session["login"] != "login_ee" or session["login"]=="" :
        return redirect (url_for("dep_login") )
    post = get_post(id)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        date1=request.form['date1']
        venue=request.form['venue']
        url=request.form['url']
        time=request.form['time']
        #dept_name=request.form['dept_name']
        dept_name='eee'

        conn = get_db_connection()
        conn.execute('UPDATE posts SET title = ?, content = ?, date1=?,venue=?,url=?,time=?'
                         ' WHERE id = ?',
                         (title, content,date1,venue,url,time, id))
        conn.commit()
        conn.close()
        return redirect(url_for('login_ee'))

    return render_template('eee_edit.html', post=post)

@app.route('/department_login.html/login_ee/<int:id>/delete', methods=('POST',))
def eee_delete(id):
    if session["login"] != "login_ee" or session["login"]=="" :
        return redirect (url_for("dep_login") )
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('login_ee'))
    
@app.route('/ce')
def ce_index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts order by date1').fetchall()
    conn.close()
    return render_template('ce.html', posts=posts,dates=dates)

@app.route('/ce/<int:post_id>')
def ce_post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/department_login.html/login_ce/create', methods=('GET', 'POST'))
def ce_create():
    if session["login"] != "login_ce" or session["login"]=="" :
        return redirect (url_for("dep_login"))
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        date1=request.form['date1']
        #dept_name=request.form['dept_name']
        dept_name='ce'
        time=request.form['time']
        venue=request.form['venue']
        url=request.form['url']
        conn = get_db_connection()
        conn.execute('INSERT INTO posts (title, content,venue,dept_name,url,time,date1) VALUES (?, ?,?,?,?,?,?)',
                     (title, content,venue,dept_name,url,time,date1))
        conn.commit()
        conn.close()
        return redirect(url_for('login_ce'))
    return render_template('ce_create.html')

@app.route('/department_login.html/login_ce/<int:id>/edit', methods=('GET', 'POST'))
def ce_edit(id):
    if session["login"] != "login_ce" or session["login"]=="" :
        return redirect (url_for("dep_login"))
    post = get_post(id)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        date1=request.form['date1']
        venue=request.form['venue']
        url=request.form['url']
        time=request.form['time']
        #dept_name=request.form['dept_name']
        dept_name='ce'

        conn = get_db_connection()
        conn.execute('UPDATE posts SET title = ?, content = ?, date1=?,venue=?,url=?,time=?'
                         ' WHERE id = ?',
                         (title, content,date1,venue,url,time, id))
        conn.commit()
        conn.close()
        return redirect(url_for('login_ce'))

    return render_template('ce_edit.html', post=post)

@app.route('/department_login.html/login_ce/<int:id>/delete', methods=('POST',))
def ce_delete(id):
    if session["login"] != "login_ce" or session["login"]=="" :
        return redirect (url_for("dep_login"))
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('login_ce'))
    
@app.route('/me')
def me_index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts order by date1').fetchall()
    conn.close()
    return render_template('me.html', posts=posts,dates=dates)

@app.route('/me/<int:post_id>')
def me_post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/department_login.html/login_me/create', methods=('GET', 'POST'))
def me_create():
    if session["login"] != "login_me" or session["login"]=="" :
        return redirect (url_for("dep_login"))
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        date1=request.form['date1']
        #dept_name=request.form['dept_name']
        dept_name='me'
        time=request.form['time']
        venue=request.form['venue']
        url=request.form['url']
        conn = get_db_connection()
        conn.execute('INSERT INTO posts (title, content,venue,dept_name,url,time,date1) VALUES (?, ?,?,?,?,?,?)',
                     (title, content,venue,dept_name,url,time,date1))
        conn.commit()
        conn.close()
        return redirect(url_for('login_me'))
    return render_template('me_create.html')

@app.route('/department_login.html/login_me/<int:id>/edit', methods=('GET', 'POST'))
def me_edit(id):
    if session["login"] != "login_me" or session["login"]=="" :
        return redirect (url_for("dep_login"))
    post = get_post(id)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        date1=request.form['date1']
        venue=request.form['venue']
        url=request.form['url']
        time=request.form['time']
        #dept_name=request.form['dept_name']
        dept_name='me'

        conn = get_db_connection()
        conn.execute('UPDATE posts SET title = ?, content = ?, date1=?,venue=?,url=?,time=?'
                         ' WHERE id = ?',
                         (title, content,date1,venue,url,time, id))
        conn.commit()
        conn.close()
        return redirect(url_for('login_me'))

    return render_template('me_edit.html', post=post)

@app.route('/department_login.html/login_me/<int:id>/delete', methods=('POST',))
def me_delete(id):
    if session["login"] != "login_me" or session["login"]=="" :
        return redirect (url_for("dep_login"))
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was sucmessfully deleted!'.format(post['title']))
    return redirect(url_for('login_me'))
    
@app.route('/')
def main():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts order by date1').fetchall()
    conn.close()
    return render_template('main.html',posts=posts,dates=dates)
    
@app.route('/department_login.html')
def dep_login():
    session["login"]=""
    return render_template('department_login.html')
    
@app.route('/department_login.html/login',methods=('POST','GET'))
def login():
    session["login"]=""
    if request.method == 'POST':
        username = request.form['username']
        passwords = request.form['passwords']
        department = request.form['department']
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM login WHERE department = ? and username = ? and passwords = ? ',
                        (department,username, passwords,)).fetchone()
    conn.close()
    if post is not None:
    	session["login"]="login_"+department[:2]
    	if department=='cse':
    		return redirect(url_for('login_cs'))
    	elif department=='ece':
    		return redirect(url_for('login_ec'))
    	elif department=='eee':
    		return redirect(url_for('login_ee'))
    	elif department=='ce':
    		return redirect(url_for('login_ce'))
    	elif department=='me':
    		return redirect(url_for('login_me'))
    else:
    	flash('Invalid Credentials','error')
    	return redirect(url_for('dep_login'))
       
@app.route('/department_login.html/login_cs', methods=('POST','GET'))
def login_cs():
    if session["login"] != "login_cs" or session["login"]=="" :
        return redirect (url_for("dep_login")  )  
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts where dept_name="cse" and (status="approved" or status="rejected")').fetchall()
    conn.execute('UPDATE posts SET flag1 = 1 where dept_name="cse" and (status="approved" or status="rejected")')
    posts = conn.execute('SELECT * FROM posts order by date1').fetchall()
    conn.commit()
    conn.close()
    return render_template('login_cs.html',posts=posts,dates=dates,post=post)

@app.route('/past')
def past():
    conn=get_db_connection()
    posts=conn.execute('SELECT * FROM posts order by date1 desc').fetchall()
    conn.close()
    return render_template('past.html',posts=posts,dates=dates)

@app.route('/department_login.html/login_cs/past')
def past_cs():
    if session["login"] != "login_cs" or session["login"]=="" :
        return redirect (url_for("dep_login") )
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts order by date1 desc').fetchall()
    conn.close()
    return render_template('past_cs.html',posts=posts,dates=dates)

@app.route('/cse/past')
def past_cse():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts order by date1 desc').fetchall()
    conn.close()
    return render_template('past_cse.html',posts=posts,dates=dates)

@app.route('/department_login.html/login_ec/past')
def past_ec():
    if session["login"] != "login_ec" or session["login"]=="" :
        return redirect (url_for("dep_login") )
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts order by date1 desc').fetchall()
    conn.close()
    return render_template('past_ec.html',posts=posts,dates=dates)

@app.route('/ece/past')
def past_ece():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts order by date1 desc').fetchall()
    conn.close()
    return render_template('past_ece.html',posts=posts,dates=dates)

@app.route('/department_login.html/login_ee/past')
def past_ee():
    if session["login"] != "login_ee" or session["login"]=="" :
        return redirect (url_for("dep_login") )
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts order by date1 desc').fetchall()
    conn.close()
    return render_template('past_ee.html',posts=posts,dates=dates)

@app.route('/eee/past')
def past_eee():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts order by date1 desc').fetchall()
    conn.close()
    return render_template('past_eee.html',posts=posts,dates=dates)

@app.route('/department_login.html/login_me/past')
def past_me():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts order by date1 desc').fetchall()
    conn.close()
    return render_template('past_me.html',posts=posts,dates=dates)

@app.route('/me/past')
def past_mec():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts order by date1 desc').fetchall()
    conn.close()
    return render_template('past_mec.html',posts=posts,dates=dates)

@app.route('/department_login.html/login_ce/past')
def past_ce():
    if session["login"] != "login_ce" or session["login"]=="" :
        return redirect (url_for("dep_login"))
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts order by date1 desc').fetchall()
    conn.close()
    return render_template('past_ce.html',posts=posts,dates=dates)

@app.route('/ce/past')
def past_civ():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts order by date1 desc').fetchall()
    conn.close()
    return render_template('past_civ.html',posts=posts,dates=dates)


@app.route('/department_login.html/login_ee', methods=('POST','GET'))
def login_ee():
    if session["login"] != "login_ee" or session["login"]=="" :
        return redirect (url_for("dep_login") )
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts where dept_name="eee" and (status="approved" or status="rejected")').fetchall()
    conn.execute('UPDATE posts SET flag1 = 1 where dept_name="eee" and (status="approved" or status="rejected")')
    conn.commit()
    posts = conn.execute('SELECT * FROM posts order by date1').fetchall()
    conn.close()
    return render_template('login_ee.html',posts=posts,dates=dates,post=post)
    
@app.route('/department_login.html/login_ec', methods=('POST','GET'))
def login_ec():
    if session["login"] != "login_ec" or session["login"]=="" :
        return redirect (url_for("dep_login") )
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts where dept_name="ece" and (status="approved" or status="rejected")').fetchall()
    conn.execute('UPDATE posts SET flag1 = 1 where dept_name="ece" and (status="approved" or status="rejected")')
    conn.commit()
    posts = conn.execute('SELECT * FROM posts order by date1').fetchall()
    conn.close()
    return render_template('login_ec.html',posts=posts,dates=dates,post=post)
    
@app.route('/department_login.html/login_ce', methods=('POST','GET'))
def login_ce():
    if session["login"] != "login_ce" or session["login"]=="" :
        return redirect (url_for("dep_login") )
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts where dept_name="ce" and (status="approved" or status="rejected")').fetchall()
    conn.execute('UPDATE posts SET flag1 = 1 where dept_name="ce" and (status="approved" or status="rejected")')
    conn.commit()
    posts = conn.execute('SELECT * FROM posts order by date1').fetchall()
    conn.close()
    return render_template('login_ce.html',posts=posts,dates=dates,post=post)
    
@app.route('/department_login.html/login_me', methods=('POST','GET'))
def login_me():
    if session["login"] != "login_me" or session["login"]=="" :
        return redirect (url_for("dep_login"))
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts where dept_name="me" and (status="approved" or status="rejected")').fetchall()
    conn.execute('UPDATE posts SET flag1 = 1 where dept_name="me" and (status="approved" or status="rejected")')
    conn.commit()
    posts = conn.execute('SELECT * FROM posts order by date1').fetchall()
    conn.close()
    return render_template('login_me.html',posts=posts,dates=dates,post=post)

@app.route('/admin_login.html')
def adm_login():
    session["login1"]=""
    return render_template('admin_login.html')

@app.route('/admin_login.html/login1', methods=('POST','GET'))
def login1():
    session["login1"]=""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['passwords']
        conn = get_db_connection()
        post = conn.execute('SELECT * FROM a_login WHERE passwords = ? and username = ? ',
                (password, username,)).fetchone()
        posts = conn.execute('SELECT * FROM posts order by date1').fetchall()       
        conn.close()
    
        if post is not None:
            session["login1"]="login2"
            return redirect(url_for('login2'))
        else:
            flash ("Invalid Credentials",'admin')
            return redirect(url_for('adm_login'))
    else : 
        conn = get_db_connection()
        posts = conn.execute('SELECT * FROM posts order by date1').fetchall()       
        conn.close()
        return render_template('login2.html',posts=posts)

@app.route('/admin_login.html/login2', methods=('POST','GET'))
def login2():
    if session["login1"] != "login2" or session["login1"]=="":
        return redirect (url_for("adm_login"))
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts order by date1').fetchall()       
    conn.close()
    return render_template('login2.html',posts=posts)


@app.route('/admin_login.html/login2/<int:id>/approve', methods=('POST',))
def approve(id):
    if session["login1"] != "login2" or session["login1"]=="" :
        return redirect (url_for("adm_login"))
    post = get_post(id)
    flag=1
    status="approved"
    conn = get_db_connection()
    conn.execute('UPDATE posts SET flag = ?'
                         ' WHERE id = ?',
                         (flag, id))
    conn.execute('UPDATE posts SET status = ?'
                         ' WHERE id = ?',
                         (status, id))
   # conn.execute('UPDATE posts SET flag = 1,status = "approved" WHERE id = ?',(id))
    conn.commit()
    conn.close()
    if post['dept_name']=='cse':
      flash('"{}" was successfully approved from database!'.format(post['title']),'cse')
    elif post['dept_name']=='ece':
      flash('"{}" was successfully approved from database!'.format(post['title']),'ece')
    elif post['dept_name']=='eee':
      flash('"{}" was successfully approved from database!'.format(post['title']),'eee')
    elif post['dept_name']=='me':
      flash('"{}" was successfully approved from database!'.format(post['title']),'me')
    elif post['dept_name']=='ce':
      flash('"{}" was successfully approved from database!'.format(post['title']),'ce')
    return redirect(url_for('login1'))
@app.route('/admin_login.html/login2/<int:id>/deny', methods=('POST',))
def deny(id):
    if session["login1"] != "login2" or session["login1"]=="" :
        return redirect (url_for("adm_login"))
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('UPDATE posts SET flag = ?,status = ?'
                         ' WHERE id = ?',(0,"rejected",id))
    conn.commit()
    conn.close()
    if post['dept_name']=='cse':
      flash('"{}" was successfully deleted from database!'.format(post['title']),'cse')
    elif post['dept_name']=='ece':
      flash('"{}" was successfully deleted from database!'.format(post['title']),'ece')
    elif post['dept_name']=='eee':
      flash('"{}" was successfully deleted from database!'.format(post['title']),'eee')
    elif post['dept_name']=='me':
      flash('"{}" was successfully deleted from database!'.format(post['title']),'me')
    elif post['dept_name']=='ce':
      flash('"{}" was successfully deleted from database!'.format(post['title']),'ce')
    return redirect(url_for('login1'))
    
@app.route('/search1',methods=('POST','GET'))
def search1():
    if request.method == 'POST':
        searchtxt = request.form['searchtxt']
        conn = get_db_connection()
        posts = conn.execute("SELECT * FROM posts WHERE title like :search", {"search": '%' + searchtxt + '%'}).fetchall()
        conn.close()
        if posts is not None:
            return render_template('main.html', posts=posts,dates=dates)
        else:
    	    return 'No such event found'
    	    flash('Inavalid Credentials')
    	    return redirect(url_for('main'))
    else:
        flash('search anything')
        return redirect(url_for('main'))
@app.route('/cse/search1',methods=('POST','GET'))
def cse_search1():
    if request.method == 'POST':
        searchtxt = request.form['searchtxt']
        conn = get_db_connection()
        posts = conn.execute("SELECT * FROM posts WHERE dept_name='cse' and title like :search", {"search": '%' + searchtxt + '%'}).fetchall()
        conn.close()
        if posts is not None:
            return render_template('cse.html', posts=posts,dates=dates)
        else:
    	    return 'No such event found'
    	    flash('Inavalid Credentials')
    	    return redirect(url_for('cse'))
    else:
        flash('search anything')
        return redirect(url_for('cse'))
        
@app.route('/past_cse/search2',methods=('POST','GET'))
def past_cse_search2():
    if request.method == 'POST':
        searchtxt = request.form['searchtxt']
        conn = get_db_connection()
        posts = conn.execute("SELECT * FROM posts WHERE dept_name='cse' and title like :search", {"search": '%' + searchtxt + '%'}).fetchall()
        conn.close()
        if posts is not None:
            return render_template('past_cse.html', posts=posts,dates=dates)
        else:
    	    return 'No such event found'
    	    flash('Inavalid Credentials')
    	    return redirect(url_for('past_cse'))
    else:
        flash('search anything')
        return redirect(url_for('past_cse'))
        
@app.route('/ece/search1',methods=('POST','GET'))
def ece_search1():
    if request.method == 'POST':
        searchtxt = request.form['searchtxt']
        conn = get_db_connection()
        posts = conn.execute("SELECT * FROM posts WHERE dept_name='ece' and title like :search", {"search": '%' + searchtxt + '%'}).fetchall()
        conn.close()
        if posts is not None:
            return render_template('ece.html', posts=posts,dates=dates)
        else:
    	    return 'No such event found'
    	    flash('Inavalid Credentials')
    	    return redirect(url_for('ece'))
    else:
        flash('search anything')
        return redirect(url_for('ece'))
        
@app.route('/past_ece/search2',methods=('POST','GET'))
def past_ece_search2():
    if request.method == 'POST':
        searchtxt = request.form['searchtxt']
        conn = get_db_connection()
        posts = conn.execute("SELECT * FROM posts WHERE dept_name='ece' and title like :search", {"search": '%' + searchtxt + '%'}).fetchall()
        conn.close()
        if posts is not None:
            return render_template('past_ece.html', posts=posts,dates=dates)
        else:
    	    return 'No such event found'
    	    flash('Inavalid Credentials')
    	    return redirect(url_for('past_ece'))
    else:
        flash('search anything')
        return redirect(url_for('past_ece'))

@app.route('/eee/search1',methods=('POST','GET'))
def eee_search1():
    if request.method == 'POST':
        searchtxt = request.form['searchtxt']
        conn = get_db_connection()
        posts = conn.execute("SELECT * FROM posts WHERE dept_name='eee' and title like :search", {"search": '%' + searchtxt + '%'}).fetchall()
        conn.close()
        if posts is not None:
            return render_template('eee.html', posts=posts,dates=dates)
        else:
    	    return 'No such event found'
    	    flash('Inavalid Credentials')
    	    return redirect(url_for('eee'))
    else:
        flash('search anything')
        return redirect(url_for('eee'))
        
@app.route('/past_eee/search2',methods=('POST','GET'))
def past_eee_search2():
    if request.method == 'POST':
        searchtxt = request.form['searchtxt']
        conn = get_db_connection()
        posts = conn.execute("SELECT * FROM posts WHERE dept_name='eee' and title like :search", {"search": '%' + searchtxt + '%'}).fetchall()
        conn.close()
        if posts is not None:
            return render_template('past_eee.html', posts=posts,dates=dates)
        else:
    	    return 'No such event found'
    	    flash('Inavalid Credentials')
    	    return redirect(url_for('past_eee'))
    else:
        flash('search anything')
        return redirect(url_for('past_eee'))
        
@app.route('/civ/search1',methods=('POST','GET'))
def civ_search1():
    if request.method == 'POST':
        searchtxt = request.form['searchtxt']
        conn = get_db_connection()
        posts = conn.execute("SELECT * FROM posts WHERE dept_name='ce' and title like :search", {"search": '%' + searchtxt + '%'}).fetchall()
        conn.close()
        if posts is not None:
            return render_template('ce.html', posts=posts,dates=dates)
        else:
    	    return 'No such event found'
    	    flash('Inavalid Credentials')
    	    return redirect(url_for('ce'))
    else:
        flash('search anything')
        return redirect(url_for('ce'))
        
@app.route('/past_civ/search2',methods=('POST','GET'))
def past_civ_search2():
    if request.method == 'POST':
        searchtxt = request.form['searchtxt']
        conn = get_db_connection()
        posts = conn.execute("SELECT * FROM posts WHERE dept_name='ce' and title like :search", {"search": '%' + searchtxt + '%'}).fetchall()
        conn.close()
        if posts is not None:
            return render_template('past_civ.html', posts=posts,dates=dates)
        else:
    	    return 'No such event found'
    	    flash('Inavalid Credentials')
    	    return redirect(url_for('past_civ'))
    else:
        flash('search anything')
        return redirect(url_for('past_civ'))
@app.route('/mec/search1',methods=('POST','GET'))
def mec_search1():
    if request.method == 'POST':
        searchtxt = request.form['searchtxt']
        conn = get_db_connection()
        posts = conn.execute("SELECT * FROM posts WHERE dept_name='me' and title like :search", {"search": '%' + searchtxt + '%'}).fetchall()
        conn.close()
        if posts is not None:
            return render_template('me.html', posts=posts,dates=dates)
        else:
    	    return 'No such event found'
    	    flash('Inavalid Credentials')
    	    return redirect(url_for('me'))
    else:
        flash('search anything')
        return redirect(url_for('me'))
        
@app.route('/past_mec/search2',methods=('POST','GET'))
def past_mec_search2():
    if request.method == 'POST':
        searchtxt = request.form['searchtxt']
        conn = get_db_connection()
        posts = conn.execute("SELECT * FROM posts WHERE dept_name='me' and title like :search", {"search": '%' + searchtxt + '%'}).fetchall()
        conn.close()
        if posts is not None:
            return render_template('past_mec.html', posts=posts,dates=dates)
        else:
    	    return 'No such event found'
    	    flash('Inavalid Credentials')
    	    return redirect(url_for('past_mec'))
    else:
        flash('search anything')
        return redirect(url_for('past_mec'))
@app.route('/me/search1',methods=('POST','GET'))
def me_search1():
    if request.method == 'POST':
        searchtxt = request.form['searchtxt']
        conn = get_db_connection()
        posts = conn.execute("SELECT * FROM posts WHERE dept_name='me' and title like :search", {"search": '%' + searchtxt + '%'}).fetchall()
        conn.close()
        if posts is not None:
            return render_template('login_me.html', posts=posts,dates=dates)
        else:
    	    return 'No such event found'
    	    flash('Inavalid Credentials')
    	    return redirect(url_for('login_me'))
    else:
        flash('search anything')
        return redirect(url_for('login_me'))
        
@app.route('/ce/search1',methods=('POST','GET'))
def ce_search1():
    if request.method == 'POST':
        searchtxt = request.form['searchtxt']
        conn = get_db_connection()
        posts = conn.execute("SELECT * FROM posts WHERE dept_name='ce' and title like :search", {"search": '%' + searchtxt + '%'}).fetchall()
        conn.close()
        if posts is not None:
            return render_template('login_ce.html', posts=posts,dates=dates)
        else:
    	    return 'No such event found'
    	    flash('Inavalid Credentials')
    	    return redirect(url_for('login_ce'))
    else:
        flash('search anything')
        return redirect(url_for('login_ce'))
@app.route('/ee/search1',methods=('POST','GET'))
def ee_search1():
    if request.method == 'POST':
        searchtxt = request.form['searchtxt']
        conn = get_db_connection()
        posts = conn.execute("SELECT * FROM posts WHERE dept_name='eee' and title like :search", {"search": '%' + searchtxt + '%'}).fetchall()
        conn.close()
        if posts is not None:
            return render_template('login_ee.html', posts=posts,dates=dates)
        else:
    	    return 'No such event found'
    	    flash('Inavalid Credentials')
    	    return redirect(url_for('login_ee'))
    else:
        flash('search anything')
        return redirect(url_for('login_ee'))
@app.route('/ec/search1',methods=('POST','GET'))
def ec_search1():
    if request.method == 'POST':
        searchtxt = request.form['searchtxt']
        conn = get_db_connection()
        posts = conn.execute("SELECT * FROM posts WHERE dept_name='ece' and title like :search", {"search": '%' + searchtxt + '%'}).fetchall()
        conn.close()
        if posts is not None:
            return render_template('login_ec.html', posts=posts,dates=dates)
        else:
    	    return 'No such event found'
    	    flash('Inavalid Credentials')
    	    return redirect(url_for('login_ec'))
    else:
        flash('search anything')
        return redirect(url_for('login_ec'))
@app.route('/cs/search1',methods=('POST','GET'))
def cs_search1():
    if request.method == 'POST':
        searchtxt = request.form['searchtxt']
        conn = get_db_connection()
        posts = conn.execute("SELECT * FROM posts WHERE dept_name='cse' and title like :search", {"search": '%' + searchtxt + '%'}).fetchall()
        conn.close()
        if posts is not None:
            return render_template('login_cs.html', posts=posts,dates=dates)
        else:
    	    return 'No such event found'
    	    flash('Inavalid Credentials')
    	    return redirect(url_for('login_cs'))
    else:
        flash('search anything')
        return redirect(url_for('login_cs'))
@app.route('/past_me/search2',methods=('POST','GET'))
def past_me_search2():
    if request.method == 'POST':
        searchtxt = request.form['searchtxt']
        conn = get_db_connection()
        posts = conn.execute("SELECT * FROM posts WHERE dept_name='me' and title like :search", {"search": '%' + searchtxt + '%'}).fetchall()
        conn.close()
        if posts is not None:
            return render_template('past_me.html', posts=posts,dates=dates)
        else:
    	    return 'No such event found'
    	    flash('Inavalid Credentials')
    	    return redirect(url_for('past_me'))
    else:
        flash('search anything')
        return redirect(url_for('past_me'))
@app.route('/past_ce/search2',methods=('POST','GET'))
def past_ce_search2():
    if request.method == 'POST':
        searchtxt = request.form['searchtxt']
        conn = get_db_connection()
        posts = conn.execute("SELECT * FROM posts WHERE dept_name='ce' and title like :search", {"search": '%' + searchtxt + '%'}).fetchall()
        conn.close()
        if posts is not None:
            return render_template('past_ce.html', posts=posts,dates=dates)
        else:
    	    return 'No such event found'
    	    flash('Inavalid Credentials')
    	    return redirect(url_for('past_ce'))
    else:
        flash('search anything')
        return redirect(url_for('past_ce'))
@app.route('/past_cs/search2',methods=('POST','GET'))
def past_cs_search2():
    if request.method == 'POST':
        searchtxt = request.form['searchtxt']
        conn = get_db_connection()
        posts = conn.execute("SELECT * FROM posts WHERE dept_name='cse' and title like :search", {"search": '%' + searchtxt + '%'}).fetchall()
        conn.close()
        if posts is not None:
            return render_template('past_cs.html', posts=posts,dates=dates)
        else:
    	    return 'No such event found'
    	    flash('Inavalid Credentials')
    	    return redirect(url_for('past_cs'))
    else:
        flash('search anything')
        return redirect(url_for('past_cs'))
@app.route('/past_ee/search2',methods=('POST','GET'))
def past_ee_search2():
    if request.method == 'POST':
        searchtxt = request.form['searchtxt']
        conn = get_db_connection()
        posts = conn.execute("SELECT * FROM posts WHERE dept_name='eee' and title like :search", {"search": '%' + searchtxt + '%'}).fetchall()
        conn.close()
        if posts is not None:
            return render_template('past_ee.html', posts=posts,dates=dates)
        else:
    	    return 'No such event found'
    	    flash('Inavalid Credentials')
    	    return redirect(url_for('past_ee'))
    else:
        flash('search anything')
        return redirect(url_for('past_ee'))
@app.route('/past_ec/search2',methods=('POST','GET'))
def past_ec_search2():
    if request.method == 'POST':
        searchtxt = request.form['searchtxt']
        conn = get_db_connection()
        posts = conn.execute("SELECT * FROM posts WHERE dept_name='ece' and title like :search", {"search": '%' + searchtxt + '%'}).fetchall()
        conn.close()
        if posts is not None:
            return render_template('past_ec.html', posts=posts,dates=dates)
        else:
    	    return 'No such event found'
    	    flash('Inavalid Credentials')
    	    return redirect(url_for('past_ec'))
    else:
        flash('search anything')
        return redirect(url_for('past_ec'))
        
@app.route('/<int:post_id>',methods=('POST','GET'))
def post(post_id):
    post =get_post(post_id)
    if post['dept_name']=='cse':
    	return redirect(url_for('cse_post',post_id=post['id']))
    elif post['dept_name']=='ece':
    	return redirect(url_for('ece_post',post_id=post['id']))
    elif post['dept_name']=='eee':
    	return redirect(url_for('eee_post',post_id=post['id']))
    elif post['dept_name']=='me':
    	return redirect(url_for('me_post',post_id=post['id']))
    elif post['dept_name']=='ce':
    	return redirect(url_for('ce_post',post_id=post['id']))

@app.route('/<int:post_id>/view_feed_cs')
def view_feed_cs(post_id):
    post1 = get_post(post_id)
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM feedback WHERE id2 = ? ',
                        (post_id,)).fetchall()
    conn.commit()
    conn.close()
    return render_template('view_feed_cs.html',posts=posts,post1=post1)
@app.route('/<int:post_id>/view_feed_me')
def view_feed_me(post_id):
    post1 = get_post(post_id)
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM feedback WHERE id2 = ? ',
                        (post_id,)).fetchall()
    conn.commit()
    conn.close()
    return render_template('view_feed_me.html',posts=posts,post1=post1)
@app.route('/<int:post_id>/view_feed_ce')
def view_feed_ce(post_id):
    post1 = get_post(post_id)
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM feedback WHERE id2 = ? ',
                        (post_id,)).fetchall()
    conn.commit()
    conn.close()
    return render_template('view_feed_ce.html',posts=posts,post1=post1)
@app.route('/<int:post_id>/view_feed_ee')
def view_feed_ee(post_id):
    post1 = get_post(post_id)
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM feedback WHERE id2 = ? ',
                        (post_id,)).fetchall()
    conn.commit()
    conn.close()
    return render_template('view_feed_ee.html',posts=posts,post1=post1)
@app.route('/<int:post_id>/view_feed_ec')
def view_feed_ec(post_id):
    post1 = get_post(post_id)
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM feedback WHERE id2 = ? ',
                        (post_id,)).fetchall()
    conn.commit()
    conn.close()
    return render_template('view_feed_ec.html',posts=posts,post1=post1) 
@app.route('/<int:id>/submitfeed', methods=('GET', 'POST'))
def submitfeed(id):
    if request.method == 'POST':
        feedback = request.form['content']
        id2 = id
        conn = get_db_connection()
        conn.execute('INSERT INTO feedback (id2,feedback) VALUES (?, ?)',
                     (id2,feedback))
        conn.commit()
        conn.close()
        return redirect(url_for('past'))
    return render_template('past.html')
    
@app.route('/<int:id>/submitfeed_cs', methods=('GET', 'POST'))
def submitfeed_cs(id):
    if request.method == 'POST':
        feedback = request.form['content']
        id2 = id
        conn = get_db_connection()
        conn.execute('INSERT INTO feedback (id2,feedback) VALUES (?, ?)',
                     (id2,feedback))
        conn.commit()
        conn.close()
        return redirect(url_for('past_cse'))
    return render_template('past_cse.html')
@app.route('/<int:id>/submitfeed_ec', methods=('GET', 'POST'))
def submitfeed_ec(id):
    if request.method == 'POST':
        feedback = request.form['content']
        id2 = id
        conn = get_db_connection()
        conn.execute('INSERT INTO feedback (id2,feedback) VALUES (?, ?)',
                     (id2,feedback))
        conn.commit()
        conn.close()
        return redirect(url_for('past_ece'))
    return render_template('past_ece.html')
    
@app.route('/<int:id>/submitfeed_ee', methods=('GET', 'POST'))
def submitfeed_ee(id):
    if request.method == 'POST':
        feedback = request.form['content']
        id2 = id
        conn = get_db_connection()
        conn.execute('INSERT INTO feedback (id2,feedback) VALUES (?, ?)',
                     (id2,feedback))
        conn.commit()
        conn.close()
        return redirect(url_for('past_eee'))
    return render_template('past_eee.html')
    
@app.route('/<int:id>/submitfeed_ce', methods=('GET', 'POST'))
def submitfeed_ce(id):
    if request.method == 'POST':
        feedback = request.form['content']
        id2 = id
        conn = get_db_connection()
        conn.execute('INSERT INTO feedback (id2,feedback) VALUES (?, ?)',
                     (id2,feedback))
        conn.commit()
        conn.close()
        return redirect(url_for('past_civ'))
    return render_template('past_civ.html')
@app.route('/<int:id>/submitfeed_me', methods=('GET', 'POST'))
def submitfeed_me(id):
    if request.method == 'POST':
        feedback = request.form['content']
        id2 = id
        conn = get_db_connection()
        conn.execute('INSERT INTO feedback (id2,feedback) VALUES (?, ?)',
                     (id2,feedback))
        conn.commit()
        conn.close()
        return redirect(url_for('past_mec'))
    return render_template('past_mec.html')
       
@app.route('/search2',methods=('POST','GET'))
def search2():
    if request.method == 'POST':
        searchtxt = request.form['searchtxt']
        conn = get_db_connection()
        posts = conn.execute("SELECT * FROM posts WHERE title like :search", {"search": '%' + searchtxt + '%'}).fetchall()
        conn.close()
        if posts is not None:
            return render_template('past.html', posts=posts,dates=dates)
        else:
    	    return 'No such event found'
    	    flash('Inavalid Credentials')
    	    return redirect(url_for('past'))
    else:
        flash('search anything')
        return redirect(url_for('past'))    
@app.route('/<int:id>/feedback', methods=('GET', 'POST'))
def feedback(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        dept_name='cse'

    return render_template('feedback.html',post=post) 

@app.route('/<int:id>/feedback_cs', methods=('GET', 'POST'))
def feedback_cs(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        dept_name='cse'

    return render_template('feedback_cs.html',post=post) 
@app.route('/feedback_cs/back', methods=('GET', 'POST'))
def feedback_cs_back():
    
    return redirect(url_for('past_cse'))

@app.route('/<int:id>/feedback_ec', methods=('GET', 'POST'))
def feedback_ec(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        dept_name='cse'

    return render_template('feedback_ec.html',post=post) 

@app.route('/<int:id>/feedback_ee', methods=('GET', 'POST'))
def feedback_ee(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        dept_name='cse'

    return render_template('feedback_ee.html',post=post) 

@app.route('/<int:id>/feedback_ce', methods=('GET', 'POST'))
def feedback_ce(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        dept_name='cse'

    return render_template('feedback_ce.html',post=post) 

@app.route('/<int:id>/feedback_me', methods=('GET', 'POST'))
def feedback_me(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        dept_name='cse'

    return render_template('feedback_me.html',post=post) 


