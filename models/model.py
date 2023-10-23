class Reservation:
    def __init__(self, room_type, check_in_date, check_out_date, guest_name, email, total_cost, reservation_status, id=None):
        self.id = id
        self.room_type = room_type
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.guest_name = guest_name
        self.email = email
        self.total_cost = total_cost
        self.reservation_status = reservation_status
