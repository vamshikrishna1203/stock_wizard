const to_display = document.getElementById("display")
const stock = []
function dis(ele){
    to_display.innerText = "Todays stock closing prize of "+ ele.innerText+" is {% url 'predict' %}";
}
