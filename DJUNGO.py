manage.py
 -runserver: as the name suggests, this command runs the server for a web application.

 -migtation: this command can create a database and "migrate" or make changes to a

 -makemigration: your database will not reflect any migrations until you enact then with makemigration.


my_project: housed the configuration files for your project settings. these include:

 -_init_.py: this file is (and should remain!) empty. Its puropuse is to inform the python interpreter that
 the directory is a package. This standard among python packages.

 -settings.py: this file contains installed applications and all information pertaining to miffleware or
 software that facilates communication between the operating system and its applications. It also houses
 if templates and databases:

 -urls.py: here you can expect to find all urls relating to your project. These include urls for images,
 pages and applications. this file will process any relevant urls for images, pages and applications. this
 file will process any relevant urls and is generally used to connect the project with related web-apps.

 -wsgi.py: the web server geteway interface(wsgi) specification outlines the standard interface that connect
 web servers with python frameworks and applications. this file allows you to deploy youu applications on
 a server. you will not need to make any changes to this file.

 -asgi.py: Newer versions of django also feature this file. ASGI, like WSGI, is a specification that defines
 interactions between python-written applications and servers. ASGI can be considered the WSGI successor,
 as it provides more flexibility and freedon than the alternative. That said, both are still very much in use.



How To Set Up Your Development Environment:




What Other Skills/Languages should I Learn?
 You wn't be able to buuild a career in coding with Dhango alone I you intern t to become a full stack coder
 or any other programming-adjacent professional you should pick up a few core web development skills. These
 include (but are not limited to):

 SQL: Using django often means working with databases, so learning SQL (a popular query language used for
 accessing, managing and manipulating database information) would be halpful.

 javasci

























