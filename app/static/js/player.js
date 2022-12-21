function switchStations() {
  // console.log("got clicked.");
  var frame = document.getElementById("player");
  frame.src = "https://www.youtube.com/embed/L1zoItQw_e4?controls=0&autoplay=1&mute=0";
}

// global variable for the player
var player;

// this function gets called when API is ready to use
function onYouTubePlayerAPIReady() {
  // create the global player from the specific iframe (#video)
  player = new YT.Player("player", {
    events: {
      // call this function when player is ready to use
      'onReady': onPlayerReady
    }
  });
}

function onPlayerReady(event) {
  // // bind events
  // var playButton = document.getElementById("play-button");
  // playButton.addEventListener("click", function () {
  //   player.playVideo();
  // });

  var pauseButton = document.getElementById("pause-button");
  pauseButton.addEventListener("click", function ()
   {
    console.log('pause clicked');
    player.pauseVideo();
  }
);
}

//injecting YouTube API script
var tag = document.createElement('script');
tag.src = "//www.youtube.com/player_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
