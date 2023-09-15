
chrome.commands.onCommand.addListener(function (command) {
  if (command === "change-font") {
    // Add code here to apply your extension's effect when the shortcut is triggered
    // You can directly apply the effect or send a message to a content script to do so
    // For example:
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
      chrome.tabs.executeScript(tabs[0].id, { file: "content.js" });
    });
  }
});
