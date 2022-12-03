import fs from 'fs';

const data = fs.readFileSync('in.txt');

const example = `vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw`.split('\n');

const input = data.toString().split('\r\n');
//const input = example;

const compartments = input.map(e => {
    return {
        comp1: e.substring(0, e.length / 2),
        comp2: e.substring(e.length / 2, e.length)
    };
});

const getPriorityForItem = (char) => 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.indexOf(char) + 1;


// P1
const out = compartments
    .map(c => [...new Set(c.comp1.split(''))]
        .filter(i => c.comp2.includes(i))
        .reduce((acc, curr) => acc + getPriorityForItem(curr) , 0))
    .reduce((acc, curr) => acc + curr, 0);


// P2
const getMostPrevalent = (items) => {
    let maxEntries = 0;
    let item = '';

    items.reduce((acc, curr) => {
            const value = 1 + (acc.get(curr) || 0);
            acc.set(curr, value);

            if(value > maxEntries) {
                maxEntries = value;
                item = curr;
            }

            return acc;
        }, new Map());
        return item;    
}

let priorityAccumulator = 0;
    
for(let i = 2; i < input.length; i += 3) {
    const c1 = input[i - 2];
    const c2 = input[i - 1];
    const c3 = input[i];

    let onAllThree = c1
        .split('')
        .filter((i) => c2.indexOf(i) + c3.indexOf(i) !== -1);
    let mostPrevalent = getMostPrevalent(onAllThree);    
    priorityAccumulator += getPriorityForItem(mostPrevalent);
}

console.log(priorityAccumulator);