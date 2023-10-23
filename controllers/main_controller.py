from flask import render_template, request, redirect, url_for, flash, Blueprint
from models.data_access import *  

from models.model import Reservation

main_controller = Blueprint('main_controller', __name__)

@main_controller.route('/')
def index():
    return render_template('index.html')

@main_controller.route('/make_reservation', methods=['POST'])
def make_reservation():
    if request.method == 'POST':
        room_type = request.form.get('room_type')
        check_in_date = request.form.get('check_in')
        check_out_date = request.form.get('check_out')
        guest_name = request.form.get('guest_name')
        email = request.form.get('email')

        total_cost = 0
        reservation_status = 'PENDING'

        reservation = Reservation(room_type=room_type, 
                                  check_in_date=check_in_date, 
                                  check_out_date=check_out_date, 
                                  guest_name=guest_name, 
                                  email=email, 
                                  total_cost=total_cost, 
                                  reservation_status=reservation_status)
        
        reservation_id = create_reservation(reservation)

        flash(f'Reservation created successfully! Reservation ID: {reservation_id}', 'success')
        return redirect(url_for('main_controller.index'))

@main_controller.route('/search_reservations', methods=['GET'])
def search_reservations():
    if request.method == 'GET':
        reservation_id = request.args.get('reservation_id')

        reservation_dict = get_reservation_by_id(reservation_id)
        
        if reservation_dict:
            return render_template('reservation_details.html', reservation=reservation_dict)
        else:
            flash(f'Reservation {reservation_id} not found')
            return redirect(url_for('main_controller.index'))