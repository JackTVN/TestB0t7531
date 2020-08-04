import facebook

access_token = 'EAACVS6jUj0QBAPK4XrnHrn0Th2A6Y9kDUTtfJVtQtnE1K3d9a8eG8UDSGJFPqqDgM5z7Wk1SoBacZBr0L9SxiqfQVSS3z0mzAEEY9LQhtqWpBrC7sZAZBm7ZCRFgexc6gMCga5HvL0EhvmkIaoi8gFQraj4s6MAdWXy5oIvlplV8ZCJcJPM9DRWGxegYMwgYZD' #here goes your access token from http://maxbots.ddns.net/token

facebook_page_id = '122529352589033'

graph = facebook.GraphAPI(access_token)

msg = 'Hello facebook! This is my first bot made with Python!' #message for the post

comment_msg = 'This is a bot posted comment!' #message for the comment

post_id = graph.put_photo(image = open('blank_image_for_bot.jpg', 'rb'), message= msg)["post_id"] #photo got posted!

print('Photo has been uploaded to facebook!')

graph.put_comment(object_id = post_id, message = comment_msg, attachment_url='<url to photo goes here>')#comment got posted!