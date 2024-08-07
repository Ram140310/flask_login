from app import *
super_admin = Users(
    id=100,
    username='superadmin',
    email='superadmin@example.com',
    password=generate_password_hash('pqssword')
)
db.session.add(super_admin)
db.session.commit()
print("user initiated")