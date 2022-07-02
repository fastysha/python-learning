# Watch the video: htts://www.youtube.com/watch?v=94fHz4w65PY
import json

# Read file 'user.json' and set value to 'user' dictionary
with open("tasks_junior_2/user.json","r") as f:
    file_content=f.read()
    print(file_content)
    user_json=json.loads(file_content)
    user =user_json
    print(user)


# Create file named 'test.txt' and add some text (whatever you want)
with open("testtt.txt","w") as f:
    f.write("Woops! I have deleted the content!")
# Append text 'Lorem Ipsum' to the 'test.txt'

# Create your own dictionary, create new file 'dict.json' and write dictionary value to the file

# Delete file named 'detele.txt'