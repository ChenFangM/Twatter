function switchStations() {
  console.log("switchStations() clicked.");
  var frame = document.getElementById("player");
  frame.src = "https://www.youtube.com/embed/L1zoItQw_e4?controls=0&autoplay=1&mute=0";
}

function pause(){
  console.log("pause() clicked.");
  var frame = document.getElementById("player")
  frame.contentWindow.postMessage('{"event":"command","func":"PauseVideo","args":""}', '*');
}

function play(){
  console.log("play() clicked.");
  var frame = document.getElementById("player")
  frame.contentWindow.postMessage('{"event":"command","func":"PlayVideo","args":""}', '*');
}
