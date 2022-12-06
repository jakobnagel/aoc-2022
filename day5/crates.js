const { create } = require("domain");
const fs = require("fs");

const file = fs.readFileSync("input.txt", "utf-8");

const lines = file.split(/\r?\n/);

const crates = new Array((lines[0].length + 1) / 4);

// Loads crates from file
let fileLine = 0;
for (line = 0; line < lines.length; line++) {
  if (lines[line][1] == "1") {
    break;
  }

  const split = lines[line].match(/.{1,4}/g) || [];

  for (item in split) {
    if (split[item].includes("[")) {
      if (!crates[item]) {
        crates[item] = [split[item][1]];
      } else {
        crates[item].unshift(split[item][1]);
      }
    }
  }
  fileLine = line;
}

fileLine += 3;

// Move items
for (fileLine; fileLine < lines.length; fileLine++) {
  const line = lines[fileLine];

  const splitLine = line.split(" ");
  const amount = +splitLine[1];
  const from = +splitLine[3] - 1;
  const to = +splitLine[5] - 1;

  crates[to].push(...crates[from].splice(crates[from].length - amount));
}

for (crate of crates) {
  console.log(crate[crate.length - 1]);
}
