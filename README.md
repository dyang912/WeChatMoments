WeChatMoments
-------------
WeChat Moments is a platform where users can update their real-time information and share their rich lives. 
This project uses Python and MySQL to reproduce the WeChat Moments scenes includes functions of user registration and login, information post, 
and liking or commenting on other people’s shares.

Recommend Version
-----------------
`Python 3.7`
`MySQL 8.0`

Prerequisite
------------
Install required library:
```
pip install wxpython mysql-connector-python
```

Run
---
```
python main.py -u <database user> -p <database password>
```

Common Problems
--------
* If you meet:

    > Authentication plugin 'caching_sha2_password' cannot be loaded ...
    
    Try to run this in MySQL:
    ```SQL 
    ALTER USER 'username' IDENTIFIED WITH mysql_native_password BY 'password';
    ```