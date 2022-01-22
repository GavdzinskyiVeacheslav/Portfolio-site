var randomNumber = Math.floor(Math.random() * 100) + 1;

var guesses = document.querySelector('.guesses');
var lastResult = document.querySelector('.lastResult');
var lowOrHi = document.querySelector('.lowOrHi');

var guessSubmit = document.querySelector('.guessSubmit');
var guessField = document.querySelector('.guessField');
var resetButton = document.querySelector('.reset');
var cancelButton = document.querySelector('.cancel');

var guessCount = 1;
var resetButton;

function checkGuess() {
  var userGuess = Number(guessField.value);
  if (guessCount === 1) {
    guesses.textContent = 'Previous guesses: ';
    guesses.style.color = '#1DD300'
  }
  guesses.textContent += userGuess + ', ';

  if (userGuess === randomNumber) {
    lastResult.textContent = 'Congratulations! You got it right!';
    lastResult.style.color = '#1DD300'
    lastResult.style.backgroundColor = '#2c2c2c';
    lowOrHi.textContent = '';
    setGameOver();
  } else if (guessCount === 7) {
    lastResult.textContent = 'Attempts ended - you lost!';
    setGameOver();
  } else {
    lastResult.textContent = 'Wrong!';
    lastResult.style.color = 'red'
    lastResult.style.backgroundColor = '#2c2c2c';
    if(userGuess < randomNumber) {
      lowOrHi.textContent = 'Last guess was too low!';
      lowOrHi.style.color = 'yellow'
    } else if(userGuess > randomNumber) {
      lowOrHi.textContent = 'Last guess was too high!';
      lowOrHi.style.color = 'yellow'
    }
  }

  guessCount++;
  guessField.value = '';
  guessField.focus();
}

document.addEventListener('keyup', function(event){
    console.log(event.code);
    if (event.code === 'Enter'){
      checkGuess();
    }
});

guessSubmit.addEventListener('click', checkGuess);

function setGameOver() {
  guessField.disabled = true;
  guessSubmit.disabled = true;
  resetButton.style.visibility = 'visible';
  cancelButton.style.visibility = 'visible';
  /*
  resetButton = document.createElement('button');
  resetButton.textContent = 'Start new game';
  */
  document.body.appendChild(resetButton);
  document.body.appendChild(cancelButton);
  resetButton.addEventListener('click', resetGame);
  cancelButton.addEventListener('click', back)
}

function back() {
  location.reload()
}

function resetGame() {
  guessCount = 1;

  var resetParas = document.querySelectorAll('.resultParas p');
  for (var i = 0 ; i < resetParas.length ; i++) {
    resetParas[i].textContent = '';
  }

  resetButton.parentNode.removeChild(resetButton);
  cancelButton.parentNode.removeChild(cancelButton);

  guessField.disabled = false;
  guessSubmit.disabled = false;
  guessField.value = '';
  guessField.focus();

  lastResult.style.backgroundColor = '#2c2c2c';

  randomNumber = Math.floor(Math.random() * 100) + 1;
}