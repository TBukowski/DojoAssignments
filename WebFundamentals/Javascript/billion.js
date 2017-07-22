var reward = .01;

for(var day = 1; day <= 30; day++) {
    if(day === 1) {
        continue;
    }
    reward = reward * 2;
}

console.log('30 day reward is', '$' + reward);