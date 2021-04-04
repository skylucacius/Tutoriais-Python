var input = document.getElementById('credit-card-mask'),
    oldValue,
    regex = new RegExp(/^\d{0,16}$/g),
    mask = function(value) {
      var output = [];
        for(var i = 0; i < value.length; i++) {
          if(i !== 0 && i % 3 === 0) {
            output.push("."); // add the separator
          }
          output.push(value[i]);
        }
        return output.join("");
    },
    unmask = function(value) {/^\d{0,16}$/g
      var output = value.replace(new RegExp(/[^\d]/, 'g'), ''); // Remove every non-digit character
      return output;
    },
    keydownHandler = function(e) {
      oldValue = e.target.value;
    },
    inputHandler = function(e) {
          var el = e.target,
               newValue = el.value
          ;
          newValue = unmask(newValue);
          
          if(newValue.match(regex)) {
            newValue = mask(newValue);
            el.value = newValue;
          } else {
            el.value = oldValue;
          }
    }
;

input.addEventListener('keydown', keydownHandler );
input.addEventListener('input', inputHandler );
