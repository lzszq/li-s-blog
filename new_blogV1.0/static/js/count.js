var i = 3;
function countDown(){
	if(i == 0){
		window.location.href="http://blog.lizesen.xyz/index";
	}else{
		i = i-1;
	}
}
window.setInterval("countDown()",1000);