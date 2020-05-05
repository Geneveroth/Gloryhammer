var angus_hp = 100;
var unicorn_hp = 50;

var log = document.getElementById('log');

document.getElementById('attack').addEventListener('click', function () {
    var li = document.createElement('li');
    var p = document.createElement('p');
    var angus_defense = 12;
    var unicorn_defense = 10;
    var angus_hit = 1+ Math.ceil(Math.random() * 19);
    var angus_dmg = 5+ Math.ceil(Math.random() * 5); //gives 5-10
    var unicorn_hit = 1+ Math.ceil(Math.random() * 19);
    var unicorn_dmg = 1+ Math.ceil(Math.random() * 9)  //gives 1-10;
    if (angus_hit > unicorn_defense){
        unicorn_hp-=angus_dmg;
    }
    else if (angus_hit< unicorn_defense){
        angus_hp-=unicorn_dmg;
    }
        
    if(angus_hit > unicorn_defense) {
        var str = "Angus McFife hits the unicorn for " + (angus_dmg) + " points of damage!"
    }
    else {
        var str = "Angus McFife misses and the unicorn hits him for " + (unicorn_dmg) + " points of damage!"
    }
    if (angus_hp <= 0){
        location.assign("death_unicorn.html");
    }
    if (unicorn_hp <= 0){
        location.assign("victory_unicorn");
    }
    li.innerText = str;
    log.appendChild(li);
    document.getElementById('angus-hp').innerText = angus_hp;
    document.getElementById('unicorn-hp').innerText = unicorn_hp;
    return angus_hp, unicorn_hp
})