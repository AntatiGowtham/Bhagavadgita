
# A very simple Flask Hello World app for you to get started with...

'''from flask import Flask,render_template,request,make_response,redirect,session,url_for

app = Flask(__name__)'''

from flask import Flask, render_template, session, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a strong secret key


@app.route('/')
def home():
    return render_template('intro.html')
@app.route('/home')
def home1():
    return render_template('main.html')

@app.route('/story')
def story():
    return render_template('story.html')

@app.route('/pictures1')
def pictures1_page():
    return render_template('pictures1.html')

@app.route('/pictures2')
def pictures2_page():
    return render_template('pictures2.html')


'''@app.route('/summary1.html', methods=["GET"])
def summary1():
    selected_language = request.cookies.get('lang', 'english')
    return render_template('summary1.html', lang=selected_language)
@app.route('/set_language1', methods=["POST"])
def set_language1():
    selected_language = request.form['lang']
    resp = make_response(redirect('/summary1.html'))
    resp.set_cookie('lang', selected_language)
    return resp'''
'''@app.route('/summary1.html', methods=["GET"])
def summary1():
    # Check if the page has already been viewed in the current session
    if 'viewed_summary1' not in session:
        session['viewed_summary1'] = True  # Mark the page as viewed
        return render_template('summary1.html', lang=session.get('lang', 'english'))
    else:
        # Serve a different or modified response for subsequent views if needed
        return render_template('summary1.html', lang=session.get('lang', 'english'))

@app.route('/set_language1', methods=["POST"])
def set_language1():
    selected_language = request.form['lang']
    session['lang'] = selected_language  # Store selected language in session
    return redirect('/summary1.html')'''

@app.route('/shloka1', methods=["GET"])
def shloka1():
    return render_template('shloka1.html')

@app.route('/summary1.html', methods=["GET"])
def summary1():
    selected_language = session.get('lang', 'english')
    return render_template('summary1.html', lang=selected_language)

@app.route('/set_language1', methods=["POST"])
def set_language1():
    selected_language = request.form['lang']
    session['lang'] = selected_language
    return redirect(url_for('summary1'))




@app.route('/shloka2', methods=["GET"])
def shloka2():
    return render_template('shloka2.html')

@app.route('/summary2.html', methods=["GET"])
def summary2():
    selected_language = session.get('lang', 'english')
    return render_template('summary2.html', lang=selected_language)

@app.route('/set_language2', methods=["POST"])
def set_language2():
    selected_language = request.form['lang']
    session['lang'] = selected_language
    return redirect(url_for('summary2'))


@app.route('/shloka3', methods=["GET"])
def shloka3():
    return render_template('shloka3.html')

@app.route('/summary3.html', methods=["GET"])
def summary3():
    selected_language = session.get('lang', 'english')
    return render_template('summary3.html', lang=selected_language)

@app.route('/set_language3', methods=["POST"])
def set_language3():
    selected_language = request.form['lang']
    session['lang'] = selected_language
    return redirect(url_for('summary3'))



@app.route('/shloka4', methods=["GET"])
def shloka4():
    return render_template('shloka4.html')

@app.route('/summary4.html', methods=["GET"])
def summary4():
    selected_language = session.get('lang', 'english')
    return render_template('summary4.html', lang=selected_language)

@app.route('/set_language4', methods=["POST"])
def set_language4():
    selected_language = request.form['lang']
    session['lang'] = selected_language
    return redirect(url_for('summary4'))


@app.route('/shloka5', methods=["GET"])
def shloka5():
    return render_template('shloka5.html')

@app.route('/summary5.html', methods=["GET"])
def summary5():
    selected_language = session.get('lang', 'english')
    return render_template('summary5.html', lang=selected_language)

@app.route('/set_language5', methods=["POST"])
def set_language5():
    selected_language = request.form['lang']
    session['lang'] = selected_language
    return redirect(url_for('summary5'))


@app.route('/shloka6', methods=["GET"])
def shloka6():
    return render_template('shloka6.html')

@app.route('/summary6.html', methods=["GET"])
def summary6():
    selected_language = session.get('lang', 'english')
    return render_template('summary6.html', lang=selected_language)

@app.route('/set_language6', methods=["POST"])
def set_language6():
    selected_language = request.form['lang']
    session['lang'] = selected_language
    return redirect(url_for('summary6'))


@app.route('/shloka7', methods=["GET"])
def shloka7():
    return render_template('shloka7.html')

@app.route('/summary7.html', methods=["GET"])
def summary7():
    selected_language = session.get('lang', 'english')
    return render_template('summary7.html', lang=selected_language)

@app.route('/set_language7', methods=["POST"])
def set_language7():
    selected_language = request.form['lang']
    session['lang'] = selected_language
    return redirect(url_for('summary7'))


@app.route('/shloka8', methods=["GET"])
def shloka8():
    return render_template('shloka8.html')

@app.route('/summary8.html', methods=["GET"])
def summary8():
    selected_language = session.get('lang', 'english')
    return render_template('summary8.html', lang=selected_language)

@app.route('/set_language8', methods=["POST"])
def set_language8():
    selected_language = request.form['lang']
    session['lang'] = selected_language
    return redirect(url_for('summary8'))


@app.route('/shloka9', methods=["GET"])
def shloka9():
    return render_template('shloka9.html')

@app.route('/summary9.html', methods=["GET"])
def summary9():
    selected_language = session.get('lang', 'english')
    return render_template('summary9.html', lang=selected_language)

@app.route('/set_language9', methods=["POST"])
def set_language9():
    selected_language = request.form['lang']
    session['lang'] = selected_language
    return redirect(url_for('summary9'))


@app.route('/shloka10', methods=["GET"])
def shloka10():
    return render_template('shloka10.html')

@app.route('/summary10.html', methods=["GET"])
def summary10():
    selected_language = session.get('lang', 'english')
    return render_template('summary10.html', lang=selected_language)

@app.route('/set_language10', methods=["POST"])
def set_language10():
    selected_language = request.form['lang']
    session['lang'] = selected_language
    return redirect(url_for('summary10'))











