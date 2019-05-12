-------Introduction---------
A django web framework Quiz game with buzzer and time recorder.
It allows users connected in same wifi network to register(local game registration).
Registration can be done by visiting a link(eg. 192.168.0.101:8000), hosted by django, on browser.
Then users have to login and ready to go.
Admin can create superuser and visit admin side of django to see which competitor clicked the buzzer first.
Admin can filter, search and sort desirably

------Settings to be done-------
create a empty database in mysql named 'quizgame' (can be changed accordingly in settings.py)
run manage.py

-----Note-----
Admin have to change question in question.html after every question they ask.(This allows contestants to buzz multiple number of time)
