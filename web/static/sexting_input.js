// Makey Makey key mappings

// UP     = 65 = a
// DOWN   = 66 = b
// LEFT   = 67 = c
// RIGHT  = 68 = d
// SPACE  = 69 = e
// CLICK  = 70 = f

// D5     = 71 = g
// D4     = 72 = h
// D3     = 73 = i
// D2     = 74 = j
// D1     = 75 = k
// D0     = 76 = l

// A5     = 77 = m
// A4     = 78 = n
// A3     = 79 = o
// A2     = 80 = p
// A1     = 81 = q
// A0     = 82 = r

modKeys = [65, 66, 67, 68, 69, 70, 81];
shiftKey = 71;
otherKeys = [72, 73, 74, 75, 76, 77, 78, 79, 80, 82];

allKeys = otherKeys.concat(modKeys).concat([shiftKey]);

mappings = {
  81: { 72: ' ', 71: "ENTER", 74: "BACKSPACE" },
  65: { 72: ';', 73: '-', 74: ':', 75: '!', 76: ',', 78: '.', 82: '?' },
  66: { 72: '2', 73: '0', 74: '1', 75: '3', 76: '5', 77: '7', 78: '6', 79: '9', 80: '8', 82: '4' },
  67: { 72: 'k', 73: 'm', 74: 'l', 75: 'j', 76: 'h', 82: 'i' },
  68: { 72: 'r', 73: 't', 74: 's', 75: 'q', 76: 'o', 78: 'n', 82: 'p' },
  69: { 72: 'x', 73: 'z', 74: 'y', 75: 'w', 76: 'u', 82: 'v' },
  70: { 72: 'e', 73: 'g', 74: 'f', 75: 'd', 76: 'b', 78: 'a', 82: 'c' }
};

keyDown = {}

message = "";

$.each(allKeys, function(i, key) {
  keyDown[key] = false;
});

function updateDom() {
  $('#display').html(message + '<span class="cursor">|</span>');
  $('#message').val(message);
}

function registerChar(character) {
  console.log(character);
  message += character;
  updateDom();
}

function processEnter() {
  console.log("ENTER pressed!");
  if (message.length > 0) {
    console.log("Posting form...");
    $.post('print', $('form').serialize());
    message = "";
    updateDom();
  }
}

function processBackspace() {
  console.log("BACKSPACE pressed!");
  if (message.length > 0) {
    message = message.slice(0, message.length - 1);
    updateDom();
  }
}

function currentKeySet() {
  modKey = 0
  $.each(modKeys, function(i, key) {
    if (keyDown[key]) {
      modKey = key;
    }
  });
  if (modKey in mappings) {
    return mappings[modKey];
  }
  return [];
}

function keyPressed(key) {
  keySet = currentKeySet();

  if (key in keySet) {
    character = keySet[key];
    if (character.length == 1) {
      if (keyDown[shiftKey]) {
        character = character.toUpperCase();
      }
      registerChar(character);
    } else {
      if (character == "ENTER") {
        processEnter();
      }
      if (character == "BACKSPACE") {
        processBackspace();
      }
    }
  }
}

$(document).keydown(function(e) {
  $.each(allKeys, function(i, key) {
    if (e.which == key) {
      if (!keyDown[key]) {
        console.log('DOWN: ' + key);
        keyPressed(key);
      }
      keyDown[key] = true;
    }
  });
}).keyup(function(e) {
  $.each(allKeys, function(i, key) {
    if (e.which == key) {
      keyDown[key] = false;
      console.log('UP: ' + key);
    }
  });
});

$(function() {
  updateDom();
});
