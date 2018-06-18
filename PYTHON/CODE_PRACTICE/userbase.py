# An Python3 excersize that helps verify users
# this is quite a useful processing code structure


# some users
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print("Verifying user: " + current_user.title())	
	confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for comfirmed_user in confirmed_users:
	print(comfirmed_user.title())
