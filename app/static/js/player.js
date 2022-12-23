// Struggled with JSON parsing... so here we are...

currentDirection = true //true for forwards, false for backwards
// quick fix for a "bug" where you need to press arrowkey twice if different directions

const videoLinks =
[
    "https://www.youtube.com/embed/L1zoItQw_e4?controls=0&autoplay=1&mute=0",

    "https://www.youtube.com/embed/uYJmRShQYH0?autoplay=1&mute=0&controls=0&playsinline=1&showinfo=0&rel=0&modestbranding=1&color=black&enable&amp;wmode=transparent",

    "https://www.youtube.com/embed/jfKfPfyJRdk?autoplay=1&mute=0&controls=0&playsinline=1&showinfo=0&rel=0&modestbranding=1&color=black&enable&amp;wmode=transparent",

    "https://www.youtube.com/embed/Ui0yMdaYtc4?autoplay=1&mute=0&controls=0&playsinline=1&showinfo=0&rel=0&modestbranding=1&color=black&enable&amp;wmode=transparent",

    "https://www.youtube.com/embed/qH3fETPsqXU?autoplay=1&mute=0&controls=0&playsinline=1&showinfo=0&rel=0&modestbranding=1&color=black&enable&amp;wmode=transparent?enablejsapi=1"
]

const videoTitles =
[

  "Holiday Mood 🎅 Christmas Lofi 🎄Christmas 2023 [chill lo-fi hip hop beats]",

  "Chill Vibes 🍀 Stop Overthinking - Lofi hip hop mix - Calm Down And Relax",

  "lofi hip hop radio - beats to relax/study to",

  "VIDEO GAME RADIO [24/7 Video Game Music Live Stream]",

  "【24/7 CHILL LOFI HIP HOP RADIO】beats to sleep/relax/study to"
]


function switchStations(forward) {
  console.log("switchStations() clicked.");

  // parsed videoLinks
  var frame = document.getElementById("player");
  // frame.src = "https://www.youtube.com/embed/L1zoItQw_e4?controls=0&autoplay=1&mute=0";
  // var jsonData = JSON.parse("../json/links.json"); // Parsing wouldn't work :(
  // var jsonData = JSON.parse(data);
  console.log(videoLinks);
  frame.src = videoLinks.shift();
  videoLinks.push(frame.src);

  // parsed videoTitles
  var title = document.getElementById("video-title");
  console.log(videoTitles);
  var actual_title = videoTitles.shift()
  title.innerHTML = "Now Playing: " + actual_title
  videoTitles.push(actual_title);
}
  // if (forward){
  //   frame.src = videoLinks.shift();
  //   videoLinks.push(frame.src);
  //   var actual_title = videoTitles.shift()
  //   title.innerHTML = "Now Playing: " + actual_title
  //   videoTitles.push(actual_title);
  //   console.log("NEXT");
  // } else {
  //   frame.src = videoLinks.pop();
  //   videoLinks.unshift(frame.src);
  //   var actual_title = videoTitles.pop()
  //   title.innerHTML = "Now Playing: " + actual_title
  //   videoTitles.unshift(actual_title);
  //   console.log("BACK");
  // }
// }
//
// window.addEventListener('keydown', function(event) {
//
//   if (event.key == "ArrowLeft"){
//
//     switchStations(false);
//     if (currentDirection == true) {
//       switchStations(false);
//       currentDirection = false;
//     }
//
//   } else if (event.key == "ArrowRight"){
//
//     switchStations(true);
//     if (currentDirection == false) {
//       switchStations(true);
//       currentDirection = true;
//     }
//
//   }
// }

// document.body.addEventListener('keydown', function(event)
//                                        {
//             const key = event.key;
//             switch (key) {
//                 case "ArrowLeft":
//                     str = 'Left';
//                     break;
//                 case "ArrowRight":
//                     str = 'Right';
//                     break;
//                 case "ArrowUp":
//                     str = 'Up';
//                     break;
//                 case "ArrowDown":
//                     str = 'Down';
//                     break;
//             }


// function pause(){
//   console.log("pause() clicked.");
//   var frame = document.getElementById("player")
//   frame.contentWindow.postMessage('{"event":"command","func":"PauseVideo","args":""}', '*');
// }

// function play(){
//   console.log("play() clicked.");
//   var frame = document.getElementById("player")
//   frame.contentWindow.postMessage('{"event":"command","func":"PlayVideo","args":""}', '*');
// }
