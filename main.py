import bcrypt

# CREATING A PASSWORD AND HASHING IT
# SALT  ADDS A RANDOM GENERATED STRING TO HASHED PASSWORD
password = b'SecretPassword55'
# hashed = bcrypt.hashpw(password, bcrypt.gensalt())
# print(hashed)

# HASHED PASSWORDS FOR PASSWORD ABOVE 
# b'$2b$12$.i508fdOPWPy94pGpI.3/OEaX/S.akn/o7KN8tH7x4mF1BOgZ7Bni'
# b'$2b$12$CZLJC7YUnP0QFWG.HyLu9eIIW.JrgnaLANaa9SVmurkgQxVI5FmsS'

# LOOK UP USERNAME BY EMAIL OR SEARCH IN DB
# username = request.get.form.get('username')
# password = request.get.form.get('password').encode('utf-8')

# CHECKING IF PASSWORD MATCHES WITH ARGUEMENTS INSIDE
# if bcrypt.checkpw(password, hashed):
#     print("It matches!")
    # return redirect(url_for('user_profile'))
# else:
#     print("Didn't match!")
    # flash('invalid credentials', 'warning')

# CHECKING HOW LONG THE ROUNDS OF HASHING ARE 

import time
# add counter to gensalt (rounds='int')

start = time.time()
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
end = time.time()

f = end - start
print(f)
