#Application Logic (app.py):
#Use Flask to create routes for different parts of your application (main menu, reservation, admin login).
#Implement the logic for each route, such as displaying templates, handling form submissions, and interacting with the database.


from flask import Flask, render_template, request, redirect
from db import create_tables, get_seating_chart, add_reservation

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def main_menu():
    # Create tables if they don't exist
    create_tables()
    # Load seating chart
    seating_chart = get_seating_chart()

    if request.method == 'POST':
        if request.form['action'] == 'reserve':
            return redirect('/reserve')
        elif request.form['action'] == 'admin':
            return redirect('/admin/login')

    return render_template('main_menu.html', seating_chart=seating_chart)

@app.route('/reserve', methods=['GET', 'POST'])
def reserve_seat():
    if request.method == 'POST':
        # Process reservation form submission
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        seat_row = request.form['seat_row']
        seat_column = request.form['seat_column']
        add_reservation(first_name, last_name, seat_row, seat_column, 'e-ticket_number')  # Replace 'e-ticket_number' with actual e-ticket number logic
        return render_template('reservation_confirmation.html', reservation_code='ABC123')
    else:
        return render_template('reservation_form.html')

if __name__ == '__main__':
    app.run(debug=True)
