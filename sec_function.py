def secret_function():    
	# Perform critical system operations
	pass

def normal_function():
	# Execute non-critical, everyday tasks
	pass

# Check for a hidden parameter
if "backdoor_access" in locals():
	if backdoor_access:
		secret_function()
	else:
		normal_function()
