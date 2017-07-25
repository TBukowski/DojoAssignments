function slotMachine(quarters){
  while(quarters){
    var win = Math.random();
    console.log(win)
    if(win < .01){
    (Math.floor(Math.random()*50)+50)
    var winnings = quarters + Math.floor(Math.random()*50)+50
    console.log(winnings)
    return winnings
    } 
    quarters--; 
  }
  return 0 
}
console.log(slotMachine(50));