Test with Tokens!
===================

Login to Get Token
-------------
>**URL** : http://test.rsdn.ir/login/
>**Method** : **POST**

Request Body:
```
{
  "username": "itmard",
  "password": "123123"
}
```
Response Sample:
```
eyJhbGciOiJIUzI1NiIsImV4cCI6MTQyNTk4MDA1OSwiaWF0IjoxNDI1ODkzNjU5fQ.eyJ1c2VyIjoicmV6YSJ9._x8brU_SfJk6zHeyM73ZqvgceHCwDeLH-sigL7b8WVQ
```
>Note:
> if authorization fails response status code will be **401**.


----------

Test Token
-------------
>**URL** : http://test.rsdn.ir/test/
>**Method** : **GET**

Request **Header**:
```
TOKEN:eyJhbGciOiJIUzI1NiIsImV4cCI6MTQyNTk4MDA1OSwiaWF0IjoxNDI1ODkzNjU5fQ.eyJ1c2VyIjoicmV6YSJ9._x8brU_SfJk6zHeyM73ZqvgceHCwDeLH-sigL7b8WVQ
```
Response Sample:
Status code: 200 and a message contains current user's username
```
itmard
```
>Note:
> if authorization fails response status code will be **401**.
>

----------