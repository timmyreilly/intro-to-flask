#Intro to Flask 

### Before we get started buildling with flask we need to setup our development environment. 

1. Install Python
2. Install virtualenv
3. Install virtualenvwrapper or virtualenvwrapper-win
4. Create a virtual environment 
5. Install flask 
6. Checkout the next branch 

## 1. Install Python

[Windows](http://timmyreilly.azurewebsites.net/python-flask-windows-development-environment-setup/)

[Mac](http://docs.python-guide.org/en/latest/starting/install/osx/)

## 2. Install virtualenv

```
$ pip install virtualenv
```

## 3. Install virtualenvwrapper or virtualenvwrapper-win

virtualenv wrappers make it easy to manage multiple environments and can make iterating on project easy. 

[Windows](http://timmyreilly.azurewebsites.net/python-flask-windows-development-environment-setup/)

[Mac](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

## 4. Create a virtual environment

```
$ mkvirtualenv helloworld
```

cd into root of project

```
$ setprojectdir .

$ deactivate

$ workon helloworld
```

## 5. Install flask

Now we need [flask](http://flask.pocoo.org/) for our first website!

```
$ pip install flask
```


## 6. Checkout the next branch
```
$ git checkout hello 
```