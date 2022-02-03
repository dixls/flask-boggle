const $form = $('#guess-form');
const $guess = $('#guess');
const $word_list = $('#word_list');

let correctGuesses = []

onPageLoad();

async function onPageLoad(){
    result = await getGuesses();
    correctGuesses = result.data.answers;
    updateWordList(correctGuesses);
}

async function makeGuess(guess){
    const result = await axios.post('/guess', {'guess': guess});
    console.log(result);
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

async function submitGuess(event){
    event.preventDefault();

    const guess = $guess.val();
    let result = await makeGuess(guess);
    $guess.val('');

    correctGuesses = result.data.answers;
    updateWordList(correctGuesses);
}

$form.on('submit', submitGuess)
