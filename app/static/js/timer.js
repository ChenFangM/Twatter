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
function startTimer(){
  if (!isOn) {
    interval = setInterval(timer, 1000);
    isOn = true;
  }
}
function pauseTimer(){
  if (isOn) {
    interval = clearInterval(interval);
    isOn = false;
  }
}
function resetTimer(){
  pauseTimer();
  if(restTime) {
    time = 300;
  } else {
    time = 1500;
  }
  document.getElementById('displayTime').innerHTML = formatTime(time);
}
function switchTimer(){
  restTime = !(restTime);
  resetTimer();
}
function formatTime(num){
  const min = Math.floor(num/60);
  const sec = num%60;
  if (sec<10) {
    return min + ":0" + sec;
  } else {
    return min + ":" + sec;
  }
}
