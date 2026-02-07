var root = document.documentElement;

// Jupyter
var fontFamily = '--jp-code-font-family-default';
var currentFontFamily = getComputedStyle(root).getPropertyValue(fontFamily);
var newFontFamily = currentFontFamily === 'Jetbrains Mono' ? '' : 'Jetbrains Mono';
root.style.setProperty(fontFamily, newFontFamily);

// Gerrit
fontFamily = '--monospace-font-family';
currentFontFamily = getComputedStyle(root).getPropertyValue(fontFamily);
newFontFamily = currentFontFamily === 'Jetbrains Mono' ? '' : 'Jetbrains Mono';
root.style.setProperty(fontFamily, newFontFamily);

// Redshift Query Editor
document.querySelector('div.view-lines').style.fontFamily = 'Jetbrains Mono';