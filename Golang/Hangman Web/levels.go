package main

import (
	"fmt"
	"math/rand"
	"net/http"
	"os"
	"strconv"
	"text/template"
	"time"
)

type Input_ struct {
	PartyType        string
	Answer           string
	Mot_a_trouver    string
	PositionPendu    int
	Lettres_trouvées string
	Lettres_essayées string
	Mot_a_trou       string
	Terminé          bool
	Gagné            bool
	Level            string
}

//C'est ici qu'on construit la (ou les) partie(s)
func main() {
	mot_au_hasard := Selection_Mot("words.txt")
	lettres_validées := []byte{mot_au_hasard[len(mot_au_hasard)/2-1]}
	var lettres_essayées []byte
	position_pendu := 0

	tmpl := template.Must(template.ParseFiles("index.html"))

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		if position_pendu == 10 || Toutes_Les_Lettres_Sont_Dans_Le_Mot(lettres_validées, mot_au_hasard) {
			http.Redirect(w, r, "/restart", http.StatusSeeOther)
			return
		}
		if r.Method != http.MethodPost {
			tmpl.ExecuteTemplate(w, "index.html", Input_{PartyType: "levels", Mot_a_trouver: mot_au_hasard, PositionPendu: position_pendu, Lettres_trouvées: string(lettres_validées), Lettres_essayées: string(lettres_essayées), Mot_a_trou: Affiche_Mot_Pendu(mot_au_hasard, lettres_validées), Terminé: false, Gagné: false})
			return
		}
	})
	http.HandleFunc("/hangman", func(w http.ResponseWriter, r *http.Request) {
		if position_pendu == 10 || Toutes_Les_Lettres_Sont_Dans_Le_Mot(lettres_validées, mot_au_hasard) {
			http.Redirect(w, r, "/restart", http.StatusSeeOther)
			return
		}
		if r.Method != http.MethodPost {
			http.Redirect(w, r, "/", http.StatusSeeOther)
			return
		}
		level := r.FormValue("level")
		proposition := r.FormValue("answer")
		if len(proposition) == 1 {
			if Est_Ce_Dans_Le_Mot(proposition, mot_au_hasard) || Est_Ce_Dans_Le_Mot(string(proposition[0]-'A'+'a'), mot_au_hasard) {
				if Est_Ce_Dans_Le_Mot(proposition, mot_au_hasard) {
					lettres_validées = append(lettres_validées, proposition[0])
				}
				if Est_Ce_Dans_Le_Mot(string(proposition[0]-'A'+'a'), mot_au_hasard) {
					lettres_validées = append(lettres_validées, proposition[0]-'A'+'a')
				}
			} else if !(Est_Ce_Dans_Le_Mot(proposition, string(lettres_essayées))) && !(Est_Ce_Dans_Le_Mot(string(proposition[0]-'A'+'a'), string(lettres_essayées))) {
				lettres_essayées = append(lettres_essayées, proposition[0])
				position_pendu++
			}
		}
		if !Toutes_Les_Lettres_Sont_Dans_Le_Mot(lettres_validées, mot_au_hasard) {
			if position_pendu < 10 {
				tmpl.ExecuteTemplate(w, "index.html", Input_{Level: level, PartyType: "levels", Answer: proposition, Mot_a_trouver: r.FormValue("mat"), PositionPendu: position_pendu, Lettres_trouvées: string(lettres_validées), Lettres_essayées: string(lettres_essayées), Mot_a_trou: Affiche_Mot_Pendu(mot_au_hasard, lettres_validées), Terminé: false, Gagné: false})
			}
			if position_pendu == 10 {
				tmpl.ExecuteTemplate(w, "index.html", Input_{Level: level, PartyType: "levels", Answer: proposition, Mot_a_trouver: r.FormValue("mat"), PositionPendu: position_pendu, Lettres_trouvées: string(lettres_validées), Lettres_essayées: string(lettres_essayées), Mot_a_trou: Affiche_Mot_Pendu(mot_au_hasard, lettres_validées), Terminé: true, Gagné: false})
			}
		} else {
			tmpl.ExecuteTemplate(w, "index.html", Input_{Level: level, PartyType: "levels", Answer: proposition, Mot_a_trouver: r.FormValue("mat"), PositionPendu: position_pendu, Lettres_trouvées: string(lettres_validées), Lettres_essayées: string(lettres_essayées), Mot_a_trou: Affiche_Mot_Pendu(mot_au_hasard, lettres_validées), Terminé: true, Gagné: true})
		}
	})
	http.HandleFunc("/restart", func(w http.ResponseWriter, r *http.Request) {
		level := r.FormValue("level")
		if level == "" {
			level = "words"
		}
		mot_au_hasard = Selection_Mot(level + ".txt")
		lettres_validées = []byte{mot_au_hasard[len(mot_au_hasard)/2-1]}
		lettres_essayées = []byte{}
		position_pendu = 0
		tmpl.Execute(w, Input_{Level: level, PartyType: "levels", Mot_a_trouver: mot_au_hasard, Mot_a_trou: Affiche_Mot_Pendu(mot_au_hasard, lettres_validées), Lettres_trouvées: string(lettres_validées), Lettres_essayées: string(lettres_essayées), PositionPendu: position_pendu, Terminé: false, Gagné: false})
	})

	http.ListenAndServe(":8080", nil)
}

func Selection_Mot(file string) string {
	//- 1.1 : Mise en place de l'aléatoire
	r1 := rand.New(rand.NewSource(time.Now().UnixNano()))
	//- 1.2 : Fetch du fichier words
	f, _ := os.Open(file)
	b1 := make([]byte, 9999)
	n1, _ := f.Read(b1)

	var words [][]byte
	index := 0
	for indice, lettre := range string(b1[:n1]) {
		if lettre == 10 {
			words = append(words, b1[index:indice])
			index = indice + 1
		}
	}
	//- 1.3 : Selection aléatoire
	mot_au_hasard := string(words[r1.Intn(len(words))])
	defer f.Close()
	return mot_au_hasard
}

func Affiche_Mot_Pendu(str string, valid []byte) string {
	ret := ""
	for i, char := range str {
		if i != 0 {
			ret += " "
		}
		ecrit := 0
		for _, in_lv := range valid {
			if byte(char) == in_lv && ecrit == 0 {
				ecrit = 1
				ret += string(char - 'a' + 'A')
			}
		}
		if ecrit == 0 {
			ret += "_"
		}
	}
	return ret
}

func Est_Ce_Dans_Le_Mot(lettre string, mot string) bool {
	for _, char := range mot {
		if string(char) == lettre {
			return true
		}
	}
	return false
}

func Toutes_Les_Lettres_Sont_Dans_Le_Mot(lettres []byte, mot string) bool {
	for _, char1 := range mot {
		ecrit := 0
		for _, char2 := range lettres {
			if byte(char1) == byte(char2) {
				ecrit = 1
			}
		}
		if ecrit == 0 {
			return false
		}
	}
	return true
}

func Ending(message string, position_pendu int, mot_au_hasard string, lettres_validées []byte) {
	hangman, _ := os.Open("positions/" + strconv.Itoa(position_pendu) + ".txt")
	hangman_tab := make([]byte, 9999)
	hangman_read, _ := hangman.Read(hangman_tab)
	fmt.Println(string(hangman_tab[:hangman_read]))

	Affiche_Mot_Pendu(mot_au_hasard, lettres_validées)
	fmt.Println("\n\n" + message)
}
