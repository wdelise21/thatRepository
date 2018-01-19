/* 
Notes for Modders:

This is completely open source, and is optimized so that you can add fonts.
Removing a font may cause issues, so whenever you remove a font, add a font with the same key value (the value in the [] )
The operation may take time to complete and will halt when an error occurs
It's fairly messy, but then again I don't actually know Javascript...

Have Fun!


*/

var fontLib = {};
fontLib[1] = "Arial";
fontLib[2] = "Calibri"; 
fontLib[3] = "Ubuntu";
fontLib[4] = "Cambria";
fontLib[5] = "Corsiva";
fontLib[6] = "Consolas";
fontLib[7] = "Georgia"; 
fontLib[8] = "Garamond";
fontLib[9] = "Nunito";
fontLib[10] = "Roboto";
fontLib[11] = "Source Code Pro";
fontLib[12] = "Cuprum";
fontLib[13] = "Cormorant Garamond";
fontLib[14] = "Vollkorn";
fontLib[15] = "Rokkitt";
fontLib[16] = "Amatic SC";
fontLib[17] = "Nunito Sans";
fontLib[18] = "PT Sans Caption";
fontLib[19] = "Rubik";
fontLib[20] = "Abel";
fontLib[21] = "Karla";
fontLib[22] = "Bree Serif";
fontLib[23] = "Shadows Into Light";
fontLib[24] = "Catamaran";
fontLib[25] = "Gloria Hallelujah";
fontLib[26] = "Merriweather Sans";
fontLib[27] = "Impact";
fontLib[28] = "Lobster";
fontLib[29] = "Lora";
fontLib[30] = "Maven Pro";
fontLib[31] = "Merriweather";
fontLib[32] = "Montserrat";
fontLib[33] = "Nunito";
fontLib[34] = "Open Sans";
fontLib[35] = "Oswald";
fontLib[36] = "Pacifico";
fontLib[37] = "Playfair Display";
fontLib[38] = "Raleway";
fontLib[39] = "Roboto Mono";
fontLib[40] = "Spectral";
fontLib[41] = "Syncopate";
fontLib[42] = "Amatic SC";
fontLib[43] = "Calibri";
fontLib[44] = "Caveat";
fontLib[45] = "Comfortaa";
fontLib[46] = "Comic Sans MS";
fontLib[47] = "Comic Sans MS";
fontLib[48] = "Comic Sans MS";
fontLib[49] = "Consolas";
fontLib[50] = "Corsiva";
fontLib[51] = "Courier New";
fontLib[52] = "Dancing Script";
fontLib[53] = "Droid Sans";
fontLib[54] = "Droid Serif";
fontLib[55] = "EB Garamond";
fontLib[56] = "Georgia";
fontLib[57] = "Helvetica Neue";
fontLib[58] = "Rojdhani";
fontLib[59] = "Kanit";
fontLib[60] = "Pathway Gothic One";
fontLib[61] = "Patua One";
fontLib[62] = "Poiret One";
fontLib[63] = "Shrikhand";
fontLib[64] = "Passion One";
fontLib[65] = "Bangers";
fontLib[66] = "Khand";
fontLib[67] = "Audiowide";
fontLib[68] = "Sarala";
fontLib[69] = "Caveat";
fontLib[70] = "Architects Daughter" ;
fontLib[71] = "Jura";
fontLib[72] = "Prompt";
fontLib[73] = "Shadows Into Light Two";
fontLib[74] = "Tangerine";
fontLib[75] = "Playball";
fontLib[76] = "Yellowtail";
fontLib[77] = "Monoton";
fontLib[78] = "Cabin Sketch";
fontLib[79] = "Nothing You Could Do";
fontLib[80] = "Homemade Apple";
fontLib[81] = "Oleo Script";
fontLib[82] = "Special Elite";
fontLib[83] = "Covered By Your Grace";
fontLib[84] = "Quantico";
fontLib[85] = "Zilla Slab";
fontLib[86] = "Press Start 2P";
fontLib[87] = "Alex Brush";
fontLib[88] = "Reenie Beanie";
fontLib[89] = "Pinyon Script";
fontLib[90] = "Freckle Face";
fontLib[91] = "Ceviche One";
fontLib[92] = "Marcellus SC";
fontLib[93] = "Love Ya Like A Sister";
fontLib[94] = "Parisienne";
fontLib[95] = "Yesteryear";
fontLib[96] = "Voltaire";
fontLib[97] = "Bubblegum Sans";
fontLib[98] = "Black Ops One";
fontLib[99] = "Fredericka The Great";
fontLib[100] = "Italianno";



/* I love how the actual programming fits into 13 lines vs the 101 lines of the font designations */
var formerRange = 0;
var loopText = true;

function myFunction() {
   var latterRange = formerRange + 1;
   var ranNum = Math.floor((Math.random() * Object.keys(fontLib).length) + 1);
   var body = DocumentApp.getActiveDocument().getBody();
   var text = body.editAsText();
   text.setFontFamily(formerRange, latterRange, fontLib[ranNum]);
   formerRange += 1;
}
while (loopText == true) {
   myFunction();
}