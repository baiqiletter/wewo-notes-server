
const highlightTag = function() {
    let notes = document.getElementsByClassName('note-content')
    console.log(notes)
    for (let note of notes) {
        note.innerHTML = note.innerHTML
            .replace(/#\S+/g, match => "<a href='tag/" + match.slice(1) + "/'<span class='tag'>" + match + "</span></a>")
            .replace(/link:\/\/note\/[0-9]/g, match => "<a href='" + match.slice(7) + "/'><span class='link'>Memo</span></a>")
    }
}

highlightTag()
