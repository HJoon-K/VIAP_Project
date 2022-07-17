
const muserid = document.querySelector('#muserid');
const mpasswd =document.querySelector('#mpasswd');
const loginbtn =document.querySelector('#loginbtn');
const logoutbtn =document.querySelector('#logoutbtn');
try{
    loginbtn.addEventListener('click',()=>{
        if(muserid.value=='')alert('아이디를 입력하세요')
        else if(mpasswd.value=='')alert('비밀번호를 입력하세요')
        else {
            // document.loginfrm.action='{% url 'login' %}';
            document.loginfrm.action='/login/';
            document.loginfrm.submit();
        }
    });
}catch(e){
}

try{
    logoutbtn.addEventListener('click',()=>{
       // location.href='{% url 'logout' %}';
       location.href='/logout/';
    });
}catch(e){
}

// hamburger icon 클릭시 연동
const toogleBtn = document.querySelector('.navbar_toogleBtn');
const nav = document.querySelector('.nav');
const nmenu = document.querySelector('.navbar_menu');

toogleBtn.addEventListener('click', ()=>{
    nav.classList.toggle('active');
    nmenu.classList.toggle('active');
});

const item = document.querySelector('#nav_item') ;
const item2 = document.querySelector('#nav_item2') ;
let body = document.getElementsByTagName("body")[0];
window.onresize = function(event) {
    let innerWidth = window.innerWidth;
    console.log(innerWidth)
    if (innerWidth <= "992") {
        item.setAttribute('class', 'nav-item dropend');
        item2.setAttribute('class', 'nav-item dropend');
    } else {
        item.setAttribute('class', 'nav-item dropdown');
        item2.setAttribute('class', 'nav-item dropdown');
    };
};