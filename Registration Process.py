# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from flask_bcrypt import Bcrypt
from recommendation_system import recommend_learning_materials
from sklearn.metrics import precision_score, recall_score, f1_score  # (Optional metrics, not used directly here)

# Initialize Flask app and bcrypt for password hashing
app = Flask(__name__)
bcrypt = Bcrypt(app)

# Configure app secret key and MySQL credentials
app.secret_key = 'xyz123'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'username'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'recommendationnotetaking'

# Initialize MySQL connection
mysql = MySQL(app)

# LOGIN ROUTE
@app.route('/')
@app.route('/login', methods=['POST', 'GET'])
def login():
    message = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Retrieve form values
        username = request.form['username']
        password = request.form['password']

        # Check credentials in the database
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        users = cursor.fetchone()

        # Verify hashed password
        if users and bcrypt.check_password_hash(users['password'], password):
            session['loggedin'] = True
            session['userid'] = users['userid']
            session['username'] = users['username']
            return redirect(url_for('notes'))
        else:
            message = 'Incorrect username / password!'
    return render_template('LoginSignup.html', msg=message)

# NOTE CREATION PAGE
@app.route('/create_note')
def create_note():
    # Ensure user is logged in before creating notes
    if 'loggedin' in session:
        return render_template('CreatingNote.html')
    return redirect(url_for('login'))

# REGISTER NEW USER
@app.route('/register', methods=['POST', 'GET'])
def register():
    message = ''
    if request.method == 'POST':
        # Retrieve user input
        username = request.form.get('username')
        name = request.form.get('name')
        password = request.form.get('password')
        email = request.form.get('email')
        kindOfSchool = request.form.get('kindOfSchool')
        currentCM = request.form.get('currentCM')
        subOfInt = request.form.get('subOfInt')

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        # Check if username or email already exists
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        if cursor.fetchone():
            return render_template('LoginSignup.html', msg='Username already exists!')
        cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
        if cursor.fetchone():
            return render_template('LoginSignup.html', msg='Email address already exists!')

        # Validate form fields
        if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            return render_template('LoginSignup.html', msg='Invalid email address!')
        elif not username or not password or not email:
            return render_template('LoginSignup.html', msg='Please fill out the form!')

        # Hash password
        hashedPassword = bcrypt.generate_password_hash(password).decode('utf-8')

        try:
            # Save new user to database
            cursor.execute(
                '''INSERT INTO users (username, name, password, email, kindOfSchool, currentCM, subOfInt) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)''', 
                (username, name, hashedPassword, email, kindOfSchool, currentCM, subOfInt)
            )
            mysql.connection.commit()

            # Generate initial recommendations
            cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
            new_user = cursor.fetchone()
            userid = new_user['userid']
            recommendations = recommend_learning_materials(currentCM, subOfInt)

            # Insert recommendations into database
            for rec in recommendations:
                cursor.execute(
                    '''INSERT INTO recommendations 
                    (noteid, userid, resourceName, resourceURL, description, subjectArea, bookAuthor, is_initial, createdAt)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, NOW())''',
                    (None, userid, rec['title'], rec['url'], rec['description'], rec['subject'], rec['author'], 1)
                )
            mysql.connection.commit()
        except Exception as e:
            mysql.connection.rollback()
            message = f"An error occurred: {e}"
    return render_template('LoginSignup.html', msg=message)

# SAVE OR UPDATE A NOTE
@app.route('/save_note', methods=['POST'])
def save_note():
    if 'loggedin' in session:
        userid = session['userid']
        noteid = request.form.get('noteid')
        title = request.form.get('titleNote')
        content = request.form.get('content')

        if not title or not content:
            return 'Title and content are required fields!'
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            if noteid:
                # Update existing note
                cursor.execute(
                    'UPDATE notes SET title = %s, content = %s WHERE noteid = %s AND userid = %s',
                    (title, content, noteid, userid)
                )
            else:
                # Save new note
                cursor.execute(
                    'INSERT INTO notes (userid, title, content) VALUES (%s, %s, %s)',
                    (userid, title, content)
                )
            mysql.connection.commit()

            # Fetch updated or newly saved note
            if noteid:
                cursor.execute('SELECT * FROM notes WHERE noteid = %s AND userid = %s', (noteid, userid))
            else:
                cursor.execute('SELECT * FROM notes WHERE noteid = LAST_INSERT_ID() AND userid = %s', (userid,))
            savedNote = cursor.fetchone()

            return render_template('CreatingNote.html', note=savedNote, message="Note saved successfully!")
        except Exception as e:
            mysql.connection.rollback()
            return render_template('CreatingNote.html', message=f"An error occurred: {e}")
    return redirect(url_for('login'))

# DISPLAY ALL NOTES AND RECOMMENDATIONS
@app.route('/notes')
def notes():
    if 'loggedin' in session:
        userid = session['userid']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            # User's notes
            cursor.execute('SELECT * FROM notes WHERE userid = %s AND is_archived = 0 ORDER BY createdAt DESC', (userid,))
            userNotes = cursor.fetchall()

            # Initial recommendations
            cursor.execute('SELECT * FROM recommendations WHERE userid = %s AND is_initial = 1 ORDER BY createdAt DESC LIMIT 3', (userid,))
            initialRecommendations = cursor.fetchall()

            # History of recommended materials with feedback
            cursor.execute('''
                SELECT r.*, f.isRelevant 
                FROM recommendations r
                LEFT JOIN feedbackRelevance f 
                ON r.userid = f.userid AND r.noteid = f.noteid AND r.resourceName = f.materialTitle
                WHERE r.userid = %s AND r.is_initial = 0
                ORDER BY r.createdAt DESC
            ''', (userid,))
            recommendedHistory = cursor.fetchall()

            return render_template('notes.html', username=session['username'], notes=userNotes,
                                   initialRecommendations=initialRecommendations, recommendedHistory=recommendedHistory)
        except Exception as e:
            mysql.connection.rollback()
            return render_template('notes.html', username=session['username'], error=f"An error occurred: {e}")
    return redirect(url_for('login'))

# SUBMIT FEEDBACK ON RECOMMENDATION RELEVANCE
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
            # Avoid duplicate feedback
            cursor.execute('''
                SELECT * FROM feedbackRelevance 
                WHERE userid = %s AND noteid = %s AND materialTitle = %s
            ''', (userid, noteid, title))
            if cursor.fetchone():
                return jsonify({'message': 'Duplicate feedback detected.'})

            # Save feedback
            cursor.execute('''
                INSERT INTO feedbackRelevance (userid, noteid, materialTitle, isRelevant) 
                VALUES (%s, %s, %s, %s)
            ''', (userid, noteid, title, isRelevant))
            mysql.connection.commit()
            return jsonify({'message': 'Feedback submitted successfully!'})
        except Exception as e:
            mysql.connection.rollback()
            return jsonify({'message': f'Error: {e}'})
    return jsonify({'message': 'User not logged in.'})

# DELETE NON-INITIAL RECOMMENDATIONS
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
            print(f"An error occurred: {e}")
        return redirect(url_for('notes'))
    return redirect(url_for('login'))

# GENERATE NEW RECOMMENDATIONS FROM NOTE
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
            for rec in recommendations:
                cursor.execute(
                    'SELECT * FROM recommendations WHERE userid = %s AND noteid = %s AND resourceName = %s',
                    (userid, noteid, rec['title'])
                )
                if not cursor.fetchone():
                    cursor.execute(
                        '''INSERT INTO recommendations 
                        (noteid, userid, resourceName, resourceURL, description, subjectArea, bookAuthor, createdAt)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, NOW())''',
                        (noteid, userid, rec['title'], rec['url'], rec['description'], rec['subject'], rec['author'])
                    )
                    mysql.connection.commit()
        except Exception as e:
            mysql.connection.rollback()
            return render_template('CreatingNote.html', message=f"Error saving recommendations: {e}")

        note = {'title': title, 'content': content, 'noteid': noteid}
        return render_template('CreatingNote.html', username=session['username'], recommendations=recommendations, note=note)
    return redirect(url_for('login'))

# VIEW A NOTE
@app.route('/view_note/<int:noteid>')
def view_note(noteid):
    if 'loggedin' in session:
        userid = session['userid']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute('SELECT * FROM notes WHERE userid = %s and noteid = %s', (userid, noteid,))
            note = cursor.fetchone()
            if note:
                return render_template('CreatingNote.html', username=session['username'], note=note)
        except Exception as e:
            return render_template('notes.html', username=session['username'], error=f"An error occurred: {e}")
    return redirect(url_for('login'))

# DELETE A RECOMMENDATION
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

# DELETE A NOTE AND ITS ASSOCIATED DATA
@app.route('/delete_note/<int:noteid>', methods=['GET'])
def delete_note(noteid):
    if 'loggedin' in session:
        userid = session['userid']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            # Delete related records
            cursor.execute('DELETE FROM recommendations WHERE noteid = %s AND userid = %s', (noteid, userid,))
            cursor.execute('DELETE FROM feedbackRelevance WHERE noteid = %s AND userid = %s', (noteid, userid,))
            cursor.execute('DELETE FROM notes WHERE noteid = %s AND userid = %s', (noteid, userid,))
            cursor.connection.commit()
            return redirect(url_for('notes'))
        except Exception as e:
            mysql.connection.rollback()
            return f"An error occurred: {e}"
    return redirect(url_for('login'))

# VIEW AND EDIT PROFILE
@app.route('/profile_settings')
def profile_settings():
    if 'loggedin' in session:
        userid = session['userid']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE userid = %s', (userid,))
        allUserInfo = cursor.fetchone()
        return render_template('profileSettings.html', username=session['username'], userInfo=allUserInfo)
    return redirect(url_for('login'))

# UPDATE PROFILE INFO AND REFRESH INITIAL RECOMMENDATIONS
@app.route('/update_info', methods=['POST'])
def update_info():
    if 'loggedin' in session:
        userid = session['userid']
        # Get form values
        username = request.form.get('username')
        name = request.form.get('name')
        password = request.form.get('password')
        email = request.form.get('email')
        kindOfSchool = request.form.get('schoolType')
        currentCM = request.form.get('currentCourses')
        subOfInt = request.form.get('subjectInterest')

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        try:
            # Get existing data
            cursor.execute('SELECT * FROM users WHERE userid = %s', (userid,))
            current_user = cursor.fetchone()

            # Use new values if provided, otherwise retain old
            username = username or current_user['username']
            name = name or current_user['name']
            hashedPassword = bcrypt.generate_password_hash(password).decode('utf-8') if password else current_user['password']
            email = email or current_user['email']
            kindOfSchool = kindOfSchool or current_user['kindOfSchool']
            currentCM = currentCM or current_user['currentCM']
            subOfInt = subOfInt or current_user['subOfInt']

            # Update user
            cursor.execute('''
                UPDATE users 
                SET username = %s, name = %s, password = %s, email = %s, 
                    kindOfSchool = %s, currentCM = %s, subOfInt = %s 
                WHERE userid = %s
            ''', (username, name, hashedPassword, email, kindOfSchool, currentCM, subOfInt, userid))

            # Refresh initial recommendations
            cursor.execute('DELETE FROM recommendations WHERE userid = %s AND is_initial = 1', (userid,))
            new_recommendations = recommend_learning_materials(currentCM, subOfInt)
            for rec in new_recommendations:
                cursor.execute(
                    '''INSERT INTO recommendations 
                    (noteid, userid, resourceName, resourceURL, description, subjectArea, bookAuthor, is_initial, createdAt)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, NOW())''',
                    (None, userid, rec['title'], rec['url'], rec['description'], rec['subject'], rec['author'], 1)
                )
            mysql.connection.commit()
            return redirect(url_for('profile_settings'))
        except Exception as e:
            mysql.connection.rollback()
            return f"An error occurred: {e}"
    return redirect(url_for('login'))

# LOGOUT
@app.route('/logout')
def logout():
    # Clear session data
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('username', None)
    return redirect(url_for('login'))


# Define new route that only accepts GET requests
@app.route('/precision_evaluation', methods=['GET'])
def precision_evaluation():
    # Establish a connection to the MySQL database
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    # Fetch all relevance feedback data from ‘feedbackRelevance’ table
    cursor.execute('SELECT isRelevant FROM feedbackRelevance')
    feedback = cursor.fetchall()

    # If no feedback data is available, return an error message
    if not feedback:
        return jsonify({"error": "No feedback available to calculate precision."})
        
    # Extract the ‘isRelevant’ values from the fetched feedback
    isRelevant = [relevance['isRelevant'] for relevance in feedback]

    totalItemsRecommend = len(isRelevant)  # Total number of feedback entries
    relevantRecommend = sum(isRelevant)    # Number of items marked as relevant

    # Calculate precision: (relevant recommendations) / (total recommendations)
    precision = relevantRecommend / totalItemsRecommend if totalItemsRecommend > 0 else 0

    # Return calculation results as a JSON response
    return jsonify({
        "precision": precision,
        "relevant_items": relevantRecommend,
        "total_items_recommended": totalItemsRecommend
    })


if __name__ == "__main__":
    app.run()
