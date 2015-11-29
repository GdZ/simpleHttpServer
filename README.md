### Simple multi-threaded file-based HTTP server

##### Functionality:
* multi-threaded using thread pool
* support for GET requests only
* support for static content only
* support for mime types
* support for 200, 206 and 404 HTTP response status codes
* support for single range HTTP GET requests (RFC 2616)

##### Install:

1. clone repository from github
	```
	$ git clone https://github.com/gdz/simpleHttpServer.git simpleHttpServer
	```

2. create virtual enviroment
	```
	$ virtualenv rt
	```
	```
	$ source rt/bin/activate
	```

3. install requirements for server
	```
	$ pip install -r requirements.txt
	```

#### Run:

1. run server

	```
	$ rt/bin/python run.py
	```

2. open latest Chrome browser
    * open url: http://localhost:5555/home


#### Possibilities:
* Command line parameters for run.py
* Add dynamic url routes and views
* Templating
* And so much more ...



---

TIPS:

- this is fork from
```
https://github.com/ercchy/simpleHttpServer.git
```
