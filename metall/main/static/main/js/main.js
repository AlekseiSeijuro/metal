function SubCheck(){
    var error=''

    if (document.getElementById("name").value==''){
        error='Введённое имя некорректно!';
        document.getElementById('error').innerHTML=error;
        return false;
    }

    var phone=document.getElementById("phone");
    var phoneNum = /(\+7|8)[- _]*\(?[- _]*(\d{3}[- _]*\)?([- _]*\d){7}|\d\d[- _]*\d\d[- _]*\)?([- _]*\d){6})/g;
            if(!phone.value.match(phoneNum)) {
                error='Телефон введён некорректно!';
                document.getElementById('error').innerHTML=error;
                return false;
            }

    return true;
}


for(var i=0; i<length; i++){
    checked[i]=true;
}

function clicked(id){
    pole=document.getElementById(id);
    if(pole.disabled){
        pole.value='';
    }
    pole.disabled=!pole.disabled;
}
