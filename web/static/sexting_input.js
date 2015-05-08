
charKeys = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74];
modKeys = [75, 76, 77, 78, 79, 80];
shiftKey = 81;

allKeys = charKeys.concat(modKeys).concat([shiftKey]);

mappings = {
  0: { 65: ' ', 66: "ENTER", 67: "BACKSPACE" },
  75: { 65: 'a', 66: 'b', 67: 'c', 68: 'd', 69: 'e', 70: 'f', 71: 'g' },
  76: { 65: 'h', 66: 'i', 67: 'j', 68: 'k', 69: 'l', 70: 'm' },
  77: { 65: 'n', 66: 'o', 67: 'p', 68: 'q', 69: 'r', 70: 's', 71: 't' },
  78: { 65: 'u', 66: 'v', 67: 'w', 68: 'x', 69: 'y', 70: 'z' },
  79: { 65: '0', 66: '1', 67: '2', 68: '3', 69: '4', 70: '5', 71: '6', 72: '7', 73: '8', 74: '9' },
  80: { 65: '.', 66: ',', 67: '?', 68: '!', 69: ';', 70: ':', 71: '-' }
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

function currentModKey() {
  modKey = 0
  $.each(modKeys, function(i, key) {
    if (keyDown[key]) {
      modKey = key;
    }
  });
  return modKey;
}

function keyPressed(key) {
  modKey = currentModKey();

  d = mappings[modKey];
  if (key in d) {
    character = d[key];
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
