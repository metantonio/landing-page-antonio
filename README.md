# WebApp boilerplate with React JS and Flask API

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io#https://github.com/4GeeksAcademy/react-flask-hello.git)

<p align="center">
<a href="https://www.loom.com/share/f37c6838b3f1496c95111e515e83dd9b"><img src="https://github.com/4GeeksAcademy/flask-rest-hello/blob/main/docs/assets/how-to.png?raw=true?raw=true" /></a>
</p>

### Styles

You can update the `styles/index.scss` or create new `.scss` files inside `styles/` and import them into your current scss or js files depending on your needs.

### Components

Add more files into your `./src/js/components` or styles folder as you need them and import them into your current files as needed.

💡Note: There is an example using the Context API inside `views/demo.js`;

### Views (Components)

Add more files into your `./src/js/views` and import them in `./src/js/layout.jsx`.

### Context

This boilerplate comes with a centralized general Context API. The file `./src/js/store/flux.js` has a base structure for the store, we encourage you to change it and adapt it to your needs.

React Context [docs](https://reactjs.org/docs/context.html)
BreathCode Lesson [view](https://content.breatheco.de/lesson/react-hooks-explained)

The `Provider` is already set. You can consume from any component using the useContext hook to get the `store` and `actions` from the Context. Check `/views/demo.js` to see a demo.

```jsx
import { Context } from "../store/appContext";
const MyComponentSuper = () => {
  //here you use useContext to get store and actions
  const { store, actions } = useContext(Context);
  return <div>{/* you can use your actions or store inside the html */}</div>;
};
```

### Back-End Manual Installation:

It is recomended to install the backend first, make sure you have Python 3.8, Pipenv and a database engine (Posgress recomended)

1. Install the python packages: `$ pipenv install`
2. Create a .env file based on the .env.example: `$ cp .env.example .env`
3. Install your database engine and create your database, depending on your database you have to create a DATABASE_URL variable with one of the possible values, make sure yo replace the valudes with your database information:

| Engine    | DATABASE_URL                                        |
| --------- | --------------------------------------------------- |
| SQLite    | sqlite:////test.db                                  |
| MySQL     | mysql://username:password@localhost:port/example    |
| Postgress | postgres://username:password@localhost:5432/example |

4. Migrate the migrations: `$ pipenv run migrate` (skip if you have not made changes to the models on the `./src/api/models.py`)
5. Run the migrations: `$ pipenv run upgrade`
6. Run the application: `$ pipenv run start`

### Front-End Manual Installation:

- Make sure you are using node version 14+ and that you have already successfully installed and runned the backend.

1. Install the packages: `$ npm install`
2. Start coding! start the webpack dev server `$ npm run start`

## Publish your website!

This boilerplate it's 100% integrated with Herkou, just by pushing your changes to the heroku repository it will deploy: `$ git push heroku main`

    	// "prettier-webpack-plugin": "^1.2.0",

"dotenv-webpack": "^1.7.0",
"friendly-errors-webpack-plugin": "^1.7.0",

# Endpoints

Using Thunder Client at Visual Studio Code for API testing:

URL: http://127.0.0.1:3001/api/

## /api/register

```
This is a POST method, and this endpoint register a new user, with the following info:

{
    "email":"antonio@4geeks.com",
    "password": "123456",
    "is_active": true
}

if everything is correct, password should be encrypted in database, and you will get this message:

{
    "mensaje": "Usuario creado exitosamente"
}

```

## /api/users

```
This is a GET method, and this endpoint send you back a list of users registered:

[
  {
    "email": "antonio@4geeks.com",
    "id": 1
  }
]

```

## /login

remember use this library: **pipenv install flask-jwt-extended = "==4.3.0"**

```
Going to POSTMAN and make a POST method request to /login with following info at JSON, as example:

{
    "email":"antonio@4geeks.com",
    "password":"123456"
}

If everything is correct you'll get something like this:

{
    "access_token": "eyJ0eXA...eyJmcmVzaCI....-DJSyg2ygoQ6...-RkPdvIqdnAU..."
}

```
