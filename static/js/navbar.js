  //const mydata = "{{ backgroundColor|safe }}";
  //console.log(mydata)
  if (localStorage.getItem("backgroundColorSteat")==null){localStorage.setItem("backgroundColorSteat",'normele')}

  console.log("G :",localStorage.getItem("backgroundColorSteat"))
  if(localStorage.getItem("backgroundColorSteat")==='dark'){document.body.classList.toggle('dark');console.log("color");}
    const toggle = document.querySelector('#toggle');
  
  toggle.addEventListener('change', () => {
    
    document.body.classList.toggle('dark');
    if(localStorage.getItem("backgroundColorSteat")==="dark"){updated("normele") }
    else if(localStorage.getItem("backgroundColorSteat")==="normele"){updated("dark")}

  
   
  })
  function  updated(  color){
  localStorage.removeItem("backgroundColorSteat");
  localStorage.setItem("backgroundColorSteat",color);
  console.log(color)
  }
  