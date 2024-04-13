import requests

# Replace 'your_access_token' with your actual Facebook access token
access_token = '612cd116f77d5e962f8e77c279d649dd'

# Replace 'your_facebook_user_id' with your actual Facebook user ID
user_id = 'your_facebook_user_id'

# The live match score you want to post
live_match_score = 'Live Match Update: Team A 120/3 vs Team B'

# The URL for the Facebook Graph API endpoint to create a post
post_url = f'https://graph.facebook.com/{user_id}/feed'

# The payload containing the message to post
payload = {
    'message': live_match_score,
    'access_token': access_token
}

# Make the POST request to the Facebook Graph API
response = requests.post(post_url, data=payload)

# Check the response
if response.status_code == 200:
    print('Successfully posted live match score to Facebook!')
else:
    print('Failed to post live match score. Error:', response.text)
