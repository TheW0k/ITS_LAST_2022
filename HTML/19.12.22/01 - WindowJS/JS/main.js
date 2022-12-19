var finestraAperta = true;
var menuAperto = true;

            function apri(){
                if(finestraAperta){
                        onClick= document.getElementById('finestra').style.opacity = 1;
                        finestraAperta = false;
                    }
                else{
                        onClick= document.getElementById('finestra').style.opacity = 0;
                        finestraAperta = true;
             }
            }

            function apriMenu(){
                if(menuAperto){
                        onClick= document.getElementById('menu').style.left = '0px';
                        menuAperto = false;
                    }
                else{
                        onClick= document.getElementById('menu').style.left = '-300px';
                        menuAperto = true;
             }
            }