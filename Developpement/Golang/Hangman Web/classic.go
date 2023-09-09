package main

//Le plus dur et le plus neuf sera au niveau du main (on y utilise net/http pour etablir un serveur et text/template pour mettre en place l'interface graphique)
//Le fichier html qui accompagne celui-ci est truffé de conditions, servant à adapter l'affichage par rapport au jeu du joueur

import (
	"fmt"
	"math/rand"
	"net/http"
	"os"
	"strconv"
	"strings"
	"text/template"
	"time"
)

//Premièrement, on a le "tableau" dans lequel on stockera les données qu'on va (ré)injecter à la page lors de chaque essai
//Vous verrez qu'on fait plusieurs fois appel à ces champs dans le fichier html. Par exemple, {{.Mot_a_trou}} est l'équivalent d'un fmt.Print; et le point juste avant la variable indique qu'il s'agit d'un "champ", d'une "variable" importée dans l'html
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
}

//C'est ici qu'on construit la (ou les) partie(s)
func main() {
	//On initialise le jeu avec ces données là
	mot_au_hasard := Selection_Mot("words.txt")
	lettres_validées := []byte{mot_au_hasard[len(mot_au_hasard)/2-1]}
	var lettres_essayées []byte
	position_pendu := 0

	//Cette fonction-ci nous sert à mettre en place le fichier html qui héberge l'interface visuelle du jeu
	tmpl := template.Must(template.ParseFiles("index.html"))

	//On va se servir des différentes redirections pour adapter la réaction du programme

	//1: on injecte les informations dans la page, à défaut de redemarrer une partie lorsque la précédente terminée (cf. la condition)
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		// http.ServeFile(w, r, "index.html")
		if position_pendu == 10 || Toutes_Les_Lettres_Sont_Dans_Le_Mot(lettres_validées, mot_au_hasard) {
			http.Redirect(w, r, "/restart", http.StatusSeeOther)
			return
		}
		if r.Method != http.MethodPost {
			//C'est précisément ici que le tour se joue, toutes les lignes commençant par "tmpl.ExecuteTemplate" auront exactement la même utilité,
			//qui est donc d'afficher l'html (2ème argument), selon un en-tête http (1er argument, en gros le truc indique quel genre de fichier c'est, et d'autres trucs du genre) et des données à injecter (3ème argument).
			//Les données sont le tableau du début rempli avec les différentes valeurs obtenue(s) au début et au cours du jeu
			tmpl.ExecuteTemplate(w, "index.html", Input_{PartyType: "classic", Mot_a_trouver: mot_au_hasard, PositionPendu: position_pendu, Lettres_trouvées: string(lettres_validées), Lettres_essayées: string(lettres_essayées), Mot_a_trou: Affiche_Mot_Pendu(mot_au_hasard, lettres_validées), Terminé: false, Gagné: false})
			return
		}
	})
	//2: on traite la requête utilisateur, à défaut de redemarrer une partie lorsque la précédente terminée (cf. la première condition)
	http.HandleFunc("/hangman", func(w http.ResponseWriter, r *http.Request) {
		if position_pendu == 10 || Toutes_Les_Lettres_Sont_Dans_Le_Mot(lettres_validées, mot_au_hasard) {
			http.Redirect(w, r, "/restart", http.StatusSeeOther)
			return
		}
		if r.Method != http.MethodPost {
			http.Redirect(w, r, "/", http.StatusSeeOther)
			return
		}
		proposition := r.FormValue("answer")
		if []byte(proposition)[0] >= 'A' && []byte(proposition)[0] <= 'Z' {
			proposition = string([]byte(proposition)[0] - 'A' + 'a')
		}
		if len(proposition) == 1 && ([]byte(proposition)[0] >= 'a' && []byte(proposition)[0] <= 'z') {
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
				tmpl.ExecuteTemplate(w, "index.html", Input_{PartyType: "classic", Answer: proposition, Mot_a_trouver: r.FormValue("mat"), PositionPendu: position_pendu, Lettres_trouvées: string(lettres_validées), Lettres_essayées: string(lettres_essayées), Mot_a_trou: Affiche_Mot_Pendu(mot_au_hasard, lettres_validées), Terminé: false, Gagné: false})
			}
			if position_pendu == 10 {
				tmpl.ExecuteTemplate(w, "index.html", Input_{PartyType: "classic", Answer: proposition, Mot_a_trouver: r.FormValue("mat"), PositionPendu: position_pendu, Lettres_trouvées: string(lettres_validées), Lettres_essayées: string(lettres_essayées), Mot_a_trou: Affiche_Mot_Pendu(mot_au_hasard, lettres_validées), Terminé: true, Gagné: false})
			}
		} else {
			tmpl.ExecuteTemplate(w, "index.html", Input_{PartyType: "classic", Answer: proposition, Mot_a_trouver: r.FormValue("mat"), PositionPendu: position_pendu, Lettres_trouvées: string(lettres_validées), Lettres_essayées: string(lettres_essayées), Mot_a_trou: Affiche_Mot_Pendu(mot_au_hasard, lettres_validées), Terminé: true, Gagné: true})
		}
	})
	//3: on redemarre la partie si besoin en réinjectant de nouvelles informations
	http.HandleFunc("/restart", func(w http.ResponseWriter, r *http.Request) {
		mot_au_hasard = Selection_Mot("words.txt")
		lettres_validées = []byte{mot_au_hasard[len(mot_au_hasard)/2-1]}
		lettres_essayées = []byte{}
		position_pendu = 0

		tmpl.Execute(w, Input_{PartyType: "classic", Mot_a_trouver: mot_au_hasard, Mot_a_trou: Affiche_Mot_Pendu(mot_au_hasard, lettres_validées), Lettres_trouvées: string(lettres_validées), Lettres_essayées: string(lettres_essayées), PositionPendu: position_pendu, Terminé: false, Gagné: false})
	})

	//Cette fonction sert à écouter (Listen) le port indiqué et en cas d'erreur nulle, à activer un serveur local pour pouvoir tester notre application
	http.ListenAndServe(":8080", nil)

	// port := "8080" // Port sur lequel votre serveur écoutera
	// fmt.Printf("Listening on port %s...\n", port)
	// err := http.ListenAndServe(":"+port, nil)
	// if err != nil {
	// 	fmt.Printf("Error: %s\n", err)
	// }
}

/*Ci-dessous des fonctions utiles au fonctionnement du hangman. Leur fonction est explicitée par leur nom*/

func Selection_Mot(file string) string {
	//- 1.1 : Mise en place de l'aléatoire
	r1 := rand.New(rand.NewSource(time.Now().UnixNano()))
	//- 1.2 : Fetch du fichier words
	f, _ := os.Open(file)
	b1 := make([]byte, 9999)
	n1, _ := f.Read(b1)

	var words []string
	index := 0
	for indice, lettre := range string(b1[:n1]) {
		if lettre == 10 {
			word := strings.TrimSpace(string(b1[index:indice]))
			if word != "" {
				words = append(words, word)
			}
			index = indice + 1
		}
	}
	//- 1.3 : Selection aléatoire
	mot_au_hasard := words[r1.Intn(len(words))]
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
