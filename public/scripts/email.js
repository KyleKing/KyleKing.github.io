// Email obfuscator script 2.1 by Tim Williams, University of Arizona
// Random encryption key feature coded by Andrew Moulden
// This code is freeware provided these four comment lines remain intact
// A wizard to generate this code is at http://www.jottings.com/obfuscator/
window.onload = function() {
  coded = "2S2ut7d6@7Scua.ByS";
  key = "bcXHx1GN2vI0i7PyFZEBwpJ3Dr6lYfud8AVnmeMOUs9Q4ajCKzhRktS5WgToqL";
  shift = coded.length;
  link = "";
  for (i = 0; i < coded.length; i++) {
    if (key.indexOf(coded.charAt(i)) == -1) {
      ltr = coded.charAt(i);
      link += (ltr);
    }
    else {
      ltr = (key.indexOf(coded.charAt(i)) - shift + key.length) % key.length;
      link += (key.charAt(ltr));
    }
  }
  $('#email-link').attr('href',"mailto:" + link);
}
