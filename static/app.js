const $form = $('#guess-form');
const $guess = $('#guess');
const $word_list = $('#word_list');
const $msg = $('#message')
const $scoreBoard = $('#scoreboard')
const $restart = $('.restartBtn')
const $timer = $('#timer')

let correctGuesses = []

onPageLoad();

async function onPageLoad(){
    result = await getGuesses();
    correctGuesses = result.data.answers;
    updateWordList(correctGuesses);
    $msg.hide()
    $scoreBoard.text(calcScore());
}

async function makeGuess(guess){
    const result = await axios.post('/guess', {'guess': guess});
    return result;
}
async function getGuesses(){
    const result = await axios.get('/guess');
    return result;
}

function updateWordList(wordList){
    $word_list.empty();
    for (let word of wordList) {
        $word_list.append(`<li>${word}</li`)
    }
}

function updateMessage(result){
    let status = result.data.result;
    let message = result.data.message;
    if (status == false){
        $msg.attr("class", "warning").show().text(message)
    } else if (status == true) { 
        $msg.attr("class", "success").show().text(message)
    } else{
        $msg.attr("class", "").hide().text('')
    }

}

function gameTimer(){
    let gameTime = 60;
    let timer = setInterval(() => {
        gameTime--
        $timer.text(gameTime)
        if (gameTime <= 0) {
            clearInterval(timer);
            $('#guess-form :input').prop("disabled", "true")
        }
    }, 1000);
}

function calcScore(){
    let score = 0;
    for (let word of correctGuesses){
        score += word.length;
    }
    return score
}

async function submitGuess(event){
    event.preventDefault();

    const guess = $guess.val();
    let result = await makeGuess(guess);
    $guess.val('');

    correctGuesses = result.data.answers;
    updateWordList(correctGuesses);

    updateMessage(result);

    $scoreBoard.text(calcScore());
}

$form.on('submit', submitGuess)

gameTimer();