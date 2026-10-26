var fibGenerator = function*() {
  let curr = 0; 
  let nxt = 1;
  while (true) {
    yield curr; 
    let temp = curr + nxt;
    curr = nxt;
    nxt = temp;
  }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */