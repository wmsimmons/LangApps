from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

# Using the standard RequestFactory API to create a form POST request
#request = factory.post('/notes/', {'title': 'new idea'})

factory = APIRequestFactory()
# user = User.objects.get(username='olivia')
# view = AccountDetail.as_view()

# Make an authenticated request to the view...
request = factory.get('/users')
print(request)
#force_authenticate(request, user=user)
# response = view(request)
# print(response)
