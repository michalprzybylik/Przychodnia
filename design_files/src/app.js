import './scss/main.scss';

import 'jquery';
import 'popper.js';
import 'bootstrap';

import './js/sticky.js';

__webpack_nonce__ = 'c29tZSBjb29sIHN0cmluZyB3aWxsIHBvcCB1cCAxMjM';


$(document).ready(function() {
  $('.toast').toast({
    delay: 6000,
  });
  $('.main-toast').toast('show');

  $('.popover-profile-lekarz').popover({
    trigger: 'hover',
    container: 'body',
    toggle: 'popover',
    placement: 'top',
    content: 'Zalogowano jako lekarz',
  });
  $('.popover-profile-rejestratorka').popover({
    trigger: 'hover',
    container: 'body',
    toggle: 'popover',
    placement: 'top',
    content: 'Zalogowano jako rejestratorka',
  });
  $('.popover-profile-laborant').popover({
    trigger: 'hover',
    container: 'body',
    toggle: 'popover',
    placement: 'top',
    content: 'Zalogowano jako laborant',
  });
  $('.popover-profile-kierlab').popover({
    trigger: 'hover',
    container: 'body',
    toggle: 'popover',
    placement: 'top',
    content: 'Zalogowano jako kierownik laboratorium',
  });
  // $(document).ready(function(){
  //   $("#sticker").sticky({
  //     topSpacing:0,
  //     responsiveWidth: true
  //   });
  // });
});

// export default func;
