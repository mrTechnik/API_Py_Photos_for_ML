## API Endpoints

Upload photo & metadata
```bash
$  curl -i -X POST -F "file=@/c/test_laught.jpg" -F 'metadata=happy' http://localhost:5000/photo
$  Photo was uploaded
```

Download photo & metadata by <photo_id>
```bash
$ curl -i -X GET http://localhost:5000/photo/<photo_id> > answer.txt
$  answer.txt
```

Delete <photo_id> photo
```bash
$  curl -i -X GET http://localhost:5000/photo/del/1
$  File was deleted
```


## Usage

This project uses the [Flask](http://flask.pocoo.org/) framework.

```
DokuScketch
	├── helpers
	│   └── sqlalchemyclass.py
	├── .gitignore
	├── requirements.txt
	├── README.MD
	├── config.yaml
	├── main.py   
	└── app.py
```

###Run server
The steps bellow will guide you through the project installation.  </br>
The following commands should be executed in your computer console at the project folder:

* Clone the project to your local repository workspace;

* Create a virtual environment for the imported application through the following command:
```
$ virtualenv <Virtual Environment name>
```
* Activate your virtual environment with the command:
```
$ <Virtual Environment name>\Scripts\activate
```
 * With the virtual environment properly activated, install the plugins available at the **requirements.txt** file through the command:
```
$ pip install -r requirements.txt
```
This process should enable your application to be deployed in a local server for test purpose.

----------
Deployment
-------------
```
$ python app.py
`