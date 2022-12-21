function switchStations() {
  // console.log("got clicked.");
  var frame = document.getElementById("player");
  frame.src = "https://www.youtube.com/embed/L1zoItQw_e4?controls=0&autoplay=1&mute=0";
}

function pause(){
  console.log("got clicked.")
  var frame = document.getElementsById("player");
  frame.contentWindow.postMessage('{"event": "command", "func": "pauseVideo", "args": ""}', '*');
}
