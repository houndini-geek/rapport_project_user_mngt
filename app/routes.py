from flask import render_template, request

from app.db_management.db_mngt import DbManagement


db_mngt = DbManagement()

def register_routes(app):

    @app.route('/')
    def home():
        return render_template('index.html')


    @app.route('/new_user',methods=['GET','POST'])
    def new_user():
        user_info = {}

    # is_active 
    
        if request.method == 'POST':
            logon_name =  request.form.get('logon_name', '')
            display_name = request.form.get('display_name','')
            user_role = request.form.get('user_role','user')
            department = request.form.get('department','')
            site_name = request.form.get('site_name','')
            initial_password =  request.form.get('password','')
            is_active = request.form.get('is_active')
            user_info['logon_name'] = logon_name
            user_info['display_name'] = display_name
            user_info['user_role'] = user_role
            user_info['department'] = department
            user_info['site_name'] = site_name
            user_info['site_name'] = site_name
            user_info['initial_password'] = initial_password
            if is_active:
                user_info['is_active'] = True
            else:
                user_info['is_active'] = False
           
            db_mngt.save_user(user_info=user_info)
        return render_template('user_create.html')


    @app.route('/user/<user_id>')
    def get_user(user_id):
        return render_template('user_details.html')