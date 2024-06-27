// let currentTabUrl = '';

// chrome.tabs.onActivated.addListener(function(activeInfo) {
//   chrome.tabs.get(activeInfo.tabId, function(tab) {
//     currentTabUrl = tab.url;
//     console.log('Current Tab URL (background):', currentTabUrl);
    
//     // You can perform additional actions with `currentTabUrl` here
//   });
// });

// chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
//   if (request.message === 'get_current_url') {
//     sendResponse({ url: currentTabUrl });
//   }
// });
