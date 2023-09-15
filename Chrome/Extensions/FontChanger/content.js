var root = document.documentElement;

// Jupyter
var currentFontFamily = getComputedStyle(root).getPropertyValue('--jp-code-font-family-default');
var newFontFamily = currentFontFamily === 'Jetbrains Mono' ? '' : 'Jetbrains Mono';
root.style.setProperty('--jp-code-font-family-default', newFontFamily);

// Gerrit
currentFontFamily = getComputedStyle(root).getPropertyValue('--monospace-font-family');
newFontFamily = currentFontFamily === 'Jetbrains Mono' ? '' : 'Jetbrains Mono';
root.style.setProperty('--monospace-font-family', newFontFamily);