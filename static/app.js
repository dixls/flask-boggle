const $form = $('#guess-form');
const $guess = $('#guess');

async function makeGuess(guess){
    const result = await axios.post('/guess', {'guess': guess});
    console.log(result);
}

$form.on('submit', function(event){
    event.preventDefault();
    const guess = $guess.value();
    let result = await makeGuess(guess);
    $guess.value() = '';

})
