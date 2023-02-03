package config

import "database/sql"

var userDB = "root"
var ip = "10.0.0.4"
var port = "3306"

type Event struct {
	Id          string `json:"id"`
	Title       string
	Description string
	Date        string
	User        User
	Note        string
	NbVote      string
}

type Comment struct {
	Id           string `json:"id"`
	Content      string
	CreationDate string
	User         User
	Event        Event
}

type User struct {
	Id       string
	Email    string
	Username string
	Moyenne  string
	Role     Role
	Events   []Event
}

type Participants struct {
	Event    Event
	User     User
	Accepted bool
}

type Role struct {
	Name string
}

type db struct {
	Database *sql.DB
}

func GetDB() db {
	var databases db

	databases.Database, _ = sql.Open("mysql", (userDB + "@tcp(" + ip + ":" + port + ")/challenge48h"))

	return databases
}
