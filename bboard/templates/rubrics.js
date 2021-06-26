const  domain = 'http://localhost:8000';
let id = document.getElementById('id')
let name=document.getElementById('name')
let rubricLoader=new XMLHttpRequest()
let list = document.getElementById('list');
let listLoader = new XMLHttpRequest();
listLoader.addEventListener('readystatechange',()=>{
    if (listLoader.readyState==4){
        if (listLoader.status == 200){
            let data = JSON.parse(listLoader.responseText);
            let s = '<ul>',d;
            for (let i = 0; i < data.length; i++){
                d = data[i];
                s+='<li>'+d.name +'<a href=""'+domain + 'rubrics/'+d.id+'/"class="detail">Chiqarish</a></li>';
            }
            s+= '</ul>';
            list.innerHTML=s;
            let links = list.querySelectorAll('ul li a.detail');
            links.forEach((link)=>
                {link.addEventListener('click',rubricLoad);}
            );
        }
        else 
            window.alert(listLoader.statusText);
    }
});
function listLoad(){
    listLoader.open('GET',domain+'rubrics/',true);
    listLoader.send();
}
listLoad();

rubricLoader.addEventListener('readystatechange',()=>{
    if (rubricLoader.readyState==4){
        if (rubricLoader.status == 200){
            let data = JSON.parse(rubricLoader.responseText);
            id.value = data.id;
            name.value = data.name;
        }
        else
            window.alert(rubricLoader.statusText);
    }
});

function rubricLoad(evt){
    evt.preventDefault();
    rubricLoader.open('GET',evt.target.href,true);
    rubricLoader.send();
}