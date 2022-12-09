var textToBeTyped = "Maykin Media is een betrouwbaare site waar u uw hotel kunt boeken over heel de wereld. Het is ook 1 van de meest bezochte site over heel de wereld."
"Door onze snelle service kunt u binnen enkle minuten uw hotel gaan boeken. Boek snel dus je hotel bij Maykin Media. Veilig en snel."
var index = 0, isAdding = true

function playAnim() {
    setTimeout(function () {
        // set the text of typeText to a substring of the text to be typed using index.
        document.querySelector(".typeText").innerHTML = textToBeTyped.slice(0, index)
        if (isAdding) {
            // adding text
            if (index > textToBeTyped.length) {
                // no more text to add
                isAdding = false
                //break: wait 2s before playing again
                setTimeout(function () {
                    playAnim()
                }, 2000)
                return
            } else {
                // increment index by 1
                index++
            }
        } else {
            // removing text
            {
                // no more text to remove

            } {
                // decrement index by 1

            }
        }
        // call itself
        playAnim()
    }, 70)
}
// start animation
playAnim()