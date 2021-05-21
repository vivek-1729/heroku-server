window.onload = function () {
var currentStat = 0;
for(i=0; i<=6; i++) {
    if(i!=currentStat) {
        var statName = "stat" + i;
        var statBlock = document.getElementById(statName);
        statBlock.style.display = "none";
    }
}
var names = {0:"person1", 1:"person2", 2:"person3", 3:"person4", 4:"person5", 5:"person6"}
var draft = document.getElementById("draft");
var submitButton = document.getElementById("submitForm");
// statBlock.style.display = "none";
}
if ("{{person}}" != names[0]) { //if the given name is not the name of the person who has the first pick 
    submitButton.style.display = "none"; //hide the multiple choice selections
}

const draftPick = new WebSocket( //create a websocket that will relay the draft pick to the backend
    'ws://'
    + window.location.host
    + '/ws/submit/'
);

var draftOrder = 0;
var increasingDraft = true; //This allows for the snaking draft  


draftPick.onmessage = function(e) { //occurs when someone else drafted and the WebSocket sends the information of who was drafted (through update_draft_room function in routing.py)
    var statMap = {0:'points',1:'assists', 2:'rebounds',3:'blocks', 4:'three pointers', 5:'fouls', 6:'free throws'}
    const data = JSON.parse(e.data);
    var lastPerson = data.name; //name of the person who last drafted
    var stat = data.stat;
    draftOrder = data.draftOrder;
    
    var nameLength = Object.keys(names).length;

    if(nameLength==draftOrder && increasingDraft == true) {
        increasingDraft = false;
        draftOrder = nameLength-1;
        console.log(draftOrder);
    } 
    
    if("{{person}}" == names[draftOrder]) {
        submitButton.style.display = "block";
    }
    else {
        submitButton.style.display = "none";
    }
    var element = document.getElementById("stat" + data.stat + data.id); //get the id of the multiple choice block that was selected (for example Jayson Tatum has an id of 1)
    element.parentNode.removeChild(element); //delete that multiple choice block (so no one else can pick the same person)
    var player = data.name + " has chosen " + data.player + " for " + statMap[stat] + '.\n'  
    document.querySelector('#chat-log').value += player; ////add who selected what player in the text box

    if(draftOrder == 0 && increasingDraft == false){
        increasingDraft = true;
        draftOrder = -1;
    }

};

function sendPick(){ 
    var selectedBox = $('input[name=test]:checked'); //get the multiple choice block that was selected
    if (selectedBox.attr('id') != undefined){
        var id = selectedBox.attr('id');
        var player = selectedBox.attr('value'); //get player name
        draftPick.send(JSON.stringify({
            'stat' : currentStat,
            'player': player,
            'id': id,
            'name': "{{person}}",
            'draftOrder' : draftOrder,
            'increasingDraft' : increasingDraft
        }));
}      
    return false; //don't refresh the page
}

function getFilter() {
    console.log("Beginning " + currentStat);
    var selectedOption = document.getElementById("drop");
    var statName = "stat" + selectedOption.value;
    var statBlock = document.getElementById(statName);

    var currentBlock = document.getElementById("stat" + currentStat);

    currentBlock.style.display = "none";
    statBlock.style.display = "block";
    currentStat = selectedOption.value;
    return false;
}
