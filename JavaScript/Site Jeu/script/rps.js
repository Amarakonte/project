let wins = 0; let loses = 0;
const choices = ["papier", "caillou", "ciseaux"];
const gameStatusRPS = document.getElementById("gameStatusRPS");
const gameScore = document.getElementById("gameScore");
const paper = document.getElementById("paper");
const rock = document.getElementById("rock");
const scissors = document.getElementById("scissors");

function runGame(userChoice) {
  const computerChoice = choices[Math.floor(Math.random() * choices.length)];

  switch(userChoice + '_' + computerChoice) {
    case 'papier_ciseaux':
    case 'caillou_papier':
    case 'ciseaux_caillou':
      loses += 1;
      gameStatusRPS.innerHTML = `Moi : ${userChoice} | Ordinateur : ${computerChoice} ---> Ordinateur Gagne`
      break;
    case 'papier_caillou':
    case 'caillou_ciseaux':
    case 'ciseaux_papier':
      wins += 1;
      gameStatusRPS.innerHTML = `Moi : ${userChoice} | Ordinateur : ${computerChoice} ---> Moi Gagne`
      break;
    case 'papier_papier':
    case 'caillou_caillou':
    case 'ciseaux_ciseaux':
      gameStatusRPS.innerHTML = `Moi : ${userChoice} | Ordinateur : ${computerChoice} ---> Egalité`
      break;
  }

  gameScore.innerHTML = `Moi : ${wins} pts | Ordinateur : ${loses} pts`;
}

paper.addEventListener("click", () => runGame("papier"));
rock.addEventListener("click", () => runGame("caillou"));
scissors.addEventListener("click", () => runGame("ciseaux"));