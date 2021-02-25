        model = UsersModel
        load_instance = True
    
    email = ma.auto_field()
    name = ma.auto_field()
    username = ma.auto_field()
    password = ma.auto_field()
    address = ma.auto_field()
    state = ma.auto_field()
    country = ma.auto_field()
    pan = ma.auto_field()
    contactNo = ma.auto_field()
    dob = ma.auto_field()
    account_type = ma.auto_field()