from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from flask_bcrypt import Bcrypt
from recommendation_system import recommend_learning_materials
from sklearn.metrics import precision_score, recall_score, f1_score



app = Flask(__name__)
bcrypt = Bcrypt(app)

app.secret_key = 'xyz123'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'username'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'recommendationnotetaking'

mysql = MySQL(app)

# @app.route('/test')
# def test_db():
#     cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#     cursor.execute('SELECT 1')
#     return "Database connection successful!"

@app.route('/')
@app.route('/login', methods=['POST', 'GET'])
def login():
    message = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        users = cursor.fetchone()
        if users and bcrypt.check_password_hash(users['password'], password):
            session['loggedin'] = True
            session['userid'] = users['userid']
            session['username'] = users['username']
            message = 'Logged in Successfully!'
            return redirect(url_for('notes'))
        else:
            message = 'Incorrect username / password!'
    return render_template('LoginSignup.html', msg = message)

@app.route('/create_note')
def create_note():
    if 'loggedin' in session:  # Check if the user is logged in
        return render_template('CreatingNote.html')
    return redirect(url_for('login'))  # Redirect to login if not logged in

@app.route('/register', methods=['POST', 'GET'])
def register():
    message = ''
    if request.method == 'POST':
        username = request.form.get('username')
        name = request.form.get('name')
        password = request.form.get('password')
        email = request.form.get('email')
        kindOfSchool = request.form.get('kindOfSchool')
        currentCM = request.form.get('currentCM')
        subOfInt = request.form.get('subOfInt')
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        # Check if the username already exists
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        existing_username = cursor.fetchone()
        if existing_username:
            message = 'Username already exists! Please choose a different username.'
            return render_template('LoginSignup.html', msg=message)

        # Check if the email already exists
        cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
        existing_email = cursor.fetchone()
        if existing_email:
            message = 'Email address already exists! Please use a different email.'
            return render_template('LoginSignup.html', msg=message)

        # Additional form validation
        if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            message = 'Invalid email address!'
            return render_template('LoginSignup.html', msg=message)
        elif not username or not password or not email:
            message = 'Please fill out the registration form completely!'
            return render_template('LoginSignup.html', msg=message)

        # Hash the password and insert the new user
        hashedPassword = bcrypt.generate_password_hash(password).decode('utf-8')
        print(f"Original Password: {password}")  # Debugging: Print original password
        print(f"Hashed Password: {hashedPassword}")  # Debugging: Print hashed password

        try:
            cursor.execute(
                '''
                INSERT INTO users (username, name, password, email, kindOfSchool, currentCM, subOfInt) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ''', 
                (username, name, hashedPassword, email, kindOfSchool, currentCM, subOfInt)
            )
            mysql.connection.commit()
            message = 'You have successfully registered!'

            # Fetch the user ID of the newly registered user
            cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
            new_user = cursor.fetchone()
            userid = new_user['userid']

            # Generate initial recommendations based on currentCM and subOfInt
            recommendations = recommend_learning_materials(currentCM, subOfInt)

            # Insert the recommendations into the database
            for recommendation in recommendations:
                cursor.execute(
                    '''
                    INSERT INTO recommendations (noteid, userid, resourceName, resourceURL, description, subjectArea, bookAuthor, is_initial, createdAt)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, NOW())
                    ''',
                    (None, userid, recommendation['title'], recommendation['url'], recommendation['description'], recommendation['subject'], recommendation['author'], 1)
                )
            
            # Commit the recommendations to the database
            mysql.connection.commit()

        except Exception as e:
            mysql.connection.rollback()
            message = f"An error occurred: {e}"
            print(message)

    elif request.method == 'POST':
        message = 'Please fill out the registration form!'
    return render_template('LoginSignup.html', msg=message)


@app.route('/save_note', methods=['POST'])
def save_note():
    if 'loggedin' in session:
        userid = session['userid']
        noteid = request.form.get('noteid')  # Get the note ID from the form (hidden input field)
        title = request.form.get('titleNote')
        content = request.form.get('content')

        if not title or not content:
            return 'Title and content are required fields!'
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            if noteid:  # If a note ID exists, update the note
                cursor.execute(
                    'UPDATE notes SET title = %s, content = %s WHERE noteid = %s AND userid = %s',
                    (title, content, noteid, userid)
                )
                message = "Note successfully updated!"
            else:  # If no note ID, create a new note
                cursor.execute(
                    'INSERT INTO notes (userid, title, content) VALUES (%s, %s, %s)',
                    (userid, title, content)
                )
                message = "Note successfully saved!"

            mysql.connection.commit()

            # Fetch the saved or updated note
            if noteid:
                cursor.execute('SELECT * FROM notes WHERE noteid = %s AND userid = %s', (noteid, userid))
            else:
                cursor.execute('SELECT * FROM notes WHERE noteid = LAST_INSERT_ID() AND userid = %s', (userid,))
            savedNote = cursor.fetchone()


            return render_template('CreatingNote.html', note=savedNote, message=message)
        except Exception as e:
            mysql.connection.rollback()
            return render_template('CreatingNote.html', message=f"An error occurred: {e}")
    else:
        return redirect(url_for('login'))

@app.route('/notes')
def notes():
    if 'loggedin' in session:
        userid = session['userid']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            # Fetch user notes
            cursor.execute('SELECT * FROM notes WHERE userid = %s AND is_archived = 0 ORDER BY createdAt DESC', (userid,))
            userNotes = cursor.fetchall()

            # Fetch initial recommendations
            cursor.execute('SELECT * FROM recommendations WHERE userid = %s AND is_initial = 1 ORDER BY createdAt DESC LIMIT 3', (userid,))
            initialRecommendations = cursor.fetchall()

            # Fetch recommendation history with feedback information
            cursor.execute('''
                SELECT r.*, f.isRelevant 
                FROM recommendations r
                LEFT JOIN feedbackRelevance f ON r.userid = f.userid AND r.noteid = f.noteid AND r.resourceName = f.materialTitle
                WHERE r.userid = %s AND r.is_initial = 0
                ORDER BY r.createdAt DESC
            ''', (userid,))
            recommendedHistory = cursor.fetchall()

            # Render the notes page
            return render_template(
                'notes.html',
                username=session['username'],
                notes=userNotes,
                initialRecommendations=initialRecommendations,
                recommendedHistory=recommendedHistory
            )
        except Exception as e:
            mysql.connection.rollback()
            return render_template('notes.html', username=session['username'], notes=[], initialRecommendations=[], recommendedHistory=[], error=f"An error occurred: {e}")
    return redirect(url_for('login'))


@app.route('/submit_feedback', methods=['POST'])
def sumbit_feedback():
    if 'loggedin' in session:
        userid = session['userid']
        data = request.json
        title = data.get('title')
        isRelevant = data.get('isRelevant')
        noteid = data.get('noteid')
        
        if not title or isRelevant is None:
            return jsonify({'message': 'Invalid feedback data.'})
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        try:
            # Check if the feedback already exists
            cursor.execute('''
                SELECT * FROM feedbackRelevance 
                WHERE userid = %s AND noteid = %s AND materialTitle = %s
            ''', (userid, noteid, title))
            existing_feedback = cursor.fetchone()

            if existing_feedback:
                return jsonify({'message': 'Duplicate feedback detected. Feedback already exists.'})

            cursor.execute('''
                    INSERT INTO feedbackRelevance (userid, noteid, materialTitle, isRelevant) 
                    VALUES (%s, %s, %s, %s)
                ''', (userid, noteid, title, isRelevant))
            mysql.connection.commit()
            return jsonify({'message': 'Feedback submitted successfully!'})
        except Exception as e:
            mysql.connection.rollback()
            return jsonify({'message': f'Error submitting feedback: {e}'})
    else:
        return jsonify({'message': 'User not logged in.'})
    

@app.route('/clear_recommendations', methods=['POST'])
def clear_recommendations():
    if 'loggedin' in session:
        userid = session['userid']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        try:
            cursor.execute('DELETE FROM recommendations WHERE userid = %s AND is_initial = 0', (userid,))
            cursor.connection.commit()
        except Exception as e:
            mysql.connection.rollback()
            message = f"An error occurred while clearing recommendations: {e}"
            print(message)

        return redirect(url_for('notes'))
    return redirect(url_for('login'))

@app.route('/recommend', methods=['POST'])
def recommend():
    if 'loggedin' in session:
        title = request.form.get('titleNote', '')
        content = request.form.get('content', '')
        userid = session['userid']
        noteid = request.form.get('noteid', None)

        recommendations = recommend_learning_materials(title, content)

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            for recommendation in recommendations:
                cursor.execute('SELECT * FROM recommendations WHERE userid = %s AND noteid = %s AND resourceName = %s', (userid, noteid, recommendation['title'],))
                existingRecommendation = cursor.fetchone()
            
                if not existingRecommendation:
                    cursor.execute('INSERT INTO recommendations (noteid, userid, resourceName, resourceURL, description, subjectArea, bookAuthor, createdAt) VALUES (%s, %s, %s, %s, %s, %s, %s, NOW())', (noteid, userid, recommendation['title'], recommendation['url'], recommendation['description'], recommendation['subject'], recommendation['author'],))
                    mysql.connection.commit()
        except Exception as e:
            mysql.connection.rollback()
            return render_template('CreatingNote.html', message=f"An error occurred while saving recommendations: {e}")

        note = {'title': title, 'content': content, 'noteid': noteid}

        return render_template('CreatingNote.html', usersername = session['username'], recommendations = recommendations, note = note)
    return redirect(url_for('login'))

@app.route('/view_note/<int:noteid>')
def view_note(noteid):
    if 'loggedin' in session:
        userid = session['userid']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute('SELECT * FROM notes WHERE userid = %s and noteid = %s ORDER BY createdAt DESC', (userid, noteid,))
            note = cursor.fetchone()

            if note:
                return render_template('CreatingNote.html', username = session['username'], note = note)
            else:
                return redirect(url_for('notes'))
        except Exception as e:
            return render_template('notes.html', username=session['username'], error=f"An error occurred: {e}")
    return redirect(url_for('login'))

@app.route('/delete_recommendation/<int:recommendationid>', methods=['GET', 'POST'])
def delete_recommendation(recommendationid):
    if 'loggedin' in session:
        userid = session['userid']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        try:
            cursor.execute('DELETE FROM recommendations WHERE recommendationid = %s AND userid = %s', (recommendationid, userid,))
            cursor.connection.commit()
            return redirect(url_for('notes'))
        except Exception as e:
            mysql.connection.rollback()
            return f"An error occurred: {e}"
    return redirect(url_for('login'))

@app.route('/delete_note/<int:noteid>', methods=['GET'])
def delete_note(noteid):
    if 'loggedin' in session:
        userid = session['userid']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        try:
            cursor.execute('DELETE FROM recommendations WHERE noteid = %s AND userid = %s', (noteid, userid,))
            cursor.execute('DELETE FROM feedbackRelevance WHERE noteid = %s AND userid = %s', (noteid, userid,))
            cursor.execute('DELETE FROM notes WHERE noteid = %s AND userid = %s', (noteid, userid,))

            cursor.connection.commit()
            return redirect(url_for('notes'))
        except Exception as e:
            mysql.connection.rollback()
            return f"An error occurred: {e}"
    return redirect(url_for('login'))


@app.route('/profile_settings')
def profile_settings():
    if 'loggedin' in session:
        userid = session['userid']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE userid = %s', (userid,))
        allUserInfo = cursor.fetchone()
        return render_template('profileSettings.html', username = session['username'], userInfo = allUserInfo)
    else:
        return redirect(url_for('login'))

@app.route('/update_info', methods=['POST'])
def update_info():
    if 'loggedin' in session:
        userid = session['userid']

        # Get the form data
        username = request.form.get('username')
        name = request.form.get('name')
        password = request.form.get('password')
        email = request.form.get('email')
        kindOfSchool = request.form.get('schoolType')
        currentCM = request.form.get('currentCourses')
        subOfInt = request.form.get('subjectInterest')

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        try:
            # Fetch the existing user data
            cursor.execute('SELECT * FROM users WHERE userid = %s', (userid,))
            current_user = cursor.fetchone()

            # Preserve fields that are not explicitly updated
            if not username:
                username = current_user['username']
            if not name:
                name = current_user['name']
            if not password:
                hashedPassword = current_user['password']  # Keep the existing hashed password
            else:
                # Hash the new password if it's updated
                hashedPassword = bcrypt.generate_password_hash(password).decode('utf-8')
            if not email:
                email = current_user['email']
            if not kindOfSchool:
                kindOfSchool = current_user['kindOfSchool']
            if not currentCM:
                currentCM = current_user['currentCM']
            if not subOfInt:
                subOfInt = current_user['subOfInt']

            # Update the user's information in the database
            cursor.execute(
                '''
                UPDATE users 
                SET username = %s, name = %s, password = %s, email = %s, 
                    kindOfSchool = %s, currentCM = %s, subOfInt = %s 
                WHERE userid = %s
                ''',
                (username, name, hashedPassword, email, kindOfSchool, currentCM, subOfInt, userid)
            )

            # Generate new recommendations based on updated profile info
            new_recommendations = recommend_learning_materials(currentCM, subOfInt)

            # Remove previous initial recommendations (if any)
            cursor.execute('DELETE FROM recommendations WHERE userid = %s AND is_initial = 1', (userid,))

            # Insert new initial recommendations
            for recommendation in new_recommendations:
                cursor.execute(
                    '''
                    INSERT INTO recommendations (noteid, userid, resourceName, resourceURL, description, subjectArea, bookAuthor, is_initial, createdAt)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, NOW())
                    ''',
                    (None, userid, recommendation['title'], recommendation['url'], recommendation['description'], recommendation['subject'], recommendation['author'], 1)
                )

            # Commit changes to the database
            mysql.connection.commit()
            return redirect(url_for('profile_settings'))
        except Exception as e:
            mysql.connection.rollback()
            return f"An error occurred: {e}"
    else:
        return redirect(url_for('login'))

    
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/precision_evaluation', methods=['GET'])
def precision_evaluation():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        cursor.execute('SELECT isRelevant FROM feedbackRelevance')
        feedback = cursor.fetchall()

        if not feedback:
            print(jsonify({"error": "No feedback available to calculate precision."}))
            return jsonify({"error": "No feedback available to calculate precision."})
        
        isRelevant = [relevance['isRelevant'] for relevance in feedback]

        totalItemsRecommend = len(isRelevant)
        relevantRecommend = sum(isRelevant)
        precision = relevantRecommend / totalItemsRecommend if totalItemsRecommend > 0 else 0

        print(jsonify({
                "precision": precision,
                "relevant_items": relevantRecommend,
                "total_items_recommended": totalItemsRecommend
            }))

        return jsonify({
                "precision": precision,
                "relevant_items": relevantRecommend,
                "total_items_recommended": totalItemsRecommend
            })
    else:
        return jsonify({"error": "Can not calculate precision of recommendation system"})
if __name__ == "__main__":
    app.run()
