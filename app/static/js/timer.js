var time = 1500;
var isOn = false;
var restTime = false;
let interval;

function timer() {
  if(time > 0) {
    time--;
    document.getElementById('displayTime').innerHTML = formatTime(time);
  } else {
    clearInterval(interval);
  }
}
<<<<<<< HEAD

=======
>>>>>>> 3fe794d44eeb1552081bf88afc0c62c638df3196
function startTimer(){
  if (!isOn) {
    interval = setInterval(timer, 1000);
    isOn = true;
  }
}
<<<<<<< HEAD

=======
>>>>>>> 3fe794d44eeb1552081bf88afc0c62c638df3196
function pauseTimer(){
  if (isOn) {
    interval = clearInterval(interval);
    isOn = false;
  }
}
<<<<<<< HEAD

=======
>>>>>>> 3fe794d44eeb1552081bf88afc0c62c638df3196
function resetTimer(){
  pauseTimer();
  if(restTime) {
    time = 300;
  } else {
    time = 1500;
  }
  document.getElementById('displayTime').innerHTML = formatTime(time);
}
<<<<<<< HEAD

=======
>>>>>>> 3fe794d44eeb1552081bf88afc0c62c638df3196
function switchTimer(){
  restTime = !(restTime);
  resetTimer();
}
<<<<<<< HEAD

=======
>>>>>>> 3fe794d44eeb1552081bf88afc0c62c638df3196
function formatTime(num){
  const min = Math.floor(num/60);
  const sec = num%60;
  if (sec<10) {
    return min + ":0" + sec;
  } else {
    return min + ":" + sec;
  }
<<<<<<< HEAD
}
=======
}
>>>>>>> 3fe794d44eeb1552081bf88afc0c62c638df3196
