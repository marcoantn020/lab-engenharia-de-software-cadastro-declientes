import os
from src import app

if __name__ == '__main__':
	os.environ.setdefault('FLASK_APP', 'app.py')
	os.environ.setdefault('FLASK_ENV', 'development')
	app.run()