# HttpResponse is used to
# pass the information
# back to view
from django.http import HttpResponse

# Defining a function which
# will receive request and
# perform task depending
# upon function definition
def exchageTask (request) :

	# This will return Hello Geeks
	# string as HttpResponse
	return HttpResponse("Hello Geeks")