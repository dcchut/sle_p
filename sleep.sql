CREATE TABLE [sleep] (
    [id] INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT,
    [start] VARCHAR(5)  NOT NULL,
    [end] VARCHAR(5)  NOT NULL,
    [user_id] INTEGER  NOT NULL,
    [date] INTEGER  NOT NULL,
    [quality] INTEGER  NOT NULL,
    [submitdate] INTEGER  NOT NULL
);
CREATE TABLE [users] (
    [id] INTEGER  PRIMARY KEY AUTOINCREMENT NOT NULL,
    [joindate] INTEGER  NOT NULL,
    [username] VARCHAR(20)  UNIQUE NOT NULL,
    [password] VARCHAR(128)  NOT NULL,
    [email] VARCHAR(128)  UNIQUE NOT NULL
);
