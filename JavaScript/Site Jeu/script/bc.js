let attempts = 0; let bulls = 0; let cows = 0;
let secretNumber = generateSecretNumber();
console.log(secretNumber);

let roundStats = {
  round: 1,
  wins: 0,
  loses: 0
}

function checkGuess() {
  let guess = document.getElementById("guessInput").value;
  let secretString = secretNumber.join('');
  bulls = 0; cows = 0;

  const checkGuessLength = new Set(guess);

  if (guess.length !== checkGuessLength.size || guess.length !== 4) {
    document.getElementById("logsArea").value += `${guess} est invalide, veuillez entrer un nombre composé de exactement 4 chiffres différents.\n`;
    return null;
  }

  attempts += 1;

  for (let i = 0; i < 4; i += 1) {
    if (secretString[i] === guess[i]) {
      bulls += 1;
    } else if (secretString.includes(guess[i])) {
      cows += 1;
    }
  }

  if (bulls === 4) {
    document.getElementById("logsArea").value += `${secretString} | Bravo, vous avez gagné en ${attempts} essais.\n`;
    roundStats.wins += 1;
    return playAgain();
  } else if (attempts === 10) {
    document.getElementById("logsArea").value += `${secretString} | Dommage, vous avez perdu !\n`;
    roundStats.loses += 1;
    return playAgain();
  }

  document.getElementById("logsArea").value += `${guess} - ${bulls}B ${cows}C, Essaie: ${attempts}\n`;
}

function playAgain() {
  roundStats.round += 1;
  printGameStats();
  attempts = 0; bulls = 0; cows = 0;
  secretNumber = generateSecretNumber();
}

function printGameStats() {
  const gameStats = document.getElementById("gameStats");
  gameStats.innerHTML = `Nbr de parties: ${roundStats.round} | Victoire : ${roundStats.wins} | Défaite : ${roundStats.loses}`;
}

function generateSecretNumber() {
  const numbers = Array.from({ length: 9}, (v, k) => k + 1);
  let currentIndex = numbers.length, randomIndex;

  while (currentIndex != 0) {
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex -= 1;

    [numbers[currentIndex], numbers[randomIndex]] = [numbers[randomIndex], numbers[currentIndex]];
  }

  return numbers.slice(0, 4);
}

function clearLogs() {
  document.getElementById("logsArea").value = "";
}

function printRules() {
  alert("Entrez un nombre composé de 4 chiffres différents dans la case à côté de 'Guess'. L'ordinateur le compare avec le code secret et vous donne deux indices: les numéros 'bulls' (B) et des cows (C). Qu'est ce que cela signifie? Un 'bulls' est un chiffre qui est présent dans les deux codes à la même position. Un 'cows' est un chiffre qui est présent dans les deux codes mais à une position différente. Par exemple, si le code secret est 7512 et que vous essayez 5392, la réponse sera '1B 1C' (1 bull 1 cow). C'est tout!")
}