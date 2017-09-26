# R-3
R cubed is a social media platform that has a stong emphasis on helping people in need. 

First in order to run the webapp install python and pip (most if not all * Nix systems have it installed)

Install django:
'pip install django'

You also need to download the python module for requests
'pip install requests'

Then clone the repo and run 
'python manage.py runserver'

*please note that most unix systems need sudo to make the pip commands work. If thats the case just add 'sudo' to the beginning of the command*

django will start a webserver on 127.0.0.1:8000

open a webrowser there

If you want to change the phone number that your emergency button sends then locate status/views.py. The number is in the payload variable inside of the emergency function. it should look like 

name=\"To\"\r\n\r\n13137278191\r\n-

only change the number and remember that if you are in the us to add a 1 to the beginning of the number
