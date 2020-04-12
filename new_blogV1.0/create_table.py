import mysql.connector

conn = mysql.connector.connect(user='***', password='****')
cursor = conn.cursor()
cursor.execute('create database if not exists `blog`;')
cursor.execute('use blog;')
cursor.execute('''create table if not exists `cppcode`(
    `id` int unsigned auto_increment, 
    `news_title` varchar(30), 
    `au01` varchar(20), 
    `au02` date, 
    `tag` varchar(20), 
    `news_about` tinytext, 
    `news_infos` text, 
    primary key(`id`)
    )charset=utf8;
''')
conn.commit()

cursor.execute('''create table if not exists `projectcode`(
    `id` int unsigned auto_increment, 
    `news_title` varchar(30), 
    `au01` varchar(20), 
    `au02` date, 
    `tag` varchar(20), 
    `news_about` tinytext, 
    `news_infos` text, 
    primary key(`id`)
    )charset=utf8;
''')
conn.commit()

cursor.execute('''create table if not exists `pythoncode`(
    `id` int unsigned auto_increment, 
    `news_title` varchar(30), 
    `au01` varchar(20), 
    `au02` date, 
    `tag` varchar(20), 
    `news_about` tinytext, 
    `news_infos` text, 
    primary key(`id`)
    )charset=utf8;
''')
conn.commit()

cursor.execute('''create table if not exists `patcode`(
    `id` int unsigned auto_increment, 
    `news_title` varchar(30), 
    `au01` varchar(20), 
    `au02` date, 
    `tag` varchar(20), 
    `news_about` tinytext, 
    `news_infos` text, 
    primary key(`id`)
    )charset=utf8;
''')
conn.commit()

cursor.execute('''create table if not exists `special`(
    `id` int unsigned auto_increment, 
    `blog_title` varchar(30),
    `info` varchar(120), 
    `au01` varchar(20), 
    `au02` date, 
    `website` varchar(200),
    primary key(`id`)
    )charset=utf8;
''')
conn.commit()

cursor.close()
conn.close()