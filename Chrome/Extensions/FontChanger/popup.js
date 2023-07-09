document.addEventListener('DOMContentLoaded', function() {
  var toggleButton = document.getElementById('toggleButton');

  toggleButton.addEventListener('click', function() {
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
      chrome.tabs.executeScript(tabs[0].id, { code: `
        var root = document.documentElement;
        var currentFontFamily = getComputedStyle(root).getPropertyValue('--jp-code-font-family-default');
        var newFontFamily = currentFontFamily === 'Jetbrains Mono' ? '' : 'Jetbrains Mono';
        root.style.setProperty('--jp-code-font-family-default', newFontFamily);

        // var codeElements = document.querySelectorAll('.blob-code-inner');
        // codeElements.forEach(function(element) {
        //   var currentFontFamily = getComputedStyle(element).getPropertyValue('--font-family');
        //   var newFontFamily = currentFontFamily === 'Jetbrains Mono' ? '' : 'Jetbrains Mono';
        //   element.style.fontFamily = newFontFamily;
        // });
      ` });
    });
  });
});
