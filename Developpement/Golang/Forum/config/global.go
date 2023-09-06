package config

import (
	"database/sql"

	_ "github.com/go-sql-driver/mysql"
)

var userDB = "root"
var ip = "localhost" // "mysql-container" ou "localhost"
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

// Fermez la connexion à la base de données lorsque vous n'en avez plus besoin
func (d *db) CloseDB() {
	if d.Database != nil {
		d.Database.Close()
	}
}
