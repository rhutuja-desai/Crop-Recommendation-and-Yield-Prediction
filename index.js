function sendMail(){
    var params={
        name:document.getElementById("Name").value,
        email:document.getElementById("eMail").value,
        phone:document.getElementById("Number").value,
        message:document.getElementById("Message").value
    }
const serviceId="service_mv6ettg";
const templateId="template_aognsyk";
emailjs
.send(serviceId,templateId,params).then(
    (res)=>{
        document.getElementById("Name").value="",
        document.getElementById("eMail").value="",
        document.getElementById("Number").value="",
        document.getElementById("Message").value="",
        console.log(res);
        alert("You will be contacted soon")
})
.catch(err=>console.log(err))
;
}
